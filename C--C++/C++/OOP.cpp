#include<iostream>
using namespace std;

class AbstractEmployee{
    virtual void askforpromotion() = 0;
};

class Employee: AbstractEmployee {

    /*private:
        string Name;
        string Company;
        int Age;*/
    protected:
        string Name;
        string Company;
        int Age;

    public:
        void setName(string name){
            Name = name;
        }
        string getName(){
            return Name;
        }

        void getCompany(string company){
            Company = company;
        }
        string getCompany(){
            return Company;
        }

        void getAge(int age){
            Age = age;
        }
        int getAge(){
            return Age;
        }
        void IntroduceYourself(){
            cout<<"Name - "<<Name<<"\n";
            cout<<"Company - "<<Company<<"\n";
            cout<<"Age - "<<Age<<"\n\n";
        }
        
        Employee(string name, string company, int age){
            Name = name;
            Company = company;
            Age = age;
        }

        void askforpromotion(){
            if (Age > 29){
                cout<<Name<<"is eligible for promotion.";
            }
            else{
                cout<<Name<<"is Not eligible for promotion.";
            }
        }
        
};

class Developer:public Employee {
    public:

        string FavProgrammingLanguage;
        Developer(string name, string company, int age, string programminglanguage)
                :Employee(name,company, age){
                FavProgrammingLanguage = programminglanguage;

        }

        void ligma(){
            cout<<getName()<<"'s favorite language is "<<FavProgrammingLanguage<<endl;
        }
    
};

class Teacher:public Employee{
    public:
        string Subject;
        void Preparetest(){
            cout<<Name<<" Lets make them regret they were ever born in "<<Subject<<endl;
        }

        void TeachLesson(){
            cout<<Name<<" welp.............teaches..."<<Subject<<endl;
        }

    Teacher(string name, string school, int age, string subject)
        :Employee(name, school, age){
            Subject = subject;
        }
};

int main(){
    /*Employee employee1 = Employee("Member1", "Company1", 25);
    employee1.IntroduceYourself();

    Employee employee2 = Employee("Member2", "Company2", 35);
    employee2.IntroduceYourself();

    employee1.askforpromotion();
    employee2.askforpromotion();*/

    Developer Dev = Developer("Excalibro", "Baro's Labours", 22 , "pascal");
    /*Dev.ligma();
    Dev.askforpromotion();*/

    Teacher redpill = Teacher("Neo", "Matrix", 35, "Virtual Reality");
    redpill.TeachLesson();
    redpill.Preparetest();
    
    return 0; 

}
