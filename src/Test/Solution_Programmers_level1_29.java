package Test;
import java.util.*;

public class Solution_Programmers_level1_29 {
    public String solution(int num) {
        String answer = "";
        if(num%2==0){
            answer="Even";
        }else{
            answer="Odd";
        }
        return answer;
    }
}
