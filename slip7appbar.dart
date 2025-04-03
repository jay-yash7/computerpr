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

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('My AppBar'),
        backgroundColor: Colors.blue,
        actions: [
          IconButton(
            icon: Icon(Icons.search),
            onPressed: () {
              print('Search clicked');
            },
          ),
          IconButton(
            icon: Icon(Icons.more_vert),
            onPressed: () {
              print('Menu clicked');
            },
          ),
        ],
      ),
      body: Center(
        child: Text('Hello, Flutter!'),
      ),
    );
  }
}