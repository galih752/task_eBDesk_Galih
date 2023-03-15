public class Main{
    public static void main(String []args) {
        Animal Chicken =new Animal();

        Chicken.setAnimal("Chicken", 4, 10);

        System.out.println(Chicken.getName());
        System.out.println(Chicken.getLegs());
        System.out.println(Chicken.getAge());

        int legs_chicken = Chicken.getLegs() - 2;
        System.out.println("Animal : "+Chicken.getName()+" Have "+ legs_chicken + " Legs");

        // Memanggil Function
        // System.out.println("Chicken berjalan " + walk("Kedepan"));
        // System.out.println("Chicken hewan dengan jenis pakan " + eat("Omnivora"));
    }

    //Function
    static String walk(String jalan){
        return jalan;
    }
    static String eat(String makan){
        return makan;
    }
}