#include<stdio.h>
#include<string.h>

int main(){

    int a = 0;
    char input[50];

    while(a == 0){
        printf(">>>");
        scanf("%s", &input);

        if (strcmp(input, "exit") == 0){
            a++;
            break;
            
        }else if(strcmp(input, "say") == 0){
            printf("Hello World!! \n");
            continue;
        }
        else{
            printf("%s\n",input);
            continue;
        }  
    }
    return 0;
}