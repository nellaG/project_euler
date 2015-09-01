#include <stdio.h>

int main()

{


	long long a = 600851475143;

	long long i = 2;

	long long largest = 0;

	while( a > 1)
	{
		if (a % i ==0)
		{
			if(i > largest)
			{
			largest = i;
			a = a / i;
			}
		}
		else i = i + 1;
	}

	printf("answer :   %lld", largest);

	return 0;

}

