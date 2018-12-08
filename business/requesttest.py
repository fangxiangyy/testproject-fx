# coding = utf-8
import requests

url = 'http://localhost:8080/regist1'
postData = {'username':'tt1','password':'tt1'}
response = requests.post(url,data='username=tt1&password=tt1')
content = response.json()
print(response.text)
print(content)

