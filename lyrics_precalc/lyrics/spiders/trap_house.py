# -*- coding: utf-8 -*-
import scrapy


class TrapHouseSpider(scrapy.Spider):
    name = 'trap_house'
    allowed_domains = ['www.azlyrics.com/lyrics/guccimane/']
    start_urls = ['https://www.azlyrics.com/lyrics/guccimane/intro.html',
    'https://www.azlyrics.com/lyrics/guccimane/traphouse.html']


    def parse(self, response):
        yield {
        'lyrics': [i.strip() for i in response.xpath('/html/body/div[3]/div/div[2]/div[5]/text()').extract()],
        'title': response.xpath('/html/body/div[3]/div/div[2]/b/text()').extract() ,
        }

