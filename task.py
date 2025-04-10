from playwright.sync_api import sync_playwright
from langchain.schema import HumanMessage, SystemMessage
import os
import base64
from langchain_google_genai import ChatGoogleGenerativeAI
import getpass

CHERRY_URL = "https://www.bbg.org/collections/cherries"
OUTPUT_IMAGE = "cherries.png"


def scrape_image():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
#
        page.goto(CHERRY_URL)
        page.wait_for_load_state("domcontentloaded")
        page.locator("#cherrymap").screenshot(path=OUTPUT_IMAGE)
        browser.close()
    print(f"Image saved to {OUTPUT_IMAGE}")

def analyze_image(iamge_path=OUTPUT_IMAGE): 
    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API Key: ")

    with open(OUTPUT_IMAGE, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-001",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    messages = [
        SystemMessage("You are a helpful assistant that can analyze images and answer questions about them."),
        HumanMessage(content=[
            {"type": "text", "text": "how many yellow dots, purple flowers, and pink flowers in the image?"},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{encoded_string}"
            }}
        ])
    ]
    ai_msg = llm.invoke(messages)
    print(ai_msg)

if __name__ == "__main__":
    scrape_image()
    #analyze_image()
