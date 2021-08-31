import requests
import json

url = "https://dev-codecamp-admin.codemao.cn/admin/courses"

payload = json.dumps({
  "description": "探月测试111",
  "knowledge_url": "https://codemaster-teaching-material.codemao.cn/课程课程知识点图-年课-暂用_1562059059992.jpg",
  "medal_img_url": "https://static-k12edu.codemao.cn/codecamp_sign_medal4_nor@3x.png",
  "medal_name": "运算勋章",
  "name": "探月测试课程20",
  "preview_url": "https://static-k12edu.codemao.cn/codecamp/beta/preview-4.png",
  "type": 8,
  "video_url": "https://static-k12edu.codemao.cn/codecamp/video/NnjbuB87x5ct6PL_p4.m3u8",
  "bcm_url": "https://static-k12edu-kids.codemao.cn/kids/1551073818365"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo4NDYsInVzZXJfdHlwZSI6ImFkbWluIiwianRpIjoiMzJkYzNlNmMtMTk1My00MGVkLWJmOTMtMmM3OGU0YzU5ZDUxIiwiaWF0IjoxNTcxNDc2MTU0fQ.CsUEo0ns5rb2iAWn5TFqpEQQLLqix4EOvS1avY-e7tE'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
