import requests


def get_latest_changes():
    index = 0
    try:
        f = open(f'result_final.txt', 'ab')
        response = requests.get('https://skimdb.npmjs.com/registry/_all_docs', stream=True, timeout=10)
        response.raise_for_status()
        for chunk in response.iter_content(chunk_size=8192):
            index += 1
            if index >= 0:
                f.write(chunk)

    except Exception:
        print('failed index:' + str(index))

get_latest_changes()