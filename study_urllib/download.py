import urllib.request

# 图片 https://gss0.baidu.com/-fo3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/b999a9014c086e06992686100d087bf40bd1cbdb.jpg
# image_url = 'https://wkphoto.cdn.bcebos.com/d31b0ef41bd5ad6ecae1fe9791cb39dbb6fd3cb6.jpg'
image_url = 'https://gss0.baidu.com/-fo3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/b999a9014c086e06992686100d087bf40bd1cbdb.jpg'

urllib.request.urlretrieve(image_url, 'file/image_download1.jpeg')

# 视频
# video_url = 'https://acgqq.cyou/ptl.php?mb=dl&fid=9&cid=az385.html&pages=MTYyNDcyNTc4Ng'
#
# urllib.request.urlretrieve(video_url, 'video_download.mp4')