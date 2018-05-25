# -*- coding: utf-8 -*-
import scrapy


class NasSpider(scrapy.Spider):
    name = 'nas'
    allowed_domains = ['www.azlyrics.com/n/nas.html']
    start_urls = ['https://www.azlyrics.com/n/nas.html']
    # linker = response.xpath('//div/div/a')
    # links = []
    # for link in linker:
    # 		response.follow(link.css('a::attr(href)').extract())

    def parse(self, response):
    	# gets hrefs
    	album_list = response.xpath('//*[@id="listAlbum"]/a')
    	for link in album_list[5:]:
    		ref = link.css('a::attr(href)').extract()[0][2:]
    		addie = 'https://www.azlyrics.com' + ref
    		yield response.follow(addie, self.lyric_parse)

    def lyric_parse(self, response):
    	yield {
    		'lyrics': [i.strip() for i in response.xpath('/html/body/div[3]/div/div[2]/div[5]/text()').extract()]
    	}
    	# yield {
     #    		'lyrics': [i.strip() for i in response.xpath('/html/body/div[3]/div/div[2]/div[5]/text()').extract()],
     #    		'title': response.xpath('/html/body/div[3]/div/div[2]/b/text()').extract(),
     #    	}
   















   #      for link in linker:
			# next_page = response.follow(link, callback= self.parse)
        
    	

# linker = response.xpath('//div/div/a')
# #generates links
# for link in linker:
#  	print(link.css('a::attr(href)').extract()