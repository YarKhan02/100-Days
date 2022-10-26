#include <stdio.h>

int main(){
    char n[10] = "Ish";
    char S = 'A', Z = 'Z', s = 'a', z = 'z';
    int A = S, B = Z, a = s, b = z;
    int MID = (A + B) / 2, mid = (a + b) / 2;
    int len = sizeof(n) / sizeof(char);

    for(int i = 0; i < len; i++){
        if((n[i] >= 65) && (n[i] <= MID) && (n[i] <= 90)){
            int in = n[i];
            int n1 = Z - (in - A);
            printf("%c", n1);
        }
        else if((n[i] >= 65) && (n[i] >= MID) && (n[i] <= 90)){
            int in = n[i];
            int n1 = A + (Z - in);
            printf("%c", n1);
        }

        if((n[i] >= 97) && (n[i] <= mid) && (n[i] <= 122)){
            int in = n[i];
            int n1 = z - (in - a);
            printf("%c", n1);
        }
        else if((n[i] >= 97) && (n[i] >= mid) && (n[i] <= 122)){
            int in = n[i];
            int n1 = a + (z - in);
            printf("%c", n1);
        }

        if(n[i] == 32){
            printf(" ");
        }
        
    }
    return 0;
}