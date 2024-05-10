import scrapy

class GonzagaSpider(scrapy.Spider):
    # name of spider
    name = 'gonzaga'
    # limit the domains to scrape
    allowed_domains = ['gonzaga.edu']
    # hold inital url to scrape
    start_urls = ['https://www.gonzaga.edu/']

    def parse(self, response):
        '''
        parse text responses from 
        all website urls
        '''
        text_data = response.css('body::text').getall()

        yield {
            'url': response.url,
            'text_data': ''.join(text_data)
        }

        # follow all links on the page
        for next_page in response.css('a::attr(href)').getall():
            yield response.follow(next_page, callback=self.parse)