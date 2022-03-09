import os
import requests


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self, token):
        """Метод загружает файл на Яндекс диск"""
        loc_file = os.path.basename(self.file_path)
        with open(self.file_path, 'rb') as f:
            file = f.read()
        header = {'Authorization': 'OAuth ' + token}
        response = requests.get(f'https://cloud-api.yandex.net:443/v1/disk/resources/upload?path={loc_file}',
                                headers=header)
        link = response.json()['href']
        requests.put(link, data=file)
        return f'Файл {loc_file} успешно загрузился.'

if __name__ == '__main__':
    path_to_file = input('Введите путь к файлу: ')
    access_token = input('Введите OAuth-токен: ')
    uploader = YaUploader(path_to_file)
    result = uploader.upload(access_token)
    print(result)