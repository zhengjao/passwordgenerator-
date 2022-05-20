import easygui,random
#Main program
while True:
    #Normal result
    try:
        #Input
        player = int(input("Password length:"))
        #Import file
        random_text = []
        with open(r"Password\standardcipher.txt") as f:
            text=f.read()
        #Algorithm
        for i in range(player):
            i=random.choice(text)
            random_text.append(i)
        #Result output
        easygui.msgbox(random_text,"random cipher")
        break
    #Error result
    except:
        print("Incorrect input information")
        continue

