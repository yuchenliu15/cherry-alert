from playwright.sync_api import sync_playwright
from langchain.schema import HumanMessage, SystemMessage
import os
import base64
from langchain_google_genai import ChatGoogleGenerativeAI
import getpass
from pydantic import BaseModel, Field, computed_field
import logging
import dotenv
dotenv.load_dotenv()

CHERRY_URL = "https://www.bbg.org/collections/cherries"
OUTPUT_IMAGE = "cherries.png"

class CherryInfo(BaseModel):
    no_blossoms: int = Field(..., description="Number of yellow dots")
    blossoms: int = Field(..., description="Number of pink and purple flowers")

    @computed_field
    def blossom_percentage(self) -> float:
        return (self.blossoms / (self.no_blossoms + self.blossoms)) * 100

def scrape_image() -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(CHERRY_URL)
        page.wait_for_load_state("domcontentloaded")
        buffer = page.locator("#cherrymap").screenshot()
        encoded = base64.b64encode(buffer).decode("utf-8")
        browser.close()
    return encoded

def analyze_image(encoded_image: str) -> CherryInfo: 
    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API Key: ")

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
                "url": f"data:image/png;base64,{encoded_image}",
            }}
        ])
    ]
    llm = llm.with_structured_output(CherryInfo)
    cherry = llm.invoke(messages)
    logging.info(f"Analyzed result: {cherry}")
    return cherry

if __name__ == "__main__":
    dotenv.load_dotenv()
    image_str = scrape_image()
    with open(OUTPUT_IMAGE, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    result = analyze_image(encoded_string)
    print(result)
