# this is a method for testing code and preventing crashes
# Try except finally

try: # The code under TRY is always executed
    
    rubychan = 1
    print((rubychan))
    rubychan = "SixNine"
    print(float(rubychan))
except NameError: # This code will run If there is an error (EXCEPTION)
    print("A variable or statement is incorrect in your code baba")
except ValueError:
    print("It's not working baba")
else:
    gameActive = True
    print("Starting game...")
finally: # THIS CODE ALWAYS RUNS, IT'S LIKE THE TERMINATOR
    rubychan = 1.0
    
