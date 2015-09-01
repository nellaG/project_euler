#include <stdio.h>
#include <stdbool.h>

int main()
{
	unsigned long long primesum = 2;
	int x = 3;

	bool isPrime ( x, num)
	{
		for ( num; num > 1; num--)
		{
			if ( x % num ==0) 
				return false;
			else if ( x % num !=0 && num == 2)
				return true;
		}
		return false;
	}

	for ( x ; x < 2000000 ; x++)
	{
		if  ( isPrime(x, x-1)) 
			primesum +=x;
		printf("x : %d, Primesum : %lld\n", x, primesum);
	}


	return 0;
}
