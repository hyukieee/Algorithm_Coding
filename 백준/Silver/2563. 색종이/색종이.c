#include<stdio.h>
int main() {
    int arr[100][100] = { 0, };
    int num = 0;
    scanf("%d", &num);

    int a, b;
    for (int i = 0;i < num;i++) {

        scanf("%d %d", &a, &b);
        for (int j = 0;j < 10;j++) {
            for (int k = 0;k < 10;k++) {
                arr[j + a][k + b] = 1;

            
            }
        }
    }
    int cnt = 0;
    for (int i = 0;i < 100;i++) {
        for (int k = 0;k < 100;k++) {
            if (arr[i][k] == 1)cnt++;
        }
    }
    printf("%d", cnt);

	return 0;
}