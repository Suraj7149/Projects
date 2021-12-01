#include<graphics.h>
#include<conio.h>

int main(){
    int gd = DETECT , gm;
    int i, x=100, y=50;
    char q[] = "C:\\TC\\BGI";

    initgraph(&gd, &gm, q);

    arc(200,200,0,130,50);

    // for (i=1; i<16; i++){
    //     setcolor(i);
    //     outtextxy(x, y, "Hello World");
    //     y = y + 30;
    // }

    getch();
    closegraph();
    return 0;
}

