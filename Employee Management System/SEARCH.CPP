//#include"CLASS.CPP"
#include<fstream.h>
#include<stdio.h>
#include<string.h>
#include<conio.h>
void search_b_file()
{
company m;
fstream file("project.dat",ios::in|ios::out|ios::binary);
int code;
long pos;
cout<<"enter the employee code whose record is to be modified\n";
cin>>code;
char found='f';
while(!file.eof())
{
file.read((char*)&m,sizeof(m));
if(m.empret()==code)
{
cout<<"RECORD FOUND"<<endl;
m.show();
found='t';
}
}
if(found=='f')
cout<<"RECORD NOT FOUND!!";
file.close();
}
