#include<stdio.h>
#include<math.h>

int isPrime(int n) {
    int i;
    if (n==1) return 0;
    for(i=2;i<=sqrt(n);i++)
        if (n%i==0)
            return 0;
    return 1;
}

int countPrimes(int n) {
    int count=0;
    int nums[n-2], i, j;
    for (i=0;i<n-2;i++)
        nums[i] = 1;
    for (i=0;i<n-2;i++)
        if (nums[i]==1 && isPrime(i+2)) 
            for (j=2;(i+2)*j<=n;j++) 
                nums[(i+2)*j-2] = 0;
    for (i=0;i<n-2;i++) 
        count += nums[i];
    return count;
}

int main(void)
{
    int testcases[] = {10, 2, 0, 3, 30};
    int i;
    for (i=0; i<5; i++)
        printf("%d\n", countPrimes(testcases[i]));
    return 0;
}

