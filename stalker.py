# -*- coding: utf-8 -*-
# @Author: Amar Prakash Pandey
# @Date:   2016-03-20
# @Email:  amar.om1994@gmail.com  
# @Github username: @amarlearning
# @Last Modified by: Amar Prakash Pandey  
# @Last Modified date: 2016-04-17
# MIT License. You can find a copy of the License
# @http://amarlearning.mit-license.org

import sys
import datetime
import urllib
import os
import re
from tabulate import tabulate
from clint.textui import colored, puts
from bs4 import BeautifulSoup

# Global variables used in program

def head() :
    """official banner for PyStalker printed in yellow color"""
    clear()
    pystalker_banner = r"""
         ____________
        |__________//
        | |       //
        | |______//
        |_|_____//
        | | \\    //
        | |  \\  // _______ ________   __                   _____  ______
        | |   \\// \\       \__  __/  //\\   ||     ||  // ||     |    //
        | |    ||   \\_____    | |   //__\\  ||     ||//   ||____ |___//
        | |    ||         //   | |  //====\\ ||     ||\\   ||     |\\
        |_|    ||   _____//    |_| //      \\||____ ||  \\ ||____ | \\
                                  

                                     - By amarlearning(@AmarPrakashPandey)
                                 
        """
    puts(colored.yellow(pystalker_banner))

def clear():
    """for removing the clutter from the screen when necessary"""
    os.system('cls' if os.name == 'nt' else 'clear')

def space() :
    """providing one line space in the console when needed"""
    print ""

def regex(username) : 
    """validating username using regular expression"""
    regex_pattern = r'^[A-Za-z0-9_]+$'
    match = re.findall(regex_pattern, username)
    if len(match) == 1 :
        return 1
    else :
        return 0

def check_already_present(username) :
    """because redundancy is not good"""
    loop = 0
    cwd = os.getcwd()
    file_path = cwd+"\DATA"   
    file_content = open(file_path)
    file_read = file_content.read()
    users_list = file_read.split()
    for user in users_list :
        if username == user :
            loop = 1
    return loop

def delete_a_username(delete_node) :
    """no need to stalk everyone everytime"""
    cwd = os.getcwd()
    file_path = cwd+"\DATA"   
    file_content = open(file_path)
    file_read = file_content.read()
    users_list = file_read.split()
    print users_list
    loop = 0
    flag = -10
    for user in users_list :
        if delete_node == user :
            flag = loop
        loop = loop + 1
    if flag > -1 :
        del users_list[flag]
        print users_list
        cwd = os.getcwd()
        file_path = cwd+"\DATA"   
        file_content = open(file_path,'w')
        for user in users_list :
            user = " " + user
            file_content.write(user)
        file_content.close()
        flag = 6
        call_defined_function(menu(flag))
    else :
        flag = 5
        call_defined_function(menu(flag))

def notification(flag) :
    """notifications tell us what going on behind the scene"""
    if flag == 1 :
        puts(colored.red("error : wrong value entered! input correct value."))
        space()
        flag = 0
    elif flag == 2 :
        puts(colored.yellow("success : username successfully added to data file."))
        space()
        flag = 0
    elif flag == 3 :
        puts(colored.red("error : invalid username entered."))
        space()
        flag = 0
    elif flag == 4 :
        puts(colored.red("error : username already present."))
        space()
        flag = 0
    elif flag == 5 :
        puts(colored.red("error : username not present in list."))
        space()
        flag = 0
    elif flag == 6 :
        puts(colored.yellow("success : username deleted successfully."))
        space()
        flag = 0

def add_name_to_data(username) :
    """adding a username to the data file"""
    flag = regex(username)
    if flag == 1 :
        carry = check_already_present(username)
        if carry == 0 :
            cwd = os.getcwd()
            file_path = cwd+"\DATA"
            file_content = open(file_path,'a')
            username = " " + username
            file_content.write(username)
            file_content.close()
            flag = 2
            call_defined_function(menu(flag))
        else :
            flag = 4
            call_defined_function(menu(flag))    
    else :
        flag = 3
        call_defined_function(menu(flag))

def get_webpage_data(webpage,username) :
    scrapper = BeautifulSoup(webpage , 'html.parser')
    matches = scrapper.prettify()
    find_what_you_are_looking_for(scrapper,username)


def print_in_style(catch,username) :
    table = [[1,username,catch[10:]]]
    headers = ["Sno.","Username", "Last Visit"]
    print tabulate(table, headers, tablefmt="grid")

def find_what_you_are_looking_for(scrapper,username) :
    matches = scrapper.find('div',{'id':'pageContent'})
    match = matches.find('div',{'class':'roundbox'})
    match = match.find('ul')
    for li in match.find_all('li') :
        catch = li.get_text()
        if "Last visit" in catch :
            catch = catch.strip()
            catch = re.sub(r"\s", "", catch)
            print_in_style(catch,username)

def check_connection(username) :
    url = "http://codeforces.com/profile/" + username
    response = urllib.urlopen(url)
    if response == None :
        print "Check your Internet conneciton! Not working."
    else :
        get_webpage_data(response,username)

def add_new_name(username) :
    """adding a username to the data file then stalking"""
    flag = regex(username)
    if flag == 1 :
        carry = check_already_present(username)
        if carry == 0 :
            cwd = os.getcwd()
            file_path = cwd+"\DATA"
            file_content = open(file_path,'a')
            username = " " + username
            file_content.write(username)
            file_content.close()
        else :
            flag = 4
            call_defined_function(menu(flag))    
    else :
        flag = 3
        call_defined_function(menu(flag))

def show_all_data() :
    """showing all entries present in the data file"""
    loop = 1
    cwd = os.getcwd()
    file_path = cwd+"\DATA"
    file_content = open(file_path)
    users_list = file_content.read().split()
    puts(colored.green("List of entries present in data file."))
    space()
    for user in users_list :
        puts(colored.yellow(str(loop)+". "+user))
        loop = loop + 1
    if loop == 1 :
        puts(colored.cyan("message : No entries found!"))
    space()
    puts(colored.magenta("Note : press '1' to return back to menu."))
    puts(colored.magenta("Note : press '0' to exit."))
    space()
    x = int(raw_input("Action : "))
    if(x == 1) :
        flag = 0
        call_defined_function(menu(flag))
    elif(x == 0) :
        clear()
    else :
        flag = 1
        call_defined_function(menu(flag))

def menu(flag) :
    """menu for pystalker take option and call desired function"""
    head()
    puts(colored.magenta("Stalkers menu : "))
    space()
    notification(flag)
    puts(colored.green("(1) Stalk for one input username. "))
    puts(colored.green("(2) Add a username to data file. "))
    puts(colored.green("(3) Delete a username from data file. "))
    puts(colored.green("(4) View all data entry. "))
    puts(colored.green("(5) Stalk for every data entry. "))
    puts(colored.yellow("Doc : press '7' to see Documentation."))
    puts(colored.red("Note : press '0' to exit!"))
    space()
    index = int(raw_input("Action : "))
    return index

def call_defined_function(value) :
    """call the function that user requested"""
    if(value == 1):
        """stalking some random remembered username ? go ahead!"""
        head()
        puts(colored.green("Fill out the username [anonymous stalking] : "))
        username = raw_input()
        space()
        what_to_do = regex(username)
        if what_to_do == 1 :
            check_connection(username)
        else :
            flag = 3
            call_defined_function(menu(flag))
    elif(value == 2):
        """add a username to the data file"""
        head()
        puts(colored.green("Fill out the username : "))
        username = raw_input()
        add_name_to_data(username)
    elif(value == 3) :
        """delete a username from the data file"""
        head()
        puts(colored.green("Fill out the username : "))
        delete_node = raw_input()
        delete_a_username(delete_node)
    elif(value == 4): 
        """display all the data present in the data file."""
        head()
        show_all_data()
    elif(value == 0):
        clear()
    else :
        flag = 1
        call_defined_function(menu(flag))
    
def main() :
    """everythings starts from here i.e. main()"""
    flag = 0
    clear()
    call_defined_function(menu(flag))
    
if __name__ == "__main__" :
    main()
