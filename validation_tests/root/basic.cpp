#include <iostream>
#include <TROOT.h>

int main()
{
  std::cout << "BEGIN Test" << std::endl;
  std::cout << gROOT->GetVersion() << std::endl;
  std::cout << "END Test" << std::endl;
  return 42;
}
