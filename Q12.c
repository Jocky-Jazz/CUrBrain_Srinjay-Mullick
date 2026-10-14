#include<stdio.h>
#include<math.h>

int powerMod (int testcase[3])
{
    int res = 1%testcase[2];
    for ( ; testcase[1]>0; --testcase[1])
        res = (res*testcase[0])%testcase[2];
    return res;
}

int main(void)
{
    int testcases[][3] = {{2, 10, 1000}, {7, 0, 13}, {9, 1, 7}, {3, 4, 1}, {0, 5, 11}};
    int i;
    for (i=0; i<5; i++)
        printf("%d\n", powerMod(testcases[i]));
    return 0;
}

