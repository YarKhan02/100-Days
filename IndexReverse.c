#include <stdio.h>

int main(){
    char c[10] = "Wali";
    int len = strlen(c);

    int l = 0, h = len - 1, temp;

    while(l < h){
        temp = c[l];
        c[l] = c[h];
        c[h] = temp;
        l++;
        h--;
    } 
    
    printf("%s", c);
}