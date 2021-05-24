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
            
        }else{
            printf("%s\n",input);
            continue;
        }
        
    }

    return 0;

}