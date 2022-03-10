/*
   stak을 사용하는 문제
   0이 들어오면 pop, 그 외의 숫자들은 push를 시키고 남은 숫자들을 모두 더한다.
*/
import java.util.Scanner;
import java.util.Stack;

class Main {
    public static void main(String[] args) 
    {         
        Stack<Integer> s = new Stack<>(); //int형 스택 선언
        
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();

        int n;
        for (int i = 0; i < k; i++)
        {
            n = sc.nextInt();
            
            if (n == 0)
                s.pop();
            else
                s.push(n);
        }
        
        int answer = 0;
        while (!s.empty())
            answer += s.pop();
        
        System.out.println(answer);       
    } 
}
