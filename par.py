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
        Empty()
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
                    fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
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
    if tokens[current_i] == "Identifier":
        if switch == "1":
            fileoutput.write("<Opt Parameter List> ::= <Parameter List>\n")
        current_i = ParaList(current_i, switch)
    else:
        if switch == "1":
            fileoutput.write("<Opt Parameter List> ::= <Epsilon>\n")
        Empty()    
    return current_i
    
def ParaList(current_i, switch):
    if switch == "1":
        fileoutput.write("<ParameterList> ::= <Parameter> <ParameterListPrime>\n")
    current_i = Paramater(current_i, switch)
    current_i = ParaListPrime(current_i, switch)
    return current_i
    
def ParaListPrime(current_i, switch):
    if tokens[current_i] == "Identifier":
        if switch == "1":
            fileoutput.write("<Parameter List Prime> ::= <Parameter List>\n")
        current_i = ParaList(current_i, switch)
    else:
        if switch == "1":
            fileoutput.write("<Parameter List Prime> ::= <Epsilon>\n")
        Empty()
    return current_i
        
def Paramater(current_i, switch):
    fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
    if switch == "1":
        fileoutput.write("<Parameter> ::= <IDs > <Qualifier> \n")
    current_i = IDs(current_i, switch)
    current_i = Qualifier(current_i, switch)
    return current_i

def OptDeclarationList(current_i, switch):
    if lexemes[current_i] == "integer":
        current_i = DeclarationList(current_i, switch)
        if switch == "1":
            fileoutput.write("<Opt Declaration List> ::= <Declaration List>\n") 
    elif lexemes[current_i] == "boolean":
        current_i = DeclarationList(current_i, switch)  
        if switch == "1":
            fileoutput.write("<Opt Declaration List> ::= <Declaration List>\n")  
    elif lexemes[current_i] == "real":
        current_i = DeclarationList(current_i, switch) 
        if switch == "1":
            fileoutput.write("<Opt Declaration List> ::= <Declaration List>\n") 
    else:    
        if switch == "1":
            fileoutput.write("<Opt Declaration List> ::= <Epsilon>\n")
        Empty()
    return current_i

def DeclarationList(current_i, switch):
    if switch == "1":
        fileoutput.write("<DeclarationList> ::= <Declaration> <DeclarationListPrime>\n")
    current_i = Declaration(current_i, switch)
    current_i = DeclarationListPrime(current_i, switch)
    return current_i

def DeclarationListPrime(current_i, switch):
    if lexemes[current_i] == "integer":
        current_i = DeclarationList(current_i, switch)
        if switch == "1":
            fileoutput.write("<Opt Declaration List Prime> ::= <Declaration List>\n") 
    elif lexemes[current_i] == "boolean":
        current_i = DeclarationList(current_i, switch)  
        if switch == "1":
            fileoutput.write("<Opt Declaration List Prime> ::= <Declaration List>\n")  
    elif lexemes[current_i] == "real":
        current_i = DeclarationList(current_i, switch) 
        if switch == "1":
            fileoutput.write("<Opt Declaration List Prime> ::= <Declaration List>\n") 
    else:    
        if switch == "1":
            fileoutput.write("<Opt Declaration List Prime> ::= <Epsilon>\n")
        Empty()
    return current_i

def Declaration(current_i, switch):
    fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
    if switch == "1":
        fileoutput.write("<Parameter> ::= <Qualifier> <IDs> \n")
    current_i = Qualifier(current_i, switch)
    current_i = IDs(current_i, switch)
    return current_i

def StatementList(current_i, switch):
    current_i += 1
    return current_i

def Body(current_i, switch):
    if lexemes[current_i] == "{":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Body> ::= { < Statement List> }")
            
        current_i = StatementList(current_i, switch)    
        
        if lexemes[current_i] == "}":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1
            if switch == "1":
                fileoutput.write("<Body> ::= { < Statement List> }")
        else:fileoutput.write("Syntax error, expected } \n")        
    else:fileoutput.write("Syntax error, expected { \n")              
    return current_i

def Compound(current_i, switch):
    if lexemes[current_i] == "{":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Compound> ::= { <Statement List> }")
            
        current_i = StatementList(current_i, switch)    
        
        if lexemes[current_i] == "}":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1
            if switch == "1":
                fileoutput.write("<Compound> ::= { <Statement List> }")
                
    return current_i

def Statement(current_i, switch):
    return current_i

def IDs(current_i, switch):
    if tokens[current_i] == "Identifier":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<IDs> ::= <Identifier> <IDsPrime>\n")
        current_i = IDSPrime(current_i, switch)             
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
            fileoutput.write("<Qualifier> ::= integer | boolean | real \n")
    elif lexemes[current_i] == "boolean":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<Qualifier> ::= integer | boolean | real \n")
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
            fileoutput.write(" <Scan> ::= scan ( <IDs> );")
        if lexemes[current_i] == "(":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1   
            if switch == "1":
                fileoutput.write(" <Scan> ::= scan ( <IDs> );")
            current_i = IDs(current_i, switch)
            if lexemes[current_i] == ")":
                fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                current_i += 1   
                if switch == "1":
                    fileoutput.write("<Scan> ::= scan ( <IDs> );")
                if lexemes[current_i] == ";":
                    fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                    current_i += 1   
                    if switch == "1":
                        fileoutput.write("<Scan> ::= scan ( <IDs> );")
                else: fileoutput.write("Syntax error, expected a ;")    
            else: fileoutput.write("Syntax error, expected a )")     
        else: fileoutput.write("Syntax error, expected a (")     
    return current_i

def Return(current_i, switch):
    if lexemes[current_i] == "return":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write("<return> ::= <return> <returnPrime>\n")
        current_i = ReturnPrime(current_i, switch)                 
    return current_i

def ReturnPrime(current_i, switch):
    if tokens[current_i] == "Identifier":
        if switch == "1":
            fileoutput.write("<returnPrime> ::= <Expression>\n")
        current_i = Expression(current_i, switch)
    elif tokens[current_i] == "Integer":
        if switch == "1":
            fileoutput.write("<returnPrime> ::= <Expression>\n")
        current_i = Expression(current_i, switch) 
    elif tokens[current_i] == "Real":
        if switch == "1":
            fileoutput.write("<returnPrime> ::= <Expression>\n")
        current_i = Expression(current_i, switch)
    elif lexemes[current_i] == "(":
        if switch == "1":
            fileoutput.write("<returnPrime> ::= <Expression>\n")
        current_i = Expression(current_i, switch)
    elif lexemes[current_i] == "true":
        if switch == "1":
            fileoutput.write("<returnPrime> ::= <Expression>\n")
        current_i = Expression(current_i, switch)         
    elif lexemes[current_i] == "false":
        if switch == "1":
            fileoutput.write("<returnPrime> ::= <Expression>\n")
        current_i = Expression(current_i, switch)             
    else:
        if switch == "1":
            fileoutput.write("<returnPrime> ::= <Epsilon>\n")
        Empty()
    return current_i

def Print(current_i, switch):
    if lexemes[current_i] == "print":
        fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
        current_i += 1
        if switch == "1":
            fileoutput.write(" <Print> ::= print ( <Expression>);")
        if lexemes[current_i] == "(":
            fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
            current_i += 1   
            if switch == "1":
                fileoutput.write(" <Print> ::= print ( <Expression>);")
            current_i = Expression(current_i, switch)
            if lexemes[current_i] == ")":
                fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                current_i += 1   
                if switch == "1":
                    fileoutput.write(" <Print> ::= print ( <Expression>);")
                if lexemes[current_i] == ";":
                    fileoutput.write(str(lexemes[current_i]) + "   " + str(tokens[current_i]) + "\n")
                    current_i += 1   
                    if switch == "1":
                        fileoutput.write(" <Print> ::= print ( <Expression>);")
                else: fileoutput.write("Syntax error, expected a ;")    
            else: fileoutput.write("Syntax error, expected a )")     
        else: fileoutput.write("Syntax error, expected a (")     
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
            
    elif tokens[current_i] == "Real":
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
    switch = input("Enter 0 (Turn off syntax) or 1 (Turn on syntax): ")
    print(lexemes)
    current_i = ParCheck(0, switch)


except OSError:
    print("Can not find the file.")