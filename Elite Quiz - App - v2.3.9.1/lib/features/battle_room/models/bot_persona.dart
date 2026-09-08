import 'dart:math';

/// Realistic Bot Persona model for Quiza 1v1 Battle matchmaking.
final class BotPersona {
  const BotPersona({
    required this.name,
    required this.profileUrl,
    required this.uid,
    this.accuracy = 82,
  });

  final String name;
  final String profileUrl;
  final String uid;
  final int accuracy; // Accuracy rate between 75% and 90%

  static const List<BotPersona> botPool = [
    BotPersona(name: 'Elif D.', profileUrl: 'assets/config/profile/2.svg', uid: 'bot_u_2', accuracy: 85),
    BotPersona(name: 'Ahmet Y.', profileUrl: 'assets/config/profile/1.svg', uid: 'bot_u_1', accuracy: 88),
    BotPersona(name: 'Merve K.', profileUrl: 'assets/config/profile/3.svg', uid: 'bot_u_3', accuracy: 82),
    BotPersona(name: 'Burak Ş.', profileUrl: 'assets/config/profile/4.svg', uid: 'bot_u_4', accuracy: 80),
    BotPersona(name: 'Zeynep Ç.', profileUrl: 'assets/config/profile/5.svg', uid: 'bot_u_5', accuracy: 90),
    BotPersona(name: 'Oğuzhan K.', profileUrl: 'assets/config/profile/6.svg', uid: 'bot_u_6', accuracy: 78),
    BotPersona(name: 'Fatma Y.', profileUrl: 'assets/config/profile/7.svg', uid: 'bot_u_7', accuracy: 84),
    BotPersona(name: 'Emre A.', profileUrl: 'assets/config/profile/8.svg', uid: 'bot_u_8', accuracy: 86),
    BotPersona(name: 'Selin A.', profileUrl: 'assets/config/profile/9.svg', uid: 'bot_u_9', accuracy: 79),
    BotPersona(name: 'Caner Ö.', profileUrl: 'assets/config/profile/10.svg', uid: 'bot_u_10', accuracy: 83),
    BotPersona(name: 'Büşra Y.', profileUrl: 'assets/config/profile/2.svg', uid: 'bot_u_11', accuracy: 87),
    BotPersona(name: 'Deniz A.', profileUrl: 'assets/config/profile/1.svg', uid: 'bot_u_12', accuracy: 81),
    BotPersona(name: 'Gamze P.', profileUrl: 'assets/config/profile/3.svg', uid: 'bot_u_13', accuracy: 76),
    BotPersona(name: 'Serkan K.', profileUrl: 'assets/config/profile/4.svg', uid: 'bot_u_14', accuracy: 89),
    BotPersona(name: 'Ebru B.', profileUrl: 'assets/config/profile/5.svg', uid: 'bot_u_15', accuracy: 84),
    BotPersona(name: 'Mustafa Ö.', profileUrl: 'assets/config/profile/6.svg', uid: 'bot_u_16', accuracy: 77),
    BotPersona(name: 'Ayşe K.', profileUrl: 'assets/config/profile/7.svg', uid: 'bot_u_17', accuracy: 86),
    BotPersona(name: 'Tolga G.', profileUrl: 'assets/config/profile/8.svg', uid: 'bot_u_18', accuracy: 80),
    BotPersona(name: 'Hilal Y.', profileUrl: 'assets/config/profile/9.svg', uid: 'bot_u_19', accuracy: 88),
    BotPersona(name: 'Yusuf K.', profileUrl: 'assets/config/profile/10.svg', uid: 'bot_u_20', accuracy: 82),
    BotPersona(name: 'Eren D.', profileUrl: 'assets/config/profile/1.svg', uid: 'bot_u_21', accuracy: 85),
    BotPersona(name: 'Seda Ç.', profileUrl: 'assets/config/profile/2.svg', uid: 'bot_u_22', accuracy: 83),
    BotPersona(name: 'Berkant Ş.', profileUrl: 'assets/config/profile/4.svg', uid: 'bot_u_23', accuracy: 79),
    BotPersona(name: 'Melis K.', profileUrl: 'assets/config/profile/3.svg', uid: 'bot_u_24', accuracy: 86),
    BotPersona(name: 'Onur V.', profileUrl: 'assets/config/profile/6.svg', uid: 'bot_u_25', accuracy: 88),
  ];

  static BotPersona getRandomBot() {
    return botPool[Random().nextInt(botPool.length)];
  }
}
