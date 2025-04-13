from upstash_redis import Redis
import logging
import os
import dotenv
dotenv.load_dotenv()

REDIS_API_TOOKEN = os.getenv("REDIS_API_TOKEN")
REDIS_API_URL = os.getenv("REDIS_API_URL")

redis = Redis(url=REDIS_API_URL, token=REDIS_API_TOOKEN)

def get_all_subscribers():
    members = redis.smembers("all_subscribers")
    logging.info(f"Fetched all subscribers: {members}")
    return members 
