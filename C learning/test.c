#include<stdio.h>
int age=20;

int main(){
	int matrix1[10][10], matrix2[10][10],matrix3[10][10], i, j;

	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			matrix1[i][j] = i+j;
		}
	}

	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			matrix2[i][j] = i+j;
		}
	}

	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			matrix3[i][j] = matrix1[i][j] + matrix2[i][j];
		}
	}

	for(i=0;i<3;i++)
  	{ printf("\n");
      for(j=0;j<3;j++)
           printf("%d\t",matrix3[i][j]);
  	}
 	printf("\n\n");
	printf("%d",age);
	return 0;
}