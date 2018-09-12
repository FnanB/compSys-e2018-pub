#include <stdio.h>
#include <stdlib.h>

void printarr(int *arr, int n) {
  for (int i = 0; i < n; i++) {
    printf("%d ", *(arr+i));
  }
  printf("\n");
}

void printfarr(float *arr, int n) {
  for (int i = 0; i < n; i++) {
    printf("%f ", *(arr+i));
  }
  printf("\n");
}

void print_one_int(void *x) {
  printf("%d", *(int*)x);
}

void print_one_float(void *x) {
  printf("%f", *(float*)x);
}

void printanyarr(void (*p)(void*),
                 unsigned char *arr, int n, int elem_size) {
  for (int i = 0; i < n; i++) {
    (*p)(arr+i*elem_size);
    printf(" ");
  }
  printf("\n");
}

int cmp_ints(const void *px, const void *py) {
  int x = *(int*)px;
  int y = *(int*)py;

  if (x == y) {
    return 0;
  } else if (x < y) {
    return -1;
  } else {
    return 1;
  }
}

int main() {
  int arr[10] = { 42, 13371337, 1, 2, 3, 1337 };

  printf("Address of arr: \t%p\n", (void*)arr);
  printf("Address of arr[0]: \t%p\n", (void*)&arr[0]);
  printf("Address of arr[1]: \t%p\n", (void*)&arr[1]);

  printarr(arr, 10);

  float farr[10] = { 1, 2, 3 };

  printfarr(farr, 10);

  printanyarr(&print_one_int,
              (unsigned char*)arr, 10, sizeof(int));

  printanyarr(&print_one_float,
              (unsigned char*)farr, 10, sizeof(float));

  qsort(arr, 10, sizeof(int), &cmp_ints);

  printanyarr(&print_one_int,
              (unsigned char*)arr, 10, sizeof(int));

  return 0;
}
