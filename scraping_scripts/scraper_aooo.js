const puppeteer = require('puppeteer');
const fs = require('fs');
const util = require('util');

const appendToJson = async (file, data) => {
  let existingData = [];

  try {
    existingData = require(file);
  } catch (err) {
    if (err.code !== 'MODULE_NOT_FOUND') {
      throw err;
    }
  }

  existingData.push(...data);
  
  await util.promisify(fs.writeFile)(file, JSON.stringify(existingData, null, 4));
};

const main = async () => {
  const browser = await puppeteer.launch({headless: false});
  const page = await browser.newPage();

  for (let i = 1; i <= 5000; i++) {
    // Replace this with the URL you wish to scrape
    const url = `https://archiveofourown.org/tags/Science%20Fiction%20*a*%20Fantasy/works?page=${i}`;
    await page.goto(url);

    // Wait for elements with class "userstuff" to appear on the page
    await page.waitForSelector('blockquote.userstuff');
    const elements = await page.$$('.userstuff');

    for (let element of elements) {
      const data = await element.evaluate(el => el.textContent.trim());

      // Create the JSON output
      const output = data !== '' ? [{instruction: '', input: '', output: data}] : [];
      console.log(output);

      // Write output to JSON file
      await appendToJson('./output.json', output);
    }

    console.log('Iteration: ', i);

    // Sleep for 3 seconds
    await new Promise(resolve => setTimeout(resolve, 3000));
  }

  await browser.close();
};

main().catch(console.error);
