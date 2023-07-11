import json
import time
import random

from playwright.sync_api import sync_playwright


def get_links(page):
    # Find all 'a' elements
    links_elements = page.query_selector_all("a")
    links = []

    for element in links_elements:
        title = element.get_attribute("title")  # Get the 'title' attribute of the 'a' element
        if title:
            title = title.replace(":", "").replace(" ", "-").replace("-Script", "")
            links.append("https://imsdb.com/scripts/" + title + ".html")

    return links


def parse_script(page, link):
    # Go to the link
    page.goto(link)
    print('Working on:', link)

    # Wait for the 'td' element with class 'scrtext' and get its content
    page.wait_for_selector("td.scrtext")
    script_content = page.inner_text("td.scrtext")

    time.sleep(random.randint(100, 120))  # Sleep for a random period of time between 100 and 120 seconds

    # Split the script content into paragraphs
    paragraphs = script_content.split("\n")

    # Iterate over the paragraphs and add each to the JSON array
    json_paragraphs = [
        {
            "instruction": "",
            "input": "",
            "output": paragraph.replace("\t", "").replace("\u00a0", "")
        } for paragraph in paragraphs if paragraph.strip() != ""
    ]

    return json_paragraphs


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        json_array = []  # The JSON array that will hold all the outputs

        page.goto('https://imsdb.com/genre/Sci-Fi')

        # Wait for the 'a' elements to appear in the page
        page.wait_for_selector("a")

        links = get_links(page)

        for link in links:
            json_array.extend(parse_script(page, link))

        # Write the JSON array to a file
        with open("output.json", "w") as outfile:
            json.dump(json_array, outfile, indent=4)

        browser.close()


if __name__ == "__main__":
    main()
