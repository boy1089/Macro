import requests
html= requests.get("https://dgkim5360.tistory.com/entry/python-requests")
html_code = html.text
if ('''code unique to the 404 page of google''' in html_code):
    print('404 positive')
else:
    print('404 negative')


    # https://www.python2.net/questions-490101.htm


html_code2 = html.status_code
print(html_code2)


# https://dgkim5360.tistory.com/entry/python-requests