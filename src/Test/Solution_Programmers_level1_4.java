package Test;

import java.util.*;

public class Solution_Programmers_level1_4 {
	    public int[] solution(int[] array, int[][] commands) {
	        int[] answer = new int[commands.length];
	        
	        for(int i=0; i<commands.length; i++){
	            int[] new_array=Arrays.copyOfRange(array,commands[i][0]-1,commands[i][1]); /* �迭�� Ư�� ��ġ�� ������, ������ �����ؼ� �߶��� 
	            copyOfRange(�迭, �����ε���, �����ε���) �޼ҵ�� 
	            �����ε����� �����ϰ�, �����ε����� �������� �ʴ´�.*/
	            Arrays.sort(new_array);
	            answer[i]=new_array[commands[i][2]-1];
	        }
	        return answer;
	    }
}
