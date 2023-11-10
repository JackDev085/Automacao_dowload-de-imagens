import requests
from bs4 import BeautifulSoup

search = str(input("What Imagens do you want to dowload? "))
num_of_img = int(input("How many images do you want to dowload? "))
directory= str(input('Directory: '))

links_list = []
img_list = []
img_index = 0

page_number = (num_of_img // 20)*20

url1 = f'https://www.google.com/search?q={search}&sca_esv=580857096&gbv=1&tbm=isch&sxsrf=AM9HkKlUPB3qJosNko3m5Tn4aeBce7k2PQ:1699538438965&source=lnms&sa=X&ved=0ahUKEwjt2b6HireCAxXkpJUCHbRGB0kQ_AUIBigB'

req = requests.get(url1)
soup = BeautifulSoup(req.text, 'html.parser')

for img in soup.find_all('img')[1:]:
    if img_index == num_of_img:
        break
    else:
        links_list.append(img.get('src'))
        img_index += 1

for links in links_list:
    img_list.append(requests.get(links))

for i, img in enumerate(img_list):
    with open(f'{directory}/{search}_{i}.png', 'wb')as f: #write byte
        f.write(img.content)

for pages in range(20, page_number+20,20):
    img_list= []
    links_list = []
    if img_index== num_of_img:
        break
    else:
        urln = f'https://www.google.com/search?q={search}&sca_esv=580857096&biw=627&bih=507&gbv=1&tbm=isch&sxsrf=AM9HkKndUxo0hVOFZO_p9qvmWlbebssR_w:1699535963504&ei=W9xMZZC4Hue95OUPt6-wwAU&start={pages}&sa=N'
        req = requests.get(urln)
        soup = BeautifulSoup(req.text, 'html.parser')
        for img in soup.find_all('img')[1:]:
            if img_index == num_of_img:
                break
            else:
                links_list.append(img.get('src'))
                img_index += 1

        for links in links_list:
            img_list.append(requests.get(links))

        for i, img in enumerate(img_list):
            with open(f'{directory}/{search}_{i+img_index-len(links_list)}.png', 'wb') as f:  # write byte
                f.write(img.content)
