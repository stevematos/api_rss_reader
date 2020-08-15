import feedparser
from dateutil import parser as date_parser


def read_rss(rss: str) -> list:
    feed = feedparser.parse(rss)
    entries = feed.entries

    res = []
    for entry in entries:
        entry_format = {
            'title': entry.get('title', ''),
            'summary': entry.get('summary', ''),
            'published': entry.get('published', None) and date_parser.parse(entry.published),
            'image': entry.get('media_content', '') and entry.get('media_content')[0].get('url'),
            'author': entry.get('author', ''),
            'link': entry.get('link', ''),
            'id_feed': entry.get('id', '')
        }
        res.append(entry_format)
    return res
