#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    char buf[8];
    if (argc < 2) {
        puts("Usage: ./check <password>");
        return 1;
    }
    strncpy(buf, argv[1], 7);
    buf[7] = 0;
    if (strcmp(buf, "secret!")) {
        puts("Wrong!");
    } else {
        puts("Correct!");
    }
    return 0;
}