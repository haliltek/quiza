import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutterquiz/core/core.dart';
import 'package:flutterquiz/features/system_config/cubits/system_config_cubit.dart';
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
    final supportedExams =
        context.read<SystemConfigCubit>().supportedQuizLanguages;

    return Scaffold(
      appBar: QAppBar(
        automaticallyImplyLeading: false,
        title: const Text('Hedef Sınavınızı Seçin'),
        usePrimaryColor: true,
      ),
      body: SafeArea(
        child: Padding(
          padding: EdgeInsets.symmetric(
            vertical: context.height * 0.02,
            horizontal: context.width * UiUtils.hzMarginPct,
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                padding: const EdgeInsets.all(14),
                decoration: BoxDecoration(
                  color: context.primaryColor.withValues(alpha: 0.08),
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(
                    color: context.primaryColor.withValues(alpha: 0.2),
                  ),
                ),
                child: Row(
                  children: [
                    Icon(
                      Icons.tips_and_updates_rounded,
                      color: context.primaryColor,
                      size: 22,
                    ),
                    const SizedBox(width: 10),
                    Expanded(
                      child: Text(
                        'Hazırlandığınız sınavı seçin. Soru kategorileri ve düellolar seçiminize göre özel hazırlanacaktır.',
                        style: TextStyle(
                          fontSize: 13,
                          color: context.primaryTextColor.withValues(alpha: 0.8),
                          height: 1.35,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 16),
              Expanded(
                child: ListView.separated(
                  itemCount: supportedExams.length,
                  separatorBuilder: (_, __) => const SizedBox(height: 10),
                  itemBuilder: (context, i) {
                    final exam = supportedExams[i];
                    final isSelected = _selectedExamId == exam.id;

                    return InkWell(
                      onTap: () {
                        setState(() {
                          _selectedExamId = exam.id;
                        });
                        context.read<QuizLanguageCubit>().languageId = exam.id;
                      },
                      borderRadius: BorderRadius.circular(14),
                      child: AnimatedContainer(
                        duration: const Duration(milliseconds: 200),
                        padding: const EdgeInsets.symmetric(
                          horizontal: 14,
                          vertical: 12,
                        ),
                        decoration: BoxDecoration(
                          color: isSelected
                              ? context.primaryColor.withValues(alpha: 0.12)
                              : context.surfaceColor,
                          border: Border.all(
                            color: isSelected
                                ? context.primaryColor
                                : context.primaryTextColor.withValues(alpha: 0.15),
                            width: isSelected ? 2 : 1,
                          ),
                          borderRadius: BorderRadius.circular(14),
                          boxShadow: isSelected
                              ? [
                                  BoxShadow(
                                    color: context.primaryColor
                                        .withValues(alpha: 0.2),
                                    blurRadius: 8,
                                    offset: const Offset(0, 3),
                                  ),
                                ]
                              : null,
                        ),
                        child: Row(
                          children: [
                            Container(
                              padding: const EdgeInsets.all(10),
                              decoration: BoxDecoration(
                                color: isSelected
                                    ? context.primaryColor
                                    : context.primaryTextColor
                                        .withValues(alpha: 0.08),
                                shape: BoxShape.circle,
                              ),
                              child: Icon(
                                _getExamIcon(exam.language),
                                color: isSelected
                                    ? Colors.white
                                    : context.primaryTextColor
                                        .withValues(alpha: 0.7),
                                size: 20,
                              ),
                            ),
                            const SizedBox(width: 14),
                            Expanded(
                              child: Text(
                                exam.language,
                                style: TextStyle(
                                  fontSize: 15,
                                  fontWeight: isSelected
                                      ? FontWeight.w800
                                      : FontWeight.w600,
                                  color: isSelected
                                      ? context.primaryColor
                                      : context.primaryTextColor,
                                ),
                              ),
                            ),
                            if (isSelected)
                              Container(
                                padding: const EdgeInsets.all(4),
                                decoration: BoxDecoration(
                                  color: context.primaryColor,
                                  shape: BoxShape.circle,
                                ),
                                child: const Icon(
                                  Icons.check_rounded,
                                  color: Colors.white,
                                  size: 16,
                                ),
                              ),
                          ],
                        ),
                      ),
                    );
                  },
                ),
              ),
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          if (_selectedExamId.isNotEmpty) {
            context.read<QuizLanguageCubit>().languageId = _selectedExamId;
          }
          Navigator.of(context).pushReplacementNamed(Routes.introSlider);
        },
        backgroundColor: context.primaryColor,
        foregroundColor: Colors.white,
        icon: const Icon(Icons.arrow_forward_rounded),
        label: const Text(
          'Başla',
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
      ),
    );
  }
}
