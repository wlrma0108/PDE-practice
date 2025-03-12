#include<iostream>
#include<climits>
//LLONG_MAX 가 포함된 라이브러리

int main(){
    long long no_overflow = LLONG_MAX;
    long long overflow = LLONG_MAX;
    //long long으로 8바이트 단위를 얻는다.
    // 위의 문제와 굉장히 유사하다. 
    overflow += LLONG_MAX;
    std:: cout << overflow;
    std:: cout << no_overflow;

}
// 결과값-9223372036854775808 9223372036854775807