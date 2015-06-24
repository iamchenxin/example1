__author__ = 'z97'

import requests


def test():
    rt=requests.get("http://hq.sinajs.cn/list=s_sh000001")
    print(rt.text)

test();