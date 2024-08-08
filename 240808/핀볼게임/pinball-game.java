import java.io.*;
import java.util.*;

public class Main {

    static int n;
    static int[][] arr;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int maxTime;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        
        arr = new int[n][n];

        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j=0; j<n; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int idx=0; idx<n; idx++) {
            maxTime = Math.max(maxTime, simulate(0, n, idx));
            maxTime = Math.max(maxTime, simulate(1, -1, idx));
            maxTime = Math.max(maxTime, simulate(2, idx, n));
            maxTime = Math.max(maxTime, simulate(3, idx, -1));
        }

        sb.append(maxTime);

        bw.write(sb.toString());
        bw.close();
        br.close();
    }

    private static int simulate(int direction, int x, int y) {
        int time = 0;

        while (true) {
            time++;
            int nx = x + dx[direction];
            int ny = y + dy[direction];

            if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                break;
            }

            if (arr[nx][ny] == 1) {
                direction = 4 - direction - 1;
            }

            if (arr[nx][ny] == 2) {
                direction = (2 + direction) % 4;
            }

            x = nx;
            y = ny;
        }

        return time;
    }
}