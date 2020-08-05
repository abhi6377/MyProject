//#include"class.cpp"
#include<fstream.h>
#include<stdio.h>
#include<conio.h>
#include<process.h>
void write_b_file()
{
ofstream fout("project.dat",ios::binary|ios::app);
if(!fout)
{
cout<<"file error";
return;
}
company c;
int n;
cout<<"Enter the number of records you want to enter";
cin>>n;
for(int i=1;i<=n;i++)
{
c.accept();
fout.write((char*)&c,sizeof(54));
}
fout.close();
}