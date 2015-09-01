#include <stdio.h>
#include <math.h>



int main()
{


	unsigned long long a = 28;

	int countDivisors (int a)
	{
		int x = a-1;
		int divNum = 1;
		for  ( x ; x > 1 ; x--)
		{
			if (a % x == 0)
				divNum++;

		}
		return divNum;
	}
	
	


	for ( a; a < pow(2,64) -1; a++)
	{
			
			printf("Number of divisors : %d , tri_number is : %lld\n", countDivisors(a*(a+1)/2), a*(a+1)/2);
			if (countDivisors(a*(a+1)/2) > 500  ) break;			
		
	}


	return 0;
}
