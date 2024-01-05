import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        // 각 원소 50보다 크거나 같은 짝수? 2로 나눈다.
        // 50보다 작은 홀수? 2를 곱한다.
        for(int i=0; i<arr.length; i++){
            if(arr[i] >= 50 && arr[i]%2 == 0){
                arr[i] = arr[i]/2;
            }else if(arr[i] < 50 && arr[i]%2 == 1){
                arr[i] = arr[i]*2;
            }
        }
        return arr;
    }
}