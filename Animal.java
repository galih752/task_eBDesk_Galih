public class Animal {
    private String name="";
    private int legs=0;
    private int age=0;

    public Animal(){
    }

    //setter
    public void setAnimal (String nm, int lgs, int ag){
        name = nm;
        legs = lgs;
        age = ag;
    }

    //getter
    public String getName(){
        return name;
    }
    public int getLegs(){
        return legs;
    }
    public int getAge(){
        return age;
    }

}

class Chicken extends Animal {

    private String name="";
    private int legs=0;
    private int age=0;
}