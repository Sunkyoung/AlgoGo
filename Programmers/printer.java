import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());
        for(int i : priorities){
            pq.add(i);
        }
        while(!pq.isEmpty()){
            for(int i=0; i<priorities.length; i++){
                if(priorities[i] == (int)pq.peek()){
                    if(i == location)
                        return answer;
                    pq.poll();
                    answer++;
                }
            }
        }
        return answer;
    }
}