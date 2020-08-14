import uvicorn
import logging

from schema import schema
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.graphql import GraphQLApp

from database import engine
from models import Base

Base.metadata.create_all(bind=engine)

# setup loggers

logging.basicConfig(
    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    filename= 'api_rss_reader.log',
    level = logging.DEBUG)

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

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
