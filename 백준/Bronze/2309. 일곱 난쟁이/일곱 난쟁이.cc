#include <iostream>
using namespace std;


int* find(int* dwarf, int* select , int target) {

    for(int i=0 ;i<9;i++){
        for(int j =i+1;j<9;j++){
            if((dwarf[i] + dwarf[j]) == target) {
                int idx =0;
                for(int k=0;k<9;k++){
                    if(k == i || k==j)continue;
                        select[idx++] = dwarf[k];
                }
                return select;
            }
        }
    }
    return nullptr;
}

int main() {
    int dwarf[9];
    int sum =0;

    for(int i=0;i<9;i++){
        cin >> dwarf[i];
        sum += dwarf[i];
    }
    int target = sum - 100;

    int select[7];
    int not1, not2;

    find(dwarf,select,target);

    int temp;

    for (int i = 0; i <7; i++) {
        for (int j = 0; j < 6; j++) {
            if (select[j] > select[j + 1]) {
                temp = select[j];
                select[j] = select[j + 1];
                select[j + 1] = temp;
            }
        }
    }

    for(int i=0;i<7;i++) cout << select[i] <<"\n";

}