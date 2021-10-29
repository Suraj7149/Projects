# include<stdio.h>
# include<string.h>

int main(){
    char input[50];
    int n = 0,i,c = 0;
    
    printf("Enter the String: ");
    scanf("%s",input);

    n = strlen(input);

    for (i = 0; i<n/2; i++){
        if (input[i] == input[n-i-1]){
            c++;
        }

    }
    if (c == i){
        printf("The String %s is palindrome.",input);
    }else{
        printf("The String %s is not palindrome.",input);
    }
    
    return 0;
}
