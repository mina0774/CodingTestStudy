package Test;
import java.util.*;

public class Solution_Programmers_level1_31 {
	 public int[] solution(int n, int m) {
	        int[] answer = new int[2];
	        int gcd=getGCD(n,m);
	        int lcm=getLCM(n,m,gcd);
	        answer[0]=gcd;
	        answer[1]=lcm;
	        return answer;
	    }
	    
	    public int getGCD(int n, int m){ // 최대공약수
	        int a=Math.max(m,n);
	        int b=Math.min(m,n);
	    
	        while(b>0){ // 유클리드 호제법
	            int tmp=a;
	            a=b;
	            b=tmp%b;
	        }
	        return a;
	    }
	    
	    public int getLCM(int n, int m, int gcd){ // 최소공배수
	        return n*m/gcd;
	    }
}
