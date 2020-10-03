package Test;
import java.util.*;

public class Solution_Programmers_level1_30 {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        // 왼쪽 손의 처음 위치 * - 10으로 대체
        // 오른쪽 손의 처음 위치 # - 12으로 대체
        // 0 - 11로 대체
        int left=10;
        int right=12;
        
        for(int i=0;i<numbers.length;i++){
            int num=numbers[i];
            
            if(num==1||num==4||num==7){
                answer+="L";
                left=num;
            }else if(num==3||num==6||num==9){
                answer+="R";
                right=num;
            }else{
                int left_distance=cal_distance(left,num);
                int right_distance=cal_distance(right,num);
                
                if(left_distance>right_distance){ // 오른쪽이 더 가까울 때
                    answer+="R";
                    right=num;
                }else if(left_distance<right_distance){ // 왼쪽이 더 가까울 때
                    answer+="L";
                    left=num;
                }else{ // 오른쪽, 왼쪽 거리가 같을 때
                    if(hand.equals("right")){// 오른손잡이일 때
                        answer+="R";
                        right=num;
                    }else{
                        answer+="L";
                        left=num;
                    }
                }
            }
        }
        return answer;
    }
    
    public int cal_distance(int location,int num){
        // 키패드값이 0일때
        if(location==0) 
            location=11;
        if(num==0)
            num=11;
        
        // 키패드 숫자에 따른 숫자 위치 좌표 ((키패드-1)/3,(키패드-1)%3)
        
        // 왼손 or 오른손 좌표
        int locationX=(location-1)/3;
        int locationY=(location-1)%3;
        
        // 다음 누를 키패드 좌표
        int numX=(num-1)/3;
        int numY=(num-1)%3;
        
        int result=Math.abs(locationX-numX)+Math.abs(locationY-numY);
        
        return result;
    }
}
