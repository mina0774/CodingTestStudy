package Test;
import java.util.*;

public class Solution_Programmers_level1_22 {
    public String solution(String s) {
        int cnt=0; // 단어의 홀/짝을 구분
        String str[]=s.split(""); //인덱스 하나하나를 따져주기 위해서 이렇게 바꿔줘!
        String answer = "";
        
        for(int i=0;i<str.length;i++){
            if(str[i].equals(" ")){ // 공백일 경우
                cnt=0;
            }
            else if(cnt%2==0){ // 짝수번째 인덱스일 경우
                cnt++;
                str[i]=str[i].toUpperCase();
            }else{ // 홀수번째 인덱스일 경우
                cnt++;
                str[i]=str[i].toLowerCase();
            }
            answer+=str[i];
        }
        return answer;
    }
}
