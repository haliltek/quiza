import 'dart:convert';
import 'dart:developer';
import 'dart:io';

import 'package:flutterquiz/core/constants/api_exception.dart';
import 'package:flutterquiz/core/constants/constants.dart';
import 'package:flutterquiz/features/quiz/models/quiz_type.dart';
import 'package:flutterquiz/utils/api_utils.dart';
import 'package:flutterquiz/utils/crashlytics_utils.dart';
import 'package:http/http.dart' as http;

final class QuizRemoteDataSource {
  static late String profile;
  static late String score;
  static late String rank;

  Future<List<Map<String, dynamic>>> getQuestionsForDailyQuiz({
    required String timezone,
    required String gmt,
    String? languageId,
  }) async {
    Map<String, String>? requestBody;
    try {
      requestBody = <String, String>{
        languageIdKey: languageId!,
        timezoneKey: timezone,
        gmtFormatKey: gmt,
      };

      if (languageId.isEmpty) {
        requestBody.remove(languageIdKey);
      }

      final response = await http.post(
        Uri.parse(getQuestionForDailyQuizUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getQuestionForDailyQuizUrl,
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
        endpoint: getQuestionForDailyQuizUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getQuestionForDailyQuizUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getQuestionByType(
    String languageId,
  ) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{typeKey: '2', languageIdKey: languageId};
      if (languageId.isEmpty) {
        requestBody.remove(languageIdKey);
      }

      final response = await http.post(
        Uri.parse(getQuestionByTypeUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;
      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getQuestionByTypeUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(responseJson['message'].toString());
      }
      return (responseJson['data'] as List).cast<Map<String, dynamic>>();
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: getQuestionByTypeUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getQuestionByTypeUrl, // Same URL as above
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getQuestionContest(
    String contestId,
  ) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{contestIdKey: contestId};

      final response = await http.post(
        Uri.parse(getQuestionContestUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getQuestionContestUrl,
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
        endpoint: getQuestionContestUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getQuestionContestUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getGuessTheWordQuestions({
    required String languageId,
    required String type, //category or subcategory
    required String typeId,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{
        languageIdKey: languageId,
        typeKey: type,
        typeIdKey: typeId,
      };

      if (languageId.isEmpty) {
        requestBody.remove(languageIdKey);
      }

      final response = await http.post(
        Uri.parse(getGuessTheWordQuestionUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;
      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getGuessTheWordQuestionUrl,
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
        endpoint: getGuessTheWordQuestionUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getGuessTheWordQuestionUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getQuestionsForQuizZone({
    required String languageId,
    required String categoryId,
    required String subcategoryId,
    required String level,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{
        languageIdKey: languageId,
        categoryKey: categoryId,
        subCategoryKey: subcategoryId,
        levelKey: level,
      };
      if (languageId.isEmpty) {
        requestBody.remove(languageIdKey);
      }
      if (categoryId.isEmpty) {
        requestBody.remove(categoryKey);
      }
      if (subcategoryId.isEmpty) {
        requestBody.remove(subCategoryKey);
      }
      if (subcategoryId.isNotEmpty) {
        requestBody.remove(categoryKey);
      }

      final response = await http.post(
        Uri.parse(getQuestionsByLevelUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getQuestionsByLevelUrl,
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
        endpoint: getQuestionsByLevelUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getQuestionsByLevelUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getQuestionByCategoryOrSubcategory({
    required String type,
    required String id,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{typeKey: type, idKey: id};

      final response = await http.post(
        Uri.parse(getQuestionsByCategoryOrSubcategory),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getQuestionsByCategoryOrSubcategory,
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
        endpoint: getQuestionsByCategoryOrSubcategory,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getQuestionsByCategoryOrSubcategory,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getAudioQuestions({
    required String type,
    required String id,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{typeKey: type, typeIdKey: id};

      final response = await http.post(
        Uri.parse(getAudioQuestionUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getAudioQuestionUrl,
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
        endpoint: getAudioQuestionUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getAudioQuestionUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getLatexQuestions({
    required String type,
    required String id,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{typeKey: type, typeIdKey: id};

      final response = await http.post(
        Uri.parse(getLatexQuestionUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getLatexQuestionUrl,
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
        endpoint: getLatexQuestionUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getLatexQuestionUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getCategoryWithUser({
    required String languageId,
    required String type,
    String? subType,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      //body of post request
      requestBody = <String, String>{
        languageIdKey: languageId,
        typeKey: type,
        subTypeKey: subType ?? '',
      };

      if (languageId.isEmpty) {
        requestBody.remove(languageIdKey);
      }

      if (subType != null && subType.isEmpty) {
        requestBody.remove(subTypeKey);
      }

      final response = await http.post(
        Uri.parse(getCategoryUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getCategoryUrl,
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
        endpoint: getCategoryUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getCategoryUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getCategory({
    required String languageId,
    required String type,
    String? subType,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      //body of post request
      requestBody = <String, String>{
        languageIdKey: languageId,
        typeKey: type,
        subTypeKey: subType ?? '',
      };

      if (languageId.isEmpty) {
        requestBody.remove(languageIdKey);
      }

      if (subType != null && subType.isEmpty) {
        requestBody.remove(subTypeKey);
      }

      final response = await http.post(
        Uri.parse(getCategoryUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getCategoryUrl, // e.g., getQuestionByTypeUrl
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
        endpoint: getCategoryUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getCategoryUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getQuestionsForSelfChallenge({
    required String languageId,
    required String categoryId,
    required String subcategoryId,
    required String numberOfQuestions,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{
        languageIdKey: languageId,
        categoryKey: categoryId,
        subCategoryKey: subcategoryId,
        limitKey: numberOfQuestions,
      };

      if (languageId.isEmpty) {
        requestBody.remove(languageIdKey);
      }

      if (subcategoryId.isEmpty) {
        requestBody.remove(subCategoryKey);
      }

      if (categoryId.isEmpty) {
        requestBody.remove(categoryKey);
      }

      final response = await http.post(
        Uri.parse(getQuestionForSelfChallengeUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getQuestionForSelfChallengeUrl,
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
        endpoint: getQuestionForSelfChallengeUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getQuestionForSelfChallengeUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getSubCategory(String category) async {
    Map<String, dynamic>? requestBody;
    try {
      //body of post request
      requestBody = <String, String>{categoryKey: category};

      final response = await http.post(
        Uri.parse(getSubCategoryUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getSubCategoryUrl,
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
        endpoint: getSubCategoryUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getSubCategoryUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<int> getUnlockedLevel(
    String category,
    String subCategory, {
    required QuizTypes quizType,
  }) async {
    Map<String, dynamic>? requestBody;
    final url = quizType == QuizTypes.quizZone
        ? getLevelUrl
        : getMultiMatchLevelDataUrl;

    try {
      // assert that quizType can only be quizzone or multimatch
      assert(
        quizType == QuizTypes.quizZone || quizType == QuizTypes.multiMatch,
        'quizType can only be quizzone or multimatch',
      );

      //body of post request
      requestBody = <String, String>{
        categoryKey: category,
        subCategoryKey: subCategory,
      };

      if (subCategory.isEmpty) requestBody.remove(subCategoryKey);

      final response = await http.post(
        Uri.parse(url),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: url,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }

      final data = responseJson['data'] as Map<String, dynamic>;

      return int.parse(data['level'] as String? ?? '0');
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: url,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: url,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<Map<String, dynamic>> getContest({
    required String languageId,
    required String timezone,
    required String gmt,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      //body of post request
      requestBody = {
        languageIdKey: languageId,
        timezoneKey: timezone,
        gmtFormatKey: gmt,
      };

      final response = await http.post(
        Uri.parse(getContestUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body);

      return responseJson as Map<String, dynamic>;
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: getContestUrl, // Same URL as above
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getContestUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<({int total, List<Map<String, dynamic>> otherUsersRanks})>
  getContestLeaderboard({
    required String contestId,
    required int limit,
    int? offset,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = {
        contestIdKey: contestId,
        limitKey: limit.toString(),
        if (offset != null) offsetKey: offset.toString(),
      };

      final response = await http.post(
        Uri.parse(getContestLeaderboardUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      final total = int.parse(
        responseJson['total']?.toString() ?? '0',
      );
      final myRank = responseJson['my_rank'] as Map<String, dynamic>;

      rank = myRank['user_rank'].toString();
      profile = myRank[profileKey].toString();
      score = myRank['score'].toString();
      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getContestLeaderboardUrl,
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: response.body,
          statusCode: response.statusCode,
        );
        throw ApiException(errorMessage);
      }

      return (
        total: total,
        otherUsersRanks: (responseJson['data'] as List? ?? [])
            .cast<Map<String, dynamic>>(),
      );
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: getContestLeaderboardUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getContestLeaderboardUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getComprehension({
    required String languageId,
    required String type,
    required String typeId,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = {
        typeKey: type,
        typeIdKey: typeId,
        languageIdKey: languageId,
      };
      if (languageId.isEmpty) {
        requestBody.remove(languageIdKey);
      }
      final response = await http.post(
        Uri.parse(getFunAndLearnUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;
      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getFunAndLearnUrl,
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
        endpoint: getFunAndLearnUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getFunAndLearnUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<List<Map<String, dynamic>>> getComprehensionQuestion(
    String? funAndLearnId,
  ) async {
    Map<String, dynamic>? requestBody;
    try {
      //body of post request
      requestBody = {funAndLearnKey: funAndLearnId};
      final response = await http.post(
        Uri.parse(getFunAndLearnQuestionsUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;
      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: getFunAndLearnQuestionsUrl, // e.g., getQuestionByTypeUrl
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
        endpoint: getFunAndLearnQuestionsUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: getFunAndLearnQuestionsUrl,
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<void> unlockPremiumCategory({required String categoryId}) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = {categoryKey: categoryId};

      log('Body $requestBody', name: 'unlockPremiumCategory API');
      final rawRes = await http.post(
        Uri.parse(unlockPremiumCategoryUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );
      final jsonRes = jsonDecode(rawRes.body) as Map<String, dynamic>;
      if (jsonRes['error'] as bool) {
        final errorMessage = jsonRes['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: unlockPremiumCategoryUrl, // e.g., getQuestionByTypeUrl
          errorMessage: errorMessage,
          requestParams: requestBody,
          responseBody: rawRes.body,
          statusCode: rawRes.statusCode,
        );
        throw ApiException(errorMessage);
      }
    } on SocketException catch (e, stackTrace) {
      await CrashlyticsUtils.logNetworkError(
        endpoint: unlockPremiumCategoryUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: unlockPremiumCategoryUrl, // Same URL as above
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }

  Future<Map<String, dynamic>> setQuizCoinScore({
    required String quizType,
    required dynamic playedQuestions,
    String? categoryId,
    String? subcategoryId,
    List<String>? lifelines,
    String? roomId,
    bool? playWithBot,
    int? noOfHintUsed,
    String? matchId,
    int? joinedUsersCount,
  }) async {
    Map<String, dynamic>? requestBody;
    try {
      requestBody = <String, String>{
        if (categoryId != null && categoryId.isNotEmpty)
          categoryKey: categoryId,
        if (subcategoryId != null && subcategoryId.isNotEmpty)
          subCategoryKey: subcategoryId,
        'quiz_type': quizType,
        'play_questions': jsonEncode(playedQuestions),
        if (lifelines != null && lifelines.isNotEmpty)
          'lifeline': lifelines.join(','),
        'no_of_hint_used': ?noOfHintUsed?.toString(),
        if (roomId != null && roomId.isNotEmpty) 'match_id': roomId,
        if (playWithBot != null) 'is_bot': playWithBot ? '1' : '0',
        'match_id': ?matchId,
        'joined_users_count': ?joinedUsersCount?.toString(),
      };

      log('Body $requestBody', name: 'setQuizCoinScore API');
      final response = await http.post(
        Uri.parse(setQuizCoinScoreUrl),
        body: requestBody,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      log('Response $responseJson', name: 'setQuizCoinScore API');
      if (responseJson['error'] as bool) {
        final errorMessage = responseJson['message'].toString();
        await CrashlyticsUtils.logApiException(
          endpoint: setQuizCoinScoreUrl,
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
        endpoint: setQuizCoinScoreUrl,
        errorDetails: e.toString(),
      );
      await CrashlyticsUtils.logException(e, stackTrace);
      throw const ApiException(errorCodeNoInternet);
    } on ApiException {
      rethrow;
    } on Exception catch (e, stackTrace) {
      await CrashlyticsUtils.logApiException(
        endpoint: setQuizCoinScoreUrl, // Same URL as above
        errorMessage: errorCodeDefaultMessage,
        requestParams: requestBody,
        stackTrace: stackTrace,
      );
      throw const ApiException(errorCodeDefaultMessage);
    }
  }
}
