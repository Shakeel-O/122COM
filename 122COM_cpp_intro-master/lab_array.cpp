#include <vector>
#include <iostream>
#include <sstream>
#include <string>
#include <stdexcept>
using namespace std;

/* Getting input from the user in C++ is simply a matter
	of saying:
		int input;
		cin >> input;
	However, getting C++ to handle invalid input is 
	surprisingly complex. So here is a input() function
	that I have written that does it all for you.
	It behaves in a similar way to input() in Python
	and will raise a runtime_error exception if the user
	trys to enter anything that can't be converted to the
	correct type. You don't need to know how this work at
	the moment, just type...
		
		input<int>();

	... to read in ints or ...
		
		input<float>();

	..if you watch to read floats etc. . */
template<typename T>
T input()
{
	string buffer;
	getline(cin, buffer);

	stringstream ss(buffer);
	T input;

	if( ss >> input && ss.eof() )
		return input;

	throw runtime_error("Input is of invalid type");
}

int main()
{
	vector<int> userinputs;

	// COMPLETE ME

	int ui = input<int>();

	// COMPLETE ME

	return 0;
}