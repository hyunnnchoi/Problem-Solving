import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 모든 수 숫자 다르다.
// N번째로 큰 수 뽑아와라.
// 그냥 heapq로 정렬한 뒤, 리스트로 바꿔서 인덱스 뽑아오면 되지 않나?

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(
                new InputStreamReader(System.in)
        );
        int N = Integer.parseInt(bf.readLine());

        PriorityQueue<Integer> minHeap = new PriorityQueue<>(Collections.reverseOrder());

        for(int i=0; i<N; i++){
            String temp = bf.readLine();
            // temp를 끊어서, minHeap에 append 하기
            StringTokenizer st = new StringTokenizer(temp);
            while(st.hasMoreTokens() == true){
                minHeap.add(Integer.parseInt(st.nextToken()));
            }
        }
        // minHeap 인덱스 기반 출력
        // 작은 숫자가 앞으로 와있고, 뒤에서 N번째 출력해야 함.
        for(int i=0; i<N-1; i++){
            minHeap.poll();
        }
        System.out.println(minHeap.poll());
    }
}