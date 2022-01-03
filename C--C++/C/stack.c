#include<stdio.h>
#include<limits.h>
#include<stdlib.h>

struct Stack{
	int top;
	unsigned capacity;
	int* array;};


struct Stack* createStack(unsigned capacity){
	struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
	stack -> capacity = capacity;
	stack ->top = -1;
	stack ->array = (int*)malloc(stack->capacity * sizeof(int));}


int isFull(struct Stack* stack){
	return stack->top == stack->capacity -1;}


int isEmpty(struct Stack* stack){
	return stack->top == -1;}


void push(struct Stack* stack, int item){
	if (isFull(stack))
		return;
	stack->array[++stack->top] = item;
	printf("%d pushed into the Stack \n",item);}


int pop(struct Stack* stack){
	if (isEmpty(stack))
		return INT_MIN;
	return stack->array[stack->top--];}


int peek(struct Stack* stack){
	if (isEmpty(stack))
		exit(0);
	return stack->array[stack->top];}


void show_items(struct Stack* stack){
	for(int i=0; i<sizeof(stack->array);i++){
		if (stack->array[i] != 0){
			printf("Element - %d, position - %d \n",stack->array[i],(i+1));
		}else{
			break;
		}}}


int main(){
	struct Stack* stack = createStack(100);
	push(stack, 10);
	push(stack, 20);
	push(stack, 30);
	printf("%d top item in the stack \n", peek(stack));
	printf("%d popped from Stack \n",pop(stack));
	show_items(stack);	

	return 0;
}
