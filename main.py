from playwright.sync_api import sync_playwright
import csv

def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # Set to True to run in headless mode
    context = browser.new_context()

    page = context.new_page()
    # page.goto("https://www.google.com/maps")
    url = f"https://www.google.com/maps/search/gym in nagpur"
    page.goto(url)
    page.wait_for_selector(".hfpxzc", timeout=10000)
    page.click(".hfpxzc")
    textdata = page.text_content(".DUwDvf")
    textdata2 = page.text_content(".Io6YTe")

    print(textdata)
    mapdata = []
    mapdata.append({'title': textdata, 'price': textdata2})
    filename='mapdata.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'price'])
        writer.writeheader()
        writer.writerows(mapdata)
 


    input("Press Enter to close the browser...")

    print("Page Title:", page.title())

    page.screenshot(path="example_screenshot.png")
    print("Screenshot saved as example_screenshot.png")

    # browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
