import json
import requests

from tool.util import get_weibo_headers, get_sign_params


class Home:
    def __init__(self):
        self.headers = get_weibo_headers()
        self.url = "https://weibo.com/ajax/profile/topicContent?tabid=231093_-_chaohua"
        self.sign_url = "https://weibo.com/p/aj/general/button?ajwvr=6&api=http://i.huati.weibo.com/aj/super/checkin&texta=%E7%AD%BE%E5%88%B0&textb=%E5%B7%B2%E7%AD%BE%E5%88%B0&status=0&id={}&location=page_100808_super_index&timezone=GMT+0800&lang=zh-cn&plat=Win32&ua=Mozilla/5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/126.0.0.0%20Safari/537.36%20Edg/126.0.0.0&screen=2048*1152&__rnd=1720793419490"
        self.list_data = "tabid=231093_-_chaohua"
        # key为超话名，value为超话id
        self.map = {}

    # 查询我关注的超话并保存到map
    def query_chaohus(self):
        response = requests.get(self.url, data=self.list_data, headers=self.headers)
        json_data = json.loads(response.text)

        # 提取需要的信息
        topics = json_data.get('data', {}).get('list', [])

        # 遍历并打印每个超话的信息
        for topic in topics:
            title = topic.get('title', 'N/A')
            link = topic.get('link', 'N/A')

            # 找到最后一个斜杠的位置
            last_slash_index = link.rfind("/")

            # 获取最后一个斜杠之后的所有字符
            id = link[last_slash_index + 1:] if last_slash_index != -1 else link
            self.map[title] = id

    def sign(self, key, value):
        sign_url = self.sign_url.format(value)
        params = get_sign_params(value)
        response = requests.get(sign_url, data=params, headers=self.headers)
        rep = json.loads(response.text.encode("utf-8"))
        print(rep)
        if rep.get('msg') == "今天已签到(382004)":
            print(key + "签到失败")
            return 0
        else:
            print(key + "签到成功")
            # 打印当前签到数
            print(rep.get('data'))
            return 1

    def main(self):
        success = 0
        fail = 0
        try:
            # 查询关注的超话
            home.query_chaohus()
            # 遍历超话列表签到
            for key in self.map:
                if home.sign(key, self.map[key]):
                    success = success + 1
                else:
                    fail = fail + 1
        except Exception as e:
            print(f'签到失败 {e}')
        print(f'签到成功 {success}，签到失败：{fail}')


if __name__ == '__main__':
    home = Home()
    home.main()
