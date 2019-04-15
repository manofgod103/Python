import urllib.request
urllib.request.urlretrieve("http://www.baidu.com", filename=r"D:\Python study\WorkSpace\Python\file01.html") # 文件名为你的想要写入的地址

# urlretrieve在执行的过程中,会产生一些缓存
# 清除缓存
urllib.request.urlcleanup()

