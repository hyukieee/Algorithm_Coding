#include <iostream>
#include <string>
using namespace std;

int arr[10001];
int top = 0;

void push(int _v) {
    arr[top] = _v;
    top++;
}

void pop() {
    if (top <= 0) {
        cout << -1 << endl;
    } else {
        top--;
        cout << arr[top] << endl;
    }
}

void size() {
    cout << top << endl;
}

void empty() {
    cout << (top == 0 ? 1 : 0) << endl;
}

void Top() {
    if (top <= 0) {
        cout << -1 << endl;
    } else {
        cout << arr[top - 1] << endl;
    }
}

int main() {
    int run;
    cin >> run;
    cin.ignore(); // 버퍼에 남아있는 개행 문자 제거

    for (int i = 0; i < run; i++) {
        string func;
        getline(cin, func);

        if (func.substr(0, 4) == "push") {
            int x = stoi(func.substr(5));
            push(x);
        } else if (func == "pop") {
            pop();
        } else if (func == "size") {
            size();
        } else if (func == "empty") {
            empty();
        } else if (func == "top") {
            Top();
        }
    }
    return 0;
}
