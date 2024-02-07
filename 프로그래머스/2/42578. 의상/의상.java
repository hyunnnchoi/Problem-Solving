import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> map = new HashMap<>();
        for(String[] list:clothes){
            map.computeIfPresent(list[1], (k,v) -> ++v);
            map.putIfAbsent(list[1],1);
        }
        for(Integer i:map.values()){
            answer *= i+1;
        }
        return --answer;
    }
}
// 2차원 배열에서, 바깥 배열에서 한가지는 무조건 있어야 하고
// 종류별로 최대 1개
// 전체가 같지 않으면 다른 방법임.
// 1 -> 2개, 2->1개, 3->1개, 4->1개
// 종류를 고르는 수 -> (4c1 + 4c2)*2 
// 선택한 카테고리의 수 * 카테고리의 개수 * 다른 카테고리의 개수..