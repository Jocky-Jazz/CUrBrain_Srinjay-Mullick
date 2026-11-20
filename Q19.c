#include <stdio.h>

int* rev(int* arr, int start, int end){
    if (start<0||end<0)
       return arr;
    int i=0, temp=0;
    for(i=0; i<(int)((end-start+1)/2); i++){
        temp = arr[i+start];
        arr[i+start]=arr[end-i];
        arr[end-i]=temp;
    }
    return arr;
}

int* rotate(int* arr, int size, int k){
    if (k > size) k = 1;
    arr = rev(arr, size-k, size-1);
    arr = rev(arr, 0, size-k-1);
    arr = rev(arr, 0, size-1);
    return arr;
}

void display(int* arr, int size){
    int i;
    for (i=0; i<size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}


int main(void){
    display(rotate((int[]){1,2,3,4,5,6,7}, 7, 3), 7);
    display(rotate((int[]){-1, -100, 3, 99}, 4, 2), 4);
    display(rotate((int[]){1, 2}, 2, 5), 2);
    display(rotate((int[]){1}, 1, 10), 1);
    display(rotate((int[]){1, 2, 3}, 3, 0), 3);
    return 0;
}