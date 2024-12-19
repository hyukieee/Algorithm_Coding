#include <iostream> 
using namespace std;

int main(){
    int n;
    cin >> n;

    int a = 0;
    int b = 1;

    int tmp =0;

    for(int i=0;i<n;i++) {

        a = b;
        b = tmp;
        tmp = a+b;

    }

    cout << tmp;
}
