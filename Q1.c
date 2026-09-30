#include<stdio.h>
#include<stdbool.h>

bool hasEvenDig(int n) {
    int c=1;
    if (n==0)
        return false;
    else {
        while((n/=10)&&(c+=1));
        return !(c%2);
    }
}

int main(void)
{
    int testcases[] = {1234, 12345, 0, -100000, -7};
    int i;
    for (i=0; i<5; i++)
        printf("%s\n", hasEvenDig(testcases[i])?"True":"False");
    return 0;
}

