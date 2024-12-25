package referanceAndObject;

public class TestTransportation {
    public static void main(String[] args) {
        Car car = new Car();
        Plane plane = new Plane();
      //  Vichle wan = new Car();
       // Car swift = new Vichle(); Cannot do downcasting like that
        //Car c = (Car)new Vichle();
        //castTest(vichle);
        //castTest(car);
        car.start();
        plane.start();

    }
    private static void castTest(Vichle v){
        v.start();
        Car c = (Car)v;
    }
}
