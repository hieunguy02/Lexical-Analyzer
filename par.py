from lexical import lexer, file_name, fileoutput, tokens, lexemes
#Finish 1 2 3 4 8 13 21 24 25 26 27 28 29
#Unfinish 5 6 7 9 10 11 12 14 15 16 17 18 19 20 22 23  

def RATS24(current_i, switch):
    fileoutput.write("Lexemes:    Tokens:\n")
    if current_i is not None and lexemes[current_i] == "$":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $\n")
        current_i = OptFunctionDef(current_i, switch)

        if current_i is not None and lexemes[current_i] == "$":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1
            current_i = OptDeclarationList(current_i, switch)

            if current_i is not None and lexemes[current_i] == "$":
                fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                current_i += 1
                current_i = StatementList(current_i, switch)

                if current_i is not None and lexemes[current_i] == "$":
                    fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                    current_i += 1
                else:
                    fileoutput.write("Syntax Error, expected a $\n")
            else:
                fileoutput.write("Syntax Error, expected a $\n")
        else:
            fileoutput.write("Syntax Error, expected a $\n")
    return current_i

def OptFunctionDef(current_i, switch):
    if lexemes[current_i] == "function":
        if switch == "1":
            fileoutput.write("<Opt Function Definitions> ::= <Function Definitions>\n")
        current_i = FunctionDef(current_i, switch)
    else:
        if switch == "1":
            fileoutput.write("<Opt Function Definitions> ::= <Epsilon>\n")
    return current_i

def FunctionDef(current_i, switch):
    if switch == "1":
        fileoutput.write("<Function Definitions> ::= <Function> <Function Definitions Prime>\n")
    current_i = Function(current_i, switch)
    current_i = FunctionDefPrime(current_i, switch)
    return current_i

def FunctionDefPrime(current_i, switch):
    if lexemes[current_i] == "function":
        if switch == "1":
            fileoutput.write("<Function Definitions Prime> ::= <Function Definitions>\n")
        current_i = FunctionDef(current_i, switch)
    else:
        if switch == "1":
            fileoutput.write("<Function Definitions Prime> ::= <Epsilon>\n")
        Empty()
    return current_i

def Function(current_i, switch):
    if lexemes[current_i] == "function":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        if switch == "1":
            fileoutput.write("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>\n")
        current_i += 1
        
        if tokens[current_i] == "Identifier":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            if switch == "1":
                fileoutput.write("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>\n")
            current_i += 1
            
            if lexemes[current_i] == "(":
                fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                if switch == "1":
                    fileoutput.write("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>\n")
                current_i += 1
                current_i = OptDeclarationList(current_i, switch)  
                
                if lexemes[current_i] == ")":
                    fileoutput.write("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>\n")
                    if switch == "1":
                        fileoutput.write("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>\n")
                    current_i += 1
                    
                    current_i = OptDeclarationList(current_i, switch)  
                    
                    current_i = Body(current_i, switch)  
                        
                else: fileoutput.write('Syntax Error, expected ) \n')
            else: fileoutput.write('Syntax Error, expected ( \n')
        else:  fileoutput.write('Syntax Error, expected identifier \n')    
    else: fileoutput.write('Syntax Error, expected function \n')
    return current_i

def OpParaList(current_i, switch):
    return current_i

def StatementList(current_i, switch):
    return current_i

def Body():
    return current_i

def OptDeclarationList(current_i, switch):
    return current_i

def Statement(current_i, switch):
    return current_i

def IDs(current_i, switch):
    if tokens[current_i] == "Identifier":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<IDs> ::= <Identifier>, <IDsPrime>\n")
        if lexemes[current_i] == ",":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1
            if switch == "1":
                fileoutput.write("<IDs> ::= <Identifier>, <IDsPrime>\n")    
            current_i = IDSPrime(current_i, switch)    
        else: fileoutput.write("Syntax Error, expected a , \n")              
    return current_i

def IDSPrime(current_i, switch):
    if tokens[current_i] == "Identifier":
        if switch == "1":
            fileoutput.write("<IDsPrime> ::= <IDs>\n")
        current_i = IDs(current_i, switch)
    else:
        if switch == "1":
            fileoutput.write("<IDsPrime> ::= <Epsilon>\n")
        Empty()
    return current_i

def Qualifier(current_i, switch):
    if lexemes[current_i] == "integer":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Qualifier> ::= integer | boolean | real")
    elif lexemes[current_i] == "boolean":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Qualifier> ::= integer | boolean | real")
    elif lexemes[current_i] == "real":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Qualifier> ::= integer | boolean | real \n")
    else: fileoutput.write("Syntax error, expected a qualifier integer, boolean or real \n")     
    return current_i

def Scan(current_i, switch):
    if lexemes[current_i] == "scan":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Scan> ::= scan ( <IDs> );")
    return current_i

def Expression(current_i, switch):
    if switch == "1":
        fileoutput.write("<Expression> ::= <Term> <Expression>")
    current_i = Term(current_i, switch)
    current_i = ExpressionPrime(current_i, switch)    
    return current_i


def ExpressionPrime(current_i, switch):
    if lexemes[current_i] == "+":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Expression Prime> ::= + <Term> <Expression Prime> \n")
        current_i = Term(current_i, switch)
        current_i = ExpressionPrime(current_i, switch)      
            
    elif lexemes[current_i] == "-":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Expression Prime> ::= - <Term> <Expression Prime> \n")
        current_i = Term(current_i, switch)
        current_i = ExpressionPrime(current_i, switch)   
            
    else:
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        if switch == "1":
            fileoutput.write("<Term Prime> ::= <Epsilon> \n")   
        Empty() 
            
    return current_i


def Term(current_i, switch):
    if switch == "1":
        fileoutput.write("<Term> ::= <Term> <TermPrime>")
    current_i = Factor(current_i, switch)
    current_i = TermPrime(current_i, switch)    
    return current_i

def TermPrime(current_i, switch):
     
    if lexemes[current_i] == "*":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Term Prime> ::= * <Factor> <Term Prime> \n")
        current_i = Factor(current_i, switch)
        current_i = TermPrime(current_i, switch)      
            
    elif lexemes[current_i] == "/":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Term Prime> ::= / <Factor> <Term Prime> \n")
        current_i = Factor(current_i, switch)
        current_i = TermPrime(current_i, switch)  
            
    else:
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        if switch == "1":
            fileoutput.write("<Term Prime> ::= <Epsilon> \n")   
        Empty() 
            
    return current_i

def Factor(current_i, switch):
    if lexemes[current_i] == "-":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write(" - <Primary>\n")
        current_i = Primary(current_i, switch)
    else:    
        current_i = Primary(current_i, switch)
        if switch == "1":
            fileoutput.write(" <Primary>\n")
    return current_i

def Primary(current_i, switch):
    if tokens[current_i] == "Identifier":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i = IDs(current_i, switch)
        if switch == "1":
            fileoutput.write("<Primary> ::= <Identifier>; \n")
            
    elif tokens[current_i] == "Integer":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Primary> ::= <Integer>; \n")
            
    elif tokens[current_i] == "real":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Primary> ::= <Real>; \n")
            
    elif lexemes[current_i] == "true":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Primary> ::= <true>; \n")        
        
    elif lexemes[current_i] == "(":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Primary> ::=  (<Expression>); \n") 
            
        current_i = Expression(current_i, switch)
        
        if lexemes[current_i] == ")":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1
            if switch == "1":
                fileoutput.write("<Primary> ::= (<Expression>); \n") 
        else: fileoutput.write("Syntax error, expected a ); \n")           
        
    
    elif lexemes[current_i] == "false":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Primary> ::= <false>; \n")  
            
    else: fileoutput.write("Syntax error, expected Identifier or Integer or (Expression) or Real or true or false")   
    
    return current_i


def Reloop(current_i, switch):
    relop = ["==", "!=", "!=", ">", "<", "<=", "=>"]
    if lexemes[current_i] in relop:
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Relop> ::= == | != | > | < | <= | =>\n")
        else:
            fileoutput.write("Syntax Error, expected a == or != or > or < or <= or =>\n")
    return current_i

def Empty():
    return

def ParCheck(current_i, switch):
    current_i = RATS24(current_i, switch)
    return current_i

try:
    lexer(file_name)
    print(lexemes)
    switch = input("Enter 0 (Turn off syntax) or 1 (Turn on syntax): ")
    current_i = ParCheck(0, switch)
    print(lexemes)

except OSError:
    print("Can not find the file.")