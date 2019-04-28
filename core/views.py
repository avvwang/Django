from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
from .functions import *
# Create your views here
import random
import json
from django.views.decorators.cache import cache_page, cache_control, never_cache
from .functions import test

def vivo(request):
    imei=request.GET.get("name")
    # url='https://video.vivo.com/list/catetory/video?vName=1.0.0&vApp=10000&dpi=480.0&categoryId=90005&carrier=%E7%A7%BB%E5%8A%A8&mac=00dbdf581f8f&from=1&net=1&appName=vivo%E8%A7%86%E9%A2%91&density=3.0&refreshCount=1&av=22&androidId=4f801605c5e500dd&t=1552103303163&imei=868453039993133&resolution=1080x1920&pName=com.vivo.video&vOs=5.1.1&model=xiaomi+6&s=2%7C4129876101%22'
    url=f"https://video.vivo.com/list/shortvideo/recommend?area=118.759404_31.983224&vName=1.1.1.0&density=3.0&appName=vivo%25E8%25A7%2586%25E9%25A2%2591&resolution=1080x2280&ft=1539575516790&mac=ae6f6909c4d8&carrier=%25E6%259C%25AA%25E7%259F%25A5&pName=com.android.VideoPlayer&t=1542985829161&av=27&imei={imei}&from=1&model=vivo%2BX21A&vOs=8.1.0&dpi=480.0&net=1&vApp=10110&androidId=7efb9fb05216e443&s=2%257C838396164&refreshCount=10&categoryId=90001"
    vivo=requests.get(url,verify=False).json()
    vivo_dict = {}
    choice=["likecount","commentcount","playCount"]
    for num,i in enumerate(vivo["data"]["videos"]):
        if i["type"]==1:
            title=str(i["basic"]["title"]).replace("\\","").replace("?","").replace("/","")[0:29]
            videoid=i["videoId"]
            likecount=i["basic"]["likedCount"]
            commentcount=i["basic"]["commentCount"]
            playurl=i["shareUrl"]
            download_url=i["play"]["urls"][0]
            playCount=i["basic"]["playCount"]
            vivo_dict[videoid]={"title":title,"likecount":likecount,"commentcount":commentcount,"playCount":playCount,"download_url":download_url}
            # print (title,downloads)
    sort=sorted(vivo_dict.items(),key=lambda x:x[1][random.choice(choice)],reverse=True)[:5]
    # print(type(sort),sort)
    # zip_sort=dict(zip(sort[0],sort[1]))
    # for index,data in enumerate(sort):
    #     print (data[0],data[1])
    k={data[0]:data[1] for index,data in enumerate(sort)}
    for values in k.values():
        # pass
        # 868451338
        download_video(values["download_url"],values["title"])
    print(k)
    # for key,values in sort[0].items():
    #     download(values["downloads"],values["title"])
    # return JsonResponse({"code":"successe"})
    # for value in k.values():
    #     download_video(value["download_url"],value["title"])

    return JsonResponse(k)

    # return render(request,"index.html",context={"data":k})



def ajax(request):
    return JsonResponse({"code":221})
    i=requests.get("http://127.0.0.1:8080/rrmovie?num=2").content
    with open("1.html",mode="wb")as f:
        f.write(i)
    return render(request,"index.html")



def html_updata(request):
    host=request.headers["Host"]
    num=request.GET.get("num")
    if num:
        i = requests.get(f"http://{host}/rrmovie?num={num}").content
        if len(i)==10:
            return JsonResponse({"msg":"下载的数据为空"})
        else:
            with open(fr"C:\Users\heliang\PycharmProjects\Django\XXOO\down_movie/{num}.html" ,mode='wb')as f:
                f.write(i)
            ftp = ftpconnect("h4999.gotoftp3.com", "h4999", "he1029")
            uploadfile(ftp, f"/wwwroot/movie/The Walking Dead/{num}.html",fr"C:\Users\heliang\PycharmProjects\Django\XXOO\down_movie/{num}.html")
    return JsonResponse({"msg":"更新下载完成"})



@cache_page(60 * 15)
def rr(request):
    num=request.GET.get("num")
    rr=renre_nmovi("11057",num)
    index=rr.rr_request()
    # return JsonResponse(index)
    print(index)
    if index:
        return render(request,template_name="movie.html",context={"data":index})
        # return JsonResponse(r)
    else:
        return JsonResponse({"msg":1})
    print(request)


def data_table(request):
    return render(request,"core_templates/data.html")


def Check(request):
    print(request.body)
    # row=request.POST.get("row-1-age")
    str1=str(request.body.decode())
    count=0
    data = {}
    for i in str1.split("&"):
        key=str(i).split("=")
        count=count+1
        data[key[0]] = key[1]
        if count % 3==0:
            test(data)
            print(data)
    return JsonResponse({"code":111})


def add(request):
    id=request.GET.get("id")
    print(id)
    return render(request,"core_templates/info.html",context={"name":id})


def index(request):
    return render(request,"core_templates/index.html")