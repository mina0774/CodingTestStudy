package Test;
import java.util.*;

class Solution_Programmers_level1_1 {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> st=new Stack<>();
        for(int i=0;i<moves.length;i++){
            for(int j=0;j<board.length;j++){
                if(board[j][moves[i]-1]!=0){
                    //해당 위치에 인형이 있는 경우
                    if(st.empty()){
                        st.push(board[j][moves[i]-1]);
                    }else{
                        if(st.peek()==board[j][moves[i]-1]){
                            st.pop();
                            answer+=2;
                        }else{
                            st.push(board[j][moves[i]-1]);
                        }
                    }
                    board[j][moves[i]-1]=0;
                    break;
                }
            }
        }
        return answer;
    }
}