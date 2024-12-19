package referanceAndObject;

public class overloading {
    public int sum(int a , int b){
        return a+b;
    }
    public int sum(int a , int b , int c){
        return a+b+c;         // you can use same name for function if the number of argument differ
    }

    public static void main(String[] args) {
        overloading obj = new overloading();
        System.out.println(obj.sum(10, 20));
        System.out.println(obj.sum(10, 20, 30));
    }
}
