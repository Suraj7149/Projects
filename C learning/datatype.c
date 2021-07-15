# include<stdio.h>
# include<string.h>
# include<math.h>


void double_solve(double a, double b, double c){
    double d = b*b - 4.0*a*c;
    double sd = sqrt(d);
    double r1 = (-b + sd) / (2.0*a);
    double r2 = (-b - sd) / (2.0*a);
    printf("%.5f\t%.5f\n", r1, r2);
}
  
// utility function which calculate roots of 
// quadratic equation using float values
void float_solve(float a, float b, float c){
    float d = b*b - 4.0f*a*c;
    float sd = sqrtf(d);
    float r1 = (-b + sd) / (2.0f*a);
    float r2 = (-b - sd) / (2.0f*a);
    printf("%.5f\t%.5f\n", r1, r2);
}   


int result(){
    float fa = 1.0f;
    float fb = -4.0000000f;
    float fc = 3.9999999f;
    double da = 1.0;
    double db = -4.0000000;
    double dc = 3.9999999;
  
    printf("roots of equation x2 - 4.0000000 x + 3.9999999 = 0 are : \n");
    printf("\nfor float values: \n");
    float_solve(fa, fb, fc);
  
    printf("\nfor double values: \n");
    double_solve(da, db, dc);
    return 0;
}


void main(){
    // basic data types:- int, char, float, double
    // C support both signed and unsigned literals.

    // int: As the name suggests, an int variable is used to store an integer.
    int integer = 1;


    // char: The most basic data type in C. It stores a single 
    //character and requires a single byte of memory in almost all compilers.
    char character[] = "G";
    

    // float: It is used to store decimal numbers with single precision.
    float Float = 2.0f;


    // double: it is used to store decimal numbers with double precision.
    double Double= 2.22;

     // the difference btw float and double is that double has 2x more precision then float.
    result();
    
   
    // Derived data types:- array, pointer, structure, union
    // Enumeratrion Data type:- enum
    // Void data Types:- void
    printf("\nProgram for Data Types in C.\n\n");

    // 

}