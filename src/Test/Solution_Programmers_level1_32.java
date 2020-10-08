package Test;

public class Solution_Programmers_level1_32 {
	public int solution(int num) {
        int answer = 0;
        long n=(long)num; // int 범위를 벗어날 것을 대비해서
        while(n!=1){
            if(n%2==0){
                n=n/2;
            }else{
                n=n*3+1;
            }
            answer++;
            if(answer>=500){
                answer=-1;
                break;
            }
        }
        return answer;
    }
}
