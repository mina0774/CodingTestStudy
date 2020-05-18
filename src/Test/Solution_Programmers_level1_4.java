package Test;

import java.util.*;

public class Solution_Programmers_level1_4 {
	    public int[] solution(int[] array, int[][] commands) {
	        int[] answer = new int[commands.length];
	        
	        for(int i=0; i<commands.length; i++){
	            int[] new_array=Arrays.copyOfRange(array,commands[i][0]-1,commands[i][1]); /* 배열에 특정 위치에 시작점, 끝점을 지정해서 잘라줌 
	            copyOfRange(배열, 시작인덱스, 종료인덱스) 메소드는 
	            시작인덱스는 포함하고, 종료인덱스는 포함하지 않는다.*/
	            Arrays.sort(new_array);
	            answer[i]=new_array[commands[i][2]-1];
	        }
	        return answer;
	    }
}
