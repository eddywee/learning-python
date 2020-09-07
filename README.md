# learning-python
an udemy course to learn python

# chapter one

basic steps to install python on mac/linux/windows... install @ windows with "adding to path" option

after finishing the installation test it:

* open a command line tool
* type: python
* within the interpreter type: "import requests"
* ctrl+z to get out

installation completed.

## the hello world example
create a file named test.py type here

 ```print("hello world")```

 save the file and run the interpreter with the command ```python test.py```

 ## basic types - numbers
 5 + 6 = 11 <br>
 "5" + "6" = 56

 mathematic and string operations are separeted like this...
 when operating with double variables use "." not ","...

 wrap numbers in functions like int:
 ```
 int("5") + int("6")
 ``` 
 **this is just working with characters that are numbers...** if you are using something like: int("hello world") you would run into an error.ss

 ## working with quotes
 to use a string use double quotes like 

 ```"hello world"``` <br>

 if you need quoatations within a quote you can esacpe with a backslash like <br>

 ```"She said \"I need to finish my business\"..."```

## booleans
be aware of quotations while checking if something is true or false for e.g. ```if( x == "True" )``` wont work..... you would have to do it more like ```if (x == True)```


## arrays & lists
["Movies", "Games", "Python"]
>> ['Movies', 'Games', 'Python']

["Movies", "Games", "Python"][0]
>> 'Movies's'

## dictonaries
are defined with ```{}```

example:
```{"name": "eddy", "age": "31", "hobby": "crossfit"}```

to access one the values use this:
```{"name": "eddy", "age": "31", "hobby": "crossfit"}["age"]```

the result would be: ```31```


## variables

easy peasy lemon squeezy

## buildin functions
int
str
fload
bool
len