int main() {
    unsigned char a;

    scanf("%hhu", &a);
    int cnt = 0;

    for (int i = 7; i >= 0; i--) {
        if ((a >> i) & 1) {
            cnt++;
        }
    }

    printf("%d", cnt);
    return 0;
}