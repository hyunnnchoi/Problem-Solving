import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        // 문자열 공백 제거
        // 한 문자열이 다른 문자열 안에 있는지..
        // 길이 짧은 순서대로 정렬
        // 짧은 애가 큰 애의 0:x에 존재하면? false
        boolean answer = true;
        HashMap<String, Integer> map = new HashMap<>();
        for(String s:phone_book){
            map.put(s, 0);
        }
        for(String s:map.keySet()){
            for(int i=0; i<s.length(); i++){
                if(map.containsKey(s.substring(0,i))){
                    return false;
                }
            }
        }
        return answer;

    }
}