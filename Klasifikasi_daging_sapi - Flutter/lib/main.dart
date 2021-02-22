// Flutter code sample for Scaffold

// This example shows a [Scaffold] with an [AppBar], a [BottomAppBar] and a
// [FloatingActionButton]. The [body] is a [Text] placed in a [Center] in order
// to center the text within the [Scaffold]. The [FloatingActionButton] is
// centered and docked within the [BottomAppBar] using
// [FloatingActionButtonLocation.centerDocked]. The [FloatingActionButton] is
// connected to a callback that increments a counter.
//
// ![](https://flutter.github.io/assets-for-api-docs/assets/material/scaffold_bottom_app_bar.png)

import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'dart:io';
import 'package:image_picker/image_picker.dart';
import 'package:klasifikasidagingsapi/api-json.dart';
//import 'package:cobaflutter/post_api.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  File _image;
  String imageName;
  String base64Image;
  User user = null;

  OpenCamera() async {
    _image = await ImagePicker.pickImage(source: ImageSource.camera);
    base64Image = base64Encode(_image.readAsBytesSync());
    imageName = _image.path.split('/').last;
//    uploadImage();
    setState(() {});
  }

  OpenGallery() async {
    _image = await ImagePicker.pickImage(source: ImageSource.gallery);
    base64Image = base64Encode(_image.readAsBytesSync());
    imageName = _image.path.split('/').last;
// //    uploadImage();

    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
          backgroundColor: Colors.white,
          body: Stack(
            children: <Widget>[
              Container(
                child: _image == null
                    ? Container(
//                        height: 500,
                        width: double.infinity,
                        color: Color(0xffF4F9FA),
                        padding: EdgeInsets.only(top: 220),
                        child: Column(
                          children: <Widget>[
                            Icon(
                              Icons.wallpaper,
                              color: Color(0xff00DCA7),
                              size: 100.0,
                            ),
                            Container(
                              padding: EdgeInsets.only(top: 20),
                              child: Text(
                                "Beef Classification Apps",
                                style: TextStyle(
                                  fontSize: 20,
                                  color: Color(0xff00DCA7),
                                ),
                              ),
                            )
                          ],
                        ))
                    : Image.file(
                        _image, fit: BoxFit.fitWidth
                      ),
              ),
              Container(
                width: double.infinity,
//                transform: Matrix4.translationValues(0.0, -45, 0.0),
                margin: EdgeInsets.only(top: 550),
                decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.only(
                      topLeft: Radius.circular(40),
                      topRight: Radius.circular(40),
                    ),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.grey.withOpacity(0.3),
                        spreadRadius: 0,
                        blurRadius: 10,
                        offset: Offset(0, -15), // changes position of shadow
                      ),
                    ]),
                child: Center(
                  child: Column(
//                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      Container(
                          padding: EdgeInsets.only(top: 30, bottom: 30),
                          child: _image == null
                              ? Container()
                              : Container(
                                  padding: EdgeInsets.only(bottom: 20),
                                  child: user != null
                                      ? Text(
                                          user.message,
                                          style: TextStyle(
                                            fontSize: 25,
                                            color: Color(0xff00DCA7),
                                          ),
                                        )
                                      : Container(
                                          width: 300,
                                          height: 50,
                                          child: RaisedButton(
                                            onPressed: () {
                                              User.connectToAPI(
                                                      imageName, base64Image)
                                                  .then((value) {
                                                user = value;
                                                setState(() {});
                                              });
                                            },
                                            child: Text(
                                              "Analyze",
                                              style: TextStyle(
                                                  color: Colors.white),
                                            ),
                                            color: Color(0xff00DCA7),
                                            shape: RoundedRectangleBorder(
                                              borderRadius:
                                                  BorderRadius.circular(50.0),
                                            ),
                                          ),
                                        ),
                                )),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: <Widget>[
                          Column(
                            children: <Widget>[
                              Container(
                                height: 70,
                                child: RaisedButton(
                                  onPressed: OpenCamera,
                                  child: Icon(
                                    Icons.camera_alt,
                                    color: Colors.white,
//                              size: 100.0,
                                  ),
                                  color: Color(0xff00DCA7),
                                  shape: CircleBorder(),
                                ),
                                padding: EdgeInsets.only(bottom: 10),
                              ),
                              Text("Camera")
                            ],
                          ),
                          Column(
                            children: <Widget>[
                              Container(
                                height: 70,
                                child: RaisedButton(
                                  onPressed: OpenGallery,
                                  child: Icon(
                                    Icons.collections,
                                    color: Colors.white,
//                              size: 100.0,
                                  ),
                                  color: Color(0xff00DCA7),
                                  shape: CircleBorder(),
                                ),
                                padding: EdgeInsets.only(
                                    bottom: 10, left: 30, right: 30),
                              ),
                              Text("Gallery")
                            ],
                          ),
                          Column(
                            children: <Widget>[
                              Container(
                                height: 70,
                                child: RaisedButton(
                                  onPressed: () {
                                    _image = null;
                                    user = null;
                                    setState(() {});
                                  },
                                  child: Icon(
                                    Icons.clear,
                                    color: Colors.white,
//                              size: 100.0,
                                  ),
                                  color: Color(0xff00DCA7),
                                  shape: CircleBorder(),
                                ),
                                padding: EdgeInsets.only(bottom: 10),
                              ),
                              Text("Clear")
                            ],
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
            ],
          )),
    );
  }
}
