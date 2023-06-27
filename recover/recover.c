#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open input file
    FILE *input_file = fopen(argv[1], "r");
    if (input_file == NULL)
    {
        printf("Could not open file\n");
        return 2;
    }

    unsigned char buffer[512];

    FILE *output_file = NULL;

    // Allocate memory for filename
    char *filename = malloc(8 * sizeof(char));

    int count_image = 0;
    while (fread(buffer, sizeof(char), 512, input_file))
    {
        // Check for JPEG signature
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (count_image > 0)
            {
                fclose(output_file);
            }

            // Create new filename for the current image
            sprintf(filename, "%03i.jpg", count_image);

            // Open new output file
            output_file = fopen(filename, "wb");

            count_image++;
        }

        // Open buffer to the output file
        if (output_file != NULL)
        {
            fwrite(buffer, sizeof(char), 512, output_file);
        }
    }


    free(filename);
    fclose(output_file);
    fclose(input_file);

    return 0;
}
