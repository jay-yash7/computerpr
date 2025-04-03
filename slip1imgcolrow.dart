
// flutter create my_project
// cd my_project
// lib/main.dart



import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: ImageGridScreen(),
    );
  }
}

class ImageGridScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Images in Row & Column")),
      body: Padding(
        padding: EdgeInsets.all(10),
        child: Column(
          children: [
            // Row of images
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Image.network(
                  'https://via.placeholder.com/100',
                  width: 100,
                  height: 100,
                ),
                Image.network(
                  'https://via.placeholder.com/100',
                  width: 100,
                  height: 100,
                ),
                Image.network(
                  'https://via.placeholder.com/100',
                  width: 100,
                  height: 100,
                ),
              ],
            ),
            SizedBox(height: 20),
            // Column of images
            Column(
              children: [
                Image.network(
                  'https://via.placeholder.com/100',
                  width: 100,
                  height: 100,
                ),
                SizedBox(height: 10),
                Image.network(
                  'https://via.placeholder.com/100',
                  width: 100,
                  height: 100,
                ),
                SizedBox(height: 10),
                Image.network(
                  'https://via.placeholder.com/100',
                  width: 100,
                  height: 100,
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
