import json
import requests
import re
from tool.util import get_headers, get_detail_params, get_cookies, js, parse_note_info

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "dnt": "1",
    "origin": "https://www.xiaohongshu.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.xiaohongshu.com/",
    "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
}

class Home:
    def __init__(self):
        self.cookies = get_cookies()
        self.headers = get_headers()
        self.feed_url = 'https://edith.xiaohongshu.com/api/sns/web/v1/feed'
        self.detail_url = 'https://www.xiaohongshu.com/explore/'

    # 获取小红书详情页数据
    def get_note_detail(self, url):
        #提取url中的note_id
        match = re.search(r'/(\w+)\?', url)
        if match:
            note_id = match.group(1)
        #提取url中的xsec_token
        match = re.search(r'xsec_token=([^&]+)', url)
        if match:
            xsec_token = match.group(1)
        self.params = get_detail_params(note_id,xsec_token)

        data = json.dumps(self.params, separators=(',', ':'), ensure_ascii=False)
        ret = js.call('get_xsxt', '/api/sns/web/v1/feed', self.params, self.cookies['a1'])
        self.headers['x-s'], self.headers['x-t'] = ret['X-s'], str(ret['X-t'])
        response = requests.post(self.feed_url, headers=self.headers, cookies=self.cookies, data=data)
        res = response.json()

        try:
            result = res['data']['items'][0]
        except:
            print(f'获取笔记 {note_id} 详情失败')
            return
        #提取小红书详情页需要的字段
        note = parse_note_info(result)
        return note

    def main(self, url_list):
        for url in url_list:
            try:
                data = self.get_note_detail(url)
                #打印结果或者导出到excel
                print(data)
            except Exception as e:
                print(f'笔记 {url} 查询失败 {e}')
                continue


if __name__ == '__main__':
    home = Home()
    url_list = [
        'https://www.xiaohongshu.com/explore/674f023a00000000080054a0?xsec_token=ABmiLX0Cc6t9VVKo-_wu1juy8O-Hu2f-NVB4_GPtFkb2o=&xsec_source=pc_search&source=web_search_result_notes'
    ]
    home.main(url_list)
