import requests


def get_latest_changes():
    try:
        response = requests.get('https://skimdb.npmjs.com/registry/_all_docs', stream=True)
        response.raise_for_status()  # 检查请求是否成功
        for chunk in response.iter_content(chunk_size=8192):
            # 在这里处理每个数据块
            # 例如，将数据块写入文件或进行其他处理
            f = open(f'result_final.txt', 'ab')
            f.write(chunk)

    except requests.exceptions.RequestException as e:
        print('API request failed:', str(e))


get_latest_changes()
