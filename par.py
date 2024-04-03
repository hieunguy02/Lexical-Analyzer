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

#R1
def RATS24(current_i, switch):
    if switch == "1":
      fileoutput.write("<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")
      if lexemes[current_i] == "$":
        current_i += 1
        OptFunctionDef(current_i, switch)
        if lexemes[current_i] == "$":
            current_i += 1
            OptDeclarationList(current_i, switch)
            if lexemes[current_i] == "$":
                current_i += 1
                StatementList(current_i, switch)
                if lexemes[current_i] == "$":
                    current_i += 1
                else: fileoutput.write("Syntax Error, expected a $")
            else: fileoutput.write("Syntax Error, expected a $")
        else: fileoutput.write("Syntax Error, expected a $")
    
    
#R2               
def OptFunctionDef(current_i, switch):
    if switch == "1":
        fileoutput.write("<Opt Function Definitions> ::= <Function Definitions> | <Empty>")
        FunctionDef(current_i, switch) or Empty()
        
#R3        
def FunctionDef(current_i, switch):
    if switch == "1":
        fileoutput.write("<Function Definitions> ::= <Function> | <Function> <Function Definitions>")
        Function(current_i, switch) 
        FunctionDef(current_i, switch); 
        
           
#R4      
def Function(current_i, switch):
    if switch == "1":
        fileoutput.write("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")
        if lexemes == "function":
            current_i += 1
            #not finish yet
            
            
def StatementList(current_i, switch):
    pass

def OptDeclarationList(current_i, switch):
    pass

#R21
def Scan(current_i, switch):
    fileoutput.write("<Scan> ::= scan ( <IDs> );")
    if lexemes[current_i] == "scan":
        current_i += 1
        if lexemes[current_i] == "(":
            current_i += 1
            IDS()
            if lexemes[current_i] == ")":
                current_i += 1
                if lexemes[current_i] == ";":
                    current_i += 1
                else: fileoutput.write("Syntax Error, Expected ;")
            else: fileoutput.write("Syntax Error, Expected )")
        else: fileoutput.write("Syntax Error, Expected ()")
    
def IDS():
    pass

#R24
def Reloop(current_i, switch):
    if switch == "1":
        fileoutput.write("<Relop> ::= == | != | > | < | <= | =>")
        relop = ["==", "!=", "!=", ">", "<", "<=", "=>"]
        if lexemes[current_i] in relop:
            current_i += 1
        else:
            fileoutput.write("Syntax Error")



#R29
def Empty():
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
