def hangman_game():   # function define
    hangman = ["""
                    --------
                    |      |
                    |     (O)
                    |      |           # This Is A Set Of Image Then Show When Answer Is Wrong
                    |     ( )
                    |
                    """,
                    """
                    --------
                    |      |
                    |     (O)
                    |      |
                    |
                    |
                    -
                    """,
                    """
                    --------
                    |      |
                    |     (O
                    |      |
                    | 
                    |   
                    -
                    """,
                    """
                    --------
                    |      |
                    |      O
                    |      |
                    | 
                    |     
                    -
                    """,
                    """
                    --------
                    |      |
                    |      O
                    |
                    |
                    |
                    -
                    """,
                    """
                    --------
                    |      |
                    |      
                    |
                    |
                    |
                    -
                    """]
    Letter_guessed,secret_word='',"siddik"  # Secret word user have to guess # Letter guessed get after user input 
    print(f"Welcome to the Hangman! \nYou have to guess {len(secret_word)} letters\n") # print when game started 
    for i in range(len(secret_word)): # for loop is used for run program till len(secret_word) will be 0
        for j in range(len(hangman)-1,-1,-1): # reverse the hangman image set
            guess = input("Enter a guess letter: ").lower() # input get lower case because secret word is in lower case
            if guess in secret_word: # check input is in secret word or not
                if guess=="": print("please enter somthing\n")   # check if user put empty string or not 
                else: # if not add input in letter guessed 
                    Letter_guessed+=guess  
                    print("Your guess is right\n")
            else:
                print(hangman[j]) # after ending the if then else will show if input not in secret word then print 0 indexing of hangman image set
        break
    print("You Won") if Letter_guessed==secret_word else print("You Lose!") # check secret word is equal to letter guessed or not
hangman_game() # fuction call