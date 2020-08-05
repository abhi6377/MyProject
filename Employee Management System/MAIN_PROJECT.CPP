#include"class.cpp"
#include"read.cpp"
#include"write.cpp"
#include"modify.cpp"
#include"search.cpp"
#include"delete.cpp"
#include<fstream.h>
#include<stdio.h>
#include<conio.h>
#include<process.h>

void main()
{   char run='y';
    int n;
    do{
    clrscr();
    cout<<"\t \t \t"<<"EMPLOYEE MANAGEMNT SYSTEM"<<endl<<endl;
    cout<<"1) Show the records of employees."<<endl<<"2) Enter a new record"<<endl<<"3) Search records of an employee."<<endl<<"4) Modify records of an employee."<<endl<<"5) Delete records of an employee.";
    cout<<endl<<"Please enter your choice number :";
    cin>>n;
    switch(n){
    case 1:
    cout<<"Employee code"<<"\t"<<"  Employee name"<<"\t"<<"    Date of joining"<<"\t"<<"   Salary"<<endl;
    read_b_file();
    break;
    case 2:
    write_b_file();
    break;
    case 3:
    search_b_file();
    break;
    case 4:
    cout<<"Employee code"<<"\t"<<"  Employee name"<<"\t"<<"    Date of joining"<<"\t"<<"   Salary"<<endl;
    modify_b_file();
    break;
    case 5:
    delete_b_file();
    break;
    default:
    cout<<"You have entered an invalid choice"<<endl<<endl;
    }
    cout<<"Do you want to continue? (Press 'y' or 'Y' for YES)  ";
    cin>>run;
    }while(run=='y' || run=='Y');

    getch();
}







