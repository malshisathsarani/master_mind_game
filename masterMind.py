again = "yes"
while again == "yes":
    
    #_______________________Generating Random list___________________________________________
    import random
    randomlist = []
    number_list = [1,2,3,4,5,6]
    randomlist = random.sample(number_list,4)
    print(randomlist)

    #________________________________
    name=" "
    name=str(input("Enter student name: "))
    print("                       Hi","<",name,">","Welcome to GameInt")
    print()
    print("Number to Guess - XXXX                            Color mapping: ")
    print("                                                     1.White 2.Blue 3.Red")
    print("                                                     4.Yellow 5.Green 6.Purple")
    print()
    print(" Attempt No                    Guess                        Result")
    print("_______________________________________________________________________________")
    print()
    #____________________________________________________________________________________________
    player_list = []
    attempts = 1
    result_1 = ""
    result_2 = ""
    result_3 = ""
    result_4 = ""
    score = 100

    


    #_______________________________________________________________________________________________

    while (attempts < 9):
        num1 ,num2 ,num3 ,num4 = input(str(attempts)+")"+" Enter 4 digit number:"+"       ").split()
        
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        num4 = int(num4)


        if num1 > 6:
            print("                         Invaliad wrong number")
            continue         
        if num2 > 6:
            print("                         Invaliad wrong number")
            continue
        if num3 > 6:
            print("                         Invaliad wrong number")
            continue
        if num4 > 6:
            print("                         Invaliad wrong number")
            continue       
            
        player_list.append(num1)
        player_list.append(num2)
        player_list.append(num3)
        player_list.append(num4)
        print(player_list)
        print()
        
        #____________________________________________________________________________________________________________

        if player_list == randomlist:
            print("----------------------------------------------------------> 1 1")
            print("                                                            1 1")
            print()
            score = 100 - 12.5 * (attempts - 1)
            print("You have scored ",score," points")
            print("Congratulations!!!!! You have won the game...")
            break
        
        if player_list == [0,0,0,0]:
            print("You have ended the game")
            break
            
        #checking 1st number
        if player_list[0] == randomlist[0]:
            result_1 = "1"
        elif player_list[0] in randomlist:
            result_1 = "0"
        else:
            result_1 = "."
        

        #cheking 2nd number
        if player_list[1] == randomlist[1]:
            result_2 = "1"
        elif player_list[1] in randomlist:
            result_2 = "0"
        else:
            result_2 = "."

        #checking 3rd number
        if player_list[2] == randomlist[2]:
            result_3 = "1"
        elif player_list[2] in randomlist:
            result_3 = "0"
        else:
            result_3 = "."

        #checking 4th number
        if player_list[3] == randomlist[3]:
            result_4 = "1"
        elif player_list[3] in randomlist:
            result_4 = "0"
        else:
            result_4 = "."

        player_list = []
        attempts = attempts + 1


        print("---------------------------------------------------------> ",result_1,result_3)
        print("                                                           ",result_2,result_4)

    again = "no"
    print()
    again =str(input("Do you want play again(yes/no)? "))  
    print("Thank you...")
    print()