import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  Color textColor = Colors.black;
  double textSize = 24.0;
  FontWeight textWeight = FontWeight.normal;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Text Styling')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              'Welcome',
              style: TextStyle(
                color: textColor,
                fontSize: textSize,
                fontWeight: textWeight,
              ),
            ),
            SizedBox(height: 20),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      textColor = Colors.red;
                    });
                  },
                  child: Text('Change Color'),
                ),
                SizedBox(width: 10),
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      textSize = textSize == 24.0 ? 32.0 : 24.0;
                    });
                  },
                  child: Text('Change Size'),
                ),
                SizedBox(width: 10),
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      textWeight = textWeight == FontWeight.normal ? FontWeight.bold : FontWeight.normal;
                    });
                  },
                  child: Text('Change Weight'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}