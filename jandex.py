import  requests
name = input('write path to file: ')
with open(f'{name}', 'rb') as f:
    list_ = [name]
    for i in list_[0]:
        if i == '/':
            index = list_[0].index(i)
            break
    name_of_file = list_[0][index:]
    resp = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={name_of_file}&overwrite=true',
                        headers={"Authorization": ""}) # <--your token
    resp_2 = requests.put(resp.json()['href'], files={"file": f})