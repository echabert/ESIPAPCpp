#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <map>

int main()
{
	std::cout << "BEGIN Test" << std::endl;
	std::vector<double> eric;
	std::map<int,int> eric2;
	std::ifstream input("file.txt");
	std::stringstream str;
	str << "1 2";
	int a=0;
	int b=0;
	str >> a;
	str >> b;
	std::cout << "END Test" << std::endl;
	return 42;
}
