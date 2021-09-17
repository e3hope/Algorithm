import java.util.*;

public class ATM {
    public static void main(String[] args) {
        System.out.println("개수를 입력하세요");
        Scanner sc = new Scanner(System.in);
        System.out.println("숫자를 입력하세요");
        int count = sc.nextInt();
        int[] num = new int[count];
        int temp,result = 0;
        if ( count == 1 )
        {
            result = 1;
        }
        else
        {
            for ( int i = 0 ; i < count ; i++ ){
                num[i] = sc.nextInt();
                for ( int j = 0 ; j < i ; j++ ){
                    if ( num[i] < num[j] ){
                        temp = num[j];
                        num[j] = num[i];
                        num[i] = temp;
                    }
                }
            }
            for ( int i = 0 ; i < count ; i++ ){
                result += num[i] * (count - i);
            }
        }
        System.out.println(result);
    }
}
