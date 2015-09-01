#include <stdio.h>


int main()
{

	int x, y;
	int palin = 0;
	int largest = 0;
	for(x = 999; x>100; x--){
		for(y = 999; y >100; y--)
		{
			palin = x*y;
		if( ((palin / 100000) == (palin % 10)) && ((palin % 100000 / 10000) == (palin % 100 / 10 )) && (( palin % 10000 / 1000) == (palin % 1000 / 100)) )
		{
			break;
		}
		}
		if(y >=100) break;
		}
	printf(" the largest palindrome is : %d\n", palin);
	printf("x = %d\n", x);	
    printf("y = %d\n", y);	
	return 0;
}

