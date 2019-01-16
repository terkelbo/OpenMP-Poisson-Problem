TARGET  = poisson_openmp1

SRC_DIR = src
OBJ_DIR = obj

SRC = $(wildcard $(SRC_DIR)/*.c)
OBJ = $(SRC:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

CPPFLAGS = -Iinclude

OPT = -g -fast -xO5 -xrestrict -xopenmp  -xloopinfo -xvpara -xautopar -xinline=no
PIC = -fPIC

CC  = suncc
CFLAGS= $(OPT) $(PIC) $(XOPTS) -std=c99

SOFLAGS = 
XLIBS   =  -lm -xopenmp

$(TARGET): $(OBJ)
	$(CC) -o $@ $(SOFLAGS) $(OBJ) $(XLIBS)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

clean:
	@/bin/rm -f core core.* $(OBJ_DIR)/$(OBJ) $(OBJ_DIR)/*.o
