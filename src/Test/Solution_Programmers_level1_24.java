package Test;
import java.util.*;

public class Solution_Programmers_level1_24 {
	    public int[] solution(long n) {
	        // 숫자를 배열로 만들기
	        String str=Long.toString(n);
	        String str1[]=str.split("");
	        int[] answer = new int[str1.length];
	        
	        // 거꾸로 뒤집기
	        int count=0;
	        for(int i=str1.length-1; i>=0; i--){
	            answer[count]=Integer.parseInt(str1[i]);
	            count++;
	        }
	        
	        return answer;
	    }
}
