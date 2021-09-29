#include<stdio.h>
#include<string.h>

int main(int argc, const char * argv[]) {
  int n;
  scanf("%d", &n);

  int count = 0;

  char s[n][21];
  for (int i = 0; i < n; i++) {
    scanf("%s", s[i]);
    
    if(strlen(s[i]) > 10) {
      count++;
      for(int j=0; j<i; j++){
        if(strcmp(s[i], s[j]) == 0) {
          count--;
          break;
        }
      }
    }
  }

  printf("%d\n", count);

  return 0;
}
