import 'dart:convert';
import 'dart:developer';
import 'dart:io';

import 'package:flutterquiz/core/constants/api_exception.dart';
import 'package:flutterquiz/core/constants/constants.dart';
import 'package:flutterquiz/utils/api_utils.dart';
import 'package:flutterquiz/utils/crashlytics_utils.dart';
import 'package:http/http.dart' as http;

final class BookmarkRemoteDataSource {
  Future<List<Map<String, dynamic>>> getBookmark(String type) async {
    Map<String, dynamic>? requestBody;
    try {
      //type is 1 - Quiz zone 3- Guess the word 4 - Audio question
      requestBody = <String, String>{typeKey: type};

      final response = await http.post(
        Uri.parse(getBookmarkUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      log(name: 'Bookmarks', responseJson.toString());

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getBookmarkUrl,
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
        endpoint: getBookmarkUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getBookmarkUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<void> updateBookmark(
    String questionId,
    String status,
    String type,
  ) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = {
        statusKey: status,
        questionIdKey: questionId,
        typeKey: type, //1 - Quiz zone 3 - Guess the word 4 - Audio questions
      };
      final response = await http.post(
        Uri.parse(updateBookmarkUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      log(name: 'Update Bookmark', responseJson.toString());

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: updateBookmarkUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: updateBookmarkUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: updateBookmarkUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }
}
