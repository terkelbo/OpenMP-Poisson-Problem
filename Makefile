TARGET_NAIVE  = poisson_naive
TARGET_1 = poisson_openmp1
TARGET_2 = poisson_openmp2
TARGET_3 = poisson_ccnuma

SRC_DIR = src
OBJ_DIR = obj

SRC = $(wildcard $(SRC_DIR)/*.c)
OBJ = $(SRC:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

CPPFLAGS = -Iinclude

OPT = -g -fast -xO5 -xrestrict -xopenmp
PIC = -fPIC

CC  = suncc
CFLAGS= $(OPT) $(PIC) $(XOPTS) -std=c99

SOFLAGS = 
XLIBS   =  -lm -xopenmp

all: $(TARGET_NAIVE) $(TARGET_1) $(TARGET_2) $(TARGET_3)

$(TARGET_NAIVE): $(OBJ_DIR)/main_naive.o $(OBJ_DIR)/jacobi_naive.o $(OBJ_DIR)/gaussseidel_naive.o $(OBJ_DIR)/inittools_naive.o
	$(CC) -o $@ $(SOFLAGS) $(OBJ_DIR)/main_naive.o $(OBJ_DIR)/jacobi_naive.o $(OBJ_DIR)/gaussseidel_naive.o $(OBJ_DIR)/inittools_naive.o $(XLIBS)

$(TARGET_1): $(OBJ_DIR)/main_openmp1.o $(OBJ_DIR)/jacobi_openmp1.o $(OBJ_DIR)/gaussseidel.o $(OBJ_DIR)/inittools.o
	$(CC) -o $@ $(SOFLAGS) $(OBJ_DIR)/main_openmp1.o $(OBJ_DIR)/jacobi_openmp1.o $(OBJ_DIR)/gaussseidel.o $(OBJ_DIR)/inittools.o $(XLIBS)

$(TARGET_2): $(OBJ_DIR)/main_openmp2.o $(OBJ_DIR)/jacobi_openmp2.o $(OBJ_DIR)/gaussseidel.o $(OBJ_DIR)/inittools.o
	$(CC) -o $@ $(SOFLAGS) $(OBJ_DIR)/main_openmp2.o $(OBJ_DIR)/jacobi_openmp2.o $(OBJ_DIR)/gaussseidel.o $(OBJ_DIR)/inittools.o $(XLIBS)

$(TARGET_3): $(OBJ_DIR)/main_openmp2.o $(OBJ_DIR)/jacobi_openmp2.o $(OBJ_DIR)/gaussseidel.o $(OBJ_DIR)/inittools_ccnuma.o
	$(CC) -o $@ $(SOFLAGS) $(OBJ_DIR)/main_openmp2.o $(OBJ_DIR)/jacobi_openmp2.o $(OBJ_DIR)/gaussseidel.o $(OBJ_DIR)/inittools_ccnuma.o $(XLIBS)

$(OBJ_DIR)/gaussseidel_naive.o: $(SRC_DIR)/gaussseidel_naive.c include/gaussseidel_naive.h
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
$(OBJ_DIR)/inittools_naive.o: $(SRC_DIR)/inittools_naive.c include/inittools_naive.h
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
$(OBJ_DIR)/gaussseidel.o: $(SRC_DIR)/gaussseidel.c include/gaussseidel.h
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
$(OBJ_DIR)/inittools.o: $(SRC_DIR)/inittools.c include/inittools.h
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
$(OBJ_DIR)/inittools_ccnuma.o: $(SRC_DIR)/inittools_ccnuma.c include/inittools.h
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
$(OBJ_DIR)/jacobi_naive.o: $(SRC_DIR)/jacobi_naive.c include/jacobi_naive.h
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
$(OBJ_DIR)/main_naive.o: $(SRC_DIR)/main_naive.c include/jacobi_naive.h include/gaussseidel_naive.h include/inittools_naive.h
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
$(OBJ_DIR)/jacobi_openmp1.o: $(SRC_DIR)/jacobi_openmp1.c include/jacobi.h
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
$(OBJ_DIR)/main_openmp1.o: $(SRC_DIR)/main_openmp1.c include/jacobi.h include/gaussseidel.h include/inittools.h
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
$(OBJ_DIR)/jacobi_openmp2.o: $(SRC_DIR)/jacobi_openmp2.c include/jacobi.h
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@
$(OBJ_DIR)/main_openmp2.o: $(SRC_DIR)/main_openmp2.c include/jacobi.h include/gaussseidel.h include/inittools.h
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

#$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
#	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

clean:
	@/bin/rm -f core core.* $(OBJ_DIR)/$(OBJ) $(OBJ_DIR)/*.o
