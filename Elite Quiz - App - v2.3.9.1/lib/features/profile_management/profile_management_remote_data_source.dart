import 'dart:convert';
import 'dart:io';

import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutterquiz/core/constants/api_exception.dart';
import 'package:flutterquiz/core/constants/constants.dart';
import 'package:flutterquiz/utils/api_utils.dart';
import 'package:flutterquiz/utils/crashlytics_utils.dart';
import 'package:http/http.dart' as http;

final class ProfileManagementRemoteDataSource {
  Future<Map<String, dynamic>> getUserDetailsById() async {
    Map<String, dynamic>? requestBody;
    try {
      final response = await http.post(
        Uri.parse(getUserDetailsByIdUrl),
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getUserDetailsByIdUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }
      return responseJson['data'] as Map<String, dynamic>;
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: getUserDetailsByIdUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getUserDetailsByIdUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<Map<String, dynamic>> addProfileImage(File? images) async {
    try {
      final fileList = <String, File?>{imageKey: images};
      final response = await postApiFile(Uri.parse(uploadProfileUrl), fileList);
      final res = json.decode(response) as Map<String, dynamic>;
      if (res['error'] as bool) {
        throw ApiException(res['message'].toString());
      }

      return res['data'] as Map<String, dynamic>;
    } on SocketException {
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception {
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<String> postApiFile(Uri url, Map<String, File?> fileList) async {
    try {
      final request = http.MultipartRequest('POST', url);
      request.headers.addAll(await ApiUtils.getHeaders());

      for (final key in fileList.keys.toList()) {
        final pic = await http.MultipartFile.fromPath(key, fileList[key]!.path);
        request.files.add(pic);
      }
      final res = await request.send();
      final responseData = await res.stream.toBytes();
      final response = String.fromCharCodes(responseData);
      if (res.statusCode == 200) {
        return response;
      } else {
        throw const ApiException(errorCodeDefaultMessage);
      }
    } on SocketException {
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception {
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<Map<String, dynamic>> updateCoins({
    required String coins,
    required String title,
    String? type, //dashing_debut, clash_winner
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{
        coinsKey: coins,
        titleKey: title,
        typeKey: type ?? '',
      };
      if (requestBody[typeKey].toString().isEmpty) {
        requestBody.remove(typeKey);
      }

      final response = await http.post(
        Uri.parse(updateUserCoinsAndScoreUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: updateUserCoinsAndScoreUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }
      return responseJson['data'] as Map<String, dynamic>;
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: updateUserCoinsAndScoreUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: updateUserCoinsAndScoreUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<void> removeAdsForUser({required bool status}) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{removeAdsKey: status ? '1' : '0'};

      final rawRes = await http.post(
        Uri.parse(updateProfileUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final resJson = jsonDecode(rawRes.body) as Map<String, dynamic>;
      if (resJson['error'] as bool) {
        final errorMessage = resJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: updateProfileUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: rawRes.body,
          statusCode: rawRes.statusCode,
        );
        throw ApiException(errorMessage);
      }
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: updateProfileUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: updateProfileUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<void> updateLanguage(String languageName) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = {'app_language': languageName};

      var token = <String, String>{};

      try {
        token = await ApiUtils.getHeaders();
      } on Exception catch (_) {}

      if (token.isEmpty) {
        return;
      }

      final rawRes = await http.post(
        Uri.parse(updateProfileUrl),
        body: requestBody,
        headers: token,
      );

      final resJson = jsonDecode(rawRes.body) as Map<String, dynamic>;
      if (resJson['error'] as bool) {
        final errorMessage = resJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: updateProfileUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: rawRes.body,
          statusCode: rawRes.statusCode,
        );
        throw ApiException(errorMessage);
      }
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: updateProfileUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: updateProfileUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<void> updateProfile({
    required String email,
    required String name,
    required String mobile,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{
        emailKey: email,
        nameKey: name,
        mobileKey: mobile,
      };

      final response = await http.post(
        Uri.parse(updateProfileUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;
      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: updateProfileUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: updateProfileUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: updateProfileUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<void> deleteAccount() async {
    try {
      await FirebaseAuth.instance.currentUser?.reload();
      await FirebaseAuth.instance.currentUser?.delete();

      final response = await http.post(
        Uri.parse(deleteUserAccountUrl),
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: deleteUserAccountUrl,
          errorMessage: errorMessage,
          requestParams: {},
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: deleteUserAccountUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on FirebaseAuthException catch (e) {
      throw ApiException(firebaseErrorCodeToNumber(e.code));
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: deleteUserAccountUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: {},
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<bool> watchedDailyAd() async {
    try {
      final rawRes = await http.post(
        Uri.parse(watchedDailyAdUrl),
        headers: await ApiUtils.getHeaders(),
      );

      final jsonRes = jsonDecode(rawRes.body) as Map<String, dynamic>;

      if (jsonRes['error'] as bool) {
        final errorMessage = jsonRes['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: watchedDailyAdUrl,
          errorMessage: errorMessage,
          requestParams: {},
          responseBody: rawRes.body,
          statusCode: rawRes.statusCode,
        );
        throw ApiException(errorMessage);
      }

      return jsonRes['message'] == errorCodeDataUpdateSuccess;
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: watchedDailyAdUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on FirebaseAuthException catch (e) {
      throw ApiException(firebaseErrorCodeToNumber(e.code));
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: watchedDailyAdUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: {},
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }
}
