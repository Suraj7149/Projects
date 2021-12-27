#include <iostream>
#include <stack>
using namespace std;


void item_check(stack<int> stack){
    if (stack.empty())
        cout<<"Stack is empty."<<endl;

    else
        cout<<"Stack size is "<<stack.size()<<endl;

}


void print_elements(stack<int> stack){
    while (!stack.empty())
    {
        cout << stack.top() << endl;
        stack.pop();
    }
    
}
int main(){
    // stack implementation.
    stack<int> num_stack;

    num_stack.push(1);
    num_stack.push(2);
    num_stack.push(3);

    item_check(num_stack);

    // num_stack.pop();
    // num_stack.pop();
    // cout<<"After Popping 2 elements."<<endl;

    print_elements(num_stack);
    //system("pause>0");
}