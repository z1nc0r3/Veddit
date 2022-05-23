import requests
import bs4
import os
import re
from termcolor import colored

print("""\        
███████╗░░███╗░░███╗░░██╗░█████╗░░█████╗░██████╗░██████╗░
╚════██║░████║░░████╗░██║██╔══██╗██╔══██╗██╔══██╗╚════██╗
░░███╔═╝██╔██║░░██╔██╗██║██║░░╚═╝██║░░██║██████╔╝░█████╔╝
██╔══╝░░╚═╝██║░░██║╚████║██║░░██╗██║░░██║██╔══██╗░╚═══██╗
███████╗███████╗██║░╚███║╚█████╔╝╚█████╔╝██║░░██║██████╔╝
╚══════╝╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
                    """)

def downloader(link) : 

    proxies = {
        'http': 'http://127.0.0.1:1081',
        'https': 'http://127.0.0.1:1081'
    }

    link = "https://redditsave.com/info?url=" + link

    res = requests.get(link, proxies=proxies)
    bs = bs4.BeautifulSoup(res.text, "html.parser")

    url = bs.find("a", {"class" : "downloadbutton"})["href"]
    title = bs.find("h2", {"class" : "text-center text-truncate"}).text.strip()
    title = re.sub(r"[/\*:?\"\|<>]", " ", title)

    print(title + " - Downloading...")

    os.system(f'aria2c.exe -d Download -o "{title}.mp4" --continue=true --all-proxy=http://127.0.0.1:1081 --summary-interval=0 --retry-wait=10 --console-log-level=error "{url}"')

    print()
    

while True:
    try :
        downloader(input(colored('\nEnter the video link : ', 'green', attrs=['bold'])))
    except:
        print("An error occured! Please try again.")