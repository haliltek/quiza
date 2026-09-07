import 'package:firebase_crashlytics/firebase_crashlytics.dart';
import 'package:flutterquiz/core/constants/api_exception.dart';

/// Utility class for logging exceptions and errors to Firebase Crashlytics
class CrashlyticsUtils {
  /// Logs an API exception with detailed context to Firebase Crashlytics
  static Future<void> logApiException({
    required String endpoint,
    required String errorMessage,
    String? errorCode,
    Map<String, dynamic>? requestParams,
    String? responseBody,
    int? statusCode,
    StackTrace? stackTrace,
  }) async {
    try {
      // Create detailed error message
      final buffer = StringBuffer('API Exception\n')
        ..write('Endpoint: $endpoint\n')
        ..write('Error: $errorMessage\n');
      if (errorCode != null) buffer.write('Error Code: $errorCode\n');
      if (statusCode != null) buffer.write('Status Code: $statusCode\n');

      // Log to Crashlytics
      final crashlytics = FirebaseCrashlytics.instance;
      await crashlytics.log(buffer.toString());

      // Set custom keys for better filtering in Firebase Console
      await crashlytics.setCustomKey('api_endpoint', endpoint);
      if (errorCode != null) {
        await crashlytics.setCustomKey('error_code', errorCode);
      }
      if (statusCode != null) {
        await crashlytics.setCustomKey('status_code', statusCode);
      }

      // Record the error with stack trace
      await crashlytics.recordError(
        ApiException(
          errorMessage,
          errorCode: errorCode,
          apiEndpoint: endpoint,
          requestParams: requestParams,
          responseBody: responseBody,
          statusCode: statusCode,
        ),
        stackTrace ?? StackTrace.current,
        reason: 'API Exception: $endpoint',
      );
    } on Exception {
      // Silently fail if Crashlytics logging fails
      // We don't want to break the app if logging fails
    }
  }

  /// Logs a generic exception to Firebase Crashlytics
  static Future<void> logException(
    dynamic exception,
    StackTrace stackTrace, {
    String? reason,
  }) async {
    try {
      await FirebaseCrashlytics.instance.recordError(
        exception,
        stackTrace,
        reason: reason,
      );
    } on Exception {
      // Silently fail
    }
  }

  /// Logs a network connectivity error
  static Future<void> logNetworkError({
    required String endpoint,
    String? errorDetails,
  }) async {
    try {
      final crashlytics = FirebaseCrashlytics.instance;
      await crashlytics.log(
        'Network Error - Endpoint: $endpoint, Details: ${errorDetails ?? "No internet connection"}',
      );
      await crashlytics.setCustomKey('network_error', true);
      await crashlytics.setCustomKey('api_endpoint', endpoint);
    } on Exception {
      // Silently fail
    }
  }
}
