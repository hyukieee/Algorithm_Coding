#include<stdio.h>
int main() {
	int a, b = 0;
	int arr[100001] = {0,};
	scanf("%d %d", &a, &b);

	for (int i = 1;i <= a;i++) {
		scanf("%d", &arr[i]);
		arr[i] = arr[i - 1] + arr[i];
	}

	int num1, num2;
	int result=0;

	for (int i = 0;i < b;i++) {
		scanf("%d %d", &num1, &num2);

		result = arr[num2] - arr[num1 - 1];

		printf("%d\n", result);

		result = 0;

	}

	return 0;
}