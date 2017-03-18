import zipfile, time, os

name = str(input('Define name of zip in quotes: ')) + '.zip'
direc = str(input('Define source directory in quotes: '))

def zipdir(path, ziph):
    # ziph = zip handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile(name, 'w', zipfile.ZIP_DEFLATED)
    zipdir(path=direc, ziph=zipf)
    zipf.close()

