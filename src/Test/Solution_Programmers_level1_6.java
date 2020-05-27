package Test;
import java.util.*;
public class Solution_Programmers_level1_6 {

	    int day_num[]={31,29,31,30,31,30,31,31,30,31,30,31};
	    String day[]={"SUN","MON","TUE","WED","THU","FRI","SAT"};
	    public String solution(int a, int b) {
	    
	        String answer = "";
	        int today_num=5;
	        int total_day=0;

	        for(int i=0;i<a-1;i++){
	            total_day+=day_num[i];
	        }
	        total_day+=b;
	        total_day-=1;
	        
	        today_num+=total_day%7;
	        today_num=today_num%7;
	       
	        answer=day[today_num];
	        return answer;
	    }
	
}
