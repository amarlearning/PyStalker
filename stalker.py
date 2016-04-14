# -*- coding: utf-8 -*-
# @Author: Amar Prakash Pandey
# @Date:   2016-03-20
# @Email:  amar.om1994@gmail.com  
# @Github username: @amarlearning
# @Last Modified by: Amar Prakash Pandey  
# @Last Modified time: 2016-04-14
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
         ___________
        |_________//
        | |      //
        | |_____//        
        |_|____//     
        | | \\    //
        | |  \\  // _______ ________   __                   _____  ______
        | |   \\// \\       \__  __/  //\\   ||     ||  // ||     |    //
        | |    ||   \\_____    | |   //__\\  ||     ||//   ||____ |___//
        | |    ||         //   | |  //----\\ ||     ||\\   ||     |\\
        )_(    )(   _____//    )_( //      \\||____ ||  \\ ||____ | \\
                                  

                                     - By amarlearning(@AmarPrakashPandey)
                                 
        """
    puts(colored.yellow(pystalker_banner))

def clear():
    """for removing the clutter from the screen when necessary"""
    os.system('cls' if os.name == 'nt' else 'clear')

def space() :
    """providing one line space in the console when needed"""
    print ""


def add_name_to_data(username) :
    """adding a username to the data file"""
    cwd = os.getcwd()
    file_path = cwd+"\DATA"
    file_content = open(file_path,'a')
    username = " " + username
    file_content.write(username)
    file_content.close()
    flag = 2
    call_defined_function(menu(flag))

def show_all_data() :
    """showing all entries present in the data file"""
    loop = 1
    cwd = os.getcwd()
    file_path = cwd+"\DATA"
    file_content = open(file_path)
    users_list = file_content.read().split()
    puts(colored.green("\tList of entries present in data file."))
    for user in users_list :
        puts(colored.yellow("\t"+str(loop)+". "+user))
        loop = loop + 1
    puts(colored.magenta("\tNote : press '1' to return back to menu."))
    puts(colored.magenta("\tNote : press '0' to exit."))
    x = int(raw_input("\tAction : "))
    if(x == 1) :
        flag = 0
        menu(flag)
    elif(x == 0) :
        clear()
    else :
        flag = 1
        menu(flag)

def menu(flag) :
    """menu for pystalker take option and call desired function"""
    head()
    puts(colored.magenta("\tStalkers menu : "))
    space()
    if flag == 1 :
        puts(colored.red("\terror : wrong value entered! input correct value."))
        space()
        flag = 0
    elif flag == 2 :
        puts(colored.yellow("\tsuccess : username successfully added to data file."))
        space()
        flag = 0
    puts(colored.green("\t(1) Stalk for one input username. "))
    puts(colored.green("\t(2) Add a username to data file. "))
    puts(colored.green("\t(3) View all data entry. "))
    puts(colored.green("\t(4) Stalk for every data entry. "))
    puts(colored.yellow("\tDoc : press '7' to see Documentation."))
    puts(colored.red("\tNote : press '0' to exit!"))
    space()
    index = int(raw_input("\tAction : "))
    return index

def call_defined_function(value) :
    if(value == 1):
        puts(colored.blue("working"))
    elif(value == 2):
        """add a username to the data file"""
        head()
        puts(colored.green("\tFill out the username : "))
        username = raw_input("\t")
        add_name_to_data(username)
    elif(value == 3): 
        head()
        show_all_data()
    elif(value == 0):
        clear()
    else :
        flag = 1
        call_defined_function(menu(flag))
    
def main() :
    """everythings starts from here i.e. main()"""
    username = ""
    flag = 0
    clear()
    call_defined_function(menu(flag))
    
if __name__ == "__main__" :
    main()