package Test;
import java.util.*;

public class Solution_Programmers_level1_11 {

	    public long solution(int a, int b) {
	        long answer = 0;
	        int temp;
	        
	        if(a>b){ //대소 관계
	            temp=a;
	            a=b;
	            b=temp;
	        }
	        
	        for(int i=a; i<=b; i++){
	            answer+=i;
	        }
	        return answer;
	    }
}
