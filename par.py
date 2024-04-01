from lexical import lexer

tokens = []
lexemes = []
token = ""
lexeme = ""
current_i = 0
find = True

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
    find = False
  except OSError:
     print("Can not find the file.")
