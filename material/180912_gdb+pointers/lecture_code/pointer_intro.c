#include <stdio.h>

void swap(int *px, int *py) {
  printf("Value of px is:\t%p\n", (void*) px);
  printf("Value of py is:\t%p\n", (void*) py);
  int tmp = *px;
  *px = *py;
  *py = tmp;
}

void recurse(int n) {
  if (n == 0) {
    return;
  } else {
    printf("Address of n: %p\n", (void*)&n);
    recurse(n-1);
  }
}

int main() {
  int x = 1, y = 2;
  printf("Value of x is:  \t%d\n", x);
  printf("Address of x is:\t%p\n", (void*) &x);
  printf("Value of y is:  \t%d\n", y);
  printf("Address of y is:\t%p\n", (void*) &y);

  swap(&x, &y);

  printf("Value of x is:  \t%d\n", x);
  printf("Address of x is:\t%p\n", (void*) &x);
  printf("Value of y is:  \t%d\n", y);
  printf("Address of y is:\t%p\n", (void*) &y);

  recurse(10);

  int *p = &x;

  printf("Value of p is:  \t%p\n", (void*)p);
  printf("Address of p is:\t%p\n", (void*)&p);

  double fy = 10; // astronomers pi
  double *py = (double*) &fy;

  printf("Value of y: %f\n", fy);
  printf("Value of *py: %f\n", *py);
  printf("Value of py: %p\n", (void*)py);

  *py = 4;

  printf("Value of y: %f\n", fy);
  printf("Value of *py: %f\n", *py);
  printf("Value of py: %p\n", (void*)py);

  return 0;
}
