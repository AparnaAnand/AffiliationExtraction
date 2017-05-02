import ExtractURLs
import WriteCSV

if __name__ == '__main__':
    urls=ExtractURLs.obtain_links()
    WriteCSV.download_files(urls)