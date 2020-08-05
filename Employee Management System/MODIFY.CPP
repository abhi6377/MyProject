
#include<fstream.h>
#include<stdio.h>
#include<string.h>
#include<conio.h>
void modify_b_file()
{
company m;
fstream file("project.dat",ios::in|ios::out|ios::binary);
int code;
long pos;
char found='f';
cout<<"enter the employee code whose record is to be modified\n";
cin>>code;
while(!file.eof())
{
pos=file.tellg();
file.read((char*)&m,sizeof(m));
if(m.empret()==code)
{
m.modify();
file.seekg(pos);
file.write((char*)&m,sizeof(m));
found='t';
break;
}
}
if(found=='f')
cout<<"record not found!!\n";

cout<<"Record modified!!";
file.close();
}

