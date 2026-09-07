import 'dart:convert';
import 'dart:io';

import 'package:flutterquiz/core/constants/api_exception.dart';
import 'package:flutterquiz/core/constants/constants.dart';
import 'package:flutterquiz/utils/api_utils.dart';
import 'package:flutterquiz/utils/crashlytics_utils.dart';
import 'package:http/http.dart' as http;

final class WalletRemoteDataSource {
  const WalletRemoteDataSource();

  Future<void> makePaymentRequest({
    required String paymentType,
    required String paymentAddress,
    required String paymentAmount,
    required String coinUsed,
    required String details,
  }) async {
    Map<String, String>? requestBody;
    try {
      requestBody = <String, String>{
        paymentTypeKey: paymentType,
        paymentAddressKey: paymentAddress,
        paymentAmountKey: paymentAmount,
        coinUsedKey: coinUsed,
        detailsKey: details,
      };

      final response = await http.post(
        Uri.parse(makePaymentRequestUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: makePaymentRequestUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: makePaymentRequestUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: makePaymentRequestUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<({int total, List<Map<String, dynamic>> data})> getTransactions({
    required String limit,
    required String offset,
  }) async {
    Map<String, String>? requestBody;
    try {
      requestBody = <String, String>{limitKey: limit, offsetKey: offset};

      final response = await http.post(
        Uri.parse(getTransactionsUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'] == errorCodeDataNotFound
            ? errorCodeNoTransactions
            : responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getTransactionsUrl,
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
        endpoint: getTransactionsUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getTransactionsUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<bool> cancelPaymentRequest({required String paymentId}) async {
    Map<String, String>? requestBody;
    try {
      requestBody = <String, String>{paymentIdKey: paymentId};

      final response = await http.post(
        Uri.parse(cancelPaymentRequestUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: cancelPaymentRequestUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }

      return responseJson['message'] as String == errorCodeDataUpdateSuccess;
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: cancelPaymentRequestUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: cancelPaymentRequestUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }
}
