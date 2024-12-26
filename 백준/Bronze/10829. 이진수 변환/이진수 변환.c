int main() {
	unsigned long long N = 0;
	scanf("%llu", &N); // long long type input = "%llf"
					 // unsigned long long type input = "%llu"

	int bit[64];

	for (int i = 63; i >= 0; i--) {
		bit[63 - i] = (N >> i) & 1;

	}
	int i = 0;
	for (i = 0;i < 64;i++) {
		if (bit[i] == 1) {
			break;
		}

	
	}
	for (i; i < 64; i++) {
		printf("%d", bit[i]);

	}


	return 0;
}