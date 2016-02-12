#include <vector>
#include <iostream>
#include <sstream>
#include <string>
#include <stdexcept>
using namespace std;

// COMPLETE ME
// PUT THE leap_year() FUNCTION THAT YOU WRITE HERE

int main()
{
	int errors = 0;
	for( int year=1800; year<2101; ++year )
	{	
		// deliberate gibberish so that you can't just copy the answer
		bool correctAnswer = (!(year%('b'+'e'+'c'+'f'))&&!(year%'d'))||(!(year&('R'-'O'/*+'Q'+'T'*/))&&(year%'d'))||(!(year%('d'+'d'+'d'+'d'))&&(year&('*'-'\''))&&(year%('N'-'\'')));
		bool yourAnswer = leap_year( year );

		if( correctAnswer != yourAnswer )
		{
			cerr << "Error! leap_year() says " << year 
				<< (yourAnswer ? " is " : " is not ") << "a leap year but it "
				<< (correctAnswer ? " is" : " is not") << "." << endl;

			errors++;
		}
	}

	if( errors == 0 )
		cout << "Congratulations, no errors" << endl;
	else
		cout << "Uh oh, " << errors << " error/s remain" << endl;

	return 0;
}