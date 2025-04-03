import 'dart:io';

void main() {
  stdout.write("Enter Principal Amount: ");
  double principal = double.parse(stdin.readLineSync()!);

  stdout.write("Enter Time (in years): ");
  double time = double.parse(stdin.readLineSync()!);

  stdout.write("Enter Rate of Interest: ");
  double rate = double.parse(stdin.readLineSync()!);

  double simpleInterest = (principal * time * rate) / 100;

  print("Simple Interest: \$${simpleInterest.toStringAsFixed(2)}");
}
