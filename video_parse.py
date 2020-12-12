"""
author: wuaho
email: 15392746632@qq.com
data:2019-11-14

#########################

edited on 2020-12-13 by wushuang.yoyo (email: wushuang.nji@gmail.com )

"""
import base64
import json
import os
import random
import re
import time
import urllib.parse
import zlib
import chardet

import requests
from faker import Faker
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class VideoParse:
    """
    西瓜视频解析
    """

    def __init__(self, url: str):
        self._faker = Faker()
        self.ucontent = self._get_url(url)
        self.vcontent = ''
        self.def_dict = {}

    def _get_url(self, url: str) -> str:
        headers = {
            'User-Agent': self._faker.user_agent(),
        }
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            return response.text
        return ''

    def get_video_id(self) -> str:
        video_id = re.findall(r'"vid":"([\w\d]+)"', self.ucontent)
        return video_id[0] if video_id else ''
    
    def get_video_title(self) -> str:
        video_title = re.findall(r'<title data-react-helmet=\"true\">([\s\S]+)</title>\n', self.ucontent)
        return (video_title[0].encode("raw_unicode_escape").decode("utf-8") \
                if chardet.detect(video_title[0].encode("raw_unicode_escape"))['encoding'] == 'utf-8' \
                else video_title[0]) if video_title else ''
    
    def list_all_definition(self):
        content_dict = json.loads(self.vcontent)
        def_cnt = 0 # 计数
        print('Auto（输入', def_cnt, '）')
        for v in content_dict['data']['video_list'].values():
            def_cnt += 1
            print(v['definition'], "（输入", def_cnt, "） : ", v['vwidth'], "x", v['vheight'])
            self.def_dict[def_cnt] = v
    
    @staticmethod
    def get_main_url(video_id: str) -> str:
        r = ''.join(random.choices('0123456789', k=16))
        url = "/video/urls/v/1/toutiao/mp4/" + video_id + "?r=" + r
        s = str(zlib.crc32(url.encode()))
        url = "https://ib.365yg.com" + url + '&s=' + s
        return url

    def get_video_url(self, source_url, try_num=3):
        video_id = self.get_video_id()
        url = self.get_main_url(video_id)
        self.vcontent = self._get_url(url)
        content = json.loads(self.vcontent)
        if content.get('code') != 0:
            if try_num > 0:
                time.sleep(2)
                return self.get_video_url(source_url, try_num - 1)
            else:
                print(content.get('message'))
                return ''
        else:
            self.list_all_definition()
            def_opt = input("选择清晰度：")
            if def_opt != '': def_opt = int(def_opt)
            if def_opt in list(self.def_dict.values()): return base64.b64decode(self.def_dict[def_opt]['main_url']).decode()
            elif def_opt == 0 or def_opt == '': return base64.b64decode(list(self.def_dict.values())[-1]['main_url']).decode() # 选了 Auto 的情况


def download_file(name, url):
    print('开始下载')
    headers = {'Proxy-Connection': 'keep-alive'}
    r = requests.get(url, stream=True, headers=headers)
    length = float(r.headers['content-length'])
    with open(name, 'wb') as f:
        count = 0
        count_tmp = 0
        last_time = time.time()
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
                count += len(chunk)
                if time.time() - last_time > 2:
                    p = count / length * 100
                    speed = (count - count_tmp) / 1024 / 1024 / 2
                    count_tmp = count
                    print('{}下载{:.2f}%---{:.2f}M/s'.format(name, p, speed))
                    last_time = time.time()
        print('下载完成')


if __name__ == '__main__':
    print('直接回车测试 https://www.ixigua.com/i6704446868685849092')
    source_url = input('输入西瓜链接：')
    if not source_url:
        source_url = 'https://www.ixigua.com/i6704446868685849092'
            
    video_parse = VideoParse(source_url)
    print('开始解析')
    video_url = video_parse.get_video_url(source_url)
    print(video_url)
    video_name = video_parse.get_video_title() + '.mp4'
    download_file(video_name, video_url)
    # os.system('pause')
