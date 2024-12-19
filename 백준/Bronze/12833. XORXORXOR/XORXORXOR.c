int main() {
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);

	int result;
	result = a;
	
	if (c % 2 == 0) {
		result = a;
	}
	else { result = a ^ b; }
	printf("%d\n", result);

	return 0;
}