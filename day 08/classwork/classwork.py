while True:
    user_input = input("chawere 3 asoiani sityva: ")

    if len(user_input) == 3:
        
        reversed_word = ""
        for i in user_input:
            reversed_word = i + reversed_word  
        
        
        print(user_input == reversed_word)
        break
    else:
        print("sityva ar aris 3 asoiani.")