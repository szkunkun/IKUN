import requests
from  moviepy.editor import *


def  shipin(api):
    url = api
    user = {'user-agent':
                           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"

                          ,"referer":
                                      "https://www.douyin.com/"
                                      }

    res = requests.get(url, headers=user)
    open("douyin01.mp4", "wb").write(res.content)
    print(res.status_code)


shipin(
" https://v26-web.douyinvod.com/856385e2916f80e16942b26f668f4ff4/68622ac6/video/tos/cn/tos-cn-ve-15/osHHBXeGEg067BPByIy4eTRaoCjAMIZ5LAebRA/?a=6383&br=281&bt=281&btag=c0000e00030000&cd=0%7C0%7C0%7C3&ch=26&cquery=100B_100x_100z_100o_100w&cr=3&cs=0&cv=1&dr=0&ds=6&dy_q=1751252693&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&ft=GN7rKGVVyw3nRKo80mo~MWwQlcfySL92bLUx0wYiZmkaY3&is_ssr=1&l=20250630110453E69DAFDD3C0A3094834C&lr=all&mime_type=video_mp4&qs=12&rc=NzVmZGhmNjw5PDYzZTg3OkBpM25xO3c5cmVneDMzNGkzM0BeMzIuMzFeXi8xNl80LjBiYSNjLWIzMmRjM2dgLS1kLS9zcw%3D%3D&__vid=7468889377976962367")
