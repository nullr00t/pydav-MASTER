#!/usr/bin/python
import os
import getpass


def usage():
    print(''' 
    This script assumes that you have dav2fs installed on your system. This script is meant to be run with a python2
    interpreter.
          ''')


def options():
    print('''
                1) Usage
                2) Mount webDAV folder
                3) Unmount webDAV folder
                4) Exit
                 ''')


usage()
while True:
        try:
            options()
            choice = raw_input('Enter your choice [ 1 - 4 ]\n')
            choice = int(choice)
            acc_strings = {'Yes', 'y', 'Y', 'yes', 'Ye', 'ye'}
            unacc_strings = {'No', 'n', 'N', 'no'}
            if choice == 4:
                print("Script termination requested, goodbye...")
                exit()
            elif choice == 1:
                usage()
            elif choice == 2:
                os.system("cd ~/")
                os.system("ls -l ~/")
                print("\n\033[1;91m[Info]These are files and directories in your home folder.\033[1;m")
                print("\n\033[1;91m[Info]If the line starts with a d, then it is a directory.\033[1;m")
                choice2opt2 = raw_input("Would you like to make a new folder in your home directory?:\n")
                choice2opt2 = str(choice2opt2)
                if choice2opt2 in acc_strings:
                    newdir = raw_input("Enter the new folder's name:\n")
                    os.system("mkdir" + " " + "~/" + newdir)
                    davurl = raw_input("Please type in the URL of the webDAV folder you would like to mount:\n")
                    u = getpass.getuser()
                    os.system("sudo mount -t davfs -o uid=" + u + "," + "gid=" + u + " " + davurl + " " + "~/" + newdir)
                    print("Operation has completed, see line above for error any error info. Exiting...")
                    exit()
            elif choice == 3:
                choice3opt1 = raw_input("Please type the address of the webDAV server that you have mounted:\n")
                choice3opt1 = str(choice3opt1)
                os.system("sudo umount" + " " + choice3opt1)
                print("Operation has completed, see line above for any error information.")
            else:
                print("Option number outside expected range. Please input a number from the options menu.\n")
        except ValueError:
            print("Not a valid input type. Please input a number from the options menu.\n")
        except NameError:
            print("Not a valid input type. Please input a number from the options menu.\n")
