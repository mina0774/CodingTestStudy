package Test;
import java.util.*;

public class Solution_Programmers_level1_5 {
	   public String solution(String s) {
	        String answer = "";
	        if(s.length()%2==0){
	            int a=s.length()/2;
	            answer=s.substring(a-1,a+1);
	        }else{
	            int a=s.length()/2;
	            answer=s.substring(a,a+1);
	        }
	        return answer;
	        
	        // 다른 풀이
	        // return s.substring((word.length()-1) / 2, word.length()/2 + 1);    
	    }
}
