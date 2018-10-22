#!/usr/bin/python
import os


def usage():
    print(''' 
    This script assumes that you have dav2fs installed on your system, as well as know absolute paths in your system
    i.e. ~/ is for your home folder, / is root, and that you have understanding of basic filesystem privileges so you know
    where to make your directory/ where to mount to and if you will be able to access or make said directory.
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
            if choice == 4:
                print("Script termination requested, goodbye...")
                exit()
            elif choice == 1:
                usage()
            elif choice == 2:
                choice2opt1 = raw_input("Please type the web address of the webDAV server:\n")
                choice2opt1 = str(choice2opt1)
                choice2opt2 = raw_input("Please type the absolute path of the folder that you want to mount:\n")
                choice2opt2 = str(choice2opt2)
                os.system("sudo mount -t davfs -o uid=" + u + "," + "gid=" + u + " " + choice2opt1 + " " + choice2opt2)
                print("Operation has completed, see line above for any error information.")
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
