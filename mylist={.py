list = print(  "1. Welcome "
    "2. Say Hi to Eleonora "
    "3. Say Hi to Sebastian "
    "4. Say, How are you? "
    "5. Pick Apple "
    "0. Exit ") 

choose = input("choose from below: ")

if choose == "1":
    print("Welcome")
elif choose == "2":
    print("Hi. Eleonora")
elif choose == "3":
    print("HI. Sebastian")
elif choose == "4":
    print("how are you?")
elif choose == "5":
    print("Pick Apple")
elif choose == "0":
    print("Exit")
else: print("invalid choice")
