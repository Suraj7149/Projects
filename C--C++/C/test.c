# include<stdio.h>
# include<string.h>
# include<conio.h>
# include<stdlib.h>


void main(){
    system("cls");
    int i,j,k;

    for (i=1; i<=5; i++){
        for (j=i; j<=5; j++){
            printf(" ");
        }
        for(k=1;k<=i; k++){
            printf("*");
        }
        printf("\n");
    }
    
    printf("\n");
    i = 0, j = 0, k = 0;
    int n = 30;

    for(i=1; i<=n; i++){
        for (j=1; j<=(40 - i); j++){
            printf(" ");
        }
        for (k=1; k<=(2*i -1); k++){
            printf("*");
        }
        printf("\n");
    }
    

}