# Code for a lexical analyzer using a Finite State Machine goes
#Helper Function
# separator_check(), operator_check(), keyword_check()
#Check to see if the char is a separator

def separator_check(char):
  separator = {'(', ')', '{', '}', '%', '@', ',', '[', ']', ';'}
  if char in separator:

    return 1
  else:
    return 0


#Check to see if the char is a operator
def operator_check(char):
  operator = {'+', '-', '*', '/', '>', '<', '=', ':'}
  if char in operator:

    return 1
  else:
    return 0


#Check to see if the str is a keyword
def keyword_check(word):
  keywords = ['integer', 'if', 'else', 'endif', 'while', 'return', 'scan', 'print', 'for', 'elseif']
  if word in keywords:
    #print ("Keyword", word)
    return 1
  else:
    return 0


def char_to_col(char):
  if (char.isdigit()):
    return 1
  elif (char == '.'):
    return 2
  elif (char.isalpha()):
    return 3
  elif (char == '_'):
    return 4
  else:
    return 5


def dfsm_int(str):
  '''
    starting state 1 accepting state 2
    array[state][col]
    array[1][1]
    array[3][1]
    0  1(d) 2(.)  3(l)  4(_)  5(invalid)      

    1   2    0      0     0      0             

    2   2    0      0     0      0             
    '''

  state = 1
  accepting_state = [2]
  table = [[0, 1, 2, 3, 4, 5], [1, 2, 0, 0, 0, 0], [2, 2, 0, 0, 0, 0]]

  for i in range(len(str)):
    col = char_to_col(str[i])
    state = table[state][col]
    if state == 0:
      break

  if state == accepting_state[0]:

    return 1
  else:
    return 0


def dfsm_real(str):
  '''

  0  1(d) 2(.)  3(l)  4(_)  5(invalid)

  1   2    0      0     0      0    

  2   2    3      0     0      0   

  3   4    0      0     0      0

  4   4    0      0     0      0
  '''
  state = 1
  accepting_state = [2, 3, 4]
  table = [[0, 1, 2, 3, 4, 5], [1, 2, 0, 0, 0, 0], [2, 2, 3, 0, 0, 0],
           [3, 4, 0, 0, 0, 0], [4, 4, 0, 0, 0, 0]]

  for i in range(len(str)):
    col = char_to_col(str[i])
    state = table[state][col]
    if state == 0:
      break

  if state == accepting_state[0] or state == accepting_state[1] or state == accepting_state[2]:
    return 1
  else:
    return 0


##Double check my work yall!
def dsfm_id(str):
  '''
  DFSM to recognize identifiers

  0  1(d) 2(.)  3(l)  4(_)  5(invalid)

  1   0    0      2     0      0    

  2   3    0      3     3      0   

  3   4    0      4     4      0

  4   4    0      4     4      0

  '''
  state = 1
  accepting_state = [2, 3, 4]
  table = [[0, 1, 2, 3, 4, 5], [1, 0, 0, 2, 0, 0], [2, 3, 0, 3, 3, 0],
           [3, 4, 0, 4, 4, 0], [4, 4, 0, 4, 4, 0]]

  for i in range(len(str)):
    col = char_to_col(str[i])
    state = table[state][col]
    if state == 0:
      break

  if state == accepting_state[0] or state == accepting_state[1] or state == accepting_state[2]:
    return 1
  else:
    return 0



def lexer(filename):
    with open(filename, "r") as file:
        content = file.read()
        word = ""
        i = 0
        in_comment = False
        
        while i < (len(content) - 1):
            char = content[i]
            if char == "[" and not in_comment:
                i += 1
                if content[i] == "*":
                    in_comment = True
                    i += 1
                    continue
            if char == "*" and in_comment:
                i += 1
                if content[i] == "]":
                    in_comment = False
                    i += 1
                    continue
            if in_comment == True:
                i += 1
                continue


            if in_comment == False:
                if char.isspace():
                    i += 1
                    continue
                
                elif operator_check(char) == 1:
                    i += 1
                    if operator_check(content[i]) == 1:
                      print(char+content[i], "                   Operator")
                      i += 1
                    elif operator_check(content[i]) == 0:
                      print(char, "                   Operator")
                      i += 1
                
                elif separator_check(char) == 1:
                    print(char, "                   Separator")
                    i += 1
                
                elif char.isalpha() or char == '':
                    word += char
                    i += 1
                    while i < len(content) and (content[i].isalnum() or content[i] == '_'):
                        word += content[i]
                        i += 1
                    if keyword_check(word) == 1:
                        print(word, "               Keywords")
                    elif dsfm_id(word) == 1:
                        print(word, "                   Identifier")
                    else:
                        print(word, "                   Invalid")
                    word = ""
                
                elif char.isdigit():
                    word += char
                    i += 1
                    while i < len(content) and (content[i].isdigit() or content[i] == '.'):
                        word += content[i]
                        i += 1
                    if dfsm_int(word) == 1:
                        print(word, "                   Integers")
                    elif dfsm_real(word) == 1:
                        print(word, "                 Reals")
                    else:
                        print(word, "                   Invalid")
                    word = ""
                else:
                    print(char, "                   Invalid")
                    i += 1
            
                        
                    

find = True
while(find):
  try:
    file_name = input('Enter the filename: ')
    print("Tokens:              Lexemes:")
    lexer(file_name)
    find = False
  except OSError:
     print("Can not find the file.")
