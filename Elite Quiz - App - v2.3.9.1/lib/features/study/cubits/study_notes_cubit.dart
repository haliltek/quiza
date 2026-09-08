import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutterquiz/features/study/models/study_note.dart';
import 'package:flutterquiz/features/study/study_repository.dart';

sealed class StudyNotesState {
  const StudyNotesState();
}

final class StudyNotesInitial extends StudyNotesState {
  const StudyNotesInitial();
}

final class StudyNotesLoading extends StudyNotesState {
  const StudyNotesLoading();
}

final class StudyNotesSuccess extends StudyNotesState {
  const StudyNotesSuccess({
    required this.topics,
    required this.totalCount,
    required this.completedCount,
    required this.progressPercent,
    required this.activeType,
  });

  final List<StudyTopic> topics;
  final int totalCount;
  final int completedCount;
  final int progressPercent;
  final String activeType;

  StudyNotesSuccess copyWith({
    List<StudyTopic>? topics,
    int? totalCount,
    int? completedCount,
    int? progressPercent,
    String? activeType,
  }) {
    return StudyNotesSuccess(
      topics: topics ?? this.topics,
      totalCount: totalCount ?? this.totalCount,
      completedCount: completedCount ?? this.completedCount,
      progressPercent: progressPercent ?? this.progressPercent,
      activeType: activeType ?? this.activeType,
    );
  }
}

final class StudyNotesFailure extends StudyNotesState {
  const StudyNotesFailure(this.errorMessage);
  final String errorMessage;
}

final class StudyNotesCubit extends Cubit<StudyNotesState> {
  StudyNotesCubit(this._studyRepository) : super(const StudyNotesInitial());

  final StudyRepository _studyRepository;

  Future<void> fetchNotes({
    required String languageId,
    required String noteType,
    String? categoryId,
  }) async {
    emit(const StudyNotesLoading());
    try {
      final res = await _studyRepository.getStudyNotes(
        languageId: languageId,
        noteType: noteType,
        categoryId: categoryId,
      );

      emit(
        StudyNotesSuccess(
          topics: res.topics,
          totalCount: res.totalCount,
          completedCount: res.completedCount,
          progressPercent: res.progressPercent,
          activeType: noteType,
        ),
      );
    } catch (e) {
      emit(StudyNotesFailure(e.toString()));
    }
  }

  Future<void> toggleNote(String noteId) async {
    final currentState = state;
    if (currentState is! StudyNotesSuccess) return;

    // Optimistically update local state
    final updatedTopics = <StudyTopic>[];
    var delta = 0;

    for (final topic in currentState.topics) {
      final updatedItems = <StudyNote>[];
      var topicCompleted = topic.completed;

      for (final item in topic.items) {
        if (item.id == noteId) {
          final newCompleted = !item.isCompleted;
          if (newCompleted) {
            delta++;
            topicCompleted++;
          } else {
            delta--;
            topicCompleted--;
          }
          updatedItems.add(item.copyWith(isCompleted: newCompleted));
        } else {
          updatedItems.add(item);
        }
      }

      updatedTopics.add(
        topic.copyWith(
          completed: topicCompleted < 0 ? 0 : topicCompleted,
          items: updatedItems,
        ),
      );
    }

    final newCompletedCount = (currentState.completedCount + delta).clamp(
      0,
      currentState.totalCount,
    );
    final newPercent = currentState.totalCount > 0
        ? ((newCompletedCount / currentState.totalCount) * 100).round()
        : 0;

    emit(
      currentState.copyWith(
        topics: updatedTopics,
        completedCount: newCompletedCount,
        progressPercent: newPercent,
      ),
    );

    try {
      await _studyRepository.toggleNoteProgress(noteId);
    } catch (_) {
      // If failed, rollback
      emit(currentState);
    }
  }
}
