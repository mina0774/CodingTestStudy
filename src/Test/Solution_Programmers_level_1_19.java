package Test;
import java.util.*;

public class Solution_Programmers_level_1_19 {
	public int solution(String s) {
        boolean sign=true;
        int answer = 0;
        
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if(ch=='-') // 부호가 -일때
                sign=false;
            else if(ch!='+') { // 문자가 +,-가 아닌 숫자일때
                // 새로운 자릿수가 나올때마다, 
                //answer에 10을 곱해줘서 다음 자릿수가 들어올 공간을 만들어줌 
                // 아스키코드 상에서 '0'을 빼줌 
                // 아스키코드상 숫자 '0'은 48인데 '1'이 나왔을 때, 
                // '0'을 빼주면 49-48=1으로 1의 값을 가리킴 
                answer=answer*10+ (ch-'0');
            }
        }
            
        if(sign==false){
            answer*=-1;
        }
        
        return answer; 
    }
}
