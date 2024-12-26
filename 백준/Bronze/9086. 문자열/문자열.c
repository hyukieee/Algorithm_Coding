int main() {

    char S[1001];
    int T = 0;
    scanf("%d\n", &T);

    for (int i = 0;i < T;i++) {
    
       
        gets(S, strlen(S));
        int len = strlen(S);
        printf("%c%c\n", S[0], S[len - 1]);
    }
    return 0;
}