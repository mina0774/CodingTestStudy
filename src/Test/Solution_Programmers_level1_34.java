package Test;

public class Solution_Programmers_level1_34 {
    public boolean solution(int x) {
        int sum = 0;
		int a = x;
      
        // 모든 자릿수 더하기
		while (a >= 1) {
			sum += a % 10;
			a /= 10;
		}
 
		if (x % sum == 0) {
			return true;
		} else
			return false;
    }
}
