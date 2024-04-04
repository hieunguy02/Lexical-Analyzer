# Lexical Analyzer
 

Project for CPSC323
Spring 24
The programming assignments are based on a language called "Rat24S" which is described as
follows. The Rat24S language is designed to be an easy to understand. It has a short grammar and relatively clean
semantics.

RAT24S
1) Lexical Conventions:
The lexical units of a program are identifiers, keywords, integers, reals, operators and other
separators. Blanks, tabs and newlines (collectively, "white space") as described below
are ignored except as they serve to separate tokens.
Some white space is required to separate otherwise adjacent identifiers, keywords, reals and integers.
<Identifier> is a sequence of letters, digits or “_”. However, the first character must be a letter. Upper and lower
cases are same.
<Integer> is an unsigned decimal integer i.e., a sequence of decimal digits.
<Real> is integer followed by “.” and Integer, e.g., 123.00
Some identifiers are reserved for use as keywords, and may not be used otherwise:
e.g., integer, if, else, endif, while, return, scan, print etc.
Comments are enclosed in [* *] and should be entirely ignored by the LA, SA etc.
2) Syntax rules : The following BNF describes the Rat24S.
R1. Rat24S ::= $ <OptFunctionDefinitions> $ <OptDeclarationList> $ <StatementList> $

R2. OptFunctionDefinitions ::= FunctionDefinitions | Empty

R3. FunctionDefinitions ::= Function | Function FunctionDefinitions

R4. Function ::= function Identifier ( <OptParameterList> ) OptDeclarationList Body

R5. OptParameterList ::= ParameterList | Empty

R6. ParameterList ::= Parameter | Parameter , ParameterList

R7. Parameter ::= IDs Qualifier

R8. Qualifier ::= integer | boolean | real

R9.Body ::= { StatementList }

R10. OptDeclarationList ::= DeclarationList | Empty

R11. DeclarationList := Declaration ; | Declaration ; DeclarationList

R12. Declaration ::= Qualifier IDs

R13. IDs ::= Identifier | Identifier, IDs

R14. StatementList ::= Statement | Statement StatementList

R15. Statement ::= Compound | Assign | If | Return | Print | Scan | While

R16. Compound ::= { StatementList }

R17. Assign ::= Identifier = Expression ;

R18. If ::= if ( Condition ) Statement endif | if ( Condition ) Statement else Statement endif

R19.Return ::= return ; | return Expression ;

R20. Print ::= print ( Expression);

R21. Scan ::= scan ( IDs );

R22. While ::= while ( Condition ) Statement endwhile

R23. Condition ::= Expression Relop Expression

R24. Relop ::= == | != | > | < | <= | =>

R25. Expression ::= Expression + Term | Expression - Term | Term

R26. Term ::= Term * Factor | Term / Factor | Factor

R27. Factor ::= - Primary | Primary

R28. Primary ::= Identifier | Integer | Identifier ( IDs ) | ( Expression ) |Real | true | false

R29. Empty ::= 


3) Some Semantics
 Rat24S is a conventional imperative programming language. A Rat24S program consists of a sequence of
functions followed by the "main body" where the program executes.
 All variables and functions must be declared before use.
 Function arguments are passed by value.
 There is an implied expressionless return at the end of all functions; the value returned by expressionless
return statement is undefined.
 Arithmetic expressions have their conventional meanings.
 Integer division ignores any remainder.
 Type casting is not allowed (e.g., assigning an integer to a real variable)
 No arithmetic operations are allowed with booleans (e.g., true + false)
 Others, as we will define during the semester

5) A sample Rat24S Program
[* this is comment for this sample code which
converts Fahrenheit into Celcius *]
$
function convertx (fahr integer)
{
return 5 * (fahr -32) / 9;
}
$
integer low, high, step; [* declarations *]
$
scan (low, high, step);
while (low <= high )
{ print (low);
print (convertx (low));
low = low + step;
}
endwhile
$
