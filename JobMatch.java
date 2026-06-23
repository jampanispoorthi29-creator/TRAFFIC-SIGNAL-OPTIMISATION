
import java.util.Scanner;

class Job {
    String title;
    int requiredSkill;
    int requiredExperience;
    int mismatchCost;

    Job(String title, int requiredSkill, int requiredExperience) {
        this.title = title;
        this.requiredSkill = requiredSkill;
        this.requiredExperience = requiredExperience;
        this.mismatchCost = 0;
    }
}

public class JobMatch {

    public static void merge(Job[] jobs, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        Job[] L = new Job[n1];
        Job[] R = new Job[n2];

        for (int i = 0; i < n1; i++)
            L[i] = jobs[left + i];

        for (int j = 0; j < n2; j++)
            R[j] = jobs[mid + 1 + j];

        int i = 0, j = 0, k = left;

        while (i < n1 && j < n2) {
            if (L[i].mismatchCost <= R[j].mismatchCost) {
                jobs[k] = L[i];
                i++;
            } else {
                jobs[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            jobs[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            jobs[k] = R[j];
            j++;
            k++;
        }
    }

    public static void mergeSort(Job[] jobs, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;

            mergeSort(jobs, left, mid);
            mergeSort(jobs, mid + 1, right);

            merge(jobs, left, mid, right);
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        Job[] jobs = {
            new Job("Software Developer", 8, 2),
            new Job("Data Analyst", 7, 1),
            new Job("Web Developer", 6, 1),
            new Job("System Engineer", 9, 3),
            new Job("Database Administrator", 8, 4)
        };

        System.out.println("=== Job Match System ===");

        System.out.print("Enter Candidate Skill Level (1-10): ");
        int candidateSkill = sc.nextInt();

        System.out.print("Enter Candidate Experience (Years): ");
        int candidateExperience = sc.nextInt();

        for (Job job : jobs) {
            job.mismatchCost =
                Math.abs(job.requiredSkill - candidateSkill)
                + Math.abs(job.requiredExperience - candidateExperience);
        }

        mergeSort(jobs, 0, jobs.length - 1);

        System.out.println("\nRanked Job Recommendations:");
        System.out.println("--------------------------------");

        for (int i = 0; i < jobs.length; i++) {
            System.out.println((i + 1) + ". " +
                    jobs[i].title +
                    " (Mismatch Cost = " +
                    jobs[i].mismatchCost + ")");
        }

        System.out.println("\nBest Job Match: " + jobs[0].title);

        sc.close();
    }
}