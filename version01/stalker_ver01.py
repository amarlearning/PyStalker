import urllib
import re
from bs4 import BeautifulSoup

def print_in_style(catch) :
    print "| Last visit : " +catch[10:]+" |"

def generate_url(username) :
    url = "http://codeforces.com/profile/" + username
    return url

def find_what_you_are_looking_for(scrapper) :
    matches = scrapper.find('div',{'id':'pageContent'})
    match = matches.find('div',{'class':'roundbox'})
    match = match.find('ul')
    check_for_status = False
    for li in match.find_all('li') :
        catch = li.get_text()
        if "Last visit" in catch :
            catch = catch.strip()
            catch = re.sub(r"\s", "", catch)
            print_in_style(catch)
            check_for_status = True
    if check_for_status == False :
        print "Username not found! Try again. "
        main()

def get_webpage_data(webpage) :
    scrapper = BeautifulSoup(webpage , 'html.parser')
    matches = scrapper.prettify()
    find_what_you_are_looking_for(scrapper)

def check_connection(username) :
    response = urllib.urlopen(generate_url(username))
    if response == None :
        print "Check your Internet conneciton! Not working."
    else :
        get_webpage_data(response)

def main() :
    username = raw_input("Stalker! You know the username of that guy, enter it : ")
    check_connection(username)
    
if __name__ == "__main__" :
    main()
