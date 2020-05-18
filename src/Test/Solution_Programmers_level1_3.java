package Test;
import java.util.*;
public class Solution_Programmers_level1_3 {
	 public int[] solution(int[] answers) {
	        int[] student1={1,2,3,4,5};
	        int[] student2={2,1,2,3,2,4,2,5};
	        int[] student3={3,3,1,1,2,2,4,4,5,5};
	        
	        List<Integer> list = new ArrayList<Integer>(); // 세학생의 맞춘 개수 저장
	        for(int i=0; i<3; i++) list.add(0);
	        
	        for(int i=0; i<answers.length; i++){
	            if(answers[i]==student1[i%5]) list.set(0,list.get(0)+1);
	            if(answers[i]==student2[i%8]) list.set(1,list.get(1)+1);
	            if(answers[i]==student3[i%10]) list.set(2,list.get(2)+1);
	        }
	        
	        int max=Collections.max(list);
	        
	        List<Integer> returnList=new ArrayList<Integer>();
	        for(int i=0; i<list.size(); i++) if(max==list.get(i)) returnList.add(i+1);
	    
	        
	        int[] answer = new int[returnList.size()];
	        for(int i=0;i<returnList.size();i++) answer[i]=returnList.get(i);
	        return answer;
	    }
}
