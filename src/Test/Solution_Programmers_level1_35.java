package Test;

public class Solution_Programmers_level1_35 {
	   public String solution(String phone_number) {
	        String answer = "";
	        String[] arr=phone_number.split("");
	        
	        // 뒷자리 4개 앞까지만 *로 변경
	        for(int i=0;i<arr.length-4;i++){
	            arr[i]="*";
	        }
	        
	        for(int i=0;i<arr.length;i++){
	            answer+=arr[i];
	        }
	        
	        return answer;
	    }
}
