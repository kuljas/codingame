#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
 int max (int a, int b){
     if (a>=b)
        return a;
    else return b;
 }
 int absoulute_value(int x){
     if (x<0)
        return -x;
    else return x;
 }

int main()
{
    int min=5527;
    int result;
    vector<int> niz;
    niz.clear();
    int n; // the number of temperatures to analyse
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int t; // a temperature expressed as an integer ranging from -273 to 5526
        cin >> t; cin.ignore();
        if (absoulute_value(t)<=min){
            min=absoulute_value(t);
            niz.push_back(t);
        }
    }
    
    if (niz.size()==0){
        result=0;
    }
    else if ((niz.size()>=2) && (absoulute_value(niz.back()) == absoulute_value(niz.at(niz.size()-2)))){
        result = max(niz.back(),niz.at(niz.size()-2));
   }
   else {
       result = niz.back(); 
   }
    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << result << endl;
}
