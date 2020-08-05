#include<stdio.h>
#include<conio.h>
#include<process.h>
#include<string.h>
#include<fstream.h>
class company
{
int empcode;
char empname[40];
long salary;
long doj;
public:
void accept();
void show();
int empret();
void modify();
};
void company::accept()
{
cout<<"Enter the employee code:  ";
cin>>empcode;
cout<<endl;
cout<<"Enter the employee name:  ";
gets(empname);
cout<<endl;
cout<<"Enter the date of joining of employee(without slashes(ddmmyyy)) ";
cin>>doj;
cout<<endl;
cout<<"enter the salary of the employee";
cin>>salary;
}

void company::show()
{
cout<<"    "<<empcode<<"\t"<<"            "<<empname<<"\t \t"<<doj<<"\t  "<<salary<<endl;
}

int company::empret()
{
return empcode;
}

void company::modify()
{
  cout<<"Employee code"<<"\t"<<"  Employee name"<<"\t"<<"    Date of joining"<<"\t"<<"   Salary"<<endl;
cout<<"    "<<empcode<<"\t"<<"            "<<empname<<"\t \t"<<doj<<"\t  "<<salary<<endl;



cout<<"Enter new details of employee"<<endl;
long sal;
char name[20];
cout<<"New name : (enter '.' to retain old one)";
cin>>name;
cout<<"New salary : (enter '0' to retain old one)";
cin>>sal;
if(strcmpi(name,".")!=1)
strcpy(empname,name);
if(sal!=0)
salary=sal;
}