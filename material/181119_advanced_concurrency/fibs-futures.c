#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

static const int PAR_THRESHOLD = 30;

int fib (int n);

void* fib_thread(void *arg) {
  int *r = malloc(sizeof(int));
  int n = *(int*)arg;

  *r = fib(n);

  return r;
}

int fib (int n) {
  if (n < 2) {
    return 1;
  } else {
    if (n >= PAR_THRESHOLD) {
      pthread_t p1, p2;
      int *x, *y;
      int n1 = n-1, n2 = n-2;
      pthread_create(&p1, NULL, fib_thread, &n1);
      pthread_create(&p2, NULL, fib_thread, &n2);
      pthread_join(p1, (void**)&x);
      pthread_join(p2, (void**)&y);
      return *x + *y;
    } else {
      return fib(n-1) + fib(n-2);
    }
  }
}

int main() {
  char *line = NULL;
  ssize_t line_len;
  size_t buf_len = 0;

  while ((line_len = getline(&line, &buf_len, stdin)) != -1) {
    int n = atoi(line);
    printf("fib(%d) = %d\n", n, fib(n));
  }

  free(line);
}
