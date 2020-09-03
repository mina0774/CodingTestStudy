package Test;
import java.util.*;

public class Solution_Programmers_level1_14 {

	    public boolean solution(String s) {
	        boolean answer = true;
	        // 문자열 길이가 4나 6이 아닐 때
	        if(!(s.length()==4||s.length()==6)){
	            answer=false;
	        // 문자열 길이가 4나 6일때
	        }else{
	            for(int i=0;i<s.length();i++){
	                // 아스키코드상 0-9까지의 값이 48-57
	                if(!((int)s.charAt(i)>=48&&(int)s.charAt(i)<=57))
	                {
	                    answer=false;
	                    break;
	                }
	            }
	        }
	        return answer;
	    }
}
