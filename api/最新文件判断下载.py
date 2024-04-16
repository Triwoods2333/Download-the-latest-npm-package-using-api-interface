import os
import json
import requests
from datetime import datetime, timezone

# 指定设定的时间
specified_time = datetime(2024, 1, 1, tzinfo=timezone.utc)  # 设定为2022年1月1日UTC时间

# 指定文件夹路径
folder_path = 'result_info'

# 获取文件夹中所有文件的文件名
file_names = os.listdir(folder_path)

# 循环遍历每个文件
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    
    # 读取 JSON 文件
    with open(file_path, 'r') as f:
        data = json.load(f)
        file_created_time = datetime.fromisoformat(data.get('time').get('created')).replace(tzinfo=timezone.utc)

        # 比较时间并输出比较信息
        if file_created_time > specified_time:
            print(f"{file_name}: 文件创建时间晚于设定时间")
        elif file_created_time < specified_time:
            print(f"{file_name}: 文件创建时间早于设定时间")
        else:
            print(f"{file_name}: 文件创建时间与设定时间相同")

    download_path = 'download'

    url = data.get('versions').get(data.get('dist-tags').get('latest')).get('dist').get('tarball')
    res = requests.get(url)

    # 使用读取的文件名作为保存文件的文件名
    file_name_without_extension = os.path.splitext(file_name)[0]
    save_file_path = os.path.join(download_path, f"{file_name_without_extension}.tgz")

    with open(save_file_path, 'wb') as f:
        f.write(res.content)
