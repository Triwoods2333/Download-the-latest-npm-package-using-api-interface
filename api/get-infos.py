import requests
import json

# 读取txt文件
with open('result_final.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 尝试将内容解析为JSON对象（这里假设内容已经是有效的JSON格式）
try:
    data = json.loads(content)
    # 如果txt文件的内容不是标准的JSON格式，可能需要先进行预处理，转换为有效的JSON格式，然后再进行解析。
    for row in data.get('rows'):
        url = 'https://skimdb.npmjs.com/' + row.get('id')
        print(url)
        r = requests.get(url)
        datax = r.text
        print(datax)
        file = open('result_info\\'+row.get('id') + '-data.txt', 'w')
        file.write(datax)
    
except json.JSONDecodeError as e:
    print("解析JSON时出错:", e)  # 如果内容不是有效的JSON格式，这里会抛出异常

