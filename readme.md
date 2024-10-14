nah who needs a readme....
but seriously read this to the end to not get any errors bc error handling is non-existent.
Java side is not deprecated cuz im not doing all that again

types: int, str, bool, list

Stack size is in length of the list not in bytes

BASIC SYNTAX:
PUSH <int>: used to push a number to the stack. can only push ints currently

READ: used to get user input 

ADD: takes the top 2 numbers in the stack then adds them. this removes those 2 items from the stack then pushes the answer

PRINT <String>: used to print out a message to stdout.

JUMP.EQ.0 <LABEL>: used to jump to a label when the top of the stack equals 0 

VAR <Type> name<String> val<Type>: used to create a variable of type with name of name

HALT: used to mark the end of a program, if this is missing you get infinite loop :)

Labels:

Labels must end with a ":" A label can look like this >>>  L1:

By default, stack is always 256 spots in size.

OL Commands:

#OL will be the basic command

#OL@ is for commands that relate to how the code is read and what needs to be created

#OL! is for specialized lexer commands

#OL@ Current Commands:

SS <int>: for the stack size

ex: #OL@SS 128

IVS: To include the variable stack

ex: #OL@IVS

EVS: To Exclude the variable stack

ex: #OL@EVS

#OL! Current Commands:

DB: to show the debug messages

ex: #OL!DB

Defaults:

Stack Size: 256

Variable stack: Disabled or Excluded

Debug: Disabled

so java side only works with integers. print statements can be strings. 
Will be adding more support for the python side, java is not looking to get many more updates :)

BTW: python will probably work better when it has better type support.

This is the op lang programming language becuase this was so goofy to code. 

|========|
|{[-OL-]}|
|========|

good luck
