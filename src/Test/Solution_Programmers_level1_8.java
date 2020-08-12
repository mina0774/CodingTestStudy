package Test;
import java.util.*;
public class Solution_Programmers_level1_8 {
	    public int solution(int n, int[] lost, int[] reserve) {
	        // ��ü ��� ������ ü������ �Ҿ���� �л� ����ŭ ����.
	        int answer = n-lost.length; 
	        
	        // ü������ �Ҿ���� �л��� �迭�� ����Ʈ�� ������ش�.
	        List<Integer> lostList=new ArrayList<Integer>();
	        for(int i:lost) lostList.add(i);
	        
	        // ������ ü������ �����ϰ� �ִ� �л��� �迭�� ����Ʈ�� ������ش�.
	        List<Integer> reserveList=new ArrayList<Integer>();
	        for(int i:reserve) reserveList.add(i);
	        
	        //������ ü������ ������ �л��� ü������ ���� ������ �� �����Ƿ�
	        // ������ ü������ �ִ� ����Ʈ�� �ִ� ���� ���� ���� ����Ʈ�� �ִ� ���� ���� ���, �� ���� ����Ʈ���� �����ϰ�, answer�� ���� 1 ������Ŵ
	        for(int i=0;i<lostList.size();i++){
	            for(int j=0;j<reserveList.size();j++){
	                if(lostList.get(i)==reserveList.get(j)){
	                    lostList.remove(i);
	                    reserveList.remove(j);
	                    answer++;
	                    i--; // �߿�! ����Ʈ ũ�Ⱑ 1���� �۾����Ƿ�, �ش� �ε����� ������ ���� �ڿ� �ִ� ���ҵ��� �ϳ��� ������ �������Ƿ� �̸� ������������.
	                    break;
	                }
	            }
	        }
	        
	        //���� ����Ʈ�� ũ�⸸ŭ �ݺ�
	        for(int i=0;i<lostList.size();i++){
	            // ���� ����Ʈ�� �ִ� ���� �ް�
	            int lostNum=lostList.get(i);
	            for(int j=0;j<reserveList.size();j++){
	                // ���� ����Ʈ�� �ִ� ���� ����
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
