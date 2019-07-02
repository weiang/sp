import sys
from aip import AipSpeech

APP_ID = '16698730'
API_KEY = 'MVrXS46cNNB6nIiS0E8oCPGS'
SECRET_KEY = 'qIVBl4oViagQGlTt26zLC8ZLbPjo46tz'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fd:
        return fd.read()


def main():
    file_name = sys.argv[1]

    ret = client.asr(get_file_content(file_name), 'pcm', 16000, {
        'dev_pid': 1536,})

    print(ret)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s <pcm_file>" % (sys.argv[0]))
        sys.exit(1)

    main()
