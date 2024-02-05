#include <iostream>
#define MAX 15
using namespace std;

int col[MAX];
int N, total = 0; // 우선 0으로 초기화하면 되는구나..


bool check(int level){
    for(int i=0; i<level; i++)
        if(col[i] == col[level] || abs(col[level] - col[i]) == level - i)
            return false;
    return true;
}
void nqueen(int x){ // x: 몇 번째 행에 있는지
    if(x == N) // 끝까지 다 돌았을 경우
        total++;
    else{
        for(int i=0; i<N; i++){
            col[x] = i; // 해당 위치에 퀸을 배치
            if(check(x))
                nqueen(x+1);
        }
    }
}
int main() {
    cin >> N;
    nqueen(0);
    cout << total;
    // n*n 테이블 생성

    return 0;
}
