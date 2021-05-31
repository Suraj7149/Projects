#include<stdio.h>
#include<string.h>

void main()
{
  char sub[50];

  printf("Enter the subjects:- \nPhysics\nChemistry\nor Both\n");
  scanf("%s", &sub);

  if (strcmp(sub, "Both")==0){
      printf("Congrats you have won 45$.\n");
  }
  else if (strcmp(sub, "Chemistry")==0){
      printf("Congrats you have won 15$.\n");
  }
  else if (strcmp(sub, "Physics")==0){
      printf("Congrats you have won 15$.\n");
  }
  else{
      printf("Wrong Input!!!\n");
  }
    
}