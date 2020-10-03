package Test;
import java.util.*;

public class Solution_Programmers_level1_27 {
	 public long solution(long n) {
		 
	        if(Math.pow((int)Math.sqrt(n),2)==n){ // n의 제곱근의 제곱이 n과 같을 경우
	            return (long)Math.pow(Math.sqrt(n)+1,2);
	        }
	        return -1;
	    }
}
