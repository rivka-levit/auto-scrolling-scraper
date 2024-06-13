"""
Models for the scraped items.
"""

import scrapy

from itemloaders.processors import Join  # noqa


def clean(q):
    """
    Clean data. Get rid of extra quotes and special characters.

    Args:
        q (list): list of one string received form item loader.

    Returns:
        str: cleaned string.
    """

    return q[0].replace('\201c', '').replace('\u201d', '').replace('\u00e9', '')


class SplashQuotesItem(scrapy.Item):
    quote = scrapy.Field(
        input_processor=clean,
        output_processor=Join()
    )
    author = scrapy.Field(
        input_processor=clean,
        output_processor=Join()
    )
