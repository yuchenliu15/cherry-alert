import logging
logging.basicConfig(level=logging.INFO)

from .emails import send
from .processing import scrape_image, analyze_image
from .redis_client import get_all_subscribers

if __name__ == '__main__':
    subscribers = get_all_subscribers()
    encoded_image = scrape_image()
    cherry = analyze_image(encoded_image)
    send(subscribers , cherry)
