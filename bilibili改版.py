import requests
from  moviepy.editor import * #moviepy 版本1.0.3


def  shipin(api):
    url = api
    user = {'user-agent':#输入user-agent 伪装
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"

                          ,"referer":#输入referer
                                      "https://www.bilibili.com/video/BV1NG3czWE76/?spm_id_from=333.1007.tianma.1-2-2.click&vd_source=1036824bc44626d60ba2ada5eb0ad244"
                                      }

    res = requests.get(url, headers=user)
    open("pq02.mp4", "wb").write(res.content)
    print(res.status_code)

def  yinpin(au):
    url = au
    user = {'user-agent': #输入user-agent 伪装
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"

                          ,"referer":#输入referer
                                      "https://www.bilibili.com/video/BV1NG3czWE76/?spm_id_from=333.1007.tianma.1-2-2.click&vd_source=1036824bc44626d60ba2ada5eb0ad244"
                                      }

    res = requests.get(url, headers=user)
    open("pq02.mp3", "wb").write(res.content)
    print(res.status_code)

yinpin("https://cn-hbwh-gd-bcache-03.bilivideo.com/upgcxcode/80/94/30758799480/30758799480-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&platform=pc&mid=316780251&oi=1865446074&gen=playurlv3&os=bcache&trid=0000ab50bd4f20214fbd86b5c38730954b6u&deadline=1751254677&nbs=1&uipk=5&og=cos&upsig=d1eea7b8a93021b1eef054f8abd2fa70&uparams=e,platform,mid,oi,gen,os,trid,deadline,nbs,uipk,og&cdnid=3762&bvc=vod&nettype=0&bw=183898&buvid=39618FFD-9D16-0013-6436-3E3B35C9FEFF21241infoc&build=0&dl=0&f=u_0_0&np=151388294&agrr=1&orderid=0,3")
#输入音频url 调用函数yinpin
shipin("https://cn-hbwh-gd-bcache-05.bilivideo.com/upgcxcode/80/94/30758799480/30758799480-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&deadline=1751254677&nbs=1&trid=0000ab50bd4f20214fbd86b5c38730954b6u&gen=playurlv3&os=bcache&og=cos&mid=316780251&uipk=5&platform=pc&oi=1865446074&upsig=5d85d65bf227fb2abad1eedf4382293d&uparams=e,deadline,nbs,trid,gen,os,og,mid,uipk,platform,oi&cdnid=3764&bvc=vod&nettype=0&bw=2038723&buvid=39618FFD-9D16-0013-6436-3E3B35C9FEFF21241infoc&build=0&dl=0&f=u_0_0&np=151388294&agrr=1&orderid=0,3")
#输入视频url 调用函数shipin

#调用moviepy将视频与音频合起来
video = VideoFileClip("pq02.mp4")
audio = AudioFileClip("pq02.mp3")

sp = video.set_audio(audio)
sp.write_videofile("爬虫视频02.mp4")
