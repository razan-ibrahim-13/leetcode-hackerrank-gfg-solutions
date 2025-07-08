#include <bits/stdc++.h>
#include <list>
using namespace std;

int main()
{
    int T;
    cin >> T ;
    list<int> my_list ;
    int d=0;
    for(int j=1;j<=T;j++){
      int s;
      cin >> s ;
      for(int i=1;i<=s;i++){
         int k;
         std::cin >> k;
         if(k<0){
             d++;
         }
         my_list.push_back(k) ;
      }
      for(int value : my_list){
         if (value==0 || d%2==0){
             std::cout << 0 << std::endl;
             break;
             break;
         }
        
        
         else if(d%2!=0){
           std::cout << 1 << std::endl;
           break;
           
         }
      }
    }
    
  

    
}