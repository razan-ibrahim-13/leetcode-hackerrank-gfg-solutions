#include <iostream>
#include <list>
using namespace std;

int main(){
    int n;
    cin >> n;

    for(int i=0;i<=n;i++){

        for(char k='A'+i;k<='A'+n-1;k++){
            cout << k;
        }
        cout << endl;
    }

}