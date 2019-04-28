import requests
import json
from ftplib import FTP


requests.packages.urllib3.disable_warnings()

def download_video(url, title):
    i = requests.get(url=url, verify=False).content
    print(i)
    if i:
        with open(fr"C:\Users\heliang\Desktop\竟品\video\video_2019-02-24/{title}.mp4", mode="wb") as f:
            print("下载中")
            f.write(i)


class renre_nmovi(object):
    def __init__(self,id,Season):
        self.Season=Season
        self.movie_id=id
        self.check_text=["磁力","诚通网盘","电驴","百度云","范特西视频","微云"]
        self.xszr_movie_url=f"http://pc.allappapi.com/index.php?g=api%2Fpv2&m=index&a=resource&accesskey=519f9cab85c8059d17544947k361a827&id={self.movie_id}"
    def for_mat(self,data):
        # formants={}
        format_list=[]
        if data.get("way_name") in self.check_text:
            # formants[data.get("way_name")] = data
            format_list.append(data)
        return format_list
    def rr_request(self):
        try:
            rr=requests.get(self.xszr_movie_url).json()
            rr_dict={}
            for number in rr["data"]["list"]:
                if self.Season==number["season"]:
                    for i in number["episodes"]:
                        try:
                            movie_page=i["episode_name"]
                            movie_download=i["files"]
                            if movie_download.get("MP4"):
                                sort = list(map(self.for_mat, movie_download.get("MP4")))
                                rr_dict[movie_page]=[x for x in sort if not len(x) <= 0]
                                # rr_dict.append([x for x in sort if not len(x) == 0])
                            elif movie_download.get("APP"):
                                sort=list(map(self.for_mat,movie_download.get("APP")))
                                rr_dict[movie_page]=[x for x in sort if not len(x)<=0]
                                # rr_dict.append([x for x in sort if not len(x) == 0])
                            else:
                                print("找不到 MP4 或 APP 类")
                        except Exception as f:
                            print(number["season_name"],movie_page,f)
            return {key:values for key,values in rr_dict.items() if not len(values)<=0}
        except Exception as f:
            print("服务器异常了",f)
            return None



def baidu_url(url):
    try:

        token="6ea49a2118ead6836ca0fd60eee64919"
        baidu_u="https://dwz.cn/admin/v2/create"
        headers = {'Content-Type':'application/json', 'Token':token}
        bodys = {'url':url}
        baidu=requests.post(url=baidu_u,data=json.dumps(bodys),verify=False,headers=headers).json()
        assert baidu["Code"]==0 ,"转换URL失败"
        return baidu["ShortUrl"]
    except Exception as f:
        print(f)
        return baidu

def ftpconnect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, 21)
    ftp.login(username, password)
    return ftp

def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp_file=open(localpath,'rb')
    ftp.storbinary('STOR ' + remotepath, fp_file, bufsize)
    ftp.set_debuglevel(0)
    ftp.close()
def test(data):
    print(data)
    try:
        name = data.get("key")
        id = data.get("key1")
        print(name, id)
    except Exception as f:
        print('NO')


if __name__=="__main__":
    # rr=renre_nmovi("11057","1")
    # print(rr.rr_request())
    # print(baidu_url("http://baidu.com"))
    ftp = ftpconnect("h4999.gotoftp3.com", "h4999", "he1029")
    uploadfile(ftp, "/wwwroot/movie/The Walking Dead/1", r"C:\Users\heliang\PycharmProjects\Django\9.html")


    # print("[{'百度云': {'name': 'yyets://N=行尸走肉.The.Walking.Dead.S01E06.END.Chi_Eng.HR-HDTV.AC3.1024X576.x264-YYeTs人人影视.mkv|S=572311490|H=5638b8c7a34f8d144377df5cd353ae464f607769|', 'format': 'APP', 'size': '0', 'way': '102', 'address': 'http://pan.baidu.com/s/1jIJqifs', 'way_name': '百度云'}}, {'范特西视频': {'name': 'yyets://N=行尸走肉.The.Walking.Dead.S01E06.END.Chi_Eng.HR-HDTV.AC3.1024X576.x264-YYeTs人人影视.mkv|S=572311490|H=5638b8c7a34f8d144377df5cd353ae464f607769|', 'format': 'APP', 'size': '0', 'way': '114', 'address': 'http://www.onln.cn/video/play.html?tvId=19291&channelId=146', 'way_name': '范特西视频'}}]")