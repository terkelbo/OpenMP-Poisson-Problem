TARGET	= mandelbrot
OBJS	= main.o mandel.o

OPT	= -g -fast -xopenmp -xloopinfo
ISA	= 
PARA	= 

ARCH	      = $(shell uname -p)

CCC	= CC
CXX	= CC

CFLAGS	= $(OPT) $(ISA) $(PARA) $(XOPT)

F90C  	= f90

LIBS	= -xopenmp 


all: $(TARGET)

$(TARGET): $(OBJS) 
	$(CCC) $(CFLAGS) -o $@ $(OBJS) $(LIBS)

clean:
	@/bin/rm -f *.o core

realclean: clean
	@rm -f $(TARGET)
	@rm -f mandelbrot.png

# dependencies
#
main.o  : main.c mandel.h
mandel.o: mandel.c
