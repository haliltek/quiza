final class StudyNote {
  const StudyNote({
    required this.id,
    required this.languageId,
    required this.categoryId,
    required this.categoryName,
    required this.subcategoryName,
    required this.noteType,
    required this.topicTitle,
    required this.content,
    required this.noteOrder,
    required this.isPremium,
    required this.isCompleted,
  });

  factory StudyNote.fromJson(Map<String, dynamic> json) {
    return StudyNote(
      id: json['id']?.toString() ?? '',
      languageId: json['language_id']?.toString() ?? '',
      categoryId: json['category_id']?.toString() ?? '',
      categoryName: json['category_name']?.toString() ?? '',
      subcategoryName: json['subcategory_name']?.toString() ?? '',
      noteType: json['note_type']?.toString() ?? 'spot',
      topicTitle: json['topic_title']?.toString() ?? '',
      content: json['content']?.toString() ?? '',
      noteOrder: int.tryParse(json['note_order']?.toString() ?? '0') ?? 0,
      isPremium: json['is_premium']?.toString() == '1',
      isCompleted: json['is_completed'] == 1 ||
          json['is_completed'] == '1' ||
          json['is_completed'] == true,
    );
  }

  final String id;
  final String languageId;
  final String categoryId;
  final String categoryName;
  final String subcategoryName;
  final String noteType;
  final String topicTitle;
  final String content;
  final int noteOrder;
  final bool isPremium;
  final bool isCompleted;

  StudyNote copyWith({
    bool? isCompleted,
  }) {
    return StudyNote(
      id: id,
      languageId: languageId,
      categoryId: categoryId,
      categoryName: categoryName,
      subcategoryName: subcategoryName,
      noteType: noteType,
      topicTitle: topicTitle,
      content: content,
      noteOrder: noteOrder,
      isPremium: isPremium,
      isCompleted: isCompleted ?? this.isCompleted,
    );
  }
}

final class StudyTopic {
  const StudyTopic({
    required this.topicTitle,
    required this.categoryId,
    required this.categoryName,
    required this.total,
    required this.completed,
    required this.items,
  });

  factory StudyTopic.fromJson(Map<String, dynamic> json) {
    return StudyTopic(
      topicTitle: json['topic_title']?.toString() ?? '',
      categoryId: json['category_id']?.toString() ?? '',
      categoryName: json['category_name']?.toString() ?? '',
      total: int.tryParse(json['total']?.toString() ?? '0') ?? 0,
      completed: int.tryParse(json['completed']?.toString() ?? '0') ?? 0,
      items: (json['items'] as List? ?? [])
          .map((item) => StudyNote.fromJson(item as Map<String, dynamic>))
          .toList(),
    );
  }

  final String topicTitle;
  final String categoryId;
  final String categoryName;
  final int total;
  final int completed;
  final List<StudyNote> items;

  StudyTopic copyWith({
    int? total,
    int? completed,
    List<StudyNote>? items,
  }) {
    return StudyTopic(
      topicTitle: topicTitle,
      categoryId: categoryId,
      categoryName: categoryName,
      total: total ?? this.total,
      completed: completed ?? this.completed,
      items: items ?? this.items,
    );
  }
}
