#include<stdio.h>

int main(){
    char oper;
    double a, b;

    printf("\nEnter the operator (+, /, *, -): ");
    scanf("%c",&oper);

    printf("\nEnter the two numbers:- ");
    scanf("%lf %lf",&a,&b);

    switch (oper)
    {
    case '+':
        printf("\nresult: %.2lf\n",(a+b));
        break;
    
    case '-':
        printf("\nresult: %.2lf\n",(a-b));
        break;

    case '*':
        printf("\nresult: %.2lf\n",(a*b));
        break;

    case '/':
        if (b != 0.0){
            printf("\nresult: %.2lf\n",(a/b));
        }else{
            printf("\n%.2lf / %.2lf unidentified\n",a,b);
        }
        break; 
    default:
        printf("\nWrong Operator.");
        break;
    }
    return 0;
}