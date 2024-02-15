#include <stdio.h>

int main(void) {
    printf("Hello, World!\n");


    char answer[100];
    printf("What's your name?\n");
    fgets(answer, sizeof(answer), stdin);
    printf("Hello, %s\n", answer);
    

}
