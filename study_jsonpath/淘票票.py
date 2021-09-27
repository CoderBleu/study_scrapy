import urllib.request
import jsonpath
import json

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1630941897985_137&jsoncallback=jsonp138&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # 一般带冒号的都是不需要的
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?city=&_ksTS=1630941896599_48&jsoncallback=jsonp49&action=cityAction&n_s=new&event_submit_doLocate=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # utf-8格式
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': 't=d0c5ec57f69575f4fdd9d10ee62a9e36; cookie2=163a8b22904d7f83bb3749f847f6e420; v=0; _tb_token_=7f8d7dbeb189a; cna=TQwsGW2qRUgCAXFXpTpP/Tmp; xlly_s=1; isg=BAwM3yF3gWlQHpUVJMvxpM9-3Wo-RbDvRehI5GbNnbda8a37jVTif1YAlflJuehH; tfstk=cenlB0NBv4z7BAzm53ZSUL_2tNOAahLzNDoq0Ddp-4W_76iuUsXduNJEsKV-ZDQC.; l=eBOzTpwugMneJlHKBO5ZPurza77tiIRb8sPzaNbMiInca6ncTFZaLNCKzbFw7dtjgtCUTe-P_1j3WRHB-ZzdNxDDBeV-1NKmfxvO.',
    'referer': 'https://dianying.taobao.com/?spm=a1z21.3046609.header.1.32c0112aR1BaSB&n_s=new',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# 处理jsonp138数据，转json
content = content.split('(')[1].split(')')[0]

with open('file/淘票票.json', 'w', encoding='utf-8') as f:
    f.write(content)

json_object = json.load(open('file/淘票票.json', 'r', encoding='utf-8'))

region_name_list = jsonpath.jsonpath(json_object, '$..regionName')
print(region_name_list)