import platform
import os, shutil, os.path, re, subprocess, io, requests, os.path
import zipfile
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
        
class ExtractZip():
    Zip32 = 'Compat32.zip'
    Zip64 = 'Compat64.zip'

    def extract_win(zip_ver):
        with zipfile.ZipFile(zip_ver) as zf:
            for i in tqdm(zf.infolist(), unit_divisor=1024, desc='Extracting... '):
                try:
                    zf.extract(i)
                except zipfile.error as e:
                    pass
        os.remove(zip_ver)

class RunCompatScans():
    def compat_scan(win10_dir):
        FNULL = open(os.devnull, 'w')
        setup_exe = 'setup.exe'
        os.chdir(win10_dir)
        args = os.getcwd() + os.sep + setup_exe + ' /Auto Upgrade /Quiet /NoReboot /DynamicUpdate Disable /Compat ScanOnly /CopyLogs ' + os.path.normpath(os.getcwd() + os.sep + os.pardir) + '\Compat.Logs'
        print(args)
        subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=True)
        
        compat_log = os.path.normpath(os.getcwd() + os.sep + os.pardir) + '\Compat.Logs\Panther\setuperr.log'

        errors= []
        linenum = 0
        substr = "0xC1900".lower()
        with open(compat_log, 'rt') as myfile:
            for line in myfile:
                linenum += 1
                if line.lower().find(substr) != -1:
                    errors.append(line.rstrip('\n'))

        results_to_text.console_info()
        stringCode = errors[1]

        errorCode = re.search('0[xX][0-9a-fA-F]+', stringCode)
        results_to_text.results('Result:' +(errorCode)[0])
        print('Result: '+(errorCode)[0])
    
class get_os_architecture():

    def os_version():
        arch = subprocess.run('cmd /c "wmic os get osarchitecture', stdout=subprocess.PIPE)
        bit_ver_substr = str(arch.stdout)
        start_with = bit_ver_substr.find('n')+1
        ends_with = bit_ver_substr.find('-', start_with)
        arch_version = bit_ver_substr[start_with:ends_with]
        return int(arch_version)
        # print(arch_version)

class results_to_text():
    def results(results_output):
        with open(os.path.normpath(os.getcwd() + os.sep + os.pardir)+ os.sep + 'Win10_Compat.txt', 'w') as text_file:
            text_file.write(results_output)

    def console_info():
        return print('------------------------------------------------------------------------------------------------------\n'
        + 'No issues found:----------------------------------------------------------------------------0xC1900210\n'
        + 'Compatibility issues found (hard block):----------------------------------------------------0xC1900208\n'
        + 'Migration choice (auto upgrade) not available (probably the wrong SKU or architecture)------0xC1900204\n'
        + 'Does not meet system requirements for Windows 10:-------------------------------------------0xC1900200\n'
        + 'Insufficient free disk space:---------------------------------------------------------------0xC190020E\n'
        + '------------------------------------------------------------------------------------------------------')

if __name__ == "__main__":
    # print(get_os_architecture.os_version())
    # get_os_architecture().os_version
    tempDir = 'C:\\Temp\\'
    toolDir = 'C:\\Temp\\tools'
    if not os.path.exists(toolDir):
        os.makedirs(toolDir)
        os.chdir(toolDir)
    else:
        os.chdir(toolDir)
    # print(os.getcwd())
    
    # if platform.architecture()[0] == "32bit":
    if get_os_architecture.os_version() == 32:
        print('32 Bit')
        download_files.download_proper_file('1jHQDJiqgLBAjpD3lsSTx37XWesphPa2i', './Compat32.zip')
        ExtractZip.extract_win('Compat32.zip')
        current_dir = os.path.normpath(os.getcwd())
        RunCompatScans.compat_scan((current_dir + os.sep + 'Win1032'))
        after_scan_dir = os.path.normpath(os.getcwd())
        shutil.rmtree(after_scan_dir + os.sep + 'Win1032')
    # elif platform.architecture()[0] == "64bit":
    elif get_os_architecture.os_version() == 64:
        print('64 Bit')
        download_files.download_proper_file('1te-8WRROCyIths4PM7q0nR4pT7RWDIpQ', './Compat64.zip')
        ExtractZip.extract_win('Compat64.zip')
        current_dir = os.path.normpath(os.getcwd())
        RunCompatScans.compat_scan(current_dir + os.sep + 'Win1064')
        after_scan_dir = os.path.normpath(os.getcwd())
        shutil.rmtree(after_scan_dir + os.sep)
        
