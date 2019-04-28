#coding:utf-8
import requests
url="http://pc.allappapi.com/index.php?g=api%2Fpv2&m=index&a=resource&accesskey=519f9cab85c8059d17544947k361a827&id=11057"
import json

class renre_nmovi(object):
    def __init__(self,id="11057",Season=9):
        self.Season=Season
        self.movie_id=id
        self.check_text=["磁力","诚通网盘","电驴","百度云","范特西视频"]
        self.xszr_movie_url=f"http://pc.allappapi.com/index.php?g=api%2Fpv2&m=index&a=resource&accesskey=519f9cab85c8059d17544947k361a827&id={self.movie_id}"
    def for_mat(self,data):
        formants={}
        if data.get("way_name") in self.check_text:
            formants[data.get("way_name")] = data
        return formants
    def rr_request(self):
        try:
            rr=requests.get(self.xszr_movie_url).json()
            rr_dict={}
            for number in rr["data"]["list"]:
                if int(self.Season)==int(number["season"]):
                    for i in number["episodes"]:
                        try:
                            movie_page=i["episode_name"]
                            movie_download=i["files"]
                            if movie_download.get("MP4"):
                                sort = list(map(self.for_mat, movie_download.get("MP4")))
                                rr_dict[movie_page]=[x for x in sort if not len(x) == 0]
                            elif movie_download.get("APP"):
                                sort=list(map(self.for_mat,movie_download.get("APP")))
                                rr_dict[movie_page]=[x for x in sort if not len(x)==0]
                            else:
                                print("找不到 MP4 或 APP 类")
                        except Exception as f:
                            print(number["season_name"],movie_page,f)
                else:
                    pass
                    # print(self.Season,self.movie_id,number["season"],"没有查到任何信息")
            return rr_dict
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


def sain_rul(url):
    try:
        url=f"http://api.t.sina.com.cn/short_url/shorten.json?source=3271760578&url_long={url}"
        get_url=requests.get(url).json()
        return get_url[0]["url_short"]
    except Exception as f:
        print(f)
        return None

if __name__=="__main__":
    # rr=renre_nmovi("11057","1")
    # print(rr.rr_request())
    import time
    a=time.time()
    time.sleep(1)
    b=time.time()

    print(b-a)