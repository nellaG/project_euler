#include <stdio.h>

int main()
{

	unsigned long long  i = 2;
	long long chainCount = 1;
	long long chainMax = 1;
	unsigned long long x;

while( i < 1000000)
{
	x = i;
	while( x > 1)
	{
		//when even
		if ( x%2 == 0)
		{
			x = x/2;
			chainCount++;
		}
		else if (x%2 !=0) //when odd 
		{
			x = 3*x+1;
			chainCount++;
		}
		if (chainMax < chainCount)
		{
			chainMax = chainCount;
		}

	}
printf(" answer is : %llu chainCount is : %llu chainMax is : %llu\n", i, chainCount, chainMax);
if (chainMax == 525) break;
	i++;
	chainCount = 1;
	
}

//printf(" answer is : %d chainMax is : %llu\n", x, chainMax);



	return 0;
}
