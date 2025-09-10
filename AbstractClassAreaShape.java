abstract class Area {
    public abstract void areas();  // abstract method, must be implemented in subclass

    void area() {
        System.out.println("The shape of the area");
    }
}

class Shape extends Area {
    // Implement abstract method from Area
    public void areas() {
        System.out.println("Calculating areas of different shapes");
    }

    public void areaofrectangle(int a, int b) {
        int A = a * b;
        System.out.println("Area of the rectangle is " + A);
    }

    public void areaofsquare(int a) {
        int A = a * a;  // fixed the formula to calculate area of square
        System.out.println("Area of the square is " + A);
    }
}

public class AbstractClassAreaShape {
    public static void main(String[] args) {
        Shape obj = new Shape();
        obj.areas();  // calling the implemented abstract method
        obj.areaofrectangle(3, 7);
        obj.areaofsquare(4);
    }
}

