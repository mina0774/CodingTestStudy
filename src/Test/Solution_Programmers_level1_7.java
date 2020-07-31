package Test;
import java.util.*;
public class Solution_Programmers_level1_7 {
	 public String solution(String s) {
	        String answer = "";
	        Character[] array=new Character[s.length()]; // 문자열을 배열에 넣기 위해 선언
	        
	        for(int i=0;i<s.length();i++){ //문자열의 개수만큼 반복
	            array[i]=s.charAt(i);
	        }
	        
	        // array 정렬 알고리즘 이용
	        // 내림차순으로 정렬하므로 Collections.reverseOrder() 이용
	        Arrays.sort(array,Collections.reverseOrder());
	        
	        // 정렬된 array를 통해 결과값 추출
	        for(int i=0; i<array.length;i++){
	            answer+=array[i];
	        }
	        
	        return answer;
	    }
}
