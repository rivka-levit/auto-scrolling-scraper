import scrapy


class ScrollingSpider(scrapy.Spider):
    name = "scrolling"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/scroll"]

    def parse(self, response, **kwargs):
        pass
