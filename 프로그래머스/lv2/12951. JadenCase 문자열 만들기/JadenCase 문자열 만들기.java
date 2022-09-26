class Solution {
    public String solution(String s) {
        String answer = "";
        String[] ssplit = s.toLowerCase().split("");
        boolean t = true;
        
        for(String sanswer : ssplit) {
            answer += t ? sanswer.toUpperCase() : sanswer;
            t = sanswer.equals(" ") ? true : false;
            
        }
        return answer;
    }
}