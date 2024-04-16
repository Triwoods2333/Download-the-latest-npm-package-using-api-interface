import requests
import sys
import time
sys.setrecursionlimit(1000000)

f = open(f'result_final.txt', 'ab')
error_index = 0
def get_latest_changes():
    global f,error_index
    print("starting")
    now_index = 0
    try:
        response = requests.get('https://skimdb.npmjs.com/registry/_all_docs', stream=True, timeout=10)
        response.raise_for_status()
        for chunk in response.iter_content(chunk_size=8192):
            now_index += 1
            print(error_index)
            print(now_index)
            if now_index >= error_index:
                f.write(chunk)

    except Exception:
        if now_index >= error_index:
            error_index = now_index
        print('failed index:' + str(error_index))
        print('restart...')
        time.sleep(10)
        get_latest_changes()

get_latest_changes()
