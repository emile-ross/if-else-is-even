#include <stdio.h>
#include <stdlib.h>

#define RED     "\033[31m"
#define GREEN   "\033[32m"
#define PURPLE  "\033[35m"
#define RESET   "\033[0m"


#define PRINT_COLOUR(message, colour)             \
    do {                                          \
        printf("%s%s%s", colour, message, RESET); \
    } while(0)
    


void printIsEven(int n)
{
    // 1 for true, 0 for false
    printf("int i = %d\n", n);
    int even = 1;
    for (int i = 0; i < n + 1; i++) {
        printf("if (i == %d){return %d;}\n", i, even);
        if (!even) {
            even = 1;
        }
        else {
            even = 0;
        }
    }
}


int main(int argc, char *argv[])
{
    if (argc != 2) {
        PRINT_COLOUR("Expected 1 argument.\n", RED);
        PRINT_COLOUR("Example command: '.\\main 10'\n", PURPLE);
        return -1;
    }

    int num = atoi(argv[1]);

    printIsEven(num);
    PRINT_COLOUR("Sucessfully generated code!\n", GREEN);
    return 0;
}
