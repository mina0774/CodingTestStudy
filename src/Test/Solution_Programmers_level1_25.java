package Test;
import java.util.*;

public class Solution_Programmers_level1_25 {
    public long solution(long n) {
        long answer = 0;
        
        // 문자 배열로 만들기
        String str=Long.toString(n);
        String str1[]=str.split("");
        
        // 배열 내림차순으로 정렬하기
        Arrays.sort(str1,Collections.reverseOrder());
        
        // 문자 배열을 문자열로 만들어주기
        str="";
        for(int i=0;i<str1.length;i++){
            str+=str1[i];
        }
        
        // 문자열을 정수로 바꿔주기
        answer=Long.parseLong(str);
        return answer;
    }
}
