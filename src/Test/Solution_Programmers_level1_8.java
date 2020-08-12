package Test;
import java.util.*;
public class Solution_Programmers_level1_8 {
	    public int solution(int n, int[] lost, int[] reserve) {
	        // 전체 사람 수에서 체육복을 잃어버린 학생 수만큼 뺀다.
	        int answer = n-lost.length; 
	        
	        // 체육복을 잃어버린 학생의 배열을 리스트로 만들어준다.
	        List<Integer> lostList=new ArrayList<Integer>();
	        for(int i:lost) lostList.add(i);
	        
	        // 여분의 체육복을 보유하고 있는 학생의 배열을 리스트로 만들어준다.
	        List<Integer> reserveList=new ArrayList<Integer>();
	        for(int i:reserve) reserveList.add(i);
	        
	        //여벌의 체육복을 가져온 학생이 체육복을 도난 당했을 수 있으므로
	        // 여벌의 체육복이 있는 리스트에 있는 값과 도난 당한 리스트에 있는 값이 같을 경우, 두 개의 리스트에서 삭제하고, answer의 값을 1 증가시킴
	        for(int i=0;i<lostList.size();i++){
	            for(int j=0;j<reserveList.size();j++){
	                if(lostList.get(i)==reserveList.get(j)){
	                    lostList.remove(i);
	                    reserveList.remove(j);
	                    answer++;
	                    i--; // 중요! 리스트 크기가 1개씩 작아지므로, 해당 인덱스의 삭제된 원소 뒤에 있는 원소들이 하나씩 앞으로 땡겨지므로 이를 적용시켜줘야함.
	                    break;
	                }
	            }
	        }
	        
	        //도난 리스트의 크기만큼 반복
	        for(int i=0;i<lostList.size();i++){
	            // 도난 리스트에 있는 값을 받고
	            int lostNum=lostList.get(i);
	            for(int j=0;j<reserveList.size();j++){
	                // 여벌 리스트에 있는 값을 받음
	                int reserveNum=reserveList.get(j); 
	                if(lostNum==reserveNum-1||lostNum==reserveNum+1){
	                    reserveList.remove(j);
	                    answer++;
	                    break;
	                }
	            }
	        }
	        return answer;
	    }
	
}
