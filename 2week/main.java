import java.io.*;

public class main {
    public static void main(String[] args) {
        System.out.println("값을입력하세요");
        Scanner scan = new Scanner(System.in);
        int request = scan.nextInt();
        System.out.println(question(request));
    }
    public static int question(int request)
    {
        int count = 0;
        int[] coinTypes = {500, 100, 50, 10};
        for (int i = 0; i < 4; i++) {
            count += request / coinTypes[i];
            request %= coinTypes[i];
        }
        return count;
    }
}
// https://github.com/e3hope/Algorithm