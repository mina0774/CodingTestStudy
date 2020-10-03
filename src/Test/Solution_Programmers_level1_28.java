package Test;
import java.util.*;

public class Solution_Programmers_level1_28 {
	 public int[] solution(int[] arr) {
	        int[] answer = {};
	       
	        if(arr.length==1){ // 배열의 길이가 1일 때, -1을 가지고 있는 배열을 return
	            return new int[]{-1};
	        }else{
	            int min=arr[0];
	            for(int i=0;i<arr.length;i++){ // 배열의 최솟값을 찾아서~
	                if(arr[i]<min)
	                    min=arr[i];
	            } 
	            
	            answer=new int[arr.length-1];
	            int j=0;
	            for(int i=0;i<arr.length;i++){ // 배열 최솟값만 뺀 배열을 만들기
	                if(arr[i]==min){
	                    continue;
	                }else{
	                    answer[j++]=arr[i];
	                }              
	            }
	            return answer;        
	        }
	        
	    }
}
