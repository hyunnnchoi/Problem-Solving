import java.util.*;

class Solution {
    public int[] solution(int[] num_list, int n) {
        // int[] 배열 안에.. 
        int arrSize = num_list.length%n== 0 ? num_list.length/n : num_list.length/n +1;
        int[] answer = new int[arrSize];
        // n 단위로 인덱스 접근..
        int count = 0;
        // 예를들어, 전체 6개에 n이 4일 경우?
        // arrSize가 1이되네...
        for(int i=0; i<num_list.length; i += n){
            answer[count] = num_list[i];
            count += 1;
        }
        return answer;
    }
}