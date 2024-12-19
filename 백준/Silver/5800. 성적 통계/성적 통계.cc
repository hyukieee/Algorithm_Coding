#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int c;
    cin >> c;
    for(int i=0;i<c;i++){
        int n =0;
        cin >> n;
        int *arr = new int[n];
        
        for(int k=0;k<n;k++){
            cin >> arr[k];
        }

        sort(arr, arr + n);

        int sub =0;
        for(int k=0;k <n-1;k++){
            int gap = arr[k + 1] - arr[k];
            if(gap> sub) sub = gap;
        }

        cout << "Class " << i+1 << "\n";
        cout << "Max " <<arr[n-1] <<", Min "<< arr[0] << ", Largest gap "<< sub<< "\n";
        delete[] arr;
    }

    return 0;
     
}