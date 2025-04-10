from .emails import send
from .processing import scrape_image, analyze_image
import dotenv
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    dotenv.load_dotenv()
    encoded_image = scrape_image()
    cherry = analyze_image(encoded_image)
    send(["eugeneliuosm@gmail.com"], cherry)
