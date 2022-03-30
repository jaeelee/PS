/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   징검다리.java                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/30 18:29:31 by jaeelee           #+#    #+#             */
/*   Updated: 2022/03/30 18:34:29 by jaeelee          ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */


// 참고1 : https://countrysides.tistory.com/72
// 참고2 : https://sonyak-ku.tistory.com/10

// 핵심 : mid를 "거리의 최소값"으로 생각하고 징검다리를 순차적으로 최대 n개까지 제거해보며 모두 간격이 mid보다 넓은지 확인하는 것
import java.util.Arrays;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        
        // 바위 순서대로 정렬
        Arrays.sort(rocks);

        int right = distance;
        int left = 0;
        int mid = 0;
        int cnt = 999;
        while(left <= right)
        {
            boolean[] remove_rocks = new boolean[rocks.length];
            
            mid = (left + right) / 2;
            // 돌과 다음 돌까지의 거리 구하기
            int start = 0;
            for (int i = 0; i < rocks.length; i++)
            {            
                if (rocks[i] - start < mid)
                    remove_rocks[i] = true;
                else
                    start = rocks[i];
            }

            //파괴한 돌 개수 구하기
            cnt = 0;
            for (int i = 0; i < rocks.length; i++)
                if (remove_rocks[i] == true)
                    cnt++;
            
            if (cnt <= n) // 파괴한 바위가 적거나 같은 경우
            {
                left = mid + 1;
                answer = mid;
            }
            else // 파괴한 바뒤가 많은 경우
                right = mid - 1;
        }
        
        return answer;
        }
}