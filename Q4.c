#include<stdio.h>

int reverse_and_double(int n) {
    int prod=1, tot=0;
    if (n==0) {
        printf("Invalid input: n=0, because n must be greater than 0.");
        return 0;
    }
    while (n>0)
    {
        prod *= n%10;
        tot += n%10;
        n/=10;
    }
    return prod-tot;
}

int main(void)
{
    int testcases[] = {234, 123, 5, 100, 999};
    int i;
    for (i=0; i<5; i++)
        printf("%d\n", reverse_and_double(testcases[i]));
    return 0;
}

