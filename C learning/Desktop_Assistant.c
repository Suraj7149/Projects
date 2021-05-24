#include<stdio.h>
#include<string.h>

int main(){

    char str[50];

    printf("started.");
    scanf("%s", str);
    if (strcmp(str, "hi") == 0){
        printf("it worked");
    }
    else{
        printf("F");
    }

    return 0;

}