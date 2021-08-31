import random

import requests
import json
import  datetime
import random

'''
批量创建课程（旧课）
'''
d=''.join(str(datetime.datetime.now().date()).split("-"))

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


for i in range(1,10):
    name=name+str(i)
    data=data.json({})


    print(name)

    name = d + "新建课程"


# host="https://test-codecamp-admin.codemao.cn/admin/courses/base"
#
# pyload={"preview_url":"https://dev-cdn-common.codemao.cn/dev/444/16303867610621.png"
# ,"video_url":"https://dev-cdn-common.codemao.cn/dev/444/163038679523220210827sight1564821_p1.m3u8",
# "real_video_url":"",
# "challenge_video_url":"",
# "bcm_url":"http://www.baidu.com",
# "name":"0831新建课程01",
# "type":8,
# "content_type":1,
# "lesson_type":1,
# "description":"1111"}
#
# print(json.dumps(pyload))