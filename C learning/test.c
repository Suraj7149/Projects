#include<stdio.h>
void display(){
    printf("fuction running.\n");
}

int main(){
    
    printf("into main.\n");
    printf("calling fuction.\n");

    display();

    printf("fuction over.\n");
    printf("2. main end.\n");  
    return 0;
    printf("1. main end.\n");
}