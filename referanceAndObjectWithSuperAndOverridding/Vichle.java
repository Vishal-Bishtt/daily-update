package referanceAndObject;

public abstract class Vichle {
    private int numberOfTires;
    Vichle(){
        this.numberOfTires=0;
    }
    Vichle(int numberOfTires){
        this.numberOfTires=numberOfTires;
    }
    public int getNumberOfTires() {
        return this.numberOfTires;
    }
    public void start(){
        System.out.println("Vichle is starting");
    }
}
