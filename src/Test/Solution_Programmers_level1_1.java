package Test;
import java.util.*;

class Solution_Programmers_level1_1 {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        Stack<Integer> st=new Stack<>();
         //moves는 움직일 칸의 열번호를 모아놓은 배열
        //board는 인형들의 배열
        
        for(int i=0;i<moves.length;i++){
            for(int j=0;j<board.length;j++){
                //해당 위치에 인형이 있는 경우, 해당 위치가 비어있지 않을 경우
                if(board[j][moves[i]-1]!=0){
                    
                    if(st.empty()){
                        //스택이 비어있을 경우 해당 위치에 있는 인형을 스택에 넣어줌
                        st.push(board[j][moves[i]-1]);
                    }else{
                        //스택이 비어있지 않을 경우
                        if(st.peek()==board[j][moves[i]-1]){
                            //스택의 가장 top과 해당 위치에 있는 인형을 비교하여 같으면
                            //스택을 pop하고 두개의 인형이 터뜨려진 것이므로 answer에 2를 +
                            st.pop();
                            answer+=2;
                        }else{
                            //같은 인형이 아니면 해당 인형을 스택에 넣어줌
                            st.push(board[j][moves[i]-1]);
                        }
                    }
                    //뽑힌 인형의 자리는 빈 칸으로 만들어줌
                    board[j][moves[i]-1]=0;
                    break;
                }
            }
        }
        return answer;
    }
}
