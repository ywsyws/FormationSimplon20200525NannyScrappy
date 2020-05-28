import scrapy

class NannySpider(scrapy.Spider):
    name = "nannies"

    def start_requests(self):
        urls = [
            'https://www.childcare.co.uk/find/Babysitters',
            'https://www.childcare.co.uk/find/Babysitters/2',
            'https://www.childcare.co.uk/find/Babysitters/3'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'nannies-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)