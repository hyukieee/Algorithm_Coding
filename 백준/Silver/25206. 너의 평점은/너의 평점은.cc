#include <iostream>
using namespace std;

class Grade{
    double credit;
    string grade;
    string name;

public:
    Grade(string name = "", double credit = 0.0, string grade = "") 
        : name(name), credit(credit), grade(grade) {}

    double retCredit() { return credit; }
    string getGrade() {return grade;}

    double retGradeToNum() {
        double res = 0.0;
        if(grade == "P" || grade == "F") return res;
        if(grade[0] == 'A'){ res = 4.0; }
        else if(grade[0] == 'B'){ res = 3.0; }        
        else if(grade[0] == 'C'){ res = 2.0; }
        else if(grade[0] == 'D'){ res = 1.0; }
        if(grade[1] == '+') res += 0.5;

        return res;
    }
};

int main()
{
    Grade arr[20];
    double credit;
    string name;
    string grade;

    double sum =0;
    int num = 0 ;

    for(int i=0;i <20;i ++){
        cin >> name >> credit >> grade;
        arr[i] = Grade(name,credit,grade);


        if(arr[i].getGrade() != "P") {
            sum  = sum + arr[i].retCredit() * arr[i].retGradeToNum();
            num += arr[i].retCredit();
        }
    }

    cout << sum/num;
}
