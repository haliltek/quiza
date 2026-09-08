import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutterquiz/core/core.dart';
import 'package:flutterquiz/features/quiz/cubits/contest_cubit.dart';
import 'package:flutterquiz/features/quiz/cubits/quiz_category_cubit.dart';
import 'package:flutterquiz/features/quiz/models/quiz_type.dart';
import 'package:flutterquiz/features/system_config/cubits/system_config_cubit.dart';
import 'package:flutterquiz/features/system_config/model/supported_question_language.dart';
import 'package:flutterquiz/ui/widgets/custom_rounded_button.dart';
import 'package:flutterquiz/utils/extensions.dart';
import 'package:flutterquiz/utils/ui_utils.dart';

Future<void> showQuizLanguageSelectorSheet(BuildContext context) async {
  return showModalBottomSheet<void>(
    context: context,
    isScrollControlled: true,
    shape: const RoundedRectangleBorder(
      borderRadius: UiUtils.bottomSheetTopRadius,
    ),
    builder: (_) => const _QuizLanguageSelectorWidget(),
  );
}

class _QuizLanguageSelectorWidget extends StatefulWidget {
  const _QuizLanguageSelectorWidget();

  @override
  State<_QuizLanguageSelectorWidget> createState() =>
      _QuizLanguageSelectorWidgetState();
}

class _QuizLanguageSelectorWidgetState
    extends State<_QuizLanguageSelectorWidget> {
  ExamTargetCategory _selectedFilter = ExamTargetCategory.all;

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
    final primary = Theme.of(context).primaryColor;

    return Padding(
      padding: const EdgeInsets.only(right: 6),
      child: InkWell(
        onTap: () {
          setState(() {
            _selectedFilter = category;
          });
        },
        borderRadius: BorderRadius.circular(16),
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 180),
          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
          decoration: BoxDecoration(
            color: isSelected
                ? primary
                : Theme.of(context).colorScheme.onTertiary.withValues(alpha: 0.05),
            borderRadius: BorderRadius.circular(16),
            border: Border.all(
              color: isSelected ? primary : Colors.transparent,
              width: 1,
            ),
          ),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(
                icon,
                size: 13,
                color: isSelected
                    ? Colors.white
                    : Theme.of(context).colorScheme.onTertiary,
              ),
              const SizedBox(width: 4),
              Text(
                label,
                style: TextStyle(
                  fontSize: 11,
                  fontWeight: isSelected ? FontWeight.w700 : FontWeight.w500,
                  color: isSelected
                      ? Colors.white
                      : Theme.of(context).colorScheme.onTertiary,
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
    final supportedLanguages =
        context.read<SystemConfigCubit>().supportedQuizLanguages;
    final filteredLanguages = _filterExams(supportedLanguages);
    final primary = Theme.of(context).primaryColor;

    return Container(
      decoration: BoxDecoration(
        color: Theme.of(context).scaffoldBackgroundColor,
        borderRadius: UiUtils.bottomSheetTopRadius,
      ),
      padding: EdgeInsets.only(
        top: context.height * .02,
        bottom: MediaQuery.of(context).viewInsets.bottom + 16,
      ),
      child: BlocConsumer<QuizLanguageCubit, QuizLanguageState>(
        listener: (context, state) {
          final currLanguageId = UiUtils.getCurrentQuizLanguageId(context);
          context.read<ContestCubit>().getContest(languageId: currLanguageId);
          context.read<QuizCategoryCubit>().getQuizCategory(
                languageId: currLanguageId,
                type: UiUtils.getCategoryTypeNumberFromQuizType(QuizTypes.quizZone),
              );
        },
        builder: (context, state) {
          final textStyle = TextStyle(
            fontWeight: FontWeight.bold,
            fontSize: 17,
            color: Theme.of(context).colorScheme.onTertiary,
          );

          var currLangId = state.languageId;

          return Padding(
            padding: EdgeInsets.symmetric(
              horizontal: context.width * UiUtils.hzMarginPct,
            ),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Container(
                  width: 36,
                  height: 4,
                  margin: const EdgeInsets.only(bottom: 10),
                  decoration: BoxDecoration(
                    color: Colors.grey.withValues(alpha: 0.4),
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
                Text('KPSS & Sınav Hedefinizi Değiştirin', style: textStyle),
                const SizedBox(height: 4),
                Text(
                  'Kategoriler ve sorular seçtiğiniz hedef kadroya göre filtrelenir',
                  style: TextStyle(
                    fontSize: 12,
                    color: context.primaryTextColor.withValues(alpha: 0.65),
                  ),
                ),
                const SizedBox(height: 10),

                // Category Filter Pills
                SingleChildScrollView(
                  scrollDirection: Axis.horizontal,
                  child: Row(
                    children: [
                      _buildFilterChip(
                        label: 'Tümü',
                        category: ExamTargetCategory.all,
                        icon: Icons.apps_rounded,
                      ),
                      _buildFilterChip(
                        label: 'B Grubu',
                        category: ExamTargetCategory.kpssEgitimDuzeyi,
                        icon: Icons.school_rounded,
                      ),
                      _buildFilterChip(
                        label: 'A Grubu',
                        category: ExamTargetCategory.kpssAGrubu,
                        icon: Icons.work_rounded,
                      ),
                      _buildFilterChip(
                        label: 'Özel Alan',
                        category: ExamTargetCategory.kpssOzelAlan,
                        icon: Icons.psychology_rounded,
                      ),
                      _buildFilterChip(
                        label: 'Diğer',
                        category: ExamTargetCategory.digerKamuveHukuk,
                        icon: Icons.gavel_rounded,
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 10),
                const Divider(),

                // List of filtered exams
                Container(
                  constraints: BoxConstraints(
                    minHeight: context.height * .25,
                    maxHeight: context.height * .52,
                  ),
                  child: filteredLanguages.isEmpty
                      ? Center(
                          child: Text(
                            'Bu filtrede sınav bulunamadı.',
                            style: TextStyle(
                              fontSize: 12,
                              color: context.primaryTextColor.withValues(alpha: 0.6),
                            ),
                          ),
                        )
                      : ListView.separated(
                          itemCount: filteredLanguages.length,
                          separatorBuilder: (_, __) => const SizedBox(height: 8),
                          itemBuilder: (_, i) {
                            final supportedLanguage = filteredLanguages[i];
                            final languageId = supportedLanguage.id;
                            final isSelected = currLangId == languageId;
                            final colorScheme = Theme.of(context).colorScheme;

                            return InkWell(
                              onTap: () {
                                currLangId = languageId;
                                if (state.languageId != languageId) {
                                  context.read<QuizLanguageCubit>().languageId =
                                      languageId;
                                }
                              },
                              borderRadius: BorderRadius.circular(14),
                              child: AnimatedContainer(
                                duration: const Duration(milliseconds: 180),
                                padding: const EdgeInsets.all(12),
                                decoration: BoxDecoration(
                                  color: isSelected
                                      ? primary.withValues(alpha: 0.1)
                                      : colorScheme.onTertiary
                                          .withValues(alpha: 0.04),
                                  border: Border.all(
                                    color: isSelected
                                        ? primary
                                        : Colors.transparent,
                                    width: 1.5,
                                  ),
                                  borderRadius: BorderRadius.circular(14),
                                ),
                                child: Row(
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Container(
                                      padding: const EdgeInsets.all(10),
                                      decoration: BoxDecoration(
                                        color: isSelected
                                            ? primary
                                            : colorScheme.onTertiary
                                                .withValues(alpha: 0.08),
                                        shape: BoxShape.circle,
                                      ),
                                      child: Icon(
                                        supportedLanguage.icon,
                                        color: isSelected
                                            ? Colors.white
                                            : colorScheme.onTertiary,
                                        size: 18,
                                      ),
                                    ),
                                    const SizedBox(width: 12),
                                    Expanded(
                                      child: Column(
                                        crossAxisAlignment:
                                            CrossAxisAlignment.start,
                                        children: [
                                          Row(
                                            children: [
                                              Expanded(
                                                child: Text(
                                                  supportedLanguage.language,
                                                  style: TextStyle(
                                                    fontSize: 14,
                                                    fontWeight: isSelected
                                                        ? FontWeight.bold
                                                        : FontWeight.w600,
                                                    color: isSelected
                                                        ? primary
                                                        : colorScheme.onTertiary,
                                                  ),
                                                ),
                                              ),
                                              if (isSelected)
                                                Icon(
                                                  Icons.check_circle_rounded,
                                                  color: primary,
                                                  size: 20,
                                                ),
                                            ],
                                          ),
                                          const SizedBox(height: 3),
                                          Container(
                                            padding: const EdgeInsets.symmetric(
                                              horizontal: 6,
                                              vertical: 2,
                                            ),
                                            decoration: BoxDecoration(
                                              color: isSelected
                                                  ? primary
                                                      .withValues(alpha: 0.15)
                                                  : colorScheme.onTertiary
                                                      .withValues(alpha: 0.06),
                                              borderRadius:
                                                  BorderRadius.circular(4),
                                            ),
                                            child: Text(
                                              supportedLanguage.shortBadge,
                                              style: TextStyle(
                                                fontSize: 9.5,
                                                fontWeight: FontWeight.bold,
                                                color: isSelected
                                                    ? primary
                                                    : colorScheme.onTertiary
                                                        .withValues(alpha: 0.7),
                                              ),
                                            ),
                                          ),
                                          const SizedBox(height: 4),
                                          Text(
                                            supportedLanguage.audienceDescription,
                                            style: TextStyle(
                                              fontSize: 11,
                                              height: 1.3,
                                              color: colorScheme.onTertiary
                                                  .withValues(alpha: 0.65),
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
                const SizedBox(height: 14),
                CustomRoundedButton(
                  onTap: Navigator.of(context).pop,
                  widthPercentage: 1,
                  backgroundColor: primary,
                  buttonTitle: context.tr('save') ?? 'Tamam',
                  radius: 12,
                  showBorder: false,
                  height: 46,
                ),
                const SizedBox(height: 6),
              ],
            ),
          );
        },
      ),
    );
  }
}

