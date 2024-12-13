#include <iostream>
using namespace std;

int main() {
    int size ;
    cin >> size;

    int *mem = new int [size];
    int tos =0;

    for(int i=0; i< size;i++){
        int val =0;
        cin >> val;

        if(val == 0){
            tos--;        
        }
        else {
            mem[tos] = val;
            tos ++;

        }
    }

    int sum =0;

    for(int i=0; i < tos; i++){
        sum += mem[i];
    }

    cout << sum;
}