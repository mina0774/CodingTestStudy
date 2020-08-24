package Test;
import java.util.*;

public class Solution_Programmers_level1_5 {
	   public String solution(String s) {
	        String answer = "";
	        if(s.length()%2==0){ //글자수가 짝수일 때
	            int a=s.length()/2;
	            answer=s.substring(a-1,a+1);
	        }else{ //글자수가 홀수일 때
	            int a=s.length()/2;
	            answer=s.substring(a,a+1);
	        }
	        return answer;
	        
	    
	    }
}
