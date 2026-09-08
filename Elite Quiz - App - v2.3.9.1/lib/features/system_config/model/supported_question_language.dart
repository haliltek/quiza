import 'package:flutter/material.dart';

enum KpssGroup {
  lisansB,
  lisansA,
  onlisans,
  ortaogretim,
  oabt,
  dhbt,
  none,
}

enum ExamTargetCategory {
  all,
  kpssEgitimDuzeyi,
  kpssAGrubu,
  kpssOzelAlan,
  digerKamuveHukuk,
}

final class QuizLanguage {
  const QuizLanguage({
    required this.id,
    required this.language,
    required this.languageCode,
    required this.isDefault,
  });

  QuizLanguage.fromJson(Map<String, dynamic> json)
    : id = json['id'] as String,
      language = json['language'] as String,
      languageCode = json['code'] as String,
      isDefault = (json['default_active'] as String) == '1';

  final String id;
  final String language;
  final String languageCode;
  final bool isDefault;

  bool get isKpss {
    final lower = language.toLowerCase();
    final code = languageCode.toLowerCase();
    return code.startsWith('kpss') ||
        lower.contains('kpss') ||
        lower.contains('öabt') ||
        lower.contains('oabt') ||
        lower.contains('dhbt');
  }

  KpssGroup get kpssGroup {
    final lower = language.toLowerCase();
    final code = languageCode.toLowerCase();

    if (code == 'kpss_aln' || (lower.contains('kpss') && lower.contains('a grubu'))) {
      return KpssGroup.lisansA;
    }
    if (code == 'kpss_onl' || lower.contains('önlisans') || lower.contains('onlisans')) {
      return KpssGroup.onlisans;
    }
    if (code == 'kpss_ort' || lower.contains('ortaöğretim') || lower.contains('lise')) {
      return KpssGroup.ortaogretim;
    }
    if (code == 'kpss_oabt' || lower.contains('öabt') || lower.contains('öğretmenlik')) {
      return KpssGroup.oabt;
    }
    if (code == 'kpss_dhbt' || lower.contains('dhbt') || lower.contains('din hizmet')) {
      return KpssGroup.dhbt;
    }
    if (code == 'kpss_lis' || lower.contains('lisans')) {
      return KpssGroup.lisansB;
    }
    return KpssGroup.none;
  }

  ExamTargetCategory get targetCategory {
    switch (kpssGroup) {
      case KpssGroup.lisansB:
      case KpssGroup.onlisans:
      case KpssGroup.ortaogretim:
        return ExamTargetCategory.kpssEgitimDuzeyi;
      case KpssGroup.lisansA:
        return ExamTargetCategory.kpssAGrubu;
      case KpssGroup.oabt:
      case KpssGroup.dhbt:
        return ExamTargetCategory.kpssOzelAlan;
      case KpssGroup.none:
        return ExamTargetCategory.digerKamuveHukuk;
    }
  }

  String get shortBadge {
    switch (kpssGroup) {
      case KpssGroup.lisansB:
        return '4 YILLIK • HER YIL';
      case KpssGroup.onlisans:
        return '2 YILLIK MYO • ÇİFT YILLAR';
      case KpssGroup.ortaogretim:
        return 'LİSE • ÇİFT YILLAR';
      case KpssGroup.lisansA:
        return 'KARİYER KADROLAR • ALAN';
      case KpssGroup.oabt:
        return 'MEB ÖĞRETMEN ATAMALARI';
      case KpssGroup.dhbt:
        return 'DİYANET İŞLERİ BAŞKANLIĞI';
      case KpssGroup.none:
        return 'MESLEKİ SINAV';
    }
  }

  String get audienceDescription {
    switch (kpssGroup) {
      case KpssGroup.lisansB:
        return '4 yıllık üniversite mezunları için Genel Yetenek - Genel Kültür (GY-GK) oturumudur. Memur, mühendis, hemşire ve B grubu tüm kadroları kapsar.';
      case KpssGroup.onlisans:
        return '2 yıllık meslek yüksekokulu mezun ve öğrencileri için çift yıllarda düzenlenen Genel Yetenek - Genel Kültür sınav oturumudur.';
      case KpssGroup.ortaogretim:
        return 'Lise mezunları ve son sınıf öğrencileri için çift yıllarda düzenlenen Genel Yetenek - Genel Kültür sınav oturumudur.';
      case KpssGroup.lisansA:
        return 'Bakanlıklar, müfettişlik, uzman yardımcılığı ve denetmenlik kadroları için GY-GK + Alan Bilgisi (Hukuk, İktisat, Maliye vb.) oturumudur.';
      case KpssGroup.oabt:
        return 'MEB öğretmen kadrolarına atanacak adayların girdiği Eğitim Bilimleri ve branş testleridir (Matematik, Türkçe, Tarih vb.).';
      case KpssGroup.dhbt:
        return 'Diyanet İşleri Başkanlığı imam-hatip, müezzin-kayyım ve Kur\'an kursu öğreticisi kadrolarına atanacak adaylar için alan sınavıdır.';
      case KpssGroup.none:
        return 'Adli-idari yargı ve kamu kurumları için hazırlanan özel kariyer sınav modülüdür.';
    }
  }

  IconData get icon {
    switch (kpssGroup) {
      case KpssGroup.lisansB:
        return Icons.school_rounded;
      case KpssGroup.onlisans:
        return Icons.auto_stories_rounded;
      case KpssGroup.ortaogretim:
        return Icons.menu_book_rounded;
      case KpssGroup.lisansA:
        return Icons.work_rounded;
      case KpssGroup.oabt:
        return Icons.psychology_rounded;
      case KpssGroup.dhbt:
        return Icons.mosque_rounded;
      case KpssGroup.none:
        final lower = language.toLowerCase();
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
          return Icons.history_edu_rounded;
        }
        return Icons.assignment_rounded;
    }
  }
}

