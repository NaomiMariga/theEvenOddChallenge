"""Use input() to read input from library and use print to write your output"""

def main():
    try:
        print("................................The Program Started!................................")
        
        print("Number of tests to run:")
        T = int(input()) #T is the number of inputs expected. We have to convert it to integer since input takes strings
        while T>=1 and T<=10: # this limits loops to 10
            print("String of alphabets:")
            S = input() #S is the string input expected
            lengthOfString = len(S) 
            if lengthOfString >= 2 and lengthOfString <= 10000: #length of string cannot be less than 2 and more than 1000 characters
                oddIndexedAsciiValues = 0
                evenIndexedAsciiValues = 0
                for index in range(lengthOfString):
                    if index/2 == 0:
                        letter = S[index]
                        evenAsciiValue = ord(letter) #convert letters to their ASCII values eg a = 97
                        if evenAsciiValue in range(65,97):
                            evenAsciiValue += 32 #convert uppercase characters to lowercase
                            evenIndexedAsciiValues += evenAsciiValue         #add all the numbers at even index            
                        elif evenAsciiValue in range(97, 123):
                            evenIndexedAsciiValues += evenAsciiValue #handling the already lowercase letters
                        else:
                            message = evenAsciiValue + " Not in the recommended range"
                            print(message)
                    else:       
                        letter = S[index]
                        oddAsciiValue = ord(letter) #convert letters to their ASCII values eg a = 97
                        if oddAsciiValue in range(65,97):
                            oddAsciiValue += 32 #convert uppercase characters to lowercase
                            oddIndexedAsciiValues += oddAsciiValue       #add all the numbers at odd index                
                        elif oddAsciiValue in range(97, 123):
                            oddIndexedAsciiValues += oddAsciiValue #handling the already lowercase letters
                        else:
                            message = oddAsciiValue + " Not in the recommended range"
                            print(message)
            else:
                message = lengthOfString + " Not within the recommended range"
                print(message)
                        

            absoluteDifference = abs(evenIndexedAsciiValues - oddIndexedAsciiValues) #get the absolute difference
            
            #Getting modolus of the difference divided by prime numbers between 1 and 10 which are (3, 5 and 7)
            
            if (absoluteDifference != 0) and ((absoluteDifference % 3 == 0) or (absoluteDifference % 5 == 0) or (absoluteDifference % 7 == 0)):
                print("Prime String")
            elif (absoluteDifference != 0) and ((absoluteDifference % 3 != 0) or (absoluteDifference % 5 != 0) or (absoluteDifference % 7 != 0)):
                print("Casual String")
            else:
                print("I don't know how to handle that request")
                

            T -= 1 #decrementing the value of T to make sure the loop will eventually end. 

        print("................................The Program Completed!................................")

    except Exception as error: #handle all errors to prevent program from crashing
        print("Oops an error occured!: \n" + str(error)) #print the error and exit the program 
        print("................................The Program Aborted!................................")
        exit()
        
main()


# Challenge instructions 
"""
Prime String (100 Marks)
Oddia and Evenia are two friends who love strings and prime numbers. Although they have the same taste and like similar things, they are enemies when it comes to even and odd numbers. Oddia likes the odd numbers and Evenia likes the even numbers. They have a problem for you to solve.


A string S of lowercase letters will be provided and you have to figure out if the given string is Prime String or not.


Prime String: A string is considered a prime string only if the absolute difference between the sum of odd indexed letters and even indexed letters is completely divisible by any of the odd prime numbers less than 10.


Note: For calculations, consider the ASCII value of lowercase letters.


Example:

String, S = abcdef

Summation of Odd Indexed letters, O = a + c + e = 97 + 99 + 101 = 297

Summation of Even Indexed letters, E = b + d + f = 98 + 100 + 102 = 300


Absolute Difference = |O-E| = |297-300| = 3


This is completely divisible by 3 and leaves 0 as remainder. Thus, the given string is a Prime String.


If the string is prime string, print Prime String otherwise print Casual String. Can you solve it?

Input Format
The first line of input consists of the number of test cases, T

Next N lines each consist of a string, S.


Note: Read the input from the console.

Constraints
1<= T <=10

2<= |S| <=10000


|S| is the length of the string.

Output Format
For each test case, print Prime String if the string is prime string otherwise print Casual String.

Sample TestCase 1
Input
2
bbae
abcdef
Output
Casual String
Prime String
Explanation
Test Case 1: 

Sum of Odd indexed letters, O = 98+97 = 195

Sum of Even indexed letters, E = 98 + 101 = 199


Absolute Difference = |195-199| = 4


This is not divisible by any of the odd prime numbers. The given string is Casual String.


Test Case 2: As explained in the example.
Time Limit(X):
0.50 sec(s) for each input.
Memory Limit:
512 MB
Source Limit:
100 KB
Allowed Languages:
C, C++, C++11, C++14, C#, Java, Java 8, Kotlin, PHP, PHP 7, Python, Python 3, Perl, Ruby, Node Js, Scala, Clojure, Haskell, Lua, Erlang, Swift, VBnet, Js, Objc, Pascal, Go, F#, D, Groovy, Tcl, Ocaml, Smalltalk, Cobol, Racket, Bash, GNU Octave, Rust, Common LISP, R, Julia, Fortran, Ada, Prolog, Icon, Elixir, CoffeeScript, Brainfuck, Pypy, Lolcode, Nim, Picolisp, Pike, pypy3


"""