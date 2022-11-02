#include <stdio.h>

#define MAX_SIZE 101
int A[MAX_SIZE];
int top = -1;

void Push(int x){
    if(top == MAX_SIZE - 1){
        printf("Error: stack overflow\n");
        return;
    }
    top++;      //A[top++] = x;
    A[top] = x;
}

int Pop(){
    if(top == -1){
        printf("Error: no element to pop\n");
        return;
    }
    int z = A[top];
    top--;

    return z;
}

int Top(){
    return A[top];
}

int Perform(int op2, int op1, char op){
    int result;
    if(op == '+'){
        result = op2 + op1;
    }
    else if(op == '-'){
        result = op2 - op1;
    }
    else if(op == '*'){
        result = op2 * op1;
    }
    else{
        result = op1 / op2;
    }

    // printf("res = %d\n", op);

    return result;
}

int Prefix(char s[], char o[], int len){
    int count = 0;

    for(int i = len - 1; i >= 0; i--){
        for(int j = 0; j < 4; j++){
            if(s[i] == o[j]){
                int op2 = Pop();
                int op1 = Pop();
                printf("op2 = %d\n", op2);
                printf("op1 = %d\n", op1);
                int result = Perform(op2, op1, o[j]);
                printf("res = %d\n", result);
                Push(result);
                count++;
            }
        }
        if(count == 0){
            int y = (int)(s[i] - '0');
                printf("%d\n", y);
                Push(y);
        }
        count = 0;
    }

    printf("%d", A[top]);

    return A[top];
}

int main(){
    char s[10] = "-+*23*549";
    char o[4] = {'+', '-', '*', '/'};
    int len = strlen(s);

    int final = Prefix(s, o, len);
    
    return final;
}