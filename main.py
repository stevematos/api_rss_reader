import uvicorn
import logging

from schema import schema
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.graphql import GraphQLApp

from database import engine
from models import Base

import asyncio
import threading

from utils import update_feeds

import argparse
import os

Base.metadata.create_all(bind=engine)

# setup loggers

logging.basicConfig(
    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    filename='api_rss_reader.log',
    level=logging.DEBUG)

# get root logger
logger = logging.getLogger(__name__)

app = FastAPI()

origins = [
    "http://localhost:5000",
    "http://0.0.0.0:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/", GraphQLApp(schema=schema))


def thr():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    logger.info('------------------------------------')
    logger.info('CRON DE ACTUALIZADO DE FEED INICIADO')
    logger.info('------------------------------------')
    try:
        asyncio.ensure_future(update_feeds())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        logger.info("Closing Loop")
        loop.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--feed_cron", help="1 activate , 0 deactivate",
                        default=0)
    args = parser.parse_args()

    thread_feed = False
    if args.feed_cron:
        thread_feed = threading.Thread(target=thr, args=())
        thread_feed.start()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    if args.feed_cron:
        os._exit(0)

# python main.py --feed_cron 1