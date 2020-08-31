package Test;
import java.util.*;

public class Solution_Programmers_level1_12 {

	    public String[] solution(String[] strings, int n) {
	        String[] answer = {};
	        
	        // 배열을 한바퀴 돌면서 특정 인덱스에 해당하는 문자값을 문자열 앞에 붙여줌
	        for(int i=0;i<strings.length;i++){
	            strings[i]=strings[i].charAt(n)+strings[i];
	        }
	        
	        // 앞글자에 특정 인덱스 문자값을 붙여줬으므로 사전 순으로 sorting
	        Arrays.sort(strings);
	        
	        answer=new String[strings.length];
	        
	        for(int i=0;i<strings.length;i++){
	            answer[i]=strings[i].substring(1,strings[i].length());
	        }
	        return answer;
	    }
}
