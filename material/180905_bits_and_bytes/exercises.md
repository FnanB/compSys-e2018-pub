# Exercises for 5/9-2018

Author: Oleks Shturmov <oleks@oleks.info> and Michael Kirkedal Thomsen <kirkedal@acm.org>

These exercises are intended to give you some practice with the sort of tasks
that you will be doing in this week's assignment.

For all of the below, you should use `make` to build your programs. To
parametrize `make` to build with all the necessary compiler flags, start by
writing down a `Makefile` containing the following:

```
CC=gcc
CFLAGS=-std=c11 -Wall -Werror -Wextra -pedantic -g
```

Now, to compile the programs below, just `make` them. For example:

```
$ make unary
```

## `./unary`

Write a C program `unary` that given a single command-line argument exits with
`EXIT_SUCCESS`. When given 0, 2, or more arguments, it should exit with
`EXIT_FAILURE`, and print a usage message to `stderr`. (Hint: `EXIT_SUCCESS`
and `EXIT_FAILURE` are defined in `stdlib.h`.)

Use `echo $?` to determine the exit code of the most recent shell command:

```
$ ./unary
$ echo $?
1
$ ./unary arg
$ echo $?
0
```

## `./hello argument`

Write a C program `hello` that handles command-line arguments as above. When
given an argument, it prints `"Hello, %s!\n"` to `stdout`, where `%s` is the
given argument. When the number of arguments is wrong, let it print a usage
message to `stderr`, with the format `"Usage: %s argument\n"`, where `%s` is
the name of the binary.

Sample interaction with `hello`:

```
$ ./hello
Usage: ./hello argument
$ echo $?
1
$ ./hello Eric
Hello, Eric!
$ echo $??

0
```

## `./readable path`

Write a C program `readable` that handles command-line arguments as above, but
calls the argument "`path`". When given a path argument, it attempts to open
the given path for reading using `fopen`. If successful, it prints the line
`Yes` to `stdout`. If unsuccessful, it prints the error reported by the
standard library and exits with `EXIT_FAILURE`.

`fopen` returns `NULL` in case of failure and sets the variable `errno` to a
numerical code representing the error. You can access `errno` if you import
`errno.h`. Furthermore, if you import `string.h`, you can use the function
`strerror` that will give a string representation of the error.

In the end, you can use the following `fprintf`-call in case of failure

```
fprintf(stderr, "%s\n", strerror(errno));
```

Sample interaction with `readable`:

```
$ ./readable
Usage: ./readable path
$ echo $?
1
$ ./readable /
Yes
$ ./readable readable
Yes
$ echo $?
0
$ ./readable vulapyk
No such file or directory
$ echo $?
1
```

## `./size path`

Write a C program `size` that handles command-line arguments as above. When
given a path argument, it attempts to determine the size of the file in bytes.
If the size can be determined, the number is printed as a line to `stdout`, and
`size` exits with `EXIT_SUCCESS`. In all other cases, it should exit with
`EXIT_FAILURE`. (Hint: Use `fseek` and `ftell`.)

Sample interaction with `size`:

```
$ ./size Makefile
58
$ ./size size.c
694
$ ./size size
14392
$ echo $?
0
$ ./size vulapyk
No such file or directory
$ echo $?
1
```

Challenge: Can you determine the size of a file without opening it?

## `.\simp_grep path needle`

Write a C program `simp_grep` that handles command-line arguments as above. When
given a path argument, it attempts to open the `path` in read-only mode and searched its contents for the substring `needle`.
If the file can be opened it prints the number of occurrences of `needle` `path` to `stdout`, and
`simp_grep` exits with `EXIT_SUCCESS`. In all other cases, it should exit with
`EXIT_FAILURE`.

## `.\file_append src_path string dst_path`
Write a C program `file_append` that handles command-line arguments as above. When
given a path argument, it attempts to open `src_path` in read-only mode, appends `string` to the end and writes it to the non-existing `dst_path`.
If `src_path` can be opened and `dst_path` does not exist, it prints a reasonable confirmation message and exits with `EXIT_SUCCESS`. In all other cases, it should print a message describing the failure and exit with `EXIT_FAILURE`.



