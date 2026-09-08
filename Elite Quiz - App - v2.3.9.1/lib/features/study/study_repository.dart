import 'dart:convert';
import 'package:flutterquiz/core/constants/api_endpoints_constants.dart';
import 'package:flutterquiz/core/constants/api_exception.dart';
import 'package:flutterquiz/core/constants/error_message_keys.dart';
import 'package:flutterquiz/features/study/models/study_note.dart';
import 'package:flutterquiz/utils/api_utils.dart';
import 'package:http/http.dart' as http;

final class StudyRepository {
  Future<
      ({
        List<StudyTopic> topics,
        int totalCount,
        int completedCount,
        int progressPercent,
      })> getStudyNotes({
    required String languageId,
    required String noteType,
    String? categoryId,
  }) async {
    try {
      final body = <String, String>{
        'language_id': languageId,
        'note_type': noteType,
      };
      if (categoryId != null && categoryId.isNotEmpty && categoryId != '0') {
        body['category_id'] = categoryId;
      }

      final response = await http.post(
        Uri.parse(getStudyNotesUrl),
        body: body,
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;

      if (responseJson['error'] as bool) {
        throw ApiException(
          responseJson['message']?.toString() ?? errorCodeDefaultMessage,
        );
      }

      final totalCount =
          int.tryParse(responseJson['total_count']?.toString() ?? '0') ?? 0;
      final completedCount =
          int.tryParse(responseJson['completed_count']?.toString() ?? '0') ?? 0;
      final progressPercent =
          int.tryParse(responseJson['progress_percent']?.toString() ?? '0') ??
              0;

      final topicsList = (responseJson['topics'] as List? ?? [])
          .map((e) => StudyTopic.fromJson(e as Map<String, dynamic>))
          .toList();

      return (
        topics: topicsList,
        totalCount: totalCount,
        completedCount: completedCount,
        progressPercent: progressPercent,
      );
    } catch (e) {
      if (e is ApiException) rethrow;
      throw ApiException(e.toString());
    }
  }

  Future<bool> toggleNoteProgress(String noteId) async {
    try {
      final response = await http.post(
        Uri.parse(toggleStudyNoteProgressUrl),
        body: {'note_id': noteId},
        headers: await ApiUtils.getHeaders(),
      );

      final responseJson = jsonDecode(response.body) as Map<String, dynamic>;
      if (responseJson['error'] as bool) {
        throw ApiException(
          responseJson['message']?.toString() ?? errorCodeDefaultMessage,
        );
      }

      return responseJson['is_completed'] == 1 ||
          responseJson['is_completed'] == '1' ||
          responseJson['is_completed'] == true;
    } catch (e) {
      if (e is ApiException) rethrow;
      throw ApiException(e.toString());
    }
  }
}
