#include<iostream>
#include<climits>
// 힌트 사용을 위한 라이브러리 호출 int max를 사용하지 않아도 되니 안써도 구현가능하다.
// unit_max를 사용해야하는 이유를 모르겠다. 

int main(){

    int no_overflow = INT_MAX;
    int overflow = INT_MAX;
    //int가 표현할 수 있는 최대 정수 2**31-1
    overflow += 1;
    //오버플로우 발생을 위한 플러스 1
    std :: cout << no_overflow;
    std :: cout << overflow
    //어떤식으로 발현되는지 살펴보자. 

}


// 출력값 2147483647-2147483648 오버플로우 발생으로 음수처리 되었다. 