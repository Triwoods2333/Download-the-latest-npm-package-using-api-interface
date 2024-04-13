import json
import requests

# 读取 JSON 文件
with open('result_info\\--data.txt', 'r') as f:
    data = json.load(f)
    print(data.get('time').get('created'))

download_path = 'download'

url = data.get('versions').get(data.get('dist-tags').get('latest')).get('dist').get('tarball')
res = requests.get(url)

with open('1.tgz', 'wb') as f:
    f.write(res.content)
