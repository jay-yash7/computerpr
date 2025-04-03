class Student {
  int _sno;
  String _name;
  String _class;
  double _per;

  Student(this._sno, this._name, this._class, this._per);

  // Getters and Setters
  int get sno => _sno;
  set sno(int sno) => _sno = sno;

  String get name => _name;
  set name(String name) => _name = name;

  String get className => _class;
  set className(String className) => _class = className;

  double get per => _per;
  set per(double per) => _per = per;

  void display() {
    print("S.No: $_sno, Name: $_name, Class: $_class, Percentage: $_per%");
  }
}

void main() {
  var student = Student(1, "John", "10th", 85.5);
  student.display();

  // Update details using setters
  student.name = "Alice";
  student.per = 90.0;
  student.display();
}
