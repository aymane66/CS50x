#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    printf("--- Words to binary converter --- \n");
    string input = get_string("Insert input you want to convert: ");

    int i, j;
    for (i = 0; i < strlen(input); i ++)
    {
        unsigned char byte = input[i];
        int binary[BITS_IN_BYTE];
        int quo = byte;
        int rem;

        for (j = 0; j < BITS_IN_BYTE; j ++)
        {
            rem = quo % 2;
            binary[j] = rem;
            quo /= 2;
        }

        for (j = BITS_IN_BYTE - 1; j >= 0; j --)
        {
            print_bulb(binary[j]);

        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
