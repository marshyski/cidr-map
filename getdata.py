import requests, os, tarfile

url = 'http://www.ipdeny.com/ipblocks/data/countries/all-zones.tar.gz'
tar = os.path.basename(url)
r = requests.get(url, stream=True)

if r.status_code == 200:
   f = open(tar, 'wb')
   f.write(r.content)
   f.close()

if tarfile.is_tarfile(tar):
    tarfile.open(tar).extractall('data')
else:
    print tar + " is not a tarfile"

os.remove(tar)
