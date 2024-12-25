package referanceAndObject;

public class Car extends Vichle{
    public int numberOfDoors(){
        return 5;
    }
    public void drive(){
        super.getNumberOfTires();
        System.out.println("Car is driving");
    }
    public void start(){
        System.out.println("Car is starting.....");

    }
}
