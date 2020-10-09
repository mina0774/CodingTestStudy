package Test;
import java.util.*;

public class Solution_Programmers_level1_36 {
public int[] solution(int N, int[] stages) {
        
        // 스테이지별 통과하지 못한 사람의 수를 저장
        int[] noClear = new int[N+1];
        for(int stage : stages){
            if(stage == N+1) continue;
            noClear[stage]++;
        }
        
        // 스테이지별 도전한 사람 수를 저장
        int[] challenger = new int[N+1];       
        // 1단계는 모든 사람이 도전함
        challenger[1]=stages.length;
        // 이전 스테이지에서 도전자 수에서 이전 스테이지를 클리어하지 못한 사람 수를 빼면
        // 이전 스테이지를 클리어한 사람 수가 되므로 다음 스테이지를 도전한 사람 수가 됨
        for(int i=2; i<=N; i++){
            challenger[i]=challenger[i-1]-noClear[i-1];
        }
        
        // 스테이지별 실패율을 저장
        double[] failRate=new double[N+1];
        // 실패율의 key를 보관
        Set<Double> fails=new HashSet<Double>();
        for (int i=1; i<=N; i++){
            if(challenger[i]==0){
                failRate[i]=0;
            }else{
                failRate[i]=(double)noClear[i]/challenger[i];
            }
            fails.add(failRate[i]);
        }
        
        // 실패율 정렬 - 오름차순로 정렬하고 뒤부터 조회!
        List<Double> failList=new ArrayList<Double>(fails);
        Collections.sort(failList);
        
        int[] answer = new int[N];
        
        int index=N-1;
        for(int i=0; i<failList.size(); i++){
            double rate=failList.get(i);
            
            // 이부분 왜이렇게 되는지 생각해보기..
            for(int j=failRate.length-1; j>0; j--){
                if(rate==failRate[j]){
                    answer[index]=j;
                    index--;
                }
            }
        }
        return answer;
    }
}
