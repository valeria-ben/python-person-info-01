from xml.etree.ElementTree import Comment


def showMenu():
    print()
    print()
    print()
    optionDict = {
        " 0": "create a new person card",
        " 1": "search a person card by id",
        " 2": "show all person cards",
        " 3": "update a person card",
        " 4": "delete a person card",
        " -1": "exit app",
    }
    for option, value in optionDict.items():
        print(f"{option}:: {value}")
    print()


while True:
    showMenu()
    option = int(input("option: "))
    if option == -1:
        """exit app"""
        break
    elif option == 0:
        pass
    elif option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    else:
        print("app just continues...")
