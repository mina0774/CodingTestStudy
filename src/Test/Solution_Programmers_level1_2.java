package Test;
import java.util.*;

public class Solution_Programmers_level1_2 {
	    public String solution(String[] participant, String[] completion) {
		// 동명이인이 있을 수 있음
	        String answer = "";
	        int val;
	        Map<String,Integer> hm=new HashMap<>(); //이름, 이름이 나온 횟수 (키,값)
	        
	        for(String part:participant){
			// get은 지정한 키에 해당하는 값을 반환
	            if(hm.get(part)==null){
			    // 해쉬맵에 동명이인이 포함되어 있지 않을 경우
	                hm.put(part,1);
	            }else{
			     // 해쉬맵에 동명이인이 포함되어 있을 경우
	                val=hm.get(part)+1;
	                hm.put(part,val);
	            }
	        }
	        
		     // 완주를 한 사람들의 이름을 바탕으로 해쉬맵에 저장된 참여자의 이름과 일치할 시에 값을 하나 감소시킴
	        for(String comp:completion){
	            val=hm.get(comp)-1;
	            hm.put(comp,val);
	        }
	        
		     // 결국 해쉬맵의 값이 1이 되면 숫자가 감소되지 않아 완주한 선수의 명단이 없는 것으로 판단이 됨
	        for(String key:hm.keySet()){
	            if(hm.get(key)==1){ 
	                answer=key;
	                break;
	                               }
	        }
	        return answer;
	    }
}
