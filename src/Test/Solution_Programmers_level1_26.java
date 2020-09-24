package Test;
import java.util.*;

public class Solution_Programmers_level1_26 {
	  public int solution(int[] d, int budget) {
	        int answer = 0;
	        int result=0;
	        // 작은 수부터 더하는 것이 가장 최대의 값을 낼 수 있을 것, 그러므로 오름차순으로 정렬
	        Arrays.sort(d);
	        
	        // 오름차순으로 정리한 부서별 예산을 차례대로 더함
	        for (int i=0;i<d.length;i++){
	            result+=d[i];
	            // 예산을 넘어서면 끝낸다
	            if(result>budget){
	                answer=i; //배열은 0부터 시작하니까 i가 답!
	                break;
	            }
	        }
	        
	        // 만약 배열에 있는 값을 다 더했어도 예산보다 적은 값이 나왔다면
	        if(result<=budget){
	            answer=d.length;
	        }
	        
	        return answer;
	    }
}
