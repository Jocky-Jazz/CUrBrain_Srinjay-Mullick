#include<stdio.h>

int reverse_and_double(int n) {
    int rev=0, copy = n;
    int sign= n>=0?1:-1;
    copy *= sign;
    while(copy>0) {
        rev = (rev*10)+(copy%10);
        copy /= 10;
    }
    if (n==rev)
        return n;
    return n+rev*sign;
}

int main(void)
{
    int testcases[] = {121, 123, 0, -45, 120};
    int i;
    for (i=0; i<5; i++)
        printf("%d\n", reverse_and_double(testcases[i]));
    return 0;
}

