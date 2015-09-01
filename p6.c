#include <stdio.h>


int hundred(n)
{	if(n<2) return 1;
	else	return n + hundred(n-1);	
	
}


/*int hsquare(n)
{	int temp;
	if(n<1) return 1;
	temp = n*n + hsquare(n-1) * hsquare(n-1);
	return temp;
}
*/
int main()
{
	int hundredsum = hundred(100)*hundred(100);
	int i;
	int squaresum = 0;

	for(i=0; i<101; i++)
	{
		squaresum += i*i;
	}


	printf("hundred is : %d\n", hundred(10000));	
	printf("hundredsum is : %d\n", hundredsum);
	printf("squaresum is : %d\n", squaresum);
	printf(" answer is  :  %d\n", hundredsum - squaresum);
	

	
	return 0;
}
