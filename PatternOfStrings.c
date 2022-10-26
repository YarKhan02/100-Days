#include <stdio.h>

void pattern(char s[], int len){
    int n = 4;
    for(int i = 0; i < len; i++){
        for(int j = 0; j < n; j ++){
            printf("%c", s[j]);
        }
        n--;
        printf("\n");
    }
}

int main(){
    char c[4] = "Wali";
    int len = sizeof(c) / sizeof(char);

    pattern(c, len);
}