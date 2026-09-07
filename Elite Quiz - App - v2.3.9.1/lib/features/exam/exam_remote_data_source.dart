import 'dart:convert';
import 'dart:io';

import 'package:flutterquiz/core/constants/api_exception.dart';
import 'package:flutterquiz/core/constants/constants.dart';
import 'package:flutterquiz/utils/api_utils.dart';
import 'package:flutterquiz/utils/crashlytics_utils.dart';
import 'package:http/http.dart' as http;

final class ExamRemoteDataSource {
  Future<({int total, List<Map<String, dynamic>> data})> getExams({
    required String languageId,
    required String type,
    required String limit,
    required String offset,
    required String timezone,
    required String gmt,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = {
        languageIdKey: languageId,
        typeKey: type, // 1 for today , 2 for completed
        limitKey: limit,
        offsetKey: offset,
        timezoneKey: timezone,
        gmtFormatKey: gmt,
      };

      if (languageId.isEmpty) {
        requestBody.remove(languageIdKey);
      }
      if (limit.isEmpty) {
        requestBody.remove(limitKey);
      }

      if (offset.isEmpty) {
        requestBody.remove(offsetKey);
      }

      final response = await http.post(
        Uri.parse(getExamModuleUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString() == errorCodeDataNotFound
              ? type == '1'
                    ? errorCodeNoExamForToday
                    : errorCodeHaveNotCompletedExam
              : responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getExamModuleUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }

      return (
        total: int.parse(responseJson['total'] as String? ?? '0'),
        data: (responseJson['data'] as List).cast<Map<String, dynamic>>(),
      );
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: getExamModuleUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getExamModuleUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getQuestionForExam({
    required String examId,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{examModuleIdKey: examId};

      final response = await http.post(
        Uri.parse(getExamModuleQuestionsUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getExamModuleQuestionsUrl,
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
        endpoint: getExamModuleQuestionsUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getExamModuleQuestionsUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<void> updateExamStatusToInExam({required String examModuleId}) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{examModuleIdKey: examModuleId};

      final response = await http.post(
        Uri.parse(setExamModuleResultUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString() == errorCodeFillAllData
              ? errorCodeAlreadyInExam
              : responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: setExamModuleResultUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: setExamModuleResultUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: setExamModuleResultUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<void> submitExamResult({
    required String examModuleId,
    required String totalDuration,
    required List<Map<String, dynamic>> statistics,
    required String obtainedMarks,
    required bool rulesViolated,
    required List<String> capturedQuestionIds,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{
        examModuleIdKey: examModuleId,
        statisticsKey: json.encode(statistics),
        totalDurationKey: totalDuration,
        obtainedMarksKey: obtainedMarks,
        rulesViolatedKey: rulesViolated ? '1' : '0',
        capturedQuestionIdsKey: json.encode(capturedQuestionIds),
      };

      final response = await http.post(
        Uri.parse(setExamModuleResultUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: setExamModuleResultUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: setExamModuleResultUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: setExamModuleResultUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }
}
