import 'dart:convert';
import 'dart:io';

import 'package:flutterquiz/core/constants/api_exception.dart';
import 'package:flutterquiz/core/constants/constants.dart';
import 'package:flutterquiz/utils/api_utils.dart';
import 'package:flutterquiz/utils/crashlytics_utils.dart';
import 'package:http/http.dart' as http;

final class SystemConfigRemoteDataSource {
  Future<Map<String, dynamic>> getSystemConfig() async {
    try {
      final response = await http.post(Uri.parse(getSystemConfigUrl));
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getSystemConfigUrl,
          errorMessage: errorMessage,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }
      return responseJson['data'] as Map<String, dynamic>;
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: getSystemConfigUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getSystemConfigUrl,
        errorMessage: errorCodeDefaultMessage,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getSupportedQuestionLanguages() async {
    try {
      final response = await http.post(
        Uri.parse(getSupportedQuestionLanguageUrl),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getSupportedQuestionLanguageUrl,
          errorMessage: errorMessage,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }
      return (responseJson['data'] as List).cast<Map<String, dynamic>>();
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: getSupportedQuestionLanguageUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getSupportedQuestionLanguageUrl,
        errorMessage: errorCodeDefaultMessage,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getSupportedLanguageList() async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = {'from': '1'};
      final response = await http.post(
        Uri.parse(getSupportedLanguageListUrl),
        //from :: 1 - App, 2 - Web
        body: requestBody,
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getSupportedLanguageListUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }
      return (responseJson['data'] as List).cast<Map<String, dynamic>>();
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: getSupportedLanguageListUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getSupportedLanguageListUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<Map<String, dynamic>> getSystemLanguage(
    String name,
    String title,
  ) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = {
        'language': name,
        //from :: 1 - App, 2 - Web
        'from': '1',
      };

      final response = await http.post(
        Uri.parse(getSystemLanguageJson),
        body: requestBody,
      );

      if (response.statusCode != 200) {
        final errorMessage = response.reasonPhrase.toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getSystemLanguageJson,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }

      final jsonData = jsonDecode(response.body) as Map<String, dynamic>;

      if (jsonData['error'] as bool) {
        final errorMessage = jsonData['message'] as String;
        await CrashlyticsUtils.logApiException(
          endpoint: getSystemLanguageJson,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }

      final translations = (jsonData['data'] as Map<String, dynamic>).map(
        (k, v) => MapEntry(k, v.toString()),
      );

      return {
        'name': name,
        'title': title,
        'app_rtl_support': jsonData['rtl_support'] as String,
        'app_version': jsonData['version'] as String,
        'app_default': jsonData['default'] as String,
        'translations': translations,
      };
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: getSystemLanguageJson,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getSystemLanguageJson,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<String> getAppSettings(String type) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = {typeKey: type};
      final response = await http.post(
        Uri.parse(getAppSettingsUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getAppSettingsUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }
      return responseJson['data'].toString();
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: getAppSettingsUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getAppSettingsUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }
}
