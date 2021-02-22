import 'dart:convert';
import 'package:http/http.dart' as http;

class User {
  String status;
  String message;

//  Constructor
  User({this.status, this.message});

//  Parsing ke Main dart
  factory User.dataAnalyze(Map<String, dynamic> object) {
    return User(
        status: object['status'].toString(),
        message: object['message']
    );
  }

  static Future<User> connectToAPI(String name, String base64Image) async {
    String url = 'http://192.168.1.5:8000';
//    Post ke server dan get json
    var apiResult = await http.post(url,
        body : {
          'files': base64Image,
          'file_name': name
        }
    );
    var jsonObject = json.decode(apiResult.body);
    var data = (jsonObject as Map<String, dynamic>);

    return User.dataAnalyze(data);
  }
}
