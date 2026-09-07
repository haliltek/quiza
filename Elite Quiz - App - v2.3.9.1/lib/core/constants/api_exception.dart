final class ApiException implements Exception {
  const ApiException(
    this.error, {
    this.errorCode,
    this.apiEndpoint,
    this.requestParams,
    this.responseBody,
    this.statusCode,
  });

  final String error;
  final String? errorCode;
  final String? apiEndpoint;
  final Map<String, dynamic>? requestParams;
  final String? responseBody;
  final int? statusCode;

  @override
  String toString() => error;

  /// Returns a detailed error message for logging purposes
  String toDetailedString() {
    final buffer = StringBuffer('API Exception: $error');
    if (errorCode != null) buffer.write('\nError Code: $errorCode');
    if (apiEndpoint != null) buffer.write('\nEndpoint: $apiEndpoint');
    if (statusCode != null) buffer.write('\nStatus Code: $statusCode');
    if (requestParams != null) {
      buffer.write('\nRequest Params: $requestParams');
    }
    if (responseBody != null) buffer.write('\nResponse: $responseBody');
    return buffer.toString();
  }
}
