import requests
import json
import csv
import time


def zhihu_hot():
    headers = {
        'accept-language': 'zh-CN,zh;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36',
        'accept': '*/*',
        'referer': 'https://www.zhihu.com/hot',
        'authority': 'www.zhihu.com',
        'x-requested-with': 'fetch',
    }

    params = (
        ('limit', '50'),
        ('desktop', 'true'),
    )

    response = requests.get('https://www.zhihu.com/api/v3/feed/topstory/hot-list-web', headers=headers, params=params)

    json_obj = json.loads(response.text)

    detester = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    print(detester)
    writer = csv.writer(open(detester + '.csv', 'w', newline='', encoding='utf-8'))
    i = 1
    for each in json_obj['data']:
        answer_count = each['feed_specific']['answer_count']
        title_area = each['target']['title_area']['text']
        metrics_area = each['target']['metrics_area']['text']
        excerpt_area = each['target']['excerpt_area']['text']
        link = each['target']['link']['url']

        result = [i, title_area, metrics_area, answer_count, link, excerpt_area]
        writer.writerow(result)
        i += 1


while True:
    zhihu_hot()
    time.sleep(300)
