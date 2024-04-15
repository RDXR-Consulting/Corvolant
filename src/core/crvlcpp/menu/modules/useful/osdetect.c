#include <iostream>

int main()
{
  lin = lindetect_try();
  win = windetect_try();
  mac = macdetect_try();

  switch(lin)
{
case 1:
  cout << "linux!";
case 0:
  cout << "не linux!";
}


  switch(win)
{
case 1:
  cout << "windows!";
case 0:
  cout << "не windows!";
}


  switch(mac)
{
case 1:
  cout << "mac!";
case 0:
  cout << "не mac!";
}

