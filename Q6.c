#include<stdio.h>

int count_diff(int testcase[3]) {
    int n=testcase[0], a=testcase[1], b=testcase[2];
    int c_a=0, c_b=0;
    if (n<0) {
        printf("Invalid input: n cannot be negative.");
        return 0;
    }
    if (a>9||a<0) {
        printf("Invalid input: a must be a single digit.");
        return 0;
    }
    if (b>9||b<0) {
        printf("Invalid input: b must be a single digit.");
        return 0;
    }
    do {
        if (n%10==a) c_a += 1;
        if (n%10==b) c_b += 1;
        n /= 10;
    } while(n>0);
    return c_a>=c_b?c_a-c_b:c_b-c_a;
}

int main(void)
{
    int testcases[][3] = {{112231, 1, 2} , {55555, 5, 2} , {123456, 3, 6} , {0, 0, 5} , {1002001, 0, 1}};
    int i;
    for (i=0; i<5; i++)
        printf("%d\n", count_diff(testcases[i]));
    return 0;
}

