package Test;
import java.util.*;
public class Solution_Programmers_level1_7 {
	 public String solution(String s) {
	        String answer = "";
	        Character[] array=new Character[s.length()]; // ���ڿ��� �迭�� �ֱ� ���� ����
	        
	        for(int i=0;i<s.length();i++){ //���ڿ��� ������ŭ �ݺ�
	            array[i]=s.charAt(i);
	        }
	        
	        // array ���� �˰��� �̿�
	        // ������������ �����ϹǷ� Collections.reverseOrder() �̿�
	        Arrays.sort(array,Collections.reverseOrder());
	        
	        // ���ĵ� array�� ���� ����� ����
	        for(int i=0; i<array.length;i++){
	            answer+=array[i];
	        }
	        
	        return answer;
	    }
}
