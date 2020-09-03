package Test;
import java.util.*;

public class Solution_Programmers_level1_13 {
	  boolean solution(String s) {
	        boolean answer = true;

	        int count_p=0; // p 개수
	        int count_y=0; // y 개수
	        
	        for(int i=0; i<s.length(); i++){
	            if(s.charAt(i)=='p'||s.charAt(i)=='P'){
	                count_p++;
	            }
	            if(s.charAt(i)=='y'||s.charAt(i)=='Y'){
	                count_y++;
	            }
	        }
	        
	        if(count_p==count_y){
	            answer=true;
	        }else{
	            answer=false;
	        }

	        return answer;
	    }
}
