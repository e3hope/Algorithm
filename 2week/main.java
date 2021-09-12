import java.io.*;

public class main {
    public static void main(String[] args) {
        System.out.println(question(1260));
    }
    public static int question(int request)
    {
        int n = 1260;
        int cnt = 0;
        int[] coinTypes = {500, 100, 50, 10};
        for (int i = 0; i < 4; i++) {
           cnt += n / coinTypes[i];
            n %= coinTypes[i];
        }
        return cnt;
    }
}
