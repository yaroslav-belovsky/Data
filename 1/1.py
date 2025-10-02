import  os
try:
    os.mkdir("SecretFolder")

    with open("SecretFolder/secret.txt", "w"):
        print("зроблено!!!")
except SyntaxError:
    print("цей файл уже існує!")
    inhui_fail = input("введіть іншу назву: ")
    os.mkdir(inhui_fail)

    with open(f"{inhui_fail}/secret.txt", "w"):
        print("зроблено!!!")
except FileExistsError:
    print("цей файл уже існує!")
    inhui_fail = input("введіть іншу назву: ")
    os.mkdir(inhui_fail)

    with open(f"{inhui_fail}/secret.txt", "w"):
        print("зроблено!!!")