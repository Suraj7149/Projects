#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(){
    
    int num_of_guess = 1, guess, number;
    srand(time(0));
    number = rand()%100 + 1;

    while (number)
    {
        printf("Enter the number:- ");
        scanf("%d",&guess);

        if (guess == number){
            printf("You guessed the correct Number.\n");
            printf("The number of guess are %d\n", num_of_guess);
            break;
        }
        else if(guess > number){
            printf("Your number is higher.\n");
            printf("The number of guess are %d\n", num_of_guess);
            num_of_guess++;
            continue;
        }else if(guess < number){
            printf("Your number is lower.\n");
            printf("The number of guess are %d\n", num_of_guess);
            num_of_guess++;
            continue;
        }else{
            printf("wrong input!!\n");
            printf("The number of guess are %d\n", num_of_guess);
        }
    }
    
    
    return 0;
}