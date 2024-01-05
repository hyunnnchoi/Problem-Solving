import java.util.*;
class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        // 숫자 두 개, 
        // 1. str로 변환하거나,
        // 2. 두번째 숫자의 자릿수를 알아서, 그만큼 곱해주고 더한다.
        
        // b 자릿수 구하기        
        String bString = Integer.toString(b);
        int bCount = bString.length();
        bCount = (int)Math.pow(10, bCount);
        // a 자릿수 구하기
        String aString = Integer.toString(a);
        int aCount = aString.length();
        aCount = (int)Math.pow(10, aCount);
        // 자릿수 -> 2 -> 100, 1 -> 10..
        
        // a+b 구하기
        int apb = a * bCount + b;
        int bpa = b * aCount + a;
        
        answer = Math.max(apb, bpa);
        return answer;

    }
}