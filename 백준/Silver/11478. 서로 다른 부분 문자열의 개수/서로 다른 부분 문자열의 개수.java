import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static List<String> comb = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        HashSet<String> set = new HashSet<>();
        // 1 2 3 4 5, 12 23 34 45, 123, 234, 345, 1234, 12345
        for(int i=0; i<s.length(); i++){
            for(int j=i+1; j<s.length()+1; j++){
                set.add(s.substring(i,j));
            }
        }
        System.out.println(set.size());
    }
//    static void nCr(char[] str, int r, String result){
//        if(r==0){
//            comb.add(result);
//            return;
//        }else{
//            for(int i=0; i<str.length; i++){
//                nCr(str, r-1, result+str[i]);
//            }
//        }
//    }
}