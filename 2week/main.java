import java.io.*;

public class main {
    public static void main(String[] args) {
        System.out.println("값을 입력하세요.동전개수와 금액");
        Scanner scan = new Scanner(System.in);
        int coin_count = scan.nextInt();
        int money = scan.nextInt();
        int[] coin = new int[coin_count];
        for( int i=0; i<coin_count; i++){
            coin[i] = scan.nextInt();
        }
        System.out.println(question(coin,coin_count,money));
    }
    public static int question(int[] coin,int coin_count,int money)
    {
        int count = 0;
        for (int i = coin_count -1; i >= 0; i--) {
            if(money>=coin[i]){
                count += money/coin[i];
                money = money%coin[i];
            }
        }
        return count;
    }
}
// https://github.com/e3hope/Algorithm