# Exercises for 10/9-2017

Author: Michael Kirkedal Thomsen <kirkedal@acm.org>

These exercises will:
* Recap some material about pointer and pointer arithmetic.
* Introduce some simple instructions and make you run the on your machine.


## `./arg_address`
Write a C program that given any number of arguments, prints the addresses of the all arguments and exits with
`EXIT_SUCCESS`.

## `./ohce`
Write a C program that given one argument, uses pointer arithmetic to print an argument in reverse order and exits with `EXIT_SUCCESS`.
All other cases should exit with `EXIT_FAILURE`.

## Memory calculation and operation from register file
* BOH 3.1  (page 218)
* BOH 3.2  (page 221)
* BOH 3.3  (page 222)

## `./origins_of_fib`
Recall the structure of the call stack. Write a C program that given number calculates the Fibonacci function using the recursive approach: `fib(n) = fib(n-1) + fib(n-2)`. Before each call returns the program should print the input value, output value and return address.

