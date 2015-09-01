#include <stdio.h>
#include <math.h>
int main()
{
	
	int a, b, c;

	for ( a = 1; a < 1000 ; a++)
	{
		for ( b = a + 1; b < 1000; b++)
		{
			if ( 2 * a + b >=1000 ) break;
			if (a + 2 * b >= 1000) break;

			c = (1000 - a - b);

			if ( a*a + b*b == c*c)
			{
				printf("abc is : %d\n", a * b * c);
				printf("a : %d b : %d c : %d\n", a, b, c);
			}
		}
	}



	return 0;
}
