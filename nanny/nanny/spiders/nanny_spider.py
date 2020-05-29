import scrapy

class NannySpider(scrapy.Spider):
    name = "nannies"
    start_urls = [
        'https://www.childcare.co.uk/find/Babysitters',
        # 'https://www.childcare.co.uk/find/Babysitters/2',
        # 'https://www.childcare.co.uk/find/Babysitters/3'
    ]

    def parse(self, response):
        for nanny in response.css("div.results"):
            yield {
                'name' : nanny.css('div.screen-name::text').getall(),
                'rating' : nanny.css('img.star-rating').re(r'\d\s'),
                'hourly_rate' : nanny.css('div.flag::text').re(r'\d*\.\d\d*')
            }
        
        next_page = response.css('a.view a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        # stopped at "More examples and patterns" in "https://docs.scrapy.org/en/latest/intro/tutorial.html"