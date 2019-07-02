import sys
from aip import AipSpeech

APP_ID = ''
API_KEY = ''
SECRTE_KEY = ''
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fd:
        return fd.read()


def main():
    file_name = sys.argv[1]

    ret = client.asr(get_file_content(file_name), 'pcm', 16000, {
        'dev_pid': 1536,})

    print ret


if __name__ == '__main__':
    main()
