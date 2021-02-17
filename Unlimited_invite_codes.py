#!/usr/bin/python
import requests,base64,json
url = "https://www.hackthebox.eu/api/invite/generate"
num = int(input('Enter the number of invite codes: '))
invites=[]
for i in range(0,num):
        headers = {'User-Agent': ''}
        result = requests.post(url,headers=headers)  
        data = json.loads(result.text)
        parse = data['data']['code']
        decodedBytes =(base64.b64decode(parse))
        decodedStr = str(decodedBytes, "utf-8")
        invites.append(decodedStr)
count=1
for i in invites:
        print(f'Invite code {count}:',i)
        count+=1








