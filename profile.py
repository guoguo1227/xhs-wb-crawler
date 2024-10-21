import requests
from tool.util import get_headers, get_cookies, parse_profile_info

class Home:
    def __init__(self):
        self.cookies = get_cookies()
        self.headers = get_headers()

    # 获取用户个人页数据
    def get_profile_info(self, url):
        response = requests.get(url, headers=self.headers, cookies=self.cookies)
        html_text = response.text
        userId = url.split('/')[-1]
        profile = parse_profile_info(userId, html_text)
        #打印结果
        print(profile)
        return profile

    def main(self, url_list):
        for url in url_list:
            try:
                self.get_profile_info(url)
            except:
                print(f'用户 {url} 查询失败')
                continue


if __name__ == '__main__':
    home = Home()
    url_list = [
        'https://www.xiaohongshu.com/user/profile/5a5cb940e8ac2b2b7d0e2d70',
    ]
    home.main(url_list)

