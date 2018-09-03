# OS X users should use additionally gcc-X, gcc will invoke the Clang compiler
CC=gcc-8
CFLAGS=-std=c11 -Wall -Werror -Wextra -pedantic

.PHONY: clean all

%.o: %.c
	$(CC) $(CFLAGS) -o $@ -c $<

# No cleaning up!!! Be aware of this...
