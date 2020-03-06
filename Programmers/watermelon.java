class Solution {
    public String solution(int n) {
        String answer = "";
        for(int i =0; i<n; i++)
            answer += i%2 == 0 ? "수" : "박";
        return answer;
    }
      public static void  main(String[] args){
          Solution sol = new Solution();
          System.out.println("n이 3인 경우: " + sol.solution(3));
          System.out.println("n이 4인 경우: " + sol.solution(4));
      }
  }