#include<stdio.h>
#include<string.h>

void literals(){
    printf("\nhttps://www.geeksforgeeks.org/literals-in-python/ \n\n");

} 

void identifiers(){
    printf("\nA Python identifier can be a combination of lowercase/ uppercase\n"
    "letters, digits, or an underscore. The following characters are valid:\n"

    "Lowercase letters (a to z)\n"
    "Uppercase letters (A to Z)\n"
    "Digits (0 to 9)\n"
    "Underscore (_)\n"

    "Some valid names are:\n"
        "myVar\n"
        "var_3\n"
        "this_works_to\n"

    "b. An identifier cannot begin with a digit.\n"
    
   "Some valid names:\n"
        "_9lives\n"
        "lives9\n"
        
    "An invalid name:\n"
        "9lives\n\n");

}

void keywords(){
    printf("\nKeywords in python are:- \n"
        "False\n"
        "None\n"
        "True\n"
        "__peg_parser__\n"
        "and\n"
        "as\n"
        "assert\n"
        "async\n"
        "await\n"
        "break\n"
        "class\n"
        "continue\n"
        "def\n"
        "del\n"
        "elif\n"
        "else\n"
        "except\n"
        "finally\n"
        "for\n"
        "from\n"
        "global\n"
        "if\n"
        "import\n"
        "in\n"
        "is\n"
        "lambda\n"
        "nonlocal\n"
        "not\n"
        "or\n"
        "pass\n"
        "raise\n"
        "return\n"
        "try\n"
        "while\n"
        "with\n"
        "yield\n\n");

}

int main(){

   int a = 0;
    char input[50];

    while(a == 0){
        printf(">>>");
        scanf("%s", &input);

        if (strcmp(input, "exit") == 0){
            a++;
            break;
            
        }else if(strcmp(input, "help") == 0){
            printf("Commands:-\n\t- help\n\t- indentifiers\n\t- literals\n\t- keywords\n\t- about\n\t- exit\n");

        }else if(strcmp(input, "about") == 0){
            printf("made by Godfather.\ncmd based program\n");

        }
        else if(strcmp(input, "literals") == 0){
            literals();

        }else if(strcmp(input, "identifiers") == 0){
            identifiers();

        }else if(strcmp(input, "keywords") == 0){
            keywords();

        }
        else{
            continue;
        }
    } 

}
