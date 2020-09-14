package Test;
import java.util.*;

public class Solution_Programmers_level_1_18 {
	 public String[] solution(int n, int[] arr1, int[] arr2) {
	        String[] answer = new String[n];
	        for (int i=0; i<n; i++){
	            // or 연산을 해준 후 바이너리 스트링으로 변환
	            answer[i]=Integer.toBinaryString(arr1[i]|arr2[i]); 
	        }
	        
	        // 문제에서 주어진 문자열로 대체해주는 작업
	        for(int i=0;i<n;i++){
	            // String.format(%5s,111)이면 문자열 길이가 총 5
	            // 앞에 2자리를 남기고, 뒤에 3자리가 111이 됨
	            answer[i]=String.format("%"+n+"s",answer[i]);
	            answer[i]=answer[i].replace('1','#');
	            answer[i]=answer[i].replace('0',' ');
	        }
	        return answer;
	    }
}
