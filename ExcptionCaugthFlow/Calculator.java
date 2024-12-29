package tryAndCatch;

import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        a();
    }
    private static void a(){
        b();
    }
    private static void b(){
        c();
    }
    private static void c(){
        d();
    }
    private static void d(){
        Scanner input = new Scanner(System.in);
        System.out.println("Welcome to devision calculator");
        System.out.print("Please enter your two number: ");
        int first = input.nextInt();
        int second = input.nextInt();
        try {
            int[] a= new int[5];
            System.out.printf("Result is d%",a[6]);
            int result = first / second;
            System.out.println("Your result is: " +a[6]);
        } catch(ArithmeticException exception){
            System.out.printf("%s, enter valid values", exception.getMessage());
        }
    }
}
