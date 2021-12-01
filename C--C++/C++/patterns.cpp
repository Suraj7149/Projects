# include<iostream>
using namespace std;

int main(){
    int row, col;

    cin>>row>>col;

    for (int i=1; i<=row; i++){
        for (int j=1; j<=col; j++){
            cout<<"*";
        }
        cout<<endl;
    }
    cout<<"\n";

    for (int i=1; i<=row; i++){
        for (int j=1; j<=col; j++){
            if(i==1 || i==row || j==1 || j==col){
                cout<<"*";
            }
            else{
                cout<<" ";
            }
        }
        cout<<endl;
    }
    cout<<"\n";

    for (int i=row; i>=1; i--){
        for (int j=1; j<=i; j++){
            cout<<"*";
        }
        cout<<endl;
    }
    cout<<"\n";

    for (int i=1; i<=row; i++){
        for (int j=1; j<=row; j++){
            if(j<=row-i){
                cout<<" ";
            }else{
                 cout<<"*";
            }
           
        }
        cout<<endl;
    }
    cout<<"\n";
    return 0;   
}