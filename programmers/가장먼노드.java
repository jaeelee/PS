import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int[] dist = new int[n+1];
        
        // 간선정보 입력받기
        ArrayList<Integer>[] node = new ArrayList[n+1]; // 간선 정보 저장
        for (int i = 1; i <= n; i++) {
            node[i] = new ArrayList<>();
        }
        
        // 간선 정보 입력
        for (int i = 0; i < edge.length; i++){
            node[edge[i][0]].add(edge[i][1]);
            node[edge[i][1]].add(edge[i][0]);
        }
        
        Queue<Integer> q = new LinkedList<>();  // BFS를 위한 큐
        Arrays.fill(dist, -1);

        q.add(1);
        dist[1] = 0;
        
        while(!q.isEmpty())
        {
            int cur = q.poll();
            
            for (int next : node[cur])
            {
                if (dist[next] == -1){
                    dist[next] = dist[cur] + 1;
                    q.add(next);
                }
                
            }
        }
        
        List<Integer> intList = new ArrayList<>();
        for (int element : dist) {
            intList.add(element);
        }

        int max = Collections.max(intList);
        
        return Collections.frequency(intList, max);

    }
}
