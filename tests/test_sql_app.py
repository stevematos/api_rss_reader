from fastapi.testclient import TestClient

from main import app
from database import Base
from database import Session
from tests.utils_test import delete_user, delete_feed

client = TestClient(app)

EMAIL_TEST = 'test@test.pe'
PASSWORD_TEST = 'test'
TEST_RSS = 'https://archivo.elcomercio.pe/feed/tvmas.xml'
TITLE_TEST = 'comercio'


def test_feed():
    response = client.post(
        "/",
        json={"query": """
              query{
                  feed(url:"https://archivo.elcomercio.pe/feed/mundo.xml"){
                    title
                    summary
                    published
                    image
                    author
                  }
                }
            """}
    )
    data = response.json()
    assert 'errors' not in data


def test_login():
    response = client.post(
        "/",
        json={"query": """mutation{{
            CreateUser(email: "{email}", password: "{password}"){{
                user{{
                  id
                  email
                }}
              }}
        }}""".format(email=EMAIL_TEST, password=PASSWORD_TEST)}
    )
    data = response.json()
    assert 'errors' not in data
    user_id = data['data']['CreateUser']['user']['id']
    response = client.post(
        "/",
        json={"query": """{{
               login(email: "{email}",password:"{password}")
           }}""".format(email=EMAIL_TEST, password=PASSWORD_TEST)}
    )
    data = response.json()
    assert 'errors' not in data
    assert data['data']['login']
    delete_user(Session, user_id)


def test_subscribe_feed():
    response = client.post(
        "/",
        json={"query": """mutation{{
            CreateUser(email: "{email}", password: "{password}"){{
                user{{
                  id
                  email
                }}
              }}
        }}""".format(email=EMAIL_TEST, password=PASSWORD_TEST)}
    )
    user_id = response.json()['data']['CreateUser']['user']['id']

    response = client.post(
        "/",
        json={"query": """  
                mutation{{
                  SubscribeFeed(
                    urlFeed: "{url_feed}",
                    userId: {user_id},
                    title:"{title}"){{
                    idFeed
                  }}
                }}""".format(url_feed=TEST_RSS, user_id=user_id, title=TITLE_TEST)}
    )
    data = response.json()
    assert 'errors' not in data
    feed_id = data['data']['SubscribeFeed']['idFeed']
    assert feed_id
    delete_user(Session, user_id)
    delete_feed(Session, feed_id)
