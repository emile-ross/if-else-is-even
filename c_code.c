#include <stdio.h>
#include <stdlib.h>



void print_is_even(int n)
{
    // 1 for true, 0 for false
    printf("    int i = %d;\n", n);
    printf("    int is_even = 0;\n");
    int even = 1;
    for (int i = 0; i < n + 1; i++) {
        printf("    if (i == %d){is_even = %d;}\n", i, even);
        even = !even;
    }
}


int main(int argc, char *argv[])
{
    if (argc != 2) {
        printf("Expected 1 argument, got %d instead\n", argc);
        printf("Example command: '.\\is_even 10'\n");
        return -1;
    }

    int num = atoi(argv[1]);
    
    printf("int main()\n{\n");
    print_is_even(num);
    printf("    printf(\"%%s\", is_even? \"true\" : \"false\");\n");
    printf("}\n");
    return 0;
}
