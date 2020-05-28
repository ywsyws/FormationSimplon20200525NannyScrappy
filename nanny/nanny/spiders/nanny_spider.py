import scrapy

class NannySpider(scrapy.Spider):
    name = "nannies"
    start_urls = [
        'https://www.childcare.co.uk/find/Babysitters',
        'https://www.childcare.co.uk/find/Babysitters/2',
        'https://www.childcare.co.uk/find/Babysitters/3'
    ]

    def parse(self, response):
        # page = response.url.split("/")[-1]
        # filename = 'nannies-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

        for nanny in response.css("div.results")[0]:
            yield {
                'name' : nanny.css('div.screen-name::text').get(),
                'rating' : nanny.css('img.star-rating').re(r'\d\sstars')[0].split(' ')[0],
                'hourly_rate' : nanny.css('div.flag::text').get(),
            }



        # response.css('div.screen-name').getall()
        # response.css('img.star-rating').re(r'\d\sstars')
        # response.css('img.star-rating').re(r'\d\sstars')[0].split(' ')[0]
        # response.css('div.flag::text').getall()

    #     nanny = response.css("div.results")[0]
    #     name = nanny.css('div.screen-name::text').get()
    #     rating = nanny.css('img.star-rating').re(r'\d\sstars')[0].split(' ')[0]
    #     hourly_rate = nanny.css('div.flag::text').get()

    #     for nanny in response.css("div.results")[0]:
    #  ...:     name = nanny.css('div.screen-name::text').get()
    #  ...:     rating = nanny.css('img.star-rating').re(r'\d\sstars')[0].split(' ')[0]
    #  ...:     hourly_rate = nanny.css('div.flag::text').get()
    #  ...:     print((dict(name=name, rating=rating, hourly_rate=hourly_rate))