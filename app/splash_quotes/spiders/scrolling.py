import scrapy

from scrapy.loader import ItemLoader

from scrapy_splash.request import SplashRequest

from splash_quotes.items import SplashQuotesItem


class ScrollingSpider(scrapy.Spider):
    name = "scrolling"
    allowed_domains = ["quotes.toscrape.com", "172.24.0.2", "splash"]
    start_urls = ["https://quotes.toscrape.com/scroll"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(
                url=url,
                callback=self.parse,
                args={'wait': 1}
            )

    def parse(self, response, **kwargs):
        containers = response.xpath('//div[@class="quote"]')

        for quote in containers:
            item = ItemLoader(
                item=SplashQuotesItem(),
                response=response,
                selector=quote
            )

            item.add_xpath(
                'quote',
                './/span[@class="text"]/text()'
            )

            item.add_xpath(
                'author',
                './/small[@class="author"]/text()'
            )

            yield item.load_item()
