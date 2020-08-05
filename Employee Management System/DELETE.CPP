#include<stdio.h>
#include<fstream.h>
#include<conio.h>
void delete_b_file()
{
company m;
ifstream file("project.dat",ios::in|ios::binary);
ofstream tempfile("temp.dat",ios::out|ios::binary);
int code;
long pos;
char found='f';
cout<<"Enter the employee code whose record is to be deleted:\n";
cin>>code;
while(!file.eof())
{
file.read((char*)&m,sizeof(m));
if(m.empret()==code)
{   found='t';
cout<<"The record to be deleted is \n";
cout<<"Employee code"<<"\t"<<"  Employee name"<<"\t"<<"    Date of joining"<<"\t"<<"   Salary"<<endl;
m.show();
}
else
tempfile.write((char*)&m,sizeof(m));
}

file.close();
tempfile.close();
remove("project.dat");
rename("temp.dat","project.dat");

if(found=='t')
cout<<"RECORD DELETED SUCCESSFULLY!"<<endl;
else
cout<<"RECORD NOT FOUND!"<<endl;
}