package Test;
import java.util.*;
public class Solution_Programmers_level1_9 {
	 public int[] solution(int []arr) {
	        
	        ArrayList<Integer> tempList=new ArrayList<Integer>();
	        int prenum=arr[0];
	        tempList.add(arr[0]);
	        
	        for (int num : arr){
	            if(prenum!=num){
	                tempList.add(num);
	            }
	            prenum=num;
	        }
	        int[] answer=new int[tempList.size()];
	        for (int i=0; i<answer.length;i++){
	            answer[i]=tempList.get(i).intValue();
	        }
	        
	        return answer;
	    }
}
