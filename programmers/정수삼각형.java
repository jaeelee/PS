/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   정수삼각형.java                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/03/27 04:04:39 by jaeelee           #+#    #+#             */
/*   Updated: 2022/03/27 04:04:39 by jaeelee          ###   ########seoul.kr  */
/*                                                                            */
/* ************************************************************************** */


'''
bottom_up 방식의 동적계획법(DP) 활용
'''
class Solution {
    public int solution(int[][] triangle) {
        int right_num = 0;
        int left_num = 0;
        
        for (int i = triangle.length - 2; i >= 0; i--)
        {
            for (int j = 0; j < triangle[i].length; j++)
            {
                left_num = triangle[i][j] + triangle[i+1][j];
                right_num = triangle[i][j] + triangle[i+1][j+1];
                if (left_num > right_num)
                    triangle[i][j] = left_num;
                else
                    triangle[i][j] = right_num;
            }
        }
        
        return triangle[0][0];
    }
}