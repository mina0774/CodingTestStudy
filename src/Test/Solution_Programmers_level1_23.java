package Test;
import java.util.*;

public class Solution_Programmers_level1_23 {
	   public int solution(int n) {
	        String str=Integer.toString(n); // 정수를 문자열로 변환
	        String str1[]=str.split(""); // 문자열을 문자 배열로 쪼개서
	         int answer = 0;
	        
	        for(int i=0; i<str1.length; i++){
	            answer+=Integer.parseInt(str1[i]);
	        }
	             
	        return answer;
	    }
}
