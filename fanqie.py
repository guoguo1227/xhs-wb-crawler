import requests
from openpyxl import Workbook, load_workbook
import execjs
import urllib.parse


class Home:
    def __init__(self, cookies=None):
        #替换成浏览器请求里的token
        self.msToken = ""
        #替换浏览器cookie
        self.cookie = ""
        #读取abogus算法
        self.js = execjs.compile(open(r"static/abogus.js", "r", encoding="utf-8").read())

    def get_headers(self):
        return {
            "accept": "application/json, text/plain, */*",
            "cookie": self.cookie,
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        }

    def searchPage(self, keyword, wb, ws):
        encode_keyword = urllib.parse.quote(keyword, 'utf-8')
        p = f"filter=127%2C127%2C127%2C127&page_count=10&page_index=0&query_type=0&query_word={encode_keyword}&msToken={self.msToken}"
        #获取a_bogus
        a_bogus = self.js.call('get_a_bogus', p)
        url = f"https://fanqienovel.com/api/author/search/search_book/v1?{p}&a_bogus={a_bogus}"
        response = requests.get(url, headers=self.get_headers())
        try:
            list = response.json()['data']['search_book_data_list']
            for item in list:
                name = item['book_name']
                read = item['read_count']
                book_id = item['book_id']
                jmp_url = f"https://fanqienovel.com/page/{book_id}"
                ws.append([keyword, name, jmp_url, read])
                wb.save('番茄小说列表.xlsx')

        except Exception as e:
            print(f'搜索：{keyword},失败 {e}')


    def main(self):
        # 创建一个新的工作簿
        wb = Workbook()
        # 选择默认的工作表
        ws = wb.active
        ws.append(['搜索关键词', '小说名称', '小说链接', '在读人数'])
        #根据关键词搜索小说名称
        self.searchPage("武侠", wb, ws)

if __name__ == '__main__':
    home = Home()
    home.main()

