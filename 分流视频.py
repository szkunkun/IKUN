import requests
from moviepy.editor import *

shade = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0","referer":"https://www.bilibili.com/video/BV1MBK8zhEjm/?spm_id_from=333.1365.list.card_archive.click&vd_source=1036824bc44626d60ba2ada5eb0ad244"}
#伪装  user-agent referer
num = 0
while True:
    bianliang = "{:05d}".format(num)

    url = f"https://tx-safety-video.acfun.cn/mediacloud/acfun/acfun_video/1f14be7fad8ed3b0-2fe25c901d2e2ad60ddc49c1d8dbdb0b-hls_720p_2.{bianliang}.ts?pkey=ABDjhWu6IkcVKNbg3AFo5tlNzRziauKfQCjTAcQUmtA6rm5b2lzlSdUKZ1UjuBuP6S00A4q657v5a1cV3k2TcL8XgiI_JgXQ38DTAmKc08majSoeNo1BJ5dLvtywKx3kZMakroREpSgx7E1vaYc6Kwp-yW7-gn9CpBpTsxC0VNG1GyRcIwrVWzM3fXItKwK5azM-G6YXLNQmmyB_9Q2BGNmIQkoTU3T8HDMgp3OTVDDitcLsMi0Ox3ZXeX-7Gl2nwac&safety_id=AAINdBINrDy6nYO8geqx5_Lk"

    res = requests.get(url, headers=shade)

    if res.status_code == 404:
        print("视频已经循环完毕")
        break

    open(f"分流视频/{num}.ts", "wb").write(res.content)
    num += 1
    print(f"以下载{num}段")
print(f"{num}段视频已下载完毕")

video_clips = []
for shipin in range(num):
    video = VideoFileClip(f"分流视频/{shipin}.ts")
    video_clips.append(video)

final = concatenate_videoclips(video_clips)
final.write_videofile("分流视频/完整视频.mp4")
print("完整视频以下载完毕")

