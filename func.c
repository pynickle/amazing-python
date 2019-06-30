#include<stdio.h>
#include<string.h>

char combine(char a[256], char b[256]){
    strcat(a, b);
}

int main(){
    char res;
    char a[] = "Hello ";
    char b[] = "World!";
    combine(a, b);
    printf("%s", a);
}