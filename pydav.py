#!/usr/bin/python
import os
import getpass

print('''
        WELCOME TO

 mmmmm m     m mmmm     mm   m    m
 #   "# "m m"  #   "m   ##   "m  m"
 #mmm#"  "#"   #    #  #  #   #  # 
 #        #    #    #  #mm#   "mm" 
 #        #    #mmm"  #    #   ##  
                Version 1.0 for Python2 
                Explicitly Meant To Be Ran In Python2
    \033[1;91mThe easy python script for setting up mounting and unmounting webDAV folders.\033[1;m
    \033[1;32m+ -- -- +=[ Original Author: Justin Ball sn:nullr00t\033[1;m
    \033[1;91mCheck out my repos on https://github.com/nullr00t for other programs or scripts by me.\033[1;m
    \033[1;91mIf you already have dav2fs installed and have your folders set up,\033[1;m
    \033[1;91mand have a broader understanding of these scripts please feel free to run pydavmin2.py \033[1;m
    \033[1;91mScript was originally wrote for Kubuntu 18.04,other Debian based and apt package managed systems \033[1;m
    \033[1;91mmay work but are not guarunteed. Script depends on having the davfs2 package installed on your\033[1;m
    \033[1;91msystem as well as being able to provide a password for sudo privileges to install dav2fs.\033[1;m
    \033[1;91mI hope you find this script useful!\033[1;m
            ''')


def options():
    print('''
                1) Install the davfs2 package
                2) Mount webDAV folder
                3) Unmount webDAV folder
                4) Exit
                 ''')


while True:
        try:
            options()
            choice = input('Enter your choice [ 1 - 4 ]\n')
            choice = int(choice)
            acc_strings = {'Yes', 'y', 'Y', 'yes', 'Ye', 'ye'}
            unacc_strings = {'No', 'n', 'N', 'no'}
            numinput = {1, 2, 3, 4}
            if choice == 1:
                os.system("sudo apt-get update && sudo apt-get install davfs2 -y")
            if choice == 4:
                print("Script termination requested, goodbye...")
                exit()
            elif choice == 2:
                os.system("cd ~/")
                os.system("ls -l ~/")
                print("\n\033[1;91m[Info]These are files and directories in your home folder.\033[1;m")
                print("\n\033[1;91m[Info]If the line starts with a d, then it is a directory.\033[1;m")
                choice2opt2 = input("Would you like to make a new folder in your home directory?:\n")
                choice2opt2 = str(choice2opt2)
                if choice2opt2 in acc_strings:
                    newdir = input("Enter the new folder's name:\n")
                    os.system("mkdir" + " " + "~/" + newdir)
                    davurl = input("Please type in the URL of the webDAV folder you would like to mount:\n")
                    u = getpass.getuser()
                    os.system("sudo mount -t davfs -o uid=" + u + "," + "gid=" + u + " " + davurl + " " + "~/" + newdir)
                    print("Operation has completed, see line above for error any error info. Exiting...")
                    exit()
            elif choice == 3:
                choice3opt1 = input("Please type the address of the webDAV server that you have mounted:\n")
                choice3opt1 = str(choice3opt1)
                os.system("sudo umount" + " " + choice3opt1)
                print("Operation has completed, see line above for any error information.")
            elif choice not in numinput:
                print("Not a valid option selection. Please try again.")
        except ValueError:
            print("Error 1 - Not a valid input type. Please input a number from the options menu.\n")
        except NameError:
            print("Error 2 - Not a valid input type. Please input a number from the options menu.\n")
