from bs4 import BeautifulSoup
import urllib
import os
import sys
import requests



def comic_downloader():
    main_url="http://theoatmeal.com/comics_pg/page:2"
    source_code=requests.get(main_url)
    plain_text=source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for comiclink in soup.findAll('a'):
        alllink=comiclink.get('href')
        split_links = alllink.split('/')
        split_len=split_links.__len__()
        if split_links[1]=='comics' and split_len== 3:
            href1='http://theoatmeal.com/comics/'+str(split_links[2])
            #print(href1)
            download(href1)





def download(href4):

    main_url_opener=urllib.request.urlopen(href4)
    main_url_response=main_url_opener.read()
    main_url_soup=BeautifulSoup(main_url_response,"html.parser")
    for img_link in main_url_soup.findAll('img'):
        mylink=img_link.get('src')
        split1 =mylink.split('/')
        if split1[4]=="comics":
            nameofthecomics=split1[5]
            print(nameofthecomics)
            print(mylink)
            filename=split1[5]+split1[6]
            print(filename)
            open_img = urllib.request.urlopen(mylink)
            img_data = open_img.read()
            comic_dir = 'C:\\Users\\ALOK\\PycharmProjects\\crawler'
            filepath=os.path.join(comic_dir,nameofthecomics)
            print(filepath)
            comic_path=os.path.join(filepath,filename)
            print(comic_path)
            if not os.path.exists(filepath):
                os.makedirs(filepath)
                print('making directory')
            else:
                 print('directory already present')

            with open(comic_path,"w",encoding='utf-8') as file:
                file.write(str(img_data))
                print('downloading'+ str(filename))


comic_downloader()
