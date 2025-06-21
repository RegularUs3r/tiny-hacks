from requests import get
from urllib3 import disable_warnings
from argparse import ArgumentParser
from bs4 import BeautifulSoup

disable_warnings()
def finder(target):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0"}
    if target[-1] != "/":
        print("[!] You're missing a slash")
    else:
        x = get(target, 
                headers=headers,
                verify=False,
                allow_redirects=True)
        ##method one
        soup = BeautifulSoup(x.text, "html.parser")
        for tag in soup.find_all('script'):
            sources = tag.get('src')
            try:
                if sources.endswith(".js"):
                    sources = sources.replace("./", "")[1:]
                    r = get(target+sources+".map", headers=headers, verify=False)
                    if r.status_code == 200:
                        print(r.url)
                else:
                    pass
            except:
                pass
                
        # if x.url != target:
        #     soup = BeautifulSoup(x.text, "html.parser")
        #     for tag in soup.find_all('script'):
        #         sources = tag.get('src')
        #         try:
        #             if sources.endswith(".js"):
        #                 sources = sources.replace("./", "")[1:]
        #                 r = get(target+sources+".map", headers=headers, verify=False)
        #                 if r.status_code == 200:
        #                     print(r.url)
        #         except:
        #             pass
        # else:
        #     soup = BeautifulSoup(x.text, "html.parser")
        #     for tag in soup.find_all('script'):
        #         sources = tag.get('src')
        #         try:
        #             if sources.endswith(".js"):
        #                 sources = sources.replace("./", "")[1:]
        #                 r = get(target+sources+".map", headers=headers, verify=False)
        #                 if r.status_code == 200:
        #                     print(r.url)
        #         except:
        #             pass




if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-t", "--target", metavar="", required=True)
    args = parser.parse_args()
    target = args.target
    finder(target)
