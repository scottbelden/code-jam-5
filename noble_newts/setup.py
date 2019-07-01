import tarfile
import requests
import os

def main():
    pwd = os.path.dirname(os.path.realpath(__file__))
    if not os.path.isdir(os.path.join(pwd, 'gsoy-latest')):
        os.mkdir('gsoy-latest')
        os.chdir('gsoy-latest')
        r = requests.get('https://www.ncei.noaa.gov/data/gsoy/archive/gsoy-latest.tar.gz', allow_redirects=True)
        open('gsoy-latest.tar.gz', 'wb').write(r.content)
        tar = tarfile.open("gsoy-latest.tar.gz")
        tar.extractall()
        tar.close()


if __name__ == "__main__":
    main()
