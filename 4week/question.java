import java.util.Arrays;

public class question {
    public static void main(String[] args) {
        int[] array = { 6, 0, 8, 2, 3, 0, 4, 0, 1 };
        reorder(array);
        System.out.println(Arrays.toString(array));
    }
    public static void reorder(int[] array) {
        int j = 0;
        for (int item : array) {
            if (item != 0) {
                array[j] = item;
                j++; 
            }
        }
        for (int i = j; i < array.length; i++) {
            array[i] = 0;
        }
    }
}
