package Test;
import java.util.*;

// 시저 암
public class Solution_Programmers_level_1_20 {
	 public String solution(String s, int n) {
	        String answer = "";
	        for(int i=0; i<s.length(); i++){
	            char ch=s.charAt(i);
	            if(ch!=' '){ //ch가 공백이 아닐 경우
	                if(Character.isLowerCase(ch)){ //ch가 소문자일 경우
	                    // 문자의 시작점 a에서 얼마나 떨어져있냐를 판단
	                    // ch+n-'a'는 시작점에서 얼마나 떨어져있냐를 나타내고
	                    // 알파벳은 총 26글자이므로 
	                    // 떨어져 있는 값이 범위를 벗어날 경우 26으로 나누어줌
	                    ch=(char)('a'+(ch+n-'a')%26);
	                }else{ //ch가 대문자일 경우
	                    // 대문자는 시작점이 A
	                    ch=(char)('A'+(ch+n-'A')%26);
	                }
	            } 
	            answer+=ch;
	        }     
	        return answer;
	    }
}
