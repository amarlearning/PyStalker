import urllib
import re
from bs4 import BeautifulSoup

username = raw_input("Stalker! You know the username of that guy, enter it : ")
url = "http://codeforces.com/profile/" + username
webpage = urllib.urlopen(url)
scrapper = BeautifulSoup(webpage , 'html.parser')
matches = scrapper.prettify()
matches = scrapper.find('div',{'id':'pageContent'})
match = matches.find('div',{'class':'roundbox'})
match = match.find('ul')
for li in match.find_all('li') :
    catch = li.get_text()
    if "Last visit" in catch :
        catch = catch.strip()
        catch = re.sub(r"\s", "", catch)
        print "--------------------------"
        print "| Last visit | " +catch[10:]+" |"
        print "--------------------------"

