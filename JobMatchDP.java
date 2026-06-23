import java.util.Scanner;

public class JobMatchDP {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of jobs: ");
        int n = sc.nextInt();

        int[] score = new int[n];
        int[] skillReq = new int[n];

        System.out.println("Enter matching scores for jobs:");
        for (int i = 0; i < n; i++) {
            score[i] = sc.nextInt();
        }

        System.out.println("Enter skill requirements for jobs:");
        for (int i = 0; i < n; i++) {
            skillReq[i] = sc.nextInt();
        }

        System.out.print("Enter candidate skill capacity: ");
        int capacity = sc.nextInt();

        int[][] dp = new int[n + 1][capacity + 1];

        for (int i = 1; i <= n; i++) {
            for (int w = 1; w <= capacity; w++) {

                if (skillReq[i - 1] <= w) {
                    dp[i][w] = Math.max(
                            score[i - 1] + dp[i - 1][w - skillReq[i - 1]],
                            dp[i - 1][w]);
                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        System.out.println("\nMaximum Job Match Score = " + dp[n][capacity]);

        System.out.println("\nSelected Jobs:");

        int w = capacity;

        for (int i = n; i > 0 && w > 0; i--) {
            if (dp[i][w] != dp[i - 1][w]) {
                System.out.println("Job " + i + " Selected");
                w -= skillReq[i - 1];
            }
        }

        sc.close();
    }
}