#include <bits/stdc++.h>
#include <list>
using namespace std;

int main()
{
    int T;
    cin >> T ;
 
    for(int j=1;j<=T;j++){
        int s;
        cin >> s;
        vector<int> my_list ;
        for(int i=1;i<=s;i++){
            int d;
            cin >> d;
            my_list.push_back(d);
        }
        for(int i=1;i<=s;i++){
           if(my_list[i]!=my_list[i+1]){
              cout << my_list[i] << " " ;
              
           }


        }
         
      }
}
    
  

    

