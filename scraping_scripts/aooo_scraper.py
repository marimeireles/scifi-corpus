import json
import time
from playwright.sync_api import sync_playwright

def append_to_json(file, data):
    try:
        with open(file, 'r+') as f:
            existing = json.load(f)
            existing.extend(data)
            f.seek(0)
            json.dump(existing, f, indent=4)
    except FileNotFoundError:
        with open(file, 'w') as f:
            json.dump(data, f, indent=4)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for i in range(1, 5000):
            # Replace this with the URL you wish to scrape
            url = 'https://archiveofourown.org/tags/Science%20Fiction%20*a*%20Fantasy/works?page=' + str(i)
            page.goto(url)

            # Extract the text within all elements with class "userstuff summary"
            page.wait_for_selector("blockquote.userstuff")
            elements = page.query_selector_all('.userstuff')

            for element in elements:
                data = element.inner_text() 
                print(data)

                # Create the JSON output
                output = [{'instruction': '', 'input': '', 'output': text} for text in data if text != '']
                print(output)

                # Write output to JSON file
                append_to_json('output.json', output)

                time.sleep(3)
            print('Iteration: ', i)

        browser.close()

main()
