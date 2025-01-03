public class varArgs {
    public static void main(String[] args) {
        sum(4,234,45,6,654,37,4657,467,345);
    }
    public static int sum(int... a){
        int sum=0;
        for(int i :a){
            sum+=1;
        }
        return sum;
    }
}
