package Test;
import java.util.*;

public class Solution_Programmers_level1_15 {
	 public String solution(String[] seoul) {
	        String answer = "";
	        for(int i=0;i<seoul.length;i++){
	            if(seoul[i].equals("Kim")){
	                answer="김서방은 "+i+"에 있다";
	            }
	        }
	        return answer;
	    }
}
