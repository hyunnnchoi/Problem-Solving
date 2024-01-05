import java.util.Collections;
import java.util.ArrayList;
import java.util.List;
class Solution {
    public int[] solution(int[] num_list) {
        // 새로운 ArrayList 생성
        List<Integer> new_list = new ArrayList<>();
        for(int number:num_list){
            new_list.add(number);
        }
        // num_list를 내림차순 정렬
        // 5개만 출력
        // 정렬
        Collections.sort(new_list);
        // 가장 처음에 5개 제거
        for(int i=0; i<5; i++){
            new_list.remove(0);
        }
        // ArrayList를 기존 List로 변환
        int[] answer = new int[new_list.size()];
        for(int i=0; i<new_list.size(); i++){
            answer[i] = new_list.get(i);
        }
        return answer;
    }
}