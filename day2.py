#python day2 abhishk veeramalla
#.py extension for pytjon files
#data type : to declear the given human radab;e data in which formate
#syntax: how your declearing that particular variable 
#dynamically typed programming language which means syntax should be decleared "abhishake"
#in built function : for each data type there is an in built function




#example for using built in function of a string to separate a username from a ARN template.
from ast import pattern
from decimal import Rounded


arn = "arn:aws:iam:1234556:user/username"
print(arn.split("/"))# gets spearated 
print(arn.split("/")[1]) #-> to get only user name when [1] added


#print the below to upper case 
name = "abhishaik"
print(name.upper())#we can also use name.lower for lower case 

#adding two different strings
str1 = "hello"
str2 = "world"
result = str1 + " " + str2 # + = concadiantion{add} in string terminology;added " " to get place between two strings 
print(result)

#to print length of the string
text = "gangadhar"
length = len(text)
print("Length of the string:", length)

#for {numbers} data types are classified into twot types int and float(decimal) 
#for rounding decimal we can use round

number = round(22.3456667)
print("Rounded:",number)
#
num1 = 4
num2 = 5
result = num1 + num2
print("addition:",result)# in same way substraction,division(//),module(%),multiplication,division.

#using absolute value for int will help us to get -ve to +value 
num = 4
num2 = 6
result = num - num2
print("Value:", abs(result))# without abs(result) will show "-2" with abs(result) will show "2"

#regular expressions help us in finding a particular pattern "re" "re.match"
#regular expression also can be used for "find all, match, replace, search, split"
#  in real case we use it for finding error logs in the log file pattern:"error:"
import re

text = "the gangadhar in"
text2 = "the sumanth in"
text3 = "the manu in"
text4 = "pooji in"
Pattern = r"the"

match = re.match(pattern, text)
if match:
    print("match found:", match.group)
else:
    print("no match:")

