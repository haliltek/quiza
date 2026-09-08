import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutterquiz/core/core.dart';
import 'package:flutterquiz/features/system_config/cubits/system_config_cubit.dart';
import 'package:flutterquiz/features/system_config/model/supported_question_language.dart';
import 'package:flutterquiz/ui/widgets/all.dart';
import 'package:flutterquiz/utils/extensions.dart';
import 'package:flutterquiz/utils/ui_utils.dart';


class InitialLanguageSelectionScreen extends StatefulWidget {
  const InitialLanguageSelectionScreen({super.key});

  @override
  State<InitialLanguageSelectionScreen> createState() =>
      _InitialLanguageSelectionScreenState();

  static Route<dynamic> route() => CupertinoPageRoute(
        builder: (_) => const InitialLanguageSelectionScreen(),
      );
}

class _InitialLanguageSelectionScreenState
    extends State<InitialLanguageSelectionScreen> {
  String _selectedExamId = '';
  ExamTargetCategory _selectedFilter = ExamTargetCategory.all;

  @override
  void initState() {
    super.initState();
    final supported = context.read<SystemConfigCubit>().supportedQuizLanguages;
    final currId = context.read<QuizLanguageCubit>().languageId;
    if (currId.isNotEmpty && supported.any((e) => e.id == currId)) {
      _selectedExamId = currId;
    } else if (supported.isNotEmpty) {
      _selectedExamId = supported.first.id;
    }
  }

  List<QuizLanguage> _filterExams(List<QuizLanguage> allExams) {
    if (_selectedFilter == ExamTargetCategory.all) {
      return allExams;
    }
    return allExams.where((e) => e.targetCategory == _selectedFilter).toList();
  }

  Widget _buildFilterChip({
    required String label,
    required ExamTargetCategory category,
    required IconData icon,
  }) {
    final isSelected = _selectedFilter == category;
    final primary = context.primaryColor;

    return Padding(
      padding: const EdgeInsets.only(right: 8),
      child: InkWell(
        onTap: () {
          setState(() {
            _selectedFilter = category;
          });
        },
        borderRadius: BorderRadius.circular(20),
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 200),
          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
          decoration: BoxDecoration(
            color: isSelected ? primary : context.surfaceColor,
            borderRadius: BorderRadius.circular(20),
            border: Border.all(
              color: isSelected
                  ? primary
                  : context.primaryTextColor.withValues(alpha: 0.15),
              width: 1.2,
            ),
            boxShadow: isSelected
                ? [
                    BoxShadow(
                      color: primary.withValues(alpha: 0.25),
                      blurRadius: 6,
                      offset: const Offset(0, 2),
                    ),
                  ]
                : null,
          ),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(
                icon,
                size: 15,
                color: isSelected ? Colors.white : context.primaryTextColor,
              ),
              const SizedBox(width: 6),
              Text(
                label,
                style: TextStyle(
                  fontSize: 12,
                  fontWeight: isSelected ? FontWeight.w700 : FontWeight.w500,
                  color: isSelected ? Colors.white : context.primaryTextColor,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final supportedExams =
        context.read<SystemConfigCubit>().supportedQuizLanguages;
    final filteredExams = _filterExams(supportedExams);
    final primary = context.primaryColor;

    return Scaffold(
      appBar: QAppBar(
        automaticallyImplyLeading: false,
        title: const Text('KPSS & Sınav Hedefiniz'),
        usePrimaryColor: true,
      ),
      body: SafeArea(
        child: Padding(
          padding: EdgeInsets.symmetric(
            vertical: context.height * 0.015,
            horizontal: context.width * UiUtils.hzMarginPct,
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Header Info Banner
              Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: primary.withValues(alpha: 0.07),
                  borderRadius: BorderRadius.circular(14),
                  border: Border.all(
                    color: primary.withValues(alpha: 0.18),
                  ),
                ),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Container(
                      padding: const EdgeInsets.all(8),
                      decoration: BoxDecoration(
                        color: primary.withValues(alpha: 0.12),
                        shape: BoxShape.circle,
                      ),
                      child: Icon(
                        Icons.verified_user_rounded,
                        color: primary,
                        size: 20,
                      ),
                    ),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            'Hazırlandığınız KPSS veya Kariyer Grubunu Seçin',
                            style: TextStyle(
                              fontSize: 13,
                              fontWeight: FontWeight.w700,
                              color: context.primaryTextColor,
                            ),
                          ),
                          const SizedBox(height: 3),
                          Text(
                            'Soru havuzu, mini denemeler ve düellolar seçtiğiniz sınav kadrosuna göre özelleştirilir.',
                            style: TextStyle(
                              fontSize: 11.5,
                              color: context.primaryTextColor.withValues(alpha: 0.75),
                              height: 1.35,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 14),

              // Filter category pills
              SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                child: Row(
                  children: [
                    _buildFilterChip(
                      label: 'Tüm Sınavlar',
                      category: ExamTargetCategory.all,
                      icon: Icons.apps_rounded,
                    ),
                    _buildFilterChip(
                      label: 'B Grubu (Lisans/Ön/Lise)',
                      category: ExamTargetCategory.kpssEgitimDuzeyi,
                      icon: Icons.school_rounded,
                    ),
                    _buildFilterChip(
                      label: 'A Grubu (Kariyer)',
                      category: ExamTargetCategory.kpssAGrubu,
                      icon: Icons.work_rounded,
                    ),
                    _buildFilterChip(
                      label: 'Özel Alan (ÖABT & DHBT)',
                      category: ExamTargetCategory.kpssOzelAlan,
                      icon: Icons.psychology_rounded,
                    ),
                    _buildFilterChip(
                      label: 'Diğer Kurumlar',
                      category: ExamTargetCategory.digerKamuveHukuk,
                      icon: Icons.gavel_rounded,
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 12),

              // Exam Cards List
              Expanded(
                child: filteredExams.isEmpty
                    ? Center(
                        child: Text(
                          'Bu kategoride sınav bulunamadı.',
                          style: TextStyle(
                            color: context.primaryTextColor.withValues(alpha: 0.6),
                          ),
                        ),
                      )
                    : ListView.separated(
                        itemCount: filteredExams.length,
                        separatorBuilder: (_, __) => const SizedBox(height: 10),
                        itemBuilder: (context, i) {
                          final exam = filteredExams[i];
                          final isSelected = _selectedExamId == exam.id;

                          return InkWell(
                            onTap: () {
                              setState(() {
                                _selectedExamId = exam.id;
                              });
                              context.read<QuizLanguageCubit>().languageId =
                                  exam.id;
                            },
                            borderRadius: BorderRadius.circular(16),
                            child: AnimatedContainer(
                              duration: const Duration(milliseconds: 200),
                              padding: const EdgeInsets.all(14),
                              decoration: BoxDecoration(
                                color: isSelected
                                    ? primary.withValues(alpha: 0.09)
                                    : context.surfaceColor,
                                border: Border.all(
                                  color: isSelected
                                      ? primary
                                      : context.primaryTextColor
                                          .withValues(alpha: 0.12),
                                  width: isSelected ? 2 : 1,
                                ),
                                borderRadius: BorderRadius.circular(16),
                                boxShadow: isSelected
                                    ? [
                                        BoxShadow(
                                          color: primary.withValues(alpha: 0.18),
                                          blurRadius: 10,
                                          offset: const Offset(0, 3),
                                        ),
                                      ]
                                    : null,
                              ),
                              child: Row(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  // Icon Badge
                                  Container(
                                    padding: const EdgeInsets.all(12),
                                    decoration: BoxDecoration(
                                      color: isSelected
                                          ? primary
                                          : context.primaryTextColor
                                              .withValues(alpha: 0.07),
                                      shape: BoxShape.circle,
                                    ),
                                    child: Icon(
                                      exam.icon,
                                      color: isSelected
                                          ? Colors.white
                                          : context.primaryTextColor
                                              .withValues(alpha: 0.8),
                                      size: 22,
                                    ),
                                  ),
                                  const SizedBox(width: 14),

                                  // Content
                                  Expanded(
                                    child: Column(
                                      crossAxisAlignment:
                                          CrossAxisAlignment.start,
                                      children: [
                                        Row(
                                          children: [
                                            Expanded(
                                              child: Text(
                                                exam.language,
                                                style: TextStyle(
                                                  fontSize: 15,
                                                  fontWeight: isSelected
                                                      ? FontWeight.w800
                                                      : FontWeight.w700,
                                                  color: isSelected
                                                      ? primary
                                                      : context
                                                          .primaryTextColor,
                                                ),
                                              ),
                                            ),
                                            if (isSelected)
                                              Container(
                                                padding:
                                                    const EdgeInsets.all(4),
                                                decoration: BoxDecoration(
                                                  color: primary,
                                                  shape: BoxShape.circle,
                                                ),
                                                child: const Icon(
                                                  Icons.check_rounded,
                                                  color: Colors.white,
                                                  size: 14,
                                                ),
                                              ),
                                          ],
                                        ),
                                        const SizedBox(height: 4),

                                        // Badge
                                        Container(
                                          padding: const EdgeInsets.symmetric(
                                            horizontal: 8,
                                            vertical: 3,
                                          ),
                                          decoration: BoxDecoration(
                                            color: isSelected
                                                ? primary.withValues(alpha: 0.15)
                                                : context.primaryTextColor
                                                    .withValues(alpha: 0.07),
                                            borderRadius:
                                                BorderRadius.circular(6),
                                          ),
                                          child: Text(
                                            exam.shortBadge,
                                            style: TextStyle(
                                              fontSize: 10,
                                              fontWeight: FontWeight.w700,
                                              letterSpacing: 0.4,
                                              color: isSelected
                                                  ? primary
                                                  : context.primaryTextColor
                                                      .withValues(alpha: 0.7),
                                            ),
                                          ),
                                        ),
                                        const SizedBox(height: 6),

                                        // Audience Description
                                        Text(
                                          exam.audienceDescription,
                                          style: TextStyle(
                                            fontSize: 12,
                                            height: 1.35,
                                            color: context.primaryTextColor
                                                .withValues(alpha: 0.7),
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          );
                        },
                      ),
              ),
              const SizedBox(height: 12),

              // Bottom CTA Button
              CustomRoundedButton(
                onTap: () {
                  if (_selectedExamId.isNotEmpty) {
                    context.read<QuizLanguageCubit>().languageId =
                        _selectedExamId;
                  }
                  Navigator.of(context)
                      .pushReplacementNamed(Routes.introSlider);
                },
                widthPercentage: 1,
                backgroundColor: primary,
                buttonTitle: 'Hedefi Belirle ve Başla',
                radius: 14,
                showBorder: false,
                height: 50,
              ),
            ],
          ),
        ),
      ),
    );
  }
}

