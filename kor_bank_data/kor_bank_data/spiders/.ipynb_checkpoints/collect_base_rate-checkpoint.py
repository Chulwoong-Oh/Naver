import scrapy
from kor_bank_data.items import KorBankDataItem

class CollectBaseRateSpider(scrapy.Spider):
    SERVICE = "StatisticSearch"
    API_KEY = "AO2SC49NZ7R6OJ1AADVT"
    CODE = "098Y001"
    CYCLE = "MM"
    FROM_YM = "201901"
    TO_YM = "202204"
    
    name = 'collect_base_rate'
    allowed_domains = ['ecos.bok.or.kr']
    start_urls = ['http://ecos.bok.or.kr/']

    collect_url = "http://ecos.bok.or.kr/api/{}/{}/json/kr/1/1000/{}/{}/{}/{}".format(
        SERVICE, API_KEY, CODE, CYCLE, FROM_YM, TO_YM
    )
    
    start_urls = [collect_url]
    
    def parse(self, response):
        item = KorBankDataItem()
        
        import json
        import pandas as pd
        result = json.loads(response.text)
        result_row = result["StatisticSearch"]["row"]
        item1 = pd.DataFrame(result_row)
        item1.to_csv('result.csv', encoding = 'utf-8-sig', index = False)
        result_row1 = result_row
        stat_code = list()
        stat_name = list()
        item_code1 = list()
        item_name1 = list()
        item_code2 = list()
        item_name2 = list()
        item_code3 = list()
        item_name3 = list()
        unit_name = list()
        time = list()
        data_value = list()
        
        for i in result_row1:
            stat_code.append(i.get("STAT_CODE", ""))
            stat_name.append(i.get("STAT_NAME", ""))
            item_code1.append(i.get("ITEM_CODE1", ""))
            item_name1.append(i.get("ITEM_NAME1", ""))
            item_code2.append(i.get("ITEM_CDOE2", ""))
            item_name2.append(i.get("ITEM_NAME2", ""))
            item_code3.append(i.get("ITEM_CODE3", ""))
            item_name3.append(i.get("ITEM_NAME3", ""))
            unit_name.append(i.get("UNIT_NAME", ""))
            time.append(i.get("TIME", ""))
            data_value.append(i.get("DATA_VALUE", ""))
        # print(stat_code)
        item['stat_code'] = stat_code
        item['stat_name'] = stat_name
        item['item_code1'] = item_code1
        item['item_name1'] = item_name1
        item['item_code2'] = item_code2
        item['item_name2'] = item_name2
        item['item_code3'] = item_code3
        item['item_name3'] = item_name3
        item['unit_name'] = unit_name
        item['time'] = time
        item['data_value'] = data_value
                      
        return item
