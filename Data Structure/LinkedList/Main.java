// import java.util.Scanner;

public class Main{
    public static void main(String[] args) throws EmptyListException {
        List b = new List();
        List l = new List();
        // Scanner input = new Scanner(System.in);
        int[] subject1 = new int[] {1,4,6,7,34};
        int[] subject2 = new int[] {1,4,6,7,34};

        for(int i=0; i<5; i++){
            // int item = input.nextInt();
            l.add(subject1[i]);
            b.add(subject2[i]);
        }
        System.out.println(l.equals(b));
        System.out.println(l.toString());

        // input.close();
    }
} 