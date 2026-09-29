#include<stdio.h>

int reverse_and_double(int n) {
    int rev=0;
    int sign= n>=0?1:-1;
    n *= sign;
    while(n>0) {
        rev = (rev*10)+(n%10);
        n /= 10;
    }
    return sign*rev<<1;
}

int main(void)
{
    int testcases[] = {123, -45, 0, 1200, 9};
    int i;
    for (i=0; i<5; i++)
        printf("%d\n", reverse_and_double(testcases[i]));
    return 0;
}

