import ExtractURLs
import DownloadPDFs

if __name__ == '__main__':
    titles,urls=ExtractURLs.obtain_links()
    #print urls
    DownloadPDFs.download_files(titles,urls)