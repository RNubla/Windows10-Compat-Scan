import requests, os
from tqdm import tqdm

class download_files():
    URL = 'https://docs.google.com/uc?export=download'
    HEADERS = {'Range' : 'bytes=0-'}

    def download_proper_file(id_param, file_name):
        id = id_param
        session = requests.Session()
        # response = session.get(download_files.URL, params = {'id' : id }, stream= True)
        response = session.get(download_files.URL, headers=download_files.HEADERS, params= {'id' : id}, stream = True)
        token = download_files.get_confirm_token(response)

        if token:
            params = {'id' : id, 'confirm' : token}
            # response = session.get(download_files.URL, params = params, stream = True)
            response = session.get(download_files.URL, headers=download_files.HEADERS, params=params, stream = True)

        download_files.save_response_content(response, file_name)

    @staticmethod
    def save_response_content(response, destination):
        CHUNK_SIZE = 1024
        content_header_range = response.headers['Content-Range']
        content_length = int(content_header_range.partition('/')[-1])
        # headers = response.headers['Content-Length']

        with open(destination, "wb") as f:
            progress_bar = tqdm(unit='B', unit_divisor=1024, unit_scale=1, total=int(content_length))
            for chunk in response.iter_content(chunk_size = CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    progress_bar.update(len(chunk))
                    f.write(chunk)

    @staticmethod
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None


if __name__ == "__main__":
    tempDir = 'C:\\Temp\\'
    downloadDir = tempDir
    os.chdir(downloadDir)
    download_files.download_proper_file('ID', './CompatScan.exe')
