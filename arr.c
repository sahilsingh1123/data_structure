#include<stdio.h>

int main()
{
	int i,j;
	int a[3][2] = {7,8,9,5,2,3};
	for (i=0;i<3;i++){
		printf("\n");
		for (j=0;j<2;j++)
			printf("%d ",a[i][j]);
	}
	printf("\n");
	return 0;
	
}
