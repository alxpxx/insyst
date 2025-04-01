#!/usr/bin/env python
#-*- encoding: utf-8 -*-

"""
User-friendly system information.
"""

## Imports

import argparse
import os
import sys
from shutil import copy
from subprocess import PIPE, STDOUT, run
from time import sleep
#import pytest
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.shortcuts import PromptSession
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.shortcuts import *
from pyfiglet import Figlet

session = PromptSession()
# Create a prompt to accept input.

bindings = KeyBindings()
# Create a container for key bindings.

file = open("myfile.txt",'w')
# Open file to store output for saving


## Application 

def main():
    # Command line arguments
    parser = argparse.ArgumentParser(prog="InSystem", description='Display user-friendly system information.')
    parser.add_argument('-o', help='Display system overview.', action="store_true")
    parser.add_argument('-n', help='Show network infomation')
    parser.add_argument('-e', help='Show system errors')
    args = parser.parse_args()
    if args.o:
        input=1
    elif args.n:
        input=4
    elif args.e:
        input=7
        
    
    # Clear the screen.
    # Call the main menu and prompt.
    os.system('clear')
    main_menu() 
    prompt_user()
    
    
def main_menu():
    # Display main header and menu
    menu_title = fig_func('InSystem')
    
    print('''
    [1] - overview
    [2] - detailed information
    [3] - hardware 
    [4] - network
    [5] - performance
    [6] - installed apps
    [7] - errors
    
    ''')


def prompt_user():
    # Prompt for user input and activate key bindings
    run_app = True
    while(run_app==True):
        try:
            message = ''' 
[ctrl + s] - save to file
[ctrl + m] - main menu
[ctrl + x] - exit

    >'''
            input = session.prompt(message, key_bindings = bindings) 
        except (KeyboardInterrupt, EOFError, SystemExit):
        # Exit sequence received: ctrl-c, ctrl-d, esc or x.
            exit 
        finally:
            file.close()
            run_app = False
    file.close()
    sys.exit        
                
def save_to_file():
    open('mysysteminfo', 'w')
    mysysteminfo = file
    print("File saved as mysysteminfo.txt")
    return
    
    
    
## Decorated Functions
    
def header_fig(orig_func):
    # Wrapper to create Figlet header
    def wrapper(*args, **kwargs):
       header = orig_func(*args, **kwargs)
       return header
    return wrapper

def run_with_args(orig_func):
    # Wrapper to create subprocess
    def wrapper(*args, **kwargs):
       result = orig_func(*args, **kwargs)
       return result
    return wrapper

def display_info(func):
    # Clear the terminal screen to print output from subprocess
    os.system('clear')
    print('''
          
    ''')
    run_in_terminal(func)
    
@header_fig
def fig_func(header):
    # Render Figlet header
    fig = Figlet(font='big')
    print(fig.renderText(header))

@run_with_args
def run_func(cmd):
    # Run subprocess
    command = run(cmd, stdout=PIPE, stderr=STDOUT, encoding='utf8')
    print(command.stdout)
    file.write(command.stdout)



## Key Bindings
@bindings.add('1')
# [o]verview of system information
def basic(event):
    @display_info
    def overview():
        fig_func('Overview')
        run_func(['inxi','-b'])
    return    
        
@bindings.add('2')
# [d]etailed information
def detailed(event):
    @display_info
    def detailed():
        fig_func('More Detail')
        run_func(['inxi','-F'])
    return

@bindings.add('7')
# [e]rrors from the system logs.        
def errors(event):
    @display_info
    def errors():
        fig_func('Errors')
        run_func(['journalctl','-n','10','-p','3'])

@bindings.add('5')
# [p]rocesses using the most cpu & memory        
def performance(event):
    @display_info
    def performance():
        fig_func('Performance')
        run_func(['ps','-eo','pid',',','cmd',',','%mem',',','%cpu',',','--sort=-%mem'])

@bindings.add('4')
# [n]etwork information
def network(event):
    @display_info
    def network():
        fig_func('Network')
        run_func(['inxi','-N'])
        run_func(['ip','addr','show'])

@bindings.add('6')
# [i]nstalled packages        
def installed(event):
    @display_info
    def installed():
        fig_func('Installed')
        run_func(['grep',' installed ','/var/log/dpkg.log'])

@bindings.add('3')
# [h]ardware    
def hardware(event):
    @display_info
    def hardware():
        fig_func('Hardware')
        run_func(['inxi','-CDm'])
        
@bindings.add('c-m')
# [m]ain menu        
def display_main(event):
    os.system('clear')
    main_menu()
    print('>')
    
@bindings.add('c-s')
# [s]ave session to file    
def save_func(event):
    save_to_file()
    return

@bindings.add('c-x')
def exit_func(event):
# ctrl+x pressed, exit sequence
    event.app.exit(exception=EOFError, style='class:exiting')
    
@bindings.add('c-d')
def _(event):
# ctrl+d pressed, exit sequence
    event.app.exit(exception=EOFError, style='class:exiting')

    
if __name__ == '__main__':
    main()
