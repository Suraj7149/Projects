#include<stdio.h>

int main(){

    int i, prime, num = 0;

    printf("Enter a Number:- ");
    scanf("%d",&prime);

    for (i=2; i<prime; i++){
        if (prime%i == 0){
            num++;
            break;
        }
    }

    if (num==0){
        printf("%d is a prime number.", prime);
    }
    else{
        printf("%d is not a prime number.", prime);
    }

}