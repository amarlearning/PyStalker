import urllib
import re
from bs4 import BeautifulSoup


def print_in_style(catch) :
    print "--------------------------"
    print "| Last visit : " +catch[10:]+" |"
    print "--------------------------"


def generate_url() :
    username = raw_input("Stalker! You know the username of that guy, enter it : ")
    url = "http://codeforces.com/profile/" + username
    return url

def find_what_you_are_looking_for(scrapper) :
    matches = scrapper.find('div',{'id':'pageContent'})
    match = matches.find('div',{'class':'roundbox'})
    match = match.find('ul')
    for li in match.find_all('li') :
        catch = li.get_text()
        if "Last visit" in catch :
            catch = catch.strip()
            catch = re.sub(r"\s", "", catch)
            print_in_style(catch)

def get_webpage_data() :
    webpage = urllib.urlopen(generate_url())
    scrapper = BeautifulSoup(webpage , 'html.parser')
    matches = scrapper.prettify()
    find_what_you_are_looking_for(scrapper)


def main() :
    get_webpage_data()


if __name__ == "__main__" :
    main()
