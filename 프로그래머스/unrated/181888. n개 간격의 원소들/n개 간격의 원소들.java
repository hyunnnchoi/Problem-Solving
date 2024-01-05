import java.util.*;

class Solution {
    public Integer[] solution(int[] num_list, int n) {
        List<Integer> a = new ArrayList<>();
        int count = 0;
        for(int i=0; i<num_list.length; i++)
            if(i%n == 0){
                a.add(num_list[i]);
            }
        int aSize = a.size();
        Integer arr[] = a.toArray(new Integer[aSize]);
        return arr;
    }
}