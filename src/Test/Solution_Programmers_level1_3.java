package Test;
import java.util.*;
public class Solution_Programmers_level1_3 {
	 public int[] solution(int[] answers) {
	        int[] student1={1,2,3,4,5};
	        int[] student2={2,1,2,3,2,4,2,5};
	        int[] student3={3,3,1,1,2,2,4,4,5,5};
	        
	        List<Integer> list = new ArrayList<Integer>(); // 세 학생의 정답을 맞춘 개수 저장
	        for(int i=0; i<3; i++) list.add(0);
	        
		 // 정답과 학생의 답안을 비교하여 맞춘 개수를 저장하기
	        for(int i=0; i<answers.length; i++){
	            if(answers[i]==student1[i%5]) list.set(0,list.get(0)+1);
	            if(answers[i]==student2[i%8]) list.set(1,list.get(1)+1);
	            if(answers[i]==student3[i%10]) list.set(2,list.get(2)+1);
	        }
	        
		 // 리스트에서 최대로 많이 맞춘 개수를 뽑음
	        int max=Collections.max(list);
	        
		 // 리스트에 정답 개수와 최대로 많이 맞춘 개수와 일치할 시에 returnList에 추가
	        List<Integer> returnList=new ArrayList<Integer>();
	        for(int i=0; i<list.size(); i++) if(max==list.get(i)) returnList.add(i+1);
	    
	        
	        int[] answer = new int[returnList.size()];
		 // returnList값 반환
	        for(int i=0;i<returnList.size();i++) answer[i]=returnList.get(i);
	        return answer;
	    }
}
