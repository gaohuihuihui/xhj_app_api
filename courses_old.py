import random

import requests
import json
import  datetime
import random

'''
批量创建课程（旧课）
'''

host="https://test-codecamp-admin.codemao.cn/admin/courses/base"

d=''.join(str(datetime.datetime.now().date()).split("-")) #获取当前日期（例如：0831）
preview_url="https://dev-cdn-common.codemao.cn/dev/444/16303867610621.png"
video_url="https://static-k12edu.codemao.cn/codecamp/HygzMgYWpQ.m3u8"
real_video_url=""
challenge_video_url=""
bcm_url="https://static.codemao.cn/nemo/BJCXohekL.bcm"
name=d+"新建课程"
type="8"
content_type="1"
lesson_type="1"
description="脚本教程数据"


headers = {
  'Content-Type': 'application/json',
  'Authorization':"Bearer+eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3R5cGUiOiJhZG1pbiIsInVzZXJfaWQiOjc0MzEsImlhdCI6MTYzMDM1NzczNiwianRpIjoiOGIyODgwNGMtMGExOS0xMWVjLThiYmQtNmQ1ODU2YmFhNTBiIn0.IHTGK-a7yhtcePDFeALu2IvgZUfIE3KR4xnbeQ4n7K4"
}

for i in range(1,2):
    name=name+str(i)
    data=json.dumps({"preview_url":preview_url,"video_url":video_url,"real_video_url":real_video_url,"challenge_video_url": challenge_video_url,
                     "bcm_url":bcm_url,"name":name,"type":type,"content_type":content_type,"lesson_type":lesson_type,
                     "description":description
                     })
    re=requests.request("POST",headers=headers,url=host,data=data)

    print(re.request.url)
    print(re.request.body)
    print(re.status_code)
    print(re.text)
    name = d + "新建课程"


