import java.util.*;

class Solution {
    public int solution(int a, int b) {
        String bStr = Integer.toString(b);
        int bCount = bStr.length();

        // 10의 ?만큼 곱해줘야 하니,
        bCount = (int)Math.pow(10, bCount);

        int aPb = a * bCount + b;

        int answer = Math.max(aPb, 2*a*b);
        return answer;
    }
}