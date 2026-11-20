#include<stdio.h>

int* runSum(int* arr, int size){
    int sum=0;
    for(int i=size-1; i>=0;i--){
        sum += arr[i];
        arr[i] = sum-arr[i];
    }
    return arr;
}

void display(int* arr, int size){
    for (int i=0; i<size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main(void){
    display(runSum((int[]){10,4,8,3}, 4), 4);
    display(runSum((int[]){5},1),1);
    display(runSum((int[]){},0),0);
    display(runSum((int[]){-2,5,-1},3),3);
    display(runSum((int[]){1,2,3,4},4),4);
}