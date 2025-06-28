#以https://www.bilibili.com/video/BV1zHK3zbEqp/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=1036824bc44626d60ba2ada5eb0ad244为例
import requests #导入requests


url = "https://upos-sz-mirrorbd.bilivideo.com/upgcxcode/63/61/25816536163/25816536163-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&mid=316780251&gen=playurlv3&og=hw&trid=a8e852ecd7cd4d148113a9e2e8d1a6bu&deadline=1751107605&nbs=1&uipk=5&oi=1734601228&os=bdbv&platform=pc&upsig=f136de9b6b94ebc8db27f4f81d21056d&uparams=e,mid,gen,og,trid,deadline,nbs,uipk,oi,os,platform&bvc=vod&nettype=0&bw=707361&build=0&dl=0&f=u_0_0&agrr=1&buvid=39618FFD-9D16-0013-6436-3E3B35C9FEFF21241infoc&orderid=0,3"
#通过f12进入控制台找到视频url 100026
shade = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0","referer":"https://www.bilibili.com/video/BV1zHK3zbEqp/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=1036824bc44626d60ba2ada5eb0ad244"}
#伪装user-agent referer
res = requests.get(url, headers=shade)
#将伪装放入请求内发出
open("pq.mp4","wb").write(res.content)
#保存视频到本地 wb 写入
url = 'https://xy58x19x152x2xy.mcdn.bilivideo.cn:8082/v1/resource/25816536163-1-30280.m4s?agrr=1&build=0&buvid=39618FFD-9D16-0013-6436-3E3B35C9FEFF21241infoc&bvc=vod&bw=185535&deadline=1751107605&dl=0&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv3&mid=316780251&nbs=1&nettype=0&og=cos&oi=1734601228&orderid=0%2C3&os=upos&platform=pc&sign=664652&traceid=trhxYmbvYbWewf_0_e_N&uipk=5&uparams=e%2Coi%2Cplatform%2Ctrid%2Cdeadline%2Cog%2Cnbs%2Cmid%2Cgen%2Cos%2Cuipk&upsig=d4f0a3ab23d16fce11e62b4e9be13f6d'
#通过f12进入控制台找到音频url 30280

shade = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0","referer":"https://www.bilibili.com/video/BV1zHK3zbEqp/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=1036824bc44626d60ba2ada5eb0ad244"}
#伪装user-agent referer
res = requests.get(url, headers=shade)
#将伪装放入请求内发出
open("pq.mp3","wb").write(res.content)
#保存音频到本地 wb 写入
from  moviepy.editor import *
#调用moviepy将视频与音频合起来
video = VideoFileClip("pq.mp4")
audio = AudioFileClip("pq.mp3")

sp = video.set_audio(audio)
sp.write_videofile("爬虫视频.mp4")

print(res.status_code)
