# include<stdio.h>
# include<ctype.h>

int main(){
    char str[]= "geek";
    printf("Select an operation to perform: \n1. ADD\n2. SUBTRACT\n3. MULTIPLY\n4. DIVIDE.");

    printf("\nEnter:- ");
    scanf("%s",&str);
    str = towlower(str);
    printf(str);
    
}