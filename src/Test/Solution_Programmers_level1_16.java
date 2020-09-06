package Test;
import java.util.*;

//에라토스테네스의 체 방식 
public class Solution_Programmers_level1_16 {
	  public int solution(int n) {
	        int answer = 0;
	        boolean[] prime_number=new boolean[n+1];
	        
	        // 2~n까지 일단 모두 소수라고 초기화
	        for(int i=2; i<=n; i++){
	            prime_number[i]=true;
	        }
	        
	        // 소수인지 확인하려면 제곱근의 배수인지 아닌지 확인하면 됨
	        // 예를 들면 12의 제곱근은 3.46인데
	        // 12의 약수는 1,2,3,4,6,12
	        // 1,12를 제외했을 때, 2*6 3*4 4*3 6*2
	        // 몫이 커지면 나누는 값이 작아지거나 나누는 값이 커지면 몫이 작아지는 반비례 관계
	        // n의 제곱근까지 나누어 떨어지는 여부를 조사하면 빠르게 소수 판별 가능
	        int root=(int)Math.sqrt(n);
	        
	        for(int i=2; i<=root; i++){
	            if(prime_number[i]==true){ //i번째의 수가 소수이면
	                for(int j=i; i*j<=n; j++) // i의 배수는 모두 false로 초기화
	                    prime_number[i*j]=false;
	            }
	            
	        }
	        
	        // 최종 소수 세기
	        for(int i=2; i<=n; i++){
	            if(prime_number[i]==true)
	                answer++;
	        }
	        return answer;
	    }
}
