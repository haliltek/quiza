import 'dart:convert';
import 'dart:io';

import 'package:flutterquiz/core/constants/api_exception.dart';
import 'package:flutterquiz/core/constants/constants.dart';
import 'package:flutterquiz/features/quiz/models/quiz_type.dart';
import 'package:flutterquiz/utils/api_utils.dart';
import 'package:flutterquiz/utils/crashlytics_utils.dart';
import 'package:http/http.dart' as http;

final class ReportQuestionRemoteDataSource {
  Future<void> reportQuestion({
    required QuizTypes quizType,
    required String questionId,
    required String message,
  }) async {
    Map<String, String>? requestBody;
    String? endpoint;
    try {
      requestBody = <String, String>{
        questionIdKey: questionId,
        messageKey: message,
      };

      endpoint = quizType == QuizTypes.multiMatch
          ? multiMatchReportQuestionUrl
          : reportQuestionUrl;

      final response = await http.post(
        Uri.parse(endpoint),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: endpoint,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: endpoint ?? 'reportQuestion',
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: endpoint ?? 'reportQuestion',
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }
}
