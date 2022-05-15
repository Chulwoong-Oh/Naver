# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KorBankDataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    stat_code = scrapy.Field()
    stat_name = scrapy.Field()
    item_code1 = scrapy.Field()
    item_name1 = scrapy.Field()
    item_code2 = scrapy.Field()
    item_name2 = scrapy.Field()
    item_code3 = scrapy.Field()
    item_name3 = scrapy.Field()
    unit_name = scrapy.Field()
    time = scrapy.Field()
    data_value = scrapy.Field()
    pass
