from lxml import etree
import urllib.request

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

def get_page_content(page):
    if(page == 1):
        url = 'https://sc.chinaz.com/tupian/nvshengtupian.html'
    else:
        #      https://sc.chinaz.com/tupian/nvshengtupian_3.html
        url = 'https://sc.chinaz.com/tupian/nvshengtupian_' + str(page) + '.html'
    request = urllib.request.Request(url=url, headers=headers)
    # 获取响应的数据
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def download_picture(download_picture):
    tree = etree.HTML(download_picture)
    # 此处同大多数网站一样，有懒加载，需要结合F12的NetWork的.html资源文件的response看
    imgs_src = tree.xpath('//div[@id="container"]//a//img//@src2')
    imgs_title = tree.xpath('//div[@id="container"]//a//img//@alt')
    for index in range(len(imgs_src)):
        image_url = 'https:' + imgs_src[index]
        image_title = imgs_title[index]
        urllib.request.urlretrieve(image_url, 'file/' + image_title + '.jpeg')

if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))

    for page in range(start_page, end_page + 1):
        # 请求对象的定制，获取页面内容
        content = get_page_content(page)
        # 下载
        download_picture(content)
