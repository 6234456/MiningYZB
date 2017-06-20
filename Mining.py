import urllib.request, urllib.parse, urllib.error, os, threading

class Downloader(threading.Thread):
    def __init__(self,  url, destination, start=0, ende = 100, idx = "0"):
        threading.Thread.__init__(self)
        self.url = url
        self.destination = destination
        self.starter = start
        self.ende = ende
        self.idx = idx
    def run(self):
        print(self.starter)
        download(self.url, self.destination, start = self.starter, ende = self.ende, idx= self.idx)

def init_Donwloader(url, destination, total = 400, start = 0, threads = 2):
    singlePiece = int((total-start + 1)/threads)
    for i in range(threads):
        upper = start + (i+1) * singlePiece
        Downloader(url, destination, start= start + i * singlePiece, ende=upper, idx = str(i)).start()
        print("Downloader " + str(i) + " initiated. " + str(start + (i+1) * singlePiece))

def download(src, destination, ende = 100, start = 0, oncomplete = None, prefix = ".ts", idx = "0"):
    fileName = "0" * (3-len(str(start)))  + str(start) + prefix
    serverFileName = str(start) + prefix
    url = src + serverFileName
    parallel(url, destination + fileName, idx)
    start += 1

    if ende >= start:
       download(src, destination, ende=ende, start=start,oncomplete=oncomplete, prefix=prefix, idx=idx)

def parallel(url, destination, idx = "0"):
    try:
        urllib.request.urlretrieve(url, destination)
        print("Download of " + url + " complete." + " Downloader " + idx)
    except:
        print("Error: " + url)

def join_parts(destionation, targetFile):
    print(r"copy /b " +  destionation + "*.ts " + targetFile)
    #os.system(r"copy /b " +  destionation + "*.ts " + targetFile)

if __name__ == '__main__':
    src = "http://alcdn.hls.xiaoka.tv/2017618/2a1/2ba/JXQcKsEEYA8mKPZV/"
    p = "C:\\Users\\Qiou\\Documents\\src\\v5\\"
    targetFile = r"C:\Users\Qiou\Documents\src\joined_files.ts"
    #download(src, p, toContinue=lambda x:x<18, start=2)
    init_Donwloader(src, p, total=450, start=0, threads=3)
    join_parts(p, targetFile)
