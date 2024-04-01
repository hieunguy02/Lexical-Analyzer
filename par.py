from lexical import lexer

tokens = []
lexemes = []
syntaxs = []

syntax = ""
token = ""
lexeme = ""



current_i = 0
find = True

#create the function needed from the syntax
#function taking a current_i

def RATS24(current_i):
    pass
        
def OptFunctionDef(current_i):
    pass       

def StatementList(current_i):
    pass

def OptDeclarationList(current_i):
    pass



while (current_i < len(tokens)):
    pass




while(find):
  try:
    file_name = input('Enter the filename: ')
    switch = input("Enter 0(Turn off syntax) or 1(Turn on synxtax): ")
    lexer(file_name)
    file_output = file_name + "_output.txt"
    fileoutput = open(file_output, "w")
    fileoutput.write("Lexemes:           Tokens:" + "\n")
    for i in range(len(tokens)):     
      fileoutput.write(str(lexemes[i]) + "            " + str(tokens[i]) + "\n")
      #Write the syntax available for whatever needed
      
      
    find = False
  except OSError:
     print("Can not find the file.")
