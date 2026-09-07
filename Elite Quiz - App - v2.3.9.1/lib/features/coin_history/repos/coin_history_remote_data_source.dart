import 'dart:convert';
import 'dart:io';

import 'package:flutterquiz/core/constants/api_exception.dart';
import 'package:flutterquiz/core/constants/constants.dart';
import 'package:flutterquiz/utils/api_utils.dart';
import 'package:flutterquiz/utils/crashlytics_utils.dart';
import 'package:http/http.dart' as http;

final class CoinHistoryRemoteDataSource {
  const CoinHistoryRemoteDataSource();

  Future<({int total, List<Map<String, dynamic>> data})> getCoinHistory({
    required String limit,
    required String offset,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{
        if (limit.isNotEmpty) limitKey: limit,
        if (offset.isNotEmpty) offsetKey: offset,
      };

      final response = await http.post(
        Uri.parse(getCoinHistoryUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getCoinHistoryUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }

      final total = int.parse(responseJson['total'] as String? ?? '0');
      final data = (responseJson['data'] as List).cast<Map<String, dynamic>>();

      return (total: total, data: data);
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: getCoinHistoryUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getCoinHistoryUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }
}
