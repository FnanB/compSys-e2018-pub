
CC = gcc
OFLAGS = -Og
CFLAGS = $(OFLAGS) -Wall -g

CINC =
F64 =-m64

.SUFFIXES: .c .64s .64o .64d

.c.s:
	$(CC) $(OFLAGS) $(CINC) -S $(F64) $*.c -o $*.s

.c.d:
	$(CC) $(CFLAGS) $(CINC) $(F64) $*.c -o $*
	objdump -d $* > $*.d
	rm -f $*

files:	a_sum.s	a_sum.d

clean:
	rm -f *~ *.s *.d sum64
