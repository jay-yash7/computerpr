class Animal {
  int id;
  String name;
  String color;

  // Constructor for Animal class
  Animal(this.id, this.name, this.color);

  // Method to display Animal details
  void display() {
    print("ID: $id, Name: $name, Color: $color");
  }
}

class Cat extends Animal {
  String sound;

  // Constructor for Cat class, which calls the parent constructor
  Cat(int id, String name, String color, this.sound) : super(id, name, color);

  // Method to display Cat details
  void displayCatDetails() {
    display();  // Calling the display method from Animal class
    print("Sound: $sound");
  }
}

void main() {
  // Creating an object of Cat class
  Cat myCat = Cat(1, "Whiskers", "Gray", "Meow");

  // Printing details of the Cat object
  myCat.displayCatDetails();
}
