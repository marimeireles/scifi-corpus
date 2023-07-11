/*
Some quick instructions to run this:
1. Make sure you have node, an initalized npm environment and puppeteer
2. Run chrome from your command line in port 9222: /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
3. Go to chrome: http://localhost:9222/json/version
4. Copy the webSocketDebuggerUrl and paste in the browserURL var
5. Make sure you're logged in your chatGPT account
6. Take into account comments in the code they're also part of the instructions
*/


const puppeteer = require('puppeteer');
const fs = require('fs');


const browserURL = ''; // your ws:// ...
const minTimeout = 2000; // Minimum timeout value (2000 milliseconds)
const maxTimeout = 3000; // Maximum timeout value (3000 milliseconds)

async function getRandomTimeout() {
    return Math.floor(Math.random() * (maxTimeout - minTimeout + 1)) + minTimeout;
}

const appendToJsonFile = async (filename, data) => {
    let fileData;
    try {
        fileData = JSON.parse(fs.readFileSync(filename));
        if (!Array.isArray(fileData)) throw new Error();
    } catch {
        fileData = [];  // If the file doesn't exist or contains invalid JSON, start a new array
    }

    fileData.push(data);
    fs.writeFileSync(filename, JSON.stringify(fileData, null, 4));
};


async function run() {
    const data = JSON.parse(fs.readFileSync('input_file.json', 'utf-8')); // Make sure this file exists

    const browser = await puppeteer.connect({ browserWSEndpoint: browserURL });
    const page = await browser.newPage();

    await page.goto('https://chat.openai.com');

    for(let entry of data) {
        const message = entry.output;
        console.log('Processing message:', message)

        await page.waitForSelector('#prompt-textarea');

        // Message to send to chatGPT
        await page.type('#prompt-textarea', 'one sentence prompt to this output, dont include anything else, just answer: ' + message);
        await page.keyboard.press('Enter');

        await page.waitForTimeout(await getRandomTimeout());

        const divs = await page.$$('div.bg-gray-50');

        if (divs.length === 0) {
            console.log('No divs found for message:', message);
            continue;
        }

        const lastDiv = divs[divs.length - 1];
        const textContent = await lastDiv.$$eval('p', ps => ps.length > 0 ? ps[0].textContent : undefined);
        console.log('Instruction:', textContent);

        // Format your dataResult to look how you need it
        const dataResult = { 
            "textContent": textContent, 
            "message": message
        };

        appendToJsonFile('output_file.json', dataResult).catch(console.error);
    }

    await page.close();
    await browser.disconnect();
}

run().catch(console.error);
