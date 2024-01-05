import java.util.Collections;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] num_list, int n) {
        // 새로운 ArrayList 생성
        List<Integer> arrayList = new ArrayList<>();
        for(int i:num_list){
            arrayList.add(i);
        }
        // 앞에 n개 제거
        for(int i=1; i<n; i++){
            arrayList.remove(0);
        }
        // arrayList -> list
        
        int[] array = new int[arrayList.size()];
        for(int i=0; i<arrayList.size(); i++){
            array[i] = arrayList.get(i);
        }
        return array;
    }
}