import requests
import sys
import json


def crawler(page):
    response = requests.get(page)
    dict_resp = json.loads(response.text)
    return dict_resp


def main():
    sys.argv
    
    page_size = 10
    LABEL = ""

    if len(sys.argv) > 1:
        if len(sys.argv) < 3:
            LABEL = sys.argv[1]
        else:
            page_size = sys.argv[1]
            LABEL = sys.argv[2]
    
    page = "http://api.stackexchange.com/questions?pagesize={0}&order=desc&sort=votes&tagged={1}&site=stackoverflow".format(page_size,LABEL)

    result = crawler(page)
 
    for numb, element in enumerate(result['items'], start = 1):
        print(numb,'-',element['title'],':\n',element['link'])


if __name__ == "__main__":
    main()
