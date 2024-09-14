# Função para forçar o input para um item dentro de uma lista
def force_list(message, list, error_message):
    choice = input(message)
    while not choice in list:
         choice = input(error_message)
    
    return choice

# Função para forçar um input a ser um número
def force_number(message, error_message):
    inpt = input(message)
    while not inpt.isnumeric():
          inpt = input(error_message)
    
    return inpt