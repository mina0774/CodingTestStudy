package Test;
import java.util.*;

public class Solution_Programmers_level1_2 {
	    public String solution(String[] participant, String[] completion) {
	        String answer = "";
	        int val;
	        Map<String,Integer> hm=new HashMap<>();
	        
	        for(String part:participant){
	            if(hm.get(part)==null){
	                hm.put(part,1);
	            }else{
	                val=hm.get(part)+1;
	                hm.put(part,val);
	            }
	        }
	        
	        for(String comp:completion){
	            val=hm.get(comp)-1;
	            hm.put(comp,val);
	        }
	        
	        for(String key:hm.keySet()){
	            if(hm.get(key)==1){ 
	                answer=key;
	                break;
	                               }
	        }
	        return answer;
	    }
}
