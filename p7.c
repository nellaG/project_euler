#include <stdio.h>
#include <math.h>
#define INT_MAX = 2100000000

int main()
{
	
	unsigned int list [10010] ;
	int x = 3;
	int i;
	int j = 1;
	list[0] = 2;

	while( x < 2100000000 )
	{
		for(i=2; i< x; i++)
		{
			if (x%i == 0) break;
			else if (i == x-1)
			{
				if (x%(i+1) == 0)
				{
					list[j] = x;
					j++;
				}
			}
		}
		x = x + 1;

		if ( j == 10001) break;
	}

	printf(" 10001th prime number : %d\n " , list[10000]); 

	return 0;


}

