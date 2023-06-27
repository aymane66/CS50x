#include <stdio.h>

int main(void)
{
    int h, i, s, j;

    do
    {
        printf("Height: ");
        scanf("%d", &h);
    }
    while (h < 1 || h > 8);

    for (i = 1; i <= h; i++)
    {
        for (j = h - i; j > 0; j--)
        {
            printf(" ");
        }
        for (s = 1; s <= i; s++)
        {
            printf("#");
        }
        printf("\n");
    }

    return 0;
}