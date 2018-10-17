import requests
import json
import os
url = "http://124.243.205.129/rest/n/feed/hot?mod=Xiaomi%28MI%205s%29&lon=0&country_code=cn&extId=43efb37d00a190f480d7dfb58939997c&did=ANDROID_824d3a8c32b19c2e&net=WIFI&app=0&oc=XIAOMI&ud=0&c=XIAOMI&sys=ANDROID_7.0&appver=5.9.3.6975&ftt=&language=en-us&iuid=&lat=0&ver=5.9&did_gt=1539759241425&max_memory=256&type=7&page=1&coldStart=false&count=20&pv=false&id=11&refreshTimes=3&pcursor=&source=1&client_key=3c2cd3f3&os=android&sig=d436209d1f3717cd77bdbca61a6eae71"
fileSave_path = "F:\kuai_video"
max_count = 100 #计数 下载video个数

while max_count > 0:
    req = requests.request(method="GET", url=url)
    res_json = json.loads(req.text)
    try:
        for i in res_json["feeds"]:
            download_url = i["main_mv_urls"][0]["url"]
            print(download_url)
            r = requests.get(download_url)
            tag = i["share_info"]
            print(tag)
            with open(r"%s\%s.mp4" %(fileSave_path,tag) , "wb") as code:
                code.write(r.content)
            max_count = max_count - 1
            print(max_count)
    except KeyError as ke:
        print(i)






