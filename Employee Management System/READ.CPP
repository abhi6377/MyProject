
#include<fstream.h>
#include<stdio.h>
#include<string.h>
#include<conio.h>
void read_b_file()
{
ifstream fin("project.dat",ios::in|ios::binary);
if(!fin)
{
cout<<"file error";
return;
}
company c;
while(!fin.eof())
{
fin.read((char*)&c,sizeof(c));
c.show();
}
fin.close();
}