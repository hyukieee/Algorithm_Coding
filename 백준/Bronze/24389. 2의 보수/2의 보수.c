int main() {
	int decimalNumber;
	int bina[32];
	int num2s[32];
	scanf("%d", &decimalNumber);

	for (int i = 31; i >= 0; i--) {
		bina[31-i] = (decimalNumber >> i) & 1;
		
	}
	
	int idx = 31;
	for (int i =31;i >= 0;i--) {
		idx--;
		if (bina[i] == 1) {
			break;
		}
		
	}
	int cnt = 0;
	for (int i = 0; i <= idx; i++) {
		num2s[i] = !bina[i];
		if (num2s[i] != bina[i]) {
			cnt++;
		}
		
	}
		printf("%d",cnt);
		
	
	return 0;
}