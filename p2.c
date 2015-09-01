#include <stdio.h>
#include <math.h>



int fibonacci(int n)
{
	if(n<=1)
	{
		return n;
	}
	else
	return fibonacci(n-1) + fibonacci(n-2); 
}





int main()
{

	int i;

	int sum=0;
	for(i=0; i<10000; i++)
	{
	if(fibonacci(i) >=4000000) break;
	else if( fibonacci(i) % 2 ==0)
	{
		sum +=fibonacci(i);
	}
	}

	printf("sum is : %d\n", sum);
	return 0;

}

