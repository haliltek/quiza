import 'dart:math' as math;

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutterquiz/core/core.dart';
import 'package:flutterquiz/features/profile_management/cubits/user_details_cubit.dart';
import 'package:flutterquiz/features/study/cubits/study_notes_cubit.dart';
import 'package:flutterquiz/features/study/models/study_note.dart';
import 'package:flutterquiz/features/study/study_repository.dart';
import 'package:flutterquiz/ui/widgets/circular_progress_container.dart';
import 'package:flutterquiz/ui/widgets/custom_back_button.dart';
import 'package:flutterquiz/ui/widgets/error_container.dart';
import 'package:flutterquiz/utils/ui_utils.dart';
import 'package:google_fonts/google_fonts.dart';

class StudyHubScreen extends StatefulWidget {
  const StudyHubScreen({super.key});

  static Route<dynamic> route() {
    return CupertinoPageRoute(
      builder: (_) => BlocProvider(
        create: (_) => StudyNotesCubit(StudyRepository()),
        child: const StudyHubScreen(),
      ),
    );
  }

  @override
  State<StudyHubScreen> createState() => _StudyHubScreenState();
}

class _StudyHubScreenState extends State<StudyHubScreen>
    with SingleTickerProviderStateMixin {
  String _activeType = 'flashcard'; // 'flashcard', 'spot', 'formula', 'summary'
  int _currentFlashcardIndex = 0;
  bool _isFlipped = false;

  late AnimationController _flipController;
  late Animation<double> _flipAnimation;

  @override
  void initState() {
    super.initState();
    _flipController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 400),
    );
    _flipAnimation = Tween<double>(begin: 0, end: 1).animate(
      CurvedAnimation(parent: _flipController, curve: Curves.easeInOut),
    );

    WidgetsBinding.instance.addPostFrameCallback((_) {
      _loadNotes();
    });
  }

  @override
  void dispose() {
    _flipController.dispose();
    super.dispose();
  }

  void _loadNotes() {
    final langId = UiUtils.getCurrentQuizLanguageId(context);
    context.read<StudyNotesCubit>().fetchNotes(
          languageId: langId.isNotEmpty ? langId : '52',
          noteType: _activeType,
        );
    setState(() {
      _currentFlashcardIndex = 0;
      _isFlipped = false;
      _flipController.reset();
    });
  }

  void _switchType(String type) {
    if (_activeType == type) return;
    setState(() {
      _activeType = type;
    });
    _loadNotes();
  }

  void _flipCard() {
    HapticFeedback.lightImpact();
    if (_isFlipped) {
      _flipController.reverse();
    } else {
      _flipController.forward();
    }
    setState(() {
      _isFlipped = !_isFlipped;
    });
  }

  @override
  Widget build(BuildContext context) {
    final primaryColor = context.primaryColor;
    final primaryTextColor = context.primaryTextColor;
    final userCoins =
        context.watch<UserDetailsCubit>().getUserProfile().coins ?? '0';

    return Scaffold(
      backgroundColor: Theme.of(context).scaffoldBackgroundColor,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: const Padding(
          padding: EdgeInsets.all(8),
          child: CustomBackButton(),
        ),
        title: Text(
          'KPSS Çalışma & Tekrar Odası',
          style: GoogleFonts.nunito(
            textStyle: TextStyle(
              color: primaryTextColor,
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
        centerTitle: true,
        actions: [
          Container(
            margin: const EdgeInsetsDirectional.only(end: 16),
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
            decoration: BoxDecoration(
              color: primaryColor.withValues(alpha: 0.1),
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: primaryColor.withValues(alpha: 0.2)),
            ),
            child: Row(
              children: [
                const Icon(Icons.monetization_on,
                    color: Colors.amber, size: 16),
                const SizedBox(width: 4),
                Text(
                  userCoins,
                  style: TextStyle(
                    color: primaryTextColor,
                    fontWeight: FontWeight.bold,
                    fontSize: 13,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
      body: Column(
        children: [
          _buildSegmentSelector(),
          Expanded(
            child: BlocBuilder<StudyNotesCubit, StudyNotesState>(
              builder: (context, state) {
                if (state is StudyNotesLoading || state is StudyNotesInitial) {
                  return const Center(child: CircularProgressContainer());
                }
                if (state is StudyNotesFailure) {
                  return Center(
                    child: ErrorContainer(
                      showBackButton: false,
                      errorMessage: state.errorMessage,
                      onTapRetry: _loadNotes,
                      showErrorImage: true,
                    ),
                  );
                }

                final success = state as StudyNotesSuccess;
                if (success.topics.isEmpty) {
                  return Center(
                    child: Text(
                      'Bu alanda henüz içerik bulunmuyor.',
                      style: TextStyle(color: primaryTextColor.withValues(alpha: 0.6)),
                    ),
                  );
                }

                if (_activeType == 'flashcard') {
                  return _buildFlashcardView(success);
                } else {
                  return _buildListView(success);
                }
              },
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSegmentSelector() {
    final segments = <({String key, IconData icon, String title})>[
      (key: 'flashcard', icon: Icons.flip_to_front, title: 'Bilgi Kartı'),
      (key: 'spot', icon: Icons.bolt, title: 'Hap Bilgi'),
      (key: 'formula', icon: Icons.functions, title: 'Formüller'),
      (key: 'summary', icon: Icons.menu_book, title: 'Özetler'),
    ];

    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      padding: const EdgeInsets.all(4),
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.surface,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: Colors.black12),
      ),
      child: Row(
        children: segments.map((s) {
          final isSelected = _activeType == s.key;
          return Expanded(
            child: GestureDetector(
              onTap: () => _switchType(s.key),
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 250),
                padding: const EdgeInsets.symmetric(vertical: 8),
                decoration: BoxDecoration(
                  color: isSelected ? context.primaryColor : Colors.transparent,
                  borderRadius: BorderRadius.circular(10),
                  boxShadow: isSelected
                      ? [
                          BoxShadow(
                            color: context.primaryColor.withValues(alpha: 0.3),
                            blurRadius: 6,
                            offset: const Offset(0, 2),
                          ),
                        ]
                      : null,
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(
                      s.icon,
                      size: 15,
                      color: isSelected ? Colors.white : context.primaryTextColor.withValues(alpha: 0.6),
                    ),
                    const SizedBox(width: 4),
                    Text(
                      s.title,
                      style: TextStyle(
                        color: isSelected ? Colors.white : context.primaryTextColor.withValues(alpha: 0.7),
                        fontSize: 12,
                        fontWeight: isSelected ? FontWeight.bold : FontWeight.w500,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          );
        }).toList(),
      ),
    );
  }

  Widget _buildProgressCard(StudyNotesSuccess success) {
    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [
            context.primaryColor.withValues(alpha: 0.85),
            context.primaryColor,
          ],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: context.primaryColor.withValues(alpha: 0.25),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                'İlerleme Durumu',
                style: GoogleFonts.nunito(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 14,
                ),
              ),
              Text(
                '%${success.progressPercent} (${success.completedCount}/${success.totalCount})',
                style: const TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 13,
                ),
              ),
            ],
          ),
          const SizedBox(height: 8),
          ClipRRect(
            borderRadius: BorderRadius.circular(6),
            child: LinearProgressIndicator(
              value: success.totalCount > 0 ? (success.completedCount / success.totalCount) : 0,
              backgroundColor: Colors.white24,
              valueColor: const AlwaysStoppedAnimation<Color>(Colors.amberAccent),
              minHeight: 7,
            ),
          ),
        ],
      ),
    );
  }

  // --- FLASHCARD / KARTI ÇEVİR GÖRÜNÜMÜ ---
  Widget _buildFlashcardView(StudyNotesSuccess success) {
    // Flatten all items across topics
    final allCards = <StudyNote>[];
    for (final topic in success.topics) {
      allCards.addAll(topic.items);
    }

    if (allCards.isEmpty) return const SizedBox();
    if (_currentFlashcardIndex >= allCards.length) {
      _currentFlashcardIndex = 0;
    }

    final card = allCards[_currentFlashcardIndex];

    return SingleChildScrollView(
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 16),
        child: Column(
          children: [
            _buildProgressCard(success),
            const SizedBox(height: 8),
            // Header stats
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                GestureDetector(
                  onTap: () {
                    HapticFeedback.lightImpact();
                    context.read<StudyNotesCubit>().toggleNote(card.id);
                  },
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                    decoration: BoxDecoration(
                      color: card.isCompleted ? Colors.green.withValues(alpha: 0.15) : Colors.black12,
                      borderRadius: BorderRadius.circular(20),
                      border: Border.all(
                        color: card.isCompleted ? Colors.green : Colors.transparent,
                      ),
                    ),
                    child: Row(
                      children: [
                        Icon(
                          card.isCompleted ? Icons.check_circle : Icons.radio_button_unchecked,
                          size: 16,
                          color: card.isCompleted ? Colors.green : Colors.black45,
                        ),
                        const SizedBox(width: 6),
                        Text(
                          card.isCompleted ? 'Öğrenildi' : 'Öğrendim Olarak İşaretle',
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.bold,
                            color: card.isCompleted ? Colors.green : Colors.black54,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
                Text(
                  'Kart ${_currentFlashcardIndex + 1}/${allCards.length}',
                  style: GoogleFonts.nunito(
                    fontSize: 13,
                    fontWeight: FontWeight.bold,
                    color: context.primaryTextColor.withValues(alpha: 0.6),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),
            // Flip card container
            GestureDetector(
              onTap: _flipCard,
              child: AnimatedBuilder(
                animation: _flipAnimation,
                builder: (context, child) {
                  final angle = _flipAnimation.value * math.pi;
                  final isUnder = angle > (math.pi / 2);

                  return Transform(
                    transform: Matrix4.identity()
                      ..setEntry(3, 2, 0.001)
                      ..rotateY(angle),
                    alignment: Alignment.center,
                    child: isUnder
                        ? Transform(
                            transform: Matrix4.identity()..rotateY(math.pi),
                            alignment: Alignment.center,
                            child: _buildCardBack(card),
                          )
                        : _buildCardFront(card),
                  );
                },
              ),
            ),
            const SizedBox(height: 24),
            // Bottom Action Navigation
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ElevatedButton.icon(
                  onPressed: _currentFlashcardIndex > 0
                      ? () {
                          if (_isFlipped) _flipCard();
                          setState(() => _currentFlashcardIndex--);
                        }
                      : null,
                  icon: const Icon(Icons.arrow_back, size: 16),
                  label: const Text('Önceki'),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: context.primaryColor.withValues(alpha: 0.1),
                    foregroundColor: context.primaryColor,
                    elevation: 0,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                    padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 12),
                  ),
                ),
                GestureDetector(
                  onTap: _flipCard,
                  child: Container(
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      color: Colors.amber,
                      shape: BoxShape.circle,
                      boxShadow: [
                        BoxShadow(
                          color: Colors.amber.withValues(alpha: 0.4),
                          blurRadius: 10,
                          offset: const Offset(0, 3),
                        ),
                      ],
                    ),
                    child: const Icon(Icons.lightbulb_rounded, color: Colors.white, size: 28),
                  ),
                ),
                ElevatedButton.icon(
                  onPressed: _currentFlashcardIndex < allCards.length - 1
                      ? () {
                          if (_isFlipped) _flipCard();
                          setState(() => _currentFlashcardIndex++);
                        }
                      : null,
                  icon: const Icon(Icons.arrow_forward, size: 16),
                  label: const Text('Sonraki'),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: context.primaryColor,
                    foregroundColor: Colors.white,
                    elevation: 2,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                    padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 12),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 20),
          ],
        ),
      ),
    );
  }

  Widget _buildCardFront(StudyNote card) {
    return Container(
      width: double.infinity,
      constraints: const BoxConstraints(minHeight: 280),
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: context.primaryColor,
        borderRadius: BorderRadius.circular(22),
        boxShadow: [
          BoxShadow(
            color: context.primaryColor.withValues(alpha: 0.3),
            blurRadius: 16,
            offset: const Offset(0, 8),
          ),
        ],
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
            decoration: BoxDecoration(
              color: Colors.white24,
              borderRadius: BorderRadius.circular(12),
            ),
            child: Text(
              card.categoryName.isNotEmpty ? card.categoryName : 'KPSS Soru Kartı',
              style: const TextStyle(color: Colors.white70, fontSize: 12, fontWeight: FontWeight.bold),
            ),
          ),
          const SizedBox(height: 28),
          Text(
            card.topicTitle,
            textAlign: TextAlign.center,
            style: GoogleFonts.nunito(
              color: Colors.white,
              fontSize: 20,
              fontWeight: FontWeight.bold,
              height: 1.4,
            ),
          ),
          const SizedBox(height: 28),
          const Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.touch_app, color: Colors.white70, size: 16),
              SizedBox(width: 6),
              Text(
                'Cevabı görmek için dokun',
                style: TextStyle(color: Colors.white70, fontSize: 12),
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildCardBack(StudyNote card) {
    return Container(
      width: double.infinity,
      constraints: const BoxConstraints(minHeight: 280),
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.surface,
        borderRadius: BorderRadius.circular(22),
        border: Border.all(color: context.primaryColor.withValues(alpha: 0.4), width: 1.5),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.08),
            blurRadius: 16,
            offset: const Offset(0, 8),
          ),
        ],
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(Icons.check_circle, color: Colors.green, size: 18),
              const SizedBox(width: 6),
              Text(
                'CEVAP & AÇIKLAMA',
                style: GoogleFonts.nunito(
                  color: Colors.green,
                  fontSize: 13,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
          const SizedBox(height: 20),
          Text(
            card.content,
            textAlign: TextAlign.center,
            style: GoogleFonts.nunito(
              color: context.primaryTextColor,
              fontSize: 16,
              fontWeight: FontWeight.w600,
              height: 1.45,
            ),
          ),
          const SizedBox(height: 24),
          const Text(
            'Tekrar çevirmek için dokun',
            style: TextStyle(color: Colors.black38, fontSize: 11),
          ),
        ],
      ),
    );
  }

  // --- HAP BİLGİ, FORMÜL VE ÖZET LİSTE GÖRÜNÜMÜ ---
  Widget _buildListView(StudyNotesSuccess success) {
    return ListView(
      padding: const EdgeInsets.only(bottom: 30),
      children: [
        _buildProgressCard(success),
        ...success.topics.map(_buildTopicAccordion),
      ],
    );
  }

  Widget _buildTopicAccordion(StudyTopic topic) {
    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.surface,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.black.withValues(alpha: 0.07)),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.02),
            blurRadius: 6,
            offset: const Offset(0, 2),
          ),
        ],
      ),
      child: Theme(
        data: Theme.of(context).copyWith(dividerColor: Colors.transparent),
        child: ExpansionTile(
          initiallyExpanded: true,
          tilePadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
          title: Text(
            topic.topicTitle,
            style: GoogleFonts.nunito(
              color: context.primaryTextColor,
              fontSize: 15,
              fontWeight: FontWeight.bold,
            ),
          ),
          subtitle: Padding(
            padding: const EdgeInsets.only(top: 4),
            child: Row(
              children: [
                Expanded(
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(4),
                    child: LinearProgressIndicator(
                      value: topic.total > 0 ? (topic.completed / topic.total) : 0,
                      backgroundColor: Colors.black12,
                      valueColor: AlwaysStoppedAnimation<Color>(context.primaryColor),
                      minHeight: 4,
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                Text(
                  '${topic.completed}/${topic.total}',
                  style: TextStyle(
                    fontSize: 11,
                    fontWeight: FontWeight.bold,
                    color: context.primaryTextColor.withValues(alpha: 0.6),
                  ),
                ),
              ],
            ),
          ),
          children: topic.items.map(_buildItemTile).toList(),
        ),
      ),
    );
  }

  Widget _buildItemTile(StudyNote item) {
    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: item.isCompleted
            ? Colors.green.withValues(alpha: 0.05)
            : Theme.of(context).scaffoldBackgroundColor,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(
          color: item.isCompleted ? Colors.green.withValues(alpha: 0.25) : Colors.black.withValues(alpha: 0.05),
        ),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            child: Text(
              item.content,
              style: GoogleFonts.nunito(
                fontSize: 14,
                height: 1.4,
                color: context.primaryTextColor.withValues(alpha: item.isCompleted ? 0.8 : 0.95),
                fontWeight: item.isCompleted ? FontWeight.w500 : FontWeight.w600,
              ),
            ),
          ),
          const SizedBox(width: 10),
          GestureDetector(
            onTap: () {
              HapticFeedback.lightImpact();
              context.read<StudyNotesCubit>().toggleNote(item.id);
            },
            child: AnimatedContainer(
              duration: const Duration(milliseconds: 200),
              width: 32,
              height: 32,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: item.isCompleted ? Colors.green : Colors.transparent,
                border: Border.all(
                  color: item.isCompleted ? Colors.green : Colors.black26,
                  width: 2,
                ),
              ),
              child: item.isCompleted
                  ? const Icon(Icons.check, color: Colors.white, size: 18)
                  : null,
            ),
          ),
        ],
      ),
    );
  }
}
