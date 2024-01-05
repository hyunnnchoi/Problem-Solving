import java.util.*;
class Solution {
    public int[] solution(int start_num, int end_num) {
        List<Integer> arrayList = new ArrayList<>();
        for(int i=start_num; i< end_num+1; i++){
            arrayList.add(i);
        }
        int[] array = new int[arrayList.size()];
        for(int i=0; i<arrayList.size(); i++){
            array[i] = arrayList.get(i);
        }
        return array;
    }
}