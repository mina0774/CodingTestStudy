package Test;
import java.util.*;

public class Soulution_Programmers_level1_10 {
	 public int[] solution(int[] arr, int divisor) {
	        int[] answer = {};
	        ArrayList<Integer> answerArray=new ArrayList<Integer>();
	        
	        for(int i=0;i<arr.length;i++){
	            if(arr[i]%divisor==0){
	                answerArray.add(arr[i]);
	            }
	        }
	        if(answerArray.isEmpty()){
	            answerArray.add(-1);
	        }
	         
	      answer = new int[answerArray.size()];
	      for(int i = 0; i < answer.length; i++){
	          answer[i] = answerArray.get(i);
	      }
	        Arrays.sort(answer);

	        return answer;
	    }
}
