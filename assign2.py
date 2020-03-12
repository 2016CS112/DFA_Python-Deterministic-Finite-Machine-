#Read character by character from file = < > ... operator ..change the state 
def Read_Character_from_file():
    state = 0
    f = open("file.txt")
    while True:
        c = f.read(1)
        if not c:
            print ("No more character is exist")
            break
        if(c=='>'):
            state = 1
            print("Relation Operater > ")
            print("State" , state)
            c = f.read(1)
            if(c==' '):
                state = 2
                print("Seprator")
                print("State" , state)
                print("Final State")
                break
                
            else:
                print("Error")
                break
            if (c=='='):
                state = 3
                print("Assignment Operator")
                print("State" , state)
                c = f.read(1)
                if(c == ' '):
                    state = 4
                    print("Seprator")
                    print("State" , state)
                    print("Final State")
                    break
        if(c=='<'):
            state = 5
            print("Relation Operater < ")
            print("State" , state)
            c = f.read(1)
            if(c=='='):
                state = 7
                print("Assignment operator =")
                print("State" , state)
                c = f.read(1)
                if(c==' '):
                    state = 8
                    print("Seprator")
                    print("State" , state)
                    print("Final State")
                    break
            if(c==' '):
                state = 6
                print("Seprator")
                print("State" , state)
                print("final State")
                break
            if(c=='>'):
                state = 9
                print("Relation Operator > ")
                print("State" , state)
             
                c = f.read(1)
                if(c==' '):
                    state = 10
                    print("Seprator")
                    print("State" , state)
                    print("Final State")
                    break
        if(c=='='):
            state = 11
            print("Assignment Operator")
            print("State " , state)
            c = f.read(1)
            if(c == ' ' ):
                state = 12
                print("Seprator")
                print("State" , state)
                print("Final State")
                break
                
Read_Character_from_file()
        
