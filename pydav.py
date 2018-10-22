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
                Version 1.2 for Python3
    \033[1;91mThe easy python script for setting up mounting and unmounting webDAV folders.\033[1;m
    \033[1;32m+ -- -- +=[ Original Author: Justin Ball sn:nullr00t\033[1;m
    \033[1;91mCheck out my repos on https://github.com/nullr00t for other programs or scripts by me.\033[1;m
    \033[1;91mIf you already have dav2fs installed and have your folders set up,\033[1;m
    \033[1;91mand have a broader understanding of these scripts please feel free to run pydavmin3.py \033[1;m
    \033[1;91mScript was originally wrote for Kubuntu 18.04,other Debian based and apt package managed systems \033[1;m
    \033[1;91mmay work but are not guarunteed. Script depends on having the davfs2 package installed on your\033[1;m
    \033[1;91msystem as well as being able to provide a password for sudo privileges to install dav2fs.\033[1;m
    \033[1;91mI hope you find this script useful!\033[1;m
               ''')


def mmenu1():
    print(''' 
1) Install davfs2 (needed for mounting DAV web folders as filesystems)
2) Mount your webDAV folder
3) Unmount your webDAV folder
4) Exit

            ''')


def choice1():
    global choicem1
    choice = input("\nWould you like to make a new directory for the webDAV mount?\n")
    choice = str(choice)
    accepted_strings = {'Yes', 'y', 'Y', 'yes', 'Ye', 'ye'}
    unaccepted_strings = {'No', 'n', 'N', 'no'}
    while True:
        try:
            if choice in accepted_strings:
                newdir = input('Enter the name of the new folder:\n')
                os.system("mkdir"+" "+"~/"+newdir)
                davurl = input('Enter the webDAV URL:\n')
                u = getpass.getuser()
                os.system("sudo mount -t davfs -o uid=" + u + "," + "gid=" + u + " " + davurl+" "+"~/"+newdir)
                print("Operation has completed, see line above for error any error info. Exiting...")
                exit()
            elif choice in unaccepted_strings:
                choicem1 = 2
            else:
                choicem1 = 1
        finally:
            exit()


def choice2():
    global choicem2
    choice = input("\nWould you like to use a current directory for the webDAV mount?\n")
    choice = str(choice)
    accepted_strings = {'Yes', 'y', 'Y', 'yes', 'Ye', 'ye'}
    unaccepted_strings = {'No', 'n', 'N', 'no'}
    if choice in accepted_strings:
        curdir = input('Enter the name of a current folder for the mount:\n')
        davurl = input('Enter the webDAV URL:\n')
        u = getpass.getuser()
        os.system("sudo mount -t davfs -o uid=" + u + "," + "gid=" + u + " " + davurl + " " + "~/" + curdir)
        print("Operation has completed, see line above for error any error info. Exiting...")
        exit()
    elif choice in unaccepted_strings:
        print("You have selected to not mount on a current folder. Terminating...")
        exit()
    else:
        choicem2 = 1


mmenu1()
choicemm1 = input('Enter your choice [ 1 - 4 ]\n')
choicemm1 = int(choicemm1)
if choicemm1 == 4:
    print("Script termination requested, goodbye...")
    exit()
if choicemm1 == 3:
    print('''
\033[1;91m[I]You normally can find the name of the mount by looking for any entries at the bottom of the list\033[1;m
\033[1;91mor that beging with http or https when you open up a terminal and type mount.\033[1;m
    ''')
    davurlpt = input("Please type the name of the webDAV url you have mounted:")
    os.system("sudo umount" + " " + davurlpt)
    print("Operation has completed, see line above for error any error info. Exiting...")
    exit()
if choicemm1 == 1:
    def installdavfs2():
        os.system('sudo apt-get update && sudo apt-get install davfs2')
    installdavfs2()
if choicemm1 == 2:
    os.system("cd ~/")
    os.system("ls -l ~/")
    print("\n\033[1;91m[I]These are files and directories in your home folder.\033[1;m")
    print("\n\033[1;91m[I]If the line starts with a d, then it is a directory.\033[1;m")
choice1()

while choicem1 is None:
    choice1()

while choicem1 == 2:
    choice2()

while choicem1 == 1:
    print("Invalid input please try again")
    pass
    choice1()
    if choicem1 == 2:
        choice2()

while choicem2 == 1:
    print("An exception has occurred, please try running the script again. Terminating...")
    exit()
