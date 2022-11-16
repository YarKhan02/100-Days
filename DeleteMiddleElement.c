#include <stdio.h>
#include <stdlib.h>

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

void Pop(){
    if(top == -1){
        printf("Error: no element to pop\n");
        return;
    }
    top--;
}

int Top(){
    return A[top];
}

void Print(){
    printf("Stack: ");

    for(int i = 0; i <= top; i++){
            printf("%d ", A[i]);
    }
    printf("\n");
}

void solve(int s[], int k){
    if(k == 0){
        Pop();
        return;
    }
    int temp = Top();
    Pop();
    solve(s, k - 1);
    Push(temp);
    return;
}

int main(){
    int s[6] = {1, 2, 3, 4 ,5, 6};

    for (int i = 0; i < 6; i++){
        Push(s[i]);
    }

    int k = ((sizeof(s) / sizeof(int))/2) - 1;

    solve(s, k);

    Print();
}