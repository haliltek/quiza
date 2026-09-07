import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutterquiz/core/core.dart';
import 'package:flutterquiz/features/quiz/cubits/contest_cubit.dart';
import 'package:flutterquiz/features/quiz/cubits/quiz_category_cubit.dart';
import 'package:flutterquiz/features/quiz/models/quiz_type.dart';
import 'package:flutterquiz/features/system_config/cubits/system_config_cubit.dart';
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

class _QuizLanguageSelectorWidget extends StatelessWidget {
  const _QuizLanguageSelectorWidget();

  IconData _getExamIcon(String name) {
    final lower = name.toLowerCase();
    if (lower.contains('hakim') || lower.contains('savci') || lower.contains('hmgs')) {
      return Icons.gavel_rounded;
    }
    if (lower.contains('icra') || lower.contains('hukuk')) {
      return Icons.balance_rounded;
    }
    if (lower.contains('kaymakam') || lower.contains('idare')) {
      return Icons.account_balance_rounded;
    }
    if (lower.contains('polis') || lower.contains('paem') || lower.contains('pomem')) {
      return Icons.local_police_rounded;
    }
    if (lower.contains('gys') || lower.contains('yukselme')) {
      return Icons.military_tech_rounded;
    }
    if (lower.contains('ales') || lower.contains('yds') || lower.contains('akademik')) {
      return Icons.school_rounded;
    }
    return Icons.menu_book_rounded;
  }

  @override
  Widget build(BuildContext context) {
    final supportedLanguages =
        context.read<SystemConfigCubit>().supportedQuizLanguages;

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
            fontSize: 18,
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
                  width: 40,
                  height: 4,
                  margin: const EdgeInsets.only(bottom: 12),
                  decoration: BoxDecoration(
                    color: Colors.grey.withValues(alpha: 0.4),
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
                Text('Hedef Sınavınızı Seçin', style: textStyle),
                const SizedBox(height: 6),
                Text(
                  'Soru kategorileri seçtiğiniz sınava göre güncellenir',
                  style: TextStyle(
                    fontSize: 12,
                    color: context.primaryTextColor.withValues(alpha: 0.6),
                  ),
                ),
                const SizedBox(height: 12),
                const Divider(),
                Container(
                  constraints: BoxConstraints(
                    minHeight: context.height * .25,
                    maxHeight: context.height * .52,
                  ),
                  child: ListView.separated(
                    itemCount: supportedLanguages.length,
                    separatorBuilder: (_, __) => const SizedBox(height: 8),
                    itemBuilder: (_, i) {
                      final supportedLanguage = supportedLanguages[i];
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
                        borderRadius: BorderRadius.circular(12),
                        child: AnimatedContainer(
                          duration: const Duration(milliseconds: 180),
                          padding: const EdgeInsets.symmetric(
                            horizontal: 14,
                            vertical: 12,
                          ),
                          decoration: BoxDecoration(
                            color: isSelected
                                ? Theme.of(context)
                                    .primaryColor
                                    .withValues(alpha: 0.12)
                                : colorScheme.onTertiary.withValues(alpha: 0.05),
                            border: Border.all(
                              color: isSelected
                                  ? Theme.of(context).primaryColor
                                  : Colors.transparent,
                              width: 1.5,
                            ),
                            borderRadius: BorderRadius.circular(12),
                          ),
                          child: Row(
                            children: [
                              Container(
                                padding: const EdgeInsets.all(8),
                                decoration: BoxDecoration(
                                  color: isSelected
                                      ? Theme.of(context).primaryColor
                                      : colorScheme.onTertiary
                                          .withValues(alpha: 0.1),
                                  shape: BoxShape.circle,
                                ),
                                child: Icon(
                                  _getExamIcon(supportedLanguage.language),
                                  color: isSelected
                                      ? Colors.white
                                      : colorScheme.onTertiary,
                                  size: 18,
                                ),
                              ),
                              const SizedBox(width: 12),
                              Expanded(
                                child: Text(
                                  supportedLanguage.language,
                                  style: TextStyle(
                                    fontSize: 15,
                                    fontWeight: isSelected
                                        ? FontWeight.bold
                                        : FontWeight.w600,
                                    color: isSelected
                                        ? Theme.of(context).primaryColor
                                        : colorScheme.onTertiary,
                                  ),
                                ),
                              ),
                              if (isSelected)
                                Icon(
                                  Icons.check_circle_rounded,
                                  color: Theme.of(context).primaryColor,
                                  size: 22,
                                ),
                            ],
                          ),
                        ),
                      );
                    },
                  ),
                ),
                const SizedBox(height: 16),
                CustomRoundedButton(
                  onTap: Navigator.of(context).pop,
                  widthPercentage: 1,
                  backgroundColor: Theme.of(context).primaryColor,
                  buttonTitle: context.tr('save') ?? 'Tamam',
                  radius: 12,
                  showBorder: false,
                  height: 48,
                ),
                const SizedBox(height: 8),
              ],
            ),
          );
        },
      ),
    );
  }
}
