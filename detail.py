import json
import requests
from tool.util import get_headers, get_detail_params, get_cookies, js, parse_note_info

class Home:
    def __init__(self):
        self.cookies = get_cookies()
        self.headers = get_headers()
        self.feed_url = 'https://edith.xiaohongshu.com/api/sns/web/v1/feed'
        self.detail_url = 'https://www.xiaohongshu.com/explore/'

    # 获取小红书详情页数据
    def get_note_detail(self, url):
        note_id = url.split('/')[-1]
        self.params = get_detail_params(note_id)
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
            except:
                print(f'笔记 {url} 查询失败')
                continue


if __name__ == '__main__':
    home = Home()
    url_list = [
        'https://www.xiaohongshu.com/explore/67125594000000001b03fd1e'
    ]
    home.main(url_list)

