
def force_list(list, error_message):
    choice = input("Select one option (1-3): ")
    while not choice in list:
         choice = input(error_message)
    
    return choice

def force_number(message, error_message):
    inpt = input(message)
    while not inpt.isnumeric():
          inpt = input(error_message)
    
    return inpt