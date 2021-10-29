# include<stdio.h>
# include<string.h>
#include<stdlib.h>

# define say(){ printf("Enter 1 to see the code of this program.\n"); \
                printf("Enter 2 to close the program:"); }

void main(void){
    int i;
    FILE *file_pointer;
    char ch[1000];

    say();
    scanf("%i", i);
    switch (i)
    {
    case 1:
        file_pointer = fopen("C:\\Users\\santo\\Desktop\\datesheet.txt" , "r");
        printf("%s", fgets(ch, 1000, file_pointer));
        fclose(file_pointer);
        break;
    
    case 2:
        break;
    default: printf("program ran.\n");
        break;
    }
    
}
