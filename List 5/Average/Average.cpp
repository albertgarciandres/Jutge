#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	
	double a,result, total, counter;
	counter = 0;
	total = 0;
	while (cin>> a){
		counter ++;
		total += a;
		
	}
	
	result = total / counter;
	std::cout << setprecision(2) << fixed;
	cout << result<< endl;
	
	return 0;
}
