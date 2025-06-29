import urllib.request


def download_image(url, filename):
    name = filename + ".jpg"
    urllib.request.urlretrieve(url, name)

download_image('https://img.shetu66.com/2022/11/03/1667459511305837.jpg','1')