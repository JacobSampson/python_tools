def get_user_int(lower=None, upper=None):
    user_input = None

    while(user_input == None):
        try:
            user_input = input("Selection ('q' to quit): ")

            if (user_input.lower() == 'q'):
                exit()
            else:
                user_input = int(user_input)

            if (lower is not None and user_input < lower) or (upper is not None and user_input > upper):
                print("Incorrect range...")
                user_input = None
        except ValueError:
            print("Incorrect selection type...")
            user_input = None
        
    return user_input