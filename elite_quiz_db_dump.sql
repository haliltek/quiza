-- MySQL dump 10.13  Distrib 8.0.46, for Linux (x86_64)
--
-- Host: localhost    Database: elite_quiz_db
-- ------------------------------------------------------
-- Server version	8.0.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_ai_questions`
--

DROP TABLE IF EXISTS `tbl_ai_questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_ai_questions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `language_id` int NOT NULL DEFAULT '0',
  `quiz_type` int NOT NULL DEFAULT '0' COMMENT '1=quiz_zone,\r\n3=guess_the_word,\r\n6=multi_match,\r\n7=contest,\r\n8=exam',
  `contest_id` int NOT NULL DEFAULT '0',
  `exam_id` int NOT NULL DEFAULT '0',
  `category` int NOT NULL,
  `subcategory` int NOT NULL DEFAULT '0',
  `level` int NOT NULL DEFAULT '0',
  `question_type` int NOT NULL DEFAULT '0' COMMENT '1=options, 2=true/false ',
  `answer_type` int NOT NULL DEFAULT '0' COMMENT '1=multiselect, 2=sequence ',
  `question` text COLLATE utf8mb4_bin NOT NULL,
  `options` longtext COLLATE utf8mb4_bin NOT NULL,
  `correct_answer` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `marks` int NOT NULL DEFAULT '0',
  `status` int NOT NULL DEFAULT '0',
  `note` varchar(255) COLLATE utf8mb4_bin DEFAULT NULL,
  `date_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `tbl_ai_questions_chk_1` CHECK (json_valid(`options`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_ai_questions`
--

LOCK TABLES `tbl_ai_questions` WRITE;
/*!40000 ALTER TABLE `tbl_ai_questions` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_ai_questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_audio_question`
--

DROP TABLE IF EXISTS `tbl_audio_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_audio_question` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` int NOT NULL,
  `subcategory` int NOT NULL,
  `language_id` int NOT NULL DEFAULT '0',
  `audio_type` int NOT NULL COMMENT '1=link,2=upload',
  `audio` varchar(255) NOT NULL,
  `question` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `question_type` tinyint NOT NULL COMMENT '1=normal, 2=true/false',
  `optiona` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optionb` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optionc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optiond` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optione` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `answer` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `note` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category` (`category`),
  KEY `subcategory` (`subcategory`) USING BTREE,
  KEY `language_id` (`language_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_audio_question`
--

LOCK TABLES `tbl_audio_question` WRITE;
/*!40000 ALTER TABLE `tbl_audio_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_audio_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_authenticate`
--

DROP TABLE IF EXISTS `tbl_authenticate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_authenticate` (
  `auth_id` int NOT NULL AUTO_INCREMENT,
  `auth_username` varchar(12) NOT NULL,
  `auth_pass` text NOT NULL,
  `role` varchar(32) NOT NULL,
  `permissions` mediumtext NOT NULL,
  `status` int NOT NULL DEFAULT '0',
  `language` varchar(255) NOT NULL DEFAULT 'english',
  `created` datetime NOT NULL,
  PRIMARY KEY (`auth_id`),
  UNIQUE KEY `auth_username` (`auth_username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_authenticate`
--

LOCK TABLES `tbl_authenticate` WRITE;
/*!40000 ALTER TABLE `tbl_authenticate` DISABLE KEYS */;
INSERT INTO `tbl_authenticate` VALUES (1,'admin','$2y$10$BMrcIYxcLaikC2E7JvQ7XepMHZv76w/ZfvRNLxzhWJxNtNORjYVi.','admin','',1,'turkce','2020-11-02 10:23:24');
/*!40000 ALTER TABLE `tbl_authenticate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_badges`
--

DROP TABLE IF EXISTS `tbl_badges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_badges` (
  `id` int NOT NULL AUTO_INCREMENT,
  `language_id` int DEFAULT '14',
  `type` varchar(100) NOT NULL,
  `badge_label` varchar(200) NOT NULL,
  `badge_note` text NOT NULL,
  `badge_reward` int NOT NULL,
  `badge_icon` varchar(100) NOT NULL,
  `badge_counter` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_badges`
--

LOCK TABLES `tbl_badges` WRITE;
/*!40000 ALTER TABLE `tbl_badges` DISABLE KEYS */;
INSERT INTO `tbl_badges` VALUES (1,14,'dashing_debut','Dashing Debut','Play first quiz zone game',2,'1636692664.png',1),(2,14,'combat_winner','Combat Winner','Won random battle. If both users have completed the battle then the badge will unlock.',5,'16366926641.png',1),(3,14,'clash_winner','Clash Winner','Won group battle. If a minimum of one opponent user has completed the battle then the badge will unlock.',2,'16366926642.png',1),(4,14,'most_wanted_winner','Most Wanted Winner','Won contest',10,'16366926643.png',1),(5,14,'ultimate_player','Ultimate Player','Highest point Gainer',1,'16366926644.png',0),(6,14,'quiz_warrior','Quiz Warrior','Won back-to-back three random battles. If both users have completed the battle then the badge will unlock.',1,'16366926645.png',3),(7,14,'super_sonic','Super Sonic','Fastest puzzle solver. Need minimum 5 questions to unlock this badge.',1,'16366926646.png',25),(8,14,'flashback','Flashback','Average time to solve fun & learn quiz questions. Need minimum 5 questions to unlock this badge.',1,'16366926647.png',8),(9,14,'brainiac','Brainiac','Completed 100% quiz without using a lifeline. Need minimum 5 questions to unlock this badge.',1,'16366926648.png',0),(10,14,'big_thing','Big Thing','5k correct answer',1,'16366926649.png',5000),(11,14,'elite','Elite','Earn coins more than 5k ',1,'163669266410.png',200),(12,14,'thirsty','Thirty','Play daily quiz continuously 30 days',1,'163669266411.png',30),(13,14,'power_elite','Power Elite','Achieved more than 10 badges',1,'163669266412.png',10),(14,14,'sharing_caring','Sharing is Caring','Share application to more than 50 users',1,'163669266413.png',50),(15,14,'streak','Streak','Maintain streak for 30 days',1,'163669266414.png',30);
/*!40000 ALTER TABLE `tbl_badges` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_battle_questions`
--

DROP TABLE IF EXISTS `tbl_battle_questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_battle_questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `match_id` varchar(128) NOT NULL,
  `entry_coin` int NOT NULL DEFAULT '0',
  `questions` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `date_created` datetime NOT NULL,
  `set_user1` int NOT NULL DEFAULT '0',
  `set_user2` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `match_id` (`match_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_battle_questions`
--

LOCK TABLES `tbl_battle_questions` WRITE;
/*!40000 ALTER TABLE `tbl_battle_questions` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_battle_questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_battle_statistics`
--

DROP TABLE IF EXISTS `tbl_battle_statistics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_battle_statistics` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id1` int NOT NULL,
  `user_id2` int NOT NULL,
  `is_drawn` tinyint NOT NULL,
  `winner_id` int NOT NULL,
  `date_created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id1` (`user_id1`),
  KEY `user_id2` (`user_id2`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_battle_statistics`
--

LOCK TABLES `tbl_battle_statistics` WRITE;
/*!40000 ALTER TABLE `tbl_battle_statistics` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_battle_statistics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_bookmark`
--

DROP TABLE IF EXISTS `tbl_bookmark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_bookmark` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `question_id` int NOT NULL,
  `status` int NOT NULL,
  `type` int NOT NULL COMMENT '1-quiz_zone, 3-guess_the_word, 4-audio_question',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `question_id` (`question_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_bookmark`
--

LOCK TABLES `tbl_bookmark` WRITE;
/*!40000 ALTER TABLE `tbl_bookmark` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_bookmark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_category`
--

DROP TABLE IF EXISTS `tbl_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `language_id` int NOT NULL DEFAULT '0',
  `category_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `slug` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `type` int NOT NULL,
  `is_premium` tinyint NOT NULL DEFAULT '0' COMMENT '0 - no , 1 - yes',
  `coins` int NOT NULL DEFAULT '0',
  `has_level` tinyint NOT NULL DEFAULT '1',
  `image` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `row_order` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `language_id` (`language_id`),
  KEY `has_level` (`has_level`)
) ENGINE=MyISAM AUTO_INCREMENT=38 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_category`
--

LOCK TABLES `tbl_category` WRITE;
/*!40000 ALTER TABLE `tbl_category` DISABLE KEYS */;
INSERT INTO `tbl_category` VALUES (8,61,'Borçlar Hukuku Genel Hükümler','borclar-hukuku',1,0,0,1,'',3),(7,61,'Ticaret Hukuku (Kıymetli Evrak & Şirketler)','ticaret-hukuku',1,0,0,1,'',2),(6,61,'İcra ve İflas Hukuku','icra-iflas-hukuku',1,0,0,1,'',1),(4,52,'Türkçe (KPSS Lisans)','kpss-turkce',1,0,0,1,'',4),(5,52,'Matematik & Sayısal Mantık','kpss-matematik',1,0,0,1,'',5),(3,52,'Vatandaşlık & Anayasa (KPSS Lisans)','kpss-vatandaslik',1,0,0,1,'',3),(1,52,'Tarih (KPSS Lisans)','kpss-tarih',1,0,0,1,'',1),(2,52,'Coğrafya (KPSS Lisans)','kpss-cografya',1,0,0,1,'',2),(9,61,'Hukuk Muhakemeleri Kanunu (HMK)','hmk-medeni-usul',1,0,0,1,'',4),(10,61,'Harçlar Kanunu ve Damga Vergisi','harclar-damga-vergisi',1,0,0,1,'',5),(11,59,'Anayasa & İdare Hukuku (Hakimlik)','hakimlik-anayasa-idare',1,0,0,1,'',1),(12,59,'Ceza Genel & Özel Hukuku (Hakimlik)','hakimlik-ceza',1,0,0,1,'',2),(13,59,'Ceza Muhakemesi Hukuku (CMK)','hakimlik-cmk',1,0,0,1,'',3),(14,59,'Medeni Hukuk & Borçlar Hukuku','hakimlik-medeni-borclar',1,0,0,1,'',4),(15,59,'İdari Yargılama Usulü Kanunu (İYUK)','hakimlik-iyuk',1,0,0,1,'',5),(16,52,'KPSS Tarih Hap Bilgiler','kpss-tarih-hap-bilgiler',2,0,0,1,'',1),(17,52,'KPSS Coğrafya Şifreleri','kpss-cografya-sifreleri',2,0,0,1,'',2),(18,52,'KPSS Vatandaşlık Notları','kpss-vatandaslik-notlari',2,0,0,1,'',3),(19,52,'KPSS Tarih Kavramları','kpss-tarih-kavramlari',3,0,0,1,'',1),(20,52,'KPSS Coğrafya Terimleri','kpss-cografya-terimleri',3,0,0,1,'',2),(21,52,'KPSS Hukuk ve Anayasa Terimleri','kpss-hukuk-terimleri',3,0,0,1,'',3),(22,52,'KPSS Temel Matematik','kpss-temel-matematik',5,0,0,1,'',1),(23,52,'KPSS Sayısal Mantık & Problemler','kpss-sayisal-mantik-problemler',5,0,0,1,'',2),(24,52,'KPSS Tarih Eşleştirmeleri','kpss-tarih-eslestirmeleri',6,0,0,1,'',1),(25,52,'KPSS Coğrafya Eşleştirmeleri','kpss-cografya-eslestirmeleri',6,0,0,1,'',2),(26,52,'KPSS Genel Kültür Eşleştirmeleri','kpss-genel-kultur-eslestirmeleri',6,0,0,1,'',3),(27,52,'KPSS Tarih Hap Bilgiler','kpss-tarih-hap-bilgiler',2,0,0,1,'',1),(28,52,'KPSS Coğrafya Şifreleri','kpss-cografya-sifreleri',2,0,0,1,'',2),(29,52,'KPSS Vatandaşlık Notları','kpss-vatandaslik-notlari',2,0,0,1,'',3),(30,52,'KPSS Tarih Kavramları','kpss-tarih-kavramlari',3,0,0,1,'',1),(31,52,'KPSS Coğrafya Terimleri','kpss-cografya-terimleri',3,0,0,1,'',2),(32,52,'KPSS Hukuk ve Anayasa Terimleri','kpss-hukuk-terimleri',3,0,0,1,'',3),(33,52,'KPSS Temel Matematik','kpss-temel-matematik',5,0,0,1,'',1),(34,52,'KPSS Sayısal Mantık & Problemler','kpss-sayisal-mantik-problemler',5,0,0,1,'',2),(35,52,'KPSS Tarih Eşleştirmeleri','kpss-tarih-eslestirmeleri',6,0,0,1,'',1),(36,52,'KPSS Coğrafya Eşleştirmeleri','kpss-cografya-eslestirmeleri',6,0,0,1,'',2),(37,52,'KPSS Genel Kültür Eşleştirmeleri','kpss-genel-kultur-eslestirmeleri',6,0,0,1,'',3);
/*!40000 ALTER TABLE `tbl_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_coin_store`
--

DROP TABLE IF EXISTS `tbl_coin_store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_coin_store` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `coins` int NOT NULL,
  `type` int NOT NULL DEFAULT '0' COMMENT '1=ads',
  `product_id` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `image` text COLLATE utf8mb4_general_ci,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `status` tinyint NOT NULL DEFAULT '1' COMMENT '0 - OFF , 1 - ON',
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_id` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_coin_store`
--

LOCK TABLES `tbl_coin_store` WRITE;
/*!40000 ALTER TABLE `tbl_coin_store` DISABLE KEYS */;
INSERT INTO `tbl_coin_store` VALUES (1,'5 Coins',5,0,'5_consumable_coin',NULL,'Small Pack',1);
/*!40000 ALTER TABLE `tbl_coin_store` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_contest`
--

DROP TABLE IF EXISTS `tbl_contest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_contest` (
  `id` int NOT NULL AUTO_INCREMENT,
  `language_id` int NOT NULL DEFAULT '0',
  `name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `image` varchar(512) NOT NULL,
  `entry` int NOT NULL,
  `prize_status` int NOT NULL,
  `date_created` datetime NOT NULL,
  `status` int NOT NULL COMMENT '0=deactive,1=active',
  PRIMARY KEY (`id`),
  KEY `language_id` (`language_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_contest`
--

LOCK TABLES `tbl_contest` WRITE;
/*!40000 ALTER TABLE `tbl_contest` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_contest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_contest_leaderboard`
--

DROP TABLE IF EXISTS `tbl_contest_leaderboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_contest_leaderboard` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `contest_id` int NOT NULL,
  `questions_attended` int NOT NULL,
  `correct_answers` int NOT NULL,
  `score` double NOT NULL,
  `last_updated` datetime NOT NULL,
  `date_created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `score` (`score`),
  KEY `user_id` (`user_id`),
  KEY `contest_id` (`contest_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_contest_leaderboard`
--

LOCK TABLES `tbl_contest_leaderboard` WRITE;
/*!40000 ALTER TABLE `tbl_contest_leaderboard` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_contest_leaderboard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_contest_prize`
--

DROP TABLE IF EXISTS `tbl_contest_prize`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_contest_prize` (
  `id` int NOT NULL AUTO_INCREMENT,
  `contest_id` int NOT NULL,
  `top_winner` int NOT NULL,
  `points` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contest_id` (`contest_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_contest_prize`
--

LOCK TABLES `tbl_contest_prize` WRITE;
/*!40000 ALTER TABLE `tbl_contest_prize` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_contest_prize` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_contest_question`
--

DROP TABLE IF EXISTS `tbl_contest_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_contest_question` (
  `id` int NOT NULL AUTO_INCREMENT,
  `langauge_id` int NOT NULL DEFAULT '0',
  `contest_id` int NOT NULL,
  `image` varchar(256) NOT NULL,
  `question` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `question_type` int NOT NULL COMMENT '1= normal, 2= true/false',
  `optiona` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optionb` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optionc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optiond` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optione` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `answer` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `note` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contest_id` (`contest_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_contest_question`
--

LOCK TABLES `tbl_contest_question` WRITE;
/*!40000 ALTER TABLE `tbl_contest_question` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_contest_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_daily_quiz`
--

DROP TABLE IF EXISTS `tbl_daily_quiz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_daily_quiz` (
  `id` int NOT NULL AUTO_INCREMENT,
  `language_id` int NOT NULL,
  `questions_id` text NOT NULL,
  `date_published` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `language_id` (`language_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_daily_quiz`
--

LOCK TABLES `tbl_daily_quiz` WRITE;
/*!40000 ALTER TABLE `tbl_daily_quiz` DISABLE KEYS */;
INSERT INTO `tbl_daily_quiz` VALUES (4,52,'1,2,3,4,5,6,7,8,9,10','2026-09-06'),(5,52,'11,12,13,14,15,16,17,18,19,20','2026-09-07'),(6,52,'21,22,23,24,25,26,27,28,29,30','2026-09-08');
/*!40000 ALTER TABLE `tbl_daily_quiz` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_daily_quiz_user`
--

DROP TABLE IF EXISTS `tbl_daily_quiz_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_daily_quiz_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_daily_quiz_user`
--

LOCK TABLES `tbl_daily_quiz_user` WRITE;
/*!40000 ALTER TABLE `tbl_daily_quiz_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_daily_quiz_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_exam_module`
--

DROP TABLE IF EXISTS `tbl_exam_module`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_exam_module` (
  `id` int NOT NULL AUTO_INCREMENT,
  `language_id` int NOT NULL DEFAULT '0',
  `title` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `date` date NOT NULL,
  `exam_key` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `duration` int NOT NULL,
  `status` int NOT NULL DEFAULT '0',
  `answer_again` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `language_id` (`language_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_exam_module`
--

LOCK TABLES `tbl_exam_module` WRITE;
/*!40000 ALTER TABLE `tbl_exam_module` DISABLE KEYS */;
INSERT INTO `tbl_exam_module` VALUES (1,52,'KPSS 2024 Genel Kültür Mini Deneme - 1 (20 Soru)','2026-09-06','1001',20,1,1),(2,52,'KPSS 2024 Genel Kültür Mini Deneme - 2 (20 Soru)','2026-09-06','1002',20,1,1),(3,52,'KPSS Tarih Branş Denemesi (20 Soru)','2026-09-06','1003',20,1,1),(4,52,'KPSS Coğrafya Hızlı Tekrar Denemesi (10 Soru)','2026-09-06','1004',10,1,1),(5,52,'KPSS Vatandaşlık & Güncel Sınavı (10 Soru)','2026-09-06','1005',10,1,1),(6,52,'KPSS Hızlı Hızlandırma Sınavı (10 Soru)','2026-09-06','1006',10,1,1);
/*!40000 ALTER TABLE `tbl_exam_module` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_exam_module_question`
--

DROP TABLE IF EXISTS `tbl_exam_module_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_exam_module_question` (
  `id` int NOT NULL AUTO_INCREMENT,
  `exam_module_id` int NOT NULL,
  `image` varchar(512) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `marks` int NOT NULL,
  `question` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `question_type` tinyint NOT NULL COMMENT '1=normal, 2=true/false',
  `optiona` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optionb` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optionc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optiond` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optione` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `answer` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category` (`exam_module_id`)
) ENGINE=MyISAM AUTO_INCREMENT=181 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_exam_module_question`
--

LOCK TABLES `tbl_exam_module_question` WRITE;
/*!40000 ALTER TABLE `tbl_exam_module_question` DISABLE KEYS */;
INSERT INTO `tbl_exam_module_question` VALUES (1,1,'',5,'İslamiyet öncesi Türk devletlerinde hükümdara yönetme yetkisinin Tanrı tarafından verildiğine inanılan anlayışa ne ad verilir?',1,'Kut Anlayışı','Töre','Kurultay','Yarlıg','Veraset','a'),(2,1,'',5,'Türk tarihinde ilk kez düzenli ordu teşkilatını (onluk sistem) kuran Türk hükümdarı kimdir?',1,'Mete Han','Teoman','Bumin Kağan','Bilge Kağan','Atilla','a'),(3,1,'',5,'İslamiyet öncesi Türk devletlerinde ölen kişinin ardından düzenlenen cenaze törenine ne ad verilir?',1,'Yuğ','Balbal','Kurgan','Uçmağ','Tamu','a'),(4,1,'',5,'Türk tarihinde kendi adına para bastıran ilk Türk hükümdarı ve devleti aşağıdakilerden hangisidir?',1,'Baga Tarkan - Türgişler','Bumin Kağan - Kök Türkler','Mete Han - Asya Hun','Kutluk Bilge Kül Kağan - Uygurlar','İlteriş Kağan - II. Kök Türk','a'),(5,1,'',5,'Türk adıyla kurulan ilk Türk devleti aşağıdakilerden hangisidir?',1,'Kök Türk Devleti','Asya Hun Devleti','Uygur Devleti','Avarlar','Hazarlar','a'),(6,1,'',5,'Orhun Yazıtları (Göktürk Kitabeleri) hangi hükümdar ve devlet adamları adına dikilmiştir?',1,'Bilge Kağan, Kül Tigin, Tonyukuk','Bumin Kağan, İstemi Yabgu, Mete Han','Mete Han, Teoman, Çiçi','Atilla, Bleda, Rua','Mukan Kağan, Tapo Kağan, Taspar Kağan','a'),(7,1,'',5,'Yerleşik hayata geçen, tarımla uğraşan ve Maniheizm dinini benimseyen ilk Türk devleti hangisidir?',1,'Uygurlar','Karluklar','Kırgızlar','Hazarlar','Peçenekler','a'),(8,1,'',5,'Museviliği resmi din olarak kabul eden tek Türk devleti aşağıdakilerden hangisidir?',1,'Hazarlar','Avarlar','Macarlar','Kıpçaklar','Bulgarlar','a'),(9,1,'',5,'Bizans ordusunda ücretli askerlik yaparken 1071 Malazgirt Savaşı\'nda Selçuklu tarafına geçen Türk toplulukları hangileridir?',1,'Peçenekler ve Uzlar','Avarlar ve Bulgarlar','Hazarlar ve Türgişler','Karluklar ve Yağmalar','Kıpçaklar ve Kumanlar','a'),(10,1,'',5,'Dünyanın en uzun destanı kabul edilen Manas Destanı hangi Türk topluluğuna aittir?',1,'Kırgızlar','Kazaklar','Uygurlar','Özbekler','Türkmenler','a'),(11,1,'',5,'İslamiyeti kabul eden ilk Türk boyu aşağıdakilerden hangisidir?',1,'Karluklar','Yağmalar','Çiğiller','Tuhsiler','Oğuzlar','a'),(12,1,'',5,'Orta Asya\'da kurulan ilk Müslüman Türk devleti aşağıdakilerden hangisidir?',1,'Karahanlılar','Gazneliler','Büyük Selçuklular','Tolunoğulları','İhşidiler','a'),(13,1,'',5,'Kaşgarlı Mahmut tarafından yazılan ve ilk Türkçe sözlük niteliği taşıyan eser hangisidir?',1,'Divânu Lugâti\'t-Türk','Kutadgu Bilig','Atabetü\'l-Hakayık','Divan-ı Hikmet','Şehnâme','a'),(14,1,'',5,'Yusuf Has Hacip tarafından Karahanlı hükümdarı Tabgaç Buğra Han\'a sunulan \'mutluluk veren bilgi\' anlamına gelen siyasetname eseri hangisidir?',1,'Kutadgu Bilig','Divan-ı Hikmet','Atabetü\'l-Hakayık','Siyasetnâme','Risaletü\'n-Nushiyye','a'),(15,1,'',5,'Mısır\'da kurulan ilk Türk-İslam devleti aşağıdakilerden hangisidir?',1,'Tolunoğulları','İhşidiler (Akşitler)','Eyyubiler','Memlükler','Fatımiler','a'),(16,1,'',5,'Hicaz bölgesine (Mekke ve Medine) hakim olan ilk Türk devleti aşağıdakilerden hangisidir?',1,'İhşidiler (Akşitler)','Tolunoğulları','Eyyubiler','Büyük Selçuklular','Osmanlı Devleti','a'),(17,1,'',5,'Sultan unvanını kullanan ilk Türk hükümdarı aşağıdakilerden hangisidir?',1,'Gazneli Mahmut','Alparslan','Tuğrul Bey','Satuk Buğra Han','Melikşah','a'),(18,1,'',5,'Anadolu\'nun kapılarını Türklere kesin olarak açan 1071 Malazgirt Savaşı hangi Selçuklu sultanı döneminde kazanılmıştır?',1,'Sultan Alparslan','Tuğrul Bey','Sultan Sencer','Melikşah','Çağrı Bey','a'),(19,1,'',5,'Anadolu\'da kurulan ilk Türk beyliği aşağıdakilerden hangisidir?',1,'Saltuklular','Danişmentliler','Mengücekliler','Artuklular','Çaka Beyliği','a'),(20,1,'',5,'Anadolu\'nun Türk yurdu olduğunu kesinleştiren ve Bizans\'ın Türkleri Anadolu\'dan atma ümidini bitiren savaş hangisidir?',1,'Miryokefalon Savaşı (1176)','Malazgirt Savaşı (1071)','Pasinler Savaşı (1048)','Dandanakan Savaşı (1040)','Yassıçemen Savaşı (1230)','a'),(21,2,'',5,'İslamiyet öncesi Türk devletlerinde hükümdara yönetme yetkisinin Tanrı tarafından verildiğine inanılan anlayışa ne ad verilir?',1,'Kut Anlayışı','Töre','Kurultay','Yarlıg','Veraset','a'),(22,2,'',5,'Türk tarihinde ilk kez düzenli ordu teşkilatını (onluk sistem) kuran Türk hükümdarı kimdir?',1,'Mete Han','Teoman','Bumin Kağan','Bilge Kağan','Atilla','a'),(23,2,'',5,'İslamiyet öncesi Türk devletlerinde ölen kişinin ardından düzenlenen cenaze törenine ne ad verilir?',1,'Yuğ','Balbal','Kurgan','Uçmağ','Tamu','a'),(24,2,'',5,'Türk tarihinde kendi adına para bastıran ilk Türk hükümdarı ve devleti aşağıdakilerden hangisidir?',1,'Baga Tarkan - Türgişler','Bumin Kağan - Kök Türkler','Mete Han - Asya Hun','Kutluk Bilge Kül Kağan - Uygurlar','İlteriş Kağan - II. Kök Türk','a'),(25,2,'',5,'Türk adıyla kurulan ilk Türk devleti aşağıdakilerden hangisidir?',1,'Kök Türk Devleti','Asya Hun Devleti','Uygur Devleti','Avarlar','Hazarlar','a'),(26,2,'',5,'Orhun Yazıtları (Göktürk Kitabeleri) hangi hükümdar ve devlet adamları adına dikilmiştir?',1,'Bilge Kağan, Kül Tigin, Tonyukuk','Bumin Kağan, İstemi Yabgu, Mete Han','Mete Han, Teoman, Çiçi','Atilla, Bleda, Rua','Mukan Kağan, Tapo Kağan, Taspar Kağan','a'),(27,2,'',5,'Yerleşik hayata geçen, tarımla uğraşan ve Maniheizm dinini benimseyen ilk Türk devleti hangisidir?',1,'Uygurlar','Karluklar','Kırgızlar','Hazarlar','Peçenekler','a'),(28,2,'',5,'Museviliği resmi din olarak kabul eden tek Türk devleti aşağıdakilerden hangisidir?',1,'Hazarlar','Avarlar','Macarlar','Kıpçaklar','Bulgarlar','a'),(29,2,'',5,'Bizans ordusunda ücretli askerlik yaparken 1071 Malazgirt Savaşı\'nda Selçuklu tarafına geçen Türk toplulukları hangileridir?',1,'Peçenekler ve Uzlar','Avarlar ve Bulgarlar','Hazarlar ve Türgişler','Karluklar ve Yağmalar','Kıpçaklar ve Kumanlar','a'),(30,2,'',5,'Dünyanın en uzun destanı kabul edilen Manas Destanı hangi Türk topluluğuna aittir?',1,'Kırgızlar','Kazaklar','Uygurlar','Özbekler','Türkmenler','a'),(31,2,'',5,'İslamiyeti kabul eden ilk Türk boyu aşağıdakilerden hangisidir?',1,'Karluklar','Yağmalar','Çiğiller','Tuhsiler','Oğuzlar','a'),(32,2,'',5,'Orta Asya\'da kurulan ilk Müslüman Türk devleti aşağıdakilerden hangisidir?',1,'Karahanlılar','Gazneliler','Büyük Selçuklular','Tolunoğulları','İhşidiler','a'),(33,2,'',5,'Kaşgarlı Mahmut tarafından yazılan ve ilk Türkçe sözlük niteliği taşıyan eser hangisidir?',1,'Divânu Lugâti\'t-Türk','Kutadgu Bilig','Atabetü\'l-Hakayık','Divan-ı Hikmet','Şehnâme','a'),(34,2,'',5,'Yusuf Has Hacip tarafından Karahanlı hükümdarı Tabgaç Buğra Han\'a sunulan \'mutluluk veren bilgi\' anlamına gelen siyasetname eseri hangisidir?',1,'Kutadgu Bilig','Divan-ı Hikmet','Atabetü\'l-Hakayık','Siyasetnâme','Risaletü\'n-Nushiyye','a'),(35,2,'',5,'Mısır\'da kurulan ilk Türk-İslam devleti aşağıdakilerden hangisidir?',1,'Tolunoğulları','İhşidiler (Akşitler)','Eyyubiler','Memlükler','Fatımiler','a'),(36,2,'',5,'Hicaz bölgesine (Mekke ve Medine) hakim olan ilk Türk devleti aşağıdakilerden hangisidir?',1,'İhşidiler (Akşitler)','Tolunoğulları','Eyyubiler','Büyük Selçuklular','Osmanlı Devleti','a'),(37,2,'',5,'Sultan unvanını kullanan ilk Türk hükümdarı aşağıdakilerden hangisidir?',1,'Gazneli Mahmut','Alparslan','Tuğrul Bey','Satuk Buğra Han','Melikşah','a'),(38,2,'',5,'Anadolu\'nun kapılarını Türklere kesin olarak açan 1071 Malazgirt Savaşı hangi Selçuklu sultanı döneminde kazanılmıştır?',1,'Sultan Alparslan','Tuğrul Bey','Sultan Sencer','Melikşah','Çağrı Bey','a'),(39,2,'',5,'Anadolu\'da kurulan ilk Türk beyliği aşağıdakilerden hangisidir?',1,'Saltuklular','Danişmentliler','Mengücekliler','Artuklular','Çaka Beyliği','a'),(40,2,'',5,'Anadolu\'nun Türk yurdu olduğunu kesinleştiren ve Bizans\'ın Türkleri Anadolu\'dan atma ümidini bitiren savaş hangisidir?',1,'Miryokefalon Savaşı (1176)','Malazgirt Savaşı (1071)','Pasinler Savaşı (1048)','Dandanakan Savaşı (1040)','Yassıçemen Savaşı (1230)','a'),(41,3,'',5,'İslamiyet öncesi Türk devletlerinde hükümdara yönetme yetkisinin Tanrı tarafından verildiğine inanılan anlayışa ne ad verilir?',1,'Kut Anlayışı','Töre','Kurultay','Yarlıg','Veraset','a'),(42,3,'',5,'Türk tarihinde ilk kez düzenli ordu teşkilatını (onluk sistem) kuran Türk hükümdarı kimdir?',1,'Mete Han','Teoman','Bumin Kağan','Bilge Kağan','Atilla','a'),(43,3,'',5,'İslamiyet öncesi Türk devletlerinde ölen kişinin ardından düzenlenen cenaze törenine ne ad verilir?',1,'Yuğ','Balbal','Kurgan','Uçmağ','Tamu','a'),(44,3,'',5,'Türk tarihinde kendi adına para bastıran ilk Türk hükümdarı ve devleti aşağıdakilerden hangisidir?',1,'Baga Tarkan - Türgişler','Bumin Kağan - Kök Türkler','Mete Han - Asya Hun','Kutluk Bilge Kül Kağan - Uygurlar','İlteriş Kağan - II. Kök Türk','a'),(45,3,'',5,'Türk adıyla kurulan ilk Türk devleti aşağıdakilerden hangisidir?',1,'Kök Türk Devleti','Asya Hun Devleti','Uygur Devleti','Avarlar','Hazarlar','a'),(46,3,'',5,'Orhun Yazıtları (Göktürk Kitabeleri) hangi hükümdar ve devlet adamları adına dikilmiştir?',1,'Bilge Kağan, Kül Tigin, Tonyukuk','Bumin Kağan, İstemi Yabgu, Mete Han','Mete Han, Teoman, Çiçi','Atilla, Bleda, Rua','Mukan Kağan, Tapo Kağan, Taspar Kağan','a'),(47,3,'',5,'Yerleşik hayata geçen, tarımla uğraşan ve Maniheizm dinini benimseyen ilk Türk devleti hangisidir?',1,'Uygurlar','Karluklar','Kırgızlar','Hazarlar','Peçenekler','a'),(48,3,'',5,'Museviliği resmi din olarak kabul eden tek Türk devleti aşağıdakilerden hangisidir?',1,'Hazarlar','Avarlar','Macarlar','Kıpçaklar','Bulgarlar','a'),(49,3,'',5,'Bizans ordusunda ücretli askerlik yaparken 1071 Malazgirt Savaşı\'nda Selçuklu tarafına geçen Türk toplulukları hangileridir?',1,'Peçenekler ve Uzlar','Avarlar ve Bulgarlar','Hazarlar ve Türgişler','Karluklar ve Yağmalar','Kıpçaklar ve Kumanlar','a'),(50,3,'',5,'Dünyanın en uzun destanı kabul edilen Manas Destanı hangi Türk topluluğuna aittir?',1,'Kırgızlar','Kazaklar','Uygurlar','Özbekler','Türkmenler','a'),(51,3,'',5,'İslamiyeti kabul eden ilk Türk boyu aşağıdakilerden hangisidir?',1,'Karluklar','Yağmalar','Çiğiller','Tuhsiler','Oğuzlar','a'),(52,3,'',5,'Orta Asya\'da kurulan ilk Müslüman Türk devleti aşağıdakilerden hangisidir?',1,'Karahanlılar','Gazneliler','Büyük Selçuklular','Tolunoğulları','İhşidiler','a'),(53,3,'',5,'Kaşgarlı Mahmut tarafından yazılan ve ilk Türkçe sözlük niteliği taşıyan eser hangisidir?',1,'Divânu Lugâti\'t-Türk','Kutadgu Bilig','Atabetü\'l-Hakayık','Divan-ı Hikmet','Şehnâme','a'),(54,3,'',5,'Yusuf Has Hacip tarafından Karahanlı hükümdarı Tabgaç Buğra Han\'a sunulan \'mutluluk veren bilgi\' anlamına gelen siyasetname eseri hangisidir?',1,'Kutadgu Bilig','Divan-ı Hikmet','Atabetü\'l-Hakayık','Siyasetnâme','Risaletü\'n-Nushiyye','a'),(55,3,'',5,'Mısır\'da kurulan ilk Türk-İslam devleti aşağıdakilerden hangisidir?',1,'Tolunoğulları','İhşidiler (Akşitler)','Eyyubiler','Memlükler','Fatımiler','a'),(56,3,'',5,'Hicaz bölgesine (Mekke ve Medine) hakim olan ilk Türk devleti aşağıdakilerden hangisidir?',1,'İhşidiler (Akşitler)','Tolunoğulları','Eyyubiler','Büyük Selçuklular','Osmanlı Devleti','a'),(57,3,'',5,'Sultan unvanını kullanan ilk Türk hükümdarı aşağıdakilerden hangisidir?',1,'Gazneli Mahmut','Alparslan','Tuğrul Bey','Satuk Buğra Han','Melikşah','a'),(58,3,'',5,'Anadolu\'nun kapılarını Türklere kesin olarak açan 1071 Malazgirt Savaşı hangi Selçuklu sultanı döneminde kazanılmıştır?',1,'Sultan Alparslan','Tuğrul Bey','Sultan Sencer','Melikşah','Çağrı Bey','a'),(59,3,'',5,'Anadolu\'da kurulan ilk Türk beyliği aşağıdakilerden hangisidir?',1,'Saltuklular','Danişmentliler','Mengücekliler','Artuklular','Çaka Beyliği','a'),(60,3,'',5,'Anadolu\'nun Türk yurdu olduğunu kesinleştiren ve Bizans\'ın Türkleri Anadolu\'dan atma ümidini bitiren savaş hangisidir?',1,'Miryokefalon Savaşı (1176)','Malazgirt Savaşı (1071)','Pasinler Savaşı (1048)','Dandanakan Savaşı (1040)','Yassıçemen Savaşı (1230)','a'),(61,4,'',5,'İslamiyet öncesi Türk devletlerinde hükümdara yönetme yetkisinin Tanrı tarafından verildiğine inanılan anlayışa ne ad verilir?',1,'Kut Anlayışı','Töre','Kurultay','Yarlıg','Veraset','a'),(62,4,'',5,'Türk tarihinde ilk kez düzenli ordu teşkilatını (onluk sistem) kuran Türk hükümdarı kimdir?',1,'Mete Han','Teoman','Bumin Kağan','Bilge Kağan','Atilla','a'),(63,4,'',5,'İslamiyet öncesi Türk devletlerinde ölen kişinin ardından düzenlenen cenaze törenine ne ad verilir?',1,'Yuğ','Balbal','Kurgan','Uçmağ','Tamu','a'),(64,4,'',5,'Türk tarihinde kendi adına para bastıran ilk Türk hükümdarı ve devleti aşağıdakilerden hangisidir?',1,'Baga Tarkan - Türgişler','Bumin Kağan - Kök Türkler','Mete Han - Asya Hun','Kutluk Bilge Kül Kağan - Uygurlar','İlteriş Kağan - II. Kök Türk','a'),(65,4,'',5,'Türk adıyla kurulan ilk Türk devleti aşağıdakilerden hangisidir?',1,'Kök Türk Devleti','Asya Hun Devleti','Uygur Devleti','Avarlar','Hazarlar','a'),(66,4,'',5,'Orhun Yazıtları (Göktürk Kitabeleri) hangi hükümdar ve devlet adamları adına dikilmiştir?',1,'Bilge Kağan, Kül Tigin, Tonyukuk','Bumin Kağan, İstemi Yabgu, Mete Han','Mete Han, Teoman, Çiçi','Atilla, Bleda, Rua','Mukan Kağan, Tapo Kağan, Taspar Kağan','a'),(67,4,'',5,'Yerleşik hayata geçen, tarımla uğraşan ve Maniheizm dinini benimseyen ilk Türk devleti hangisidir?',1,'Uygurlar','Karluklar','Kırgızlar','Hazarlar','Peçenekler','a'),(68,4,'',5,'Museviliği resmi din olarak kabul eden tek Türk devleti aşağıdakilerden hangisidir?',1,'Hazarlar','Avarlar','Macarlar','Kıpçaklar','Bulgarlar','a'),(69,4,'',5,'Bizans ordusunda ücretli askerlik yaparken 1071 Malazgirt Savaşı\'nda Selçuklu tarafına geçen Türk toplulukları hangileridir?',1,'Peçenekler ve Uzlar','Avarlar ve Bulgarlar','Hazarlar ve Türgişler','Karluklar ve Yağmalar','Kıpçaklar ve Kumanlar','a'),(70,4,'',5,'Dünyanın en uzun destanı kabul edilen Manas Destanı hangi Türk topluluğuna aittir?',1,'Kırgızlar','Kazaklar','Uygurlar','Özbekler','Türkmenler','a'),(71,5,'',5,'İslamiyet öncesi Türk devletlerinde hükümdara yönetme yetkisinin Tanrı tarafından verildiğine inanılan anlayışa ne ad verilir?',1,'Kut Anlayışı','Töre','Kurultay','Yarlıg','Veraset','a'),(72,5,'',5,'Türk tarihinde ilk kez düzenli ordu teşkilatını (onluk sistem) kuran Türk hükümdarı kimdir?',1,'Mete Han','Teoman','Bumin Kağan','Bilge Kağan','Atilla','a'),(73,5,'',5,'İslamiyet öncesi Türk devletlerinde ölen kişinin ardından düzenlenen cenaze törenine ne ad verilir?',1,'Yuğ','Balbal','Kurgan','Uçmağ','Tamu','a'),(74,5,'',5,'Türk tarihinde kendi adına para bastıran ilk Türk hükümdarı ve devleti aşağıdakilerden hangisidir?',1,'Baga Tarkan - Türgişler','Bumin Kağan - Kök Türkler','Mete Han - Asya Hun','Kutluk Bilge Kül Kağan - Uygurlar','İlteriş Kağan - II. Kök Türk','a'),(75,5,'',5,'Türk adıyla kurulan ilk Türk devleti aşağıdakilerden hangisidir?',1,'Kök Türk Devleti','Asya Hun Devleti','Uygur Devleti','Avarlar','Hazarlar','a'),(76,5,'',5,'Orhun Yazıtları (Göktürk Kitabeleri) hangi hükümdar ve devlet adamları adına dikilmiştir?',1,'Bilge Kağan, Kül Tigin, Tonyukuk','Bumin Kağan, İstemi Yabgu, Mete Han','Mete Han, Teoman, Çiçi','Atilla, Bleda, Rua','Mukan Kağan, Tapo Kağan, Taspar Kağan','a'),(77,5,'',5,'Yerleşik hayata geçen, tarımla uğraşan ve Maniheizm dinini benimseyen ilk Türk devleti hangisidir?',1,'Uygurlar','Karluklar','Kırgızlar','Hazarlar','Peçenekler','a'),(78,5,'',5,'Museviliği resmi din olarak kabul eden tek Türk devleti aşağıdakilerden hangisidir?',1,'Hazarlar','Avarlar','Macarlar','Kıpçaklar','Bulgarlar','a'),(79,5,'',5,'Bizans ordusunda ücretli askerlik yaparken 1071 Malazgirt Savaşı\'nda Selçuklu tarafına geçen Türk toplulukları hangileridir?',1,'Peçenekler ve Uzlar','Avarlar ve Bulgarlar','Hazarlar ve Türgişler','Karluklar ve Yağmalar','Kıpçaklar ve Kumanlar','a'),(80,5,'',5,'Dünyanın en uzun destanı kabul edilen Manas Destanı hangi Türk topluluğuna aittir?',1,'Kırgızlar','Kazaklar','Uygurlar','Özbekler','Türkmenler','a'),(81,6,'',5,'İslamiyet öncesi Türk devletlerinde hükümdara yönetme yetkisinin Tanrı tarafından verildiğine inanılan anlayışa ne ad verilir?',1,'Kut Anlayışı','Töre','Kurultay','Yarlıg','Veraset','a'),(82,6,'',5,'Türk tarihinde ilk kez düzenli ordu teşkilatını (onluk sistem) kuran Türk hükümdarı kimdir?',1,'Mete Han','Teoman','Bumin Kağan','Bilge Kağan','Atilla','a'),(83,6,'',5,'İslamiyet öncesi Türk devletlerinde ölen kişinin ardından düzenlenen cenaze törenine ne ad verilir?',1,'Yuğ','Balbal','Kurgan','Uçmağ','Tamu','a'),(84,6,'',5,'Türk tarihinde kendi adına para bastıran ilk Türk hükümdarı ve devleti aşağıdakilerden hangisidir?',1,'Baga Tarkan - Türgişler','Bumin Kağan - Kök Türkler','Mete Han - Asya Hun','Kutluk Bilge Kül Kağan - Uygurlar','İlteriş Kağan - II. Kök Türk','a'),(85,6,'',5,'Türk adıyla kurulan ilk Türk devleti aşağıdakilerden hangisidir?',1,'Kök Türk Devleti','Asya Hun Devleti','Uygur Devleti','Avarlar','Hazarlar','a'),(86,6,'',5,'Orhun Yazıtları (Göktürk Kitabeleri) hangi hükümdar ve devlet adamları adına dikilmiştir?',1,'Bilge Kağan, Kül Tigin, Tonyukuk','Bumin Kağan, İstemi Yabgu, Mete Han','Mete Han, Teoman, Çiçi','Atilla, Bleda, Rua','Mukan Kağan, Tapo Kağan, Taspar Kağan','a'),(87,6,'',5,'Yerleşik hayata geçen, tarımla uğraşan ve Maniheizm dinini benimseyen ilk Türk devleti hangisidir?',1,'Uygurlar','Karluklar','Kırgızlar','Hazarlar','Peçenekler','a'),(88,6,'',5,'Museviliği resmi din olarak kabul eden tek Türk devleti aşağıdakilerden hangisidir?',1,'Hazarlar','Avarlar','Macarlar','Kıpçaklar','Bulgarlar','a'),(89,6,'',5,'Bizans ordusunda ücretli askerlik yaparken 1071 Malazgirt Savaşı\'nda Selçuklu tarafına geçen Türk toplulukları hangileridir?',1,'Peçenekler ve Uzlar','Avarlar ve Bulgarlar','Hazarlar ve Türgişler','Karluklar ve Yağmalar','Kıpçaklar ve Kumanlar','a'),(90,6,'',5,'Dünyanın en uzun destanı kabul edilen Manas Destanı hangi Türk topluluğuna aittir?',1,'Kırgızlar','Kazaklar','Uygurlar','Özbekler','Türkmenler','a');
/*!40000 ALTER TABLE `tbl_exam_module_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_exam_module_result`
--

DROP TABLE IF EXISTS `tbl_exam_module_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_exam_module_result` (
  `id` int NOT NULL AUTO_INCREMENT,
  `exam_module_id` int NOT NULL,
  `user_id` int NOT NULL,
  `obtained_marks` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `total_duration` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `statistics` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `status` int NOT NULL COMMENT '2-in_exam, 3-completed',
  `rules_violated` tinyint NOT NULL,
  `captured_question_ids` text COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exam_module_id` (`exam_module_id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_exam_module_result`
--

LOCK TABLES `tbl_exam_module_result` WRITE;
/*!40000 ALTER TABLE `tbl_exam_module_result` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_exam_module_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_fun_n_learn`
--

DROP TABLE IF EXISTS `tbl_fun_n_learn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_fun_n_learn` (
  `id` int NOT NULL AUTO_INCREMENT,
  `language_id` int NOT NULL DEFAULT '0',
  `category` int NOT NULL,
  `subcategory` int NOT NULL,
  `title` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `detail` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `status` int NOT NULL DEFAULT '0',
  `content_type` tinyint NOT NULL DEFAULT '0',
  `content_data` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category` (`category`),
  KEY `subcategory` (`subcategory`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_fun_n_learn`
--

LOCK TABLES `tbl_fun_n_learn` WRITE;
/*!40000 ALTER TABLE `tbl_fun_n_learn` DISABLE KEYS */;
INSERT INTO `tbl_fun_n_learn` VALUES (1,52,16,26,'İslamiyet Öncesi Türk Devlet Teşkilatı','İslamiyet öncesi Türk devletlerinde devlet hükümdar ve ailesinin ortak malı sayılırdı (Kut Anlayışı). Hükümdarın erkek çocuklarına Tigin denirdi. Devlet işleri Kurultay (Toy) adı verilen mecliste görüşülürdü. Kurultaya boy beyleri ve Hatun da katılırdı. Ordu onluk sisteme göre teşkilatlanmıştı.',1,0,'');
/*!40000 ALTER TABLE `tbl_fun_n_learn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_fun_n_learn_question`
--

DROP TABLE IF EXISTS `tbl_fun_n_learn_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_fun_n_learn_question` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fun_n_learn_id` int NOT NULL,
  `question` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `question_type` int NOT NULL COMMENT '1= normal, 2= true/false',
  `optiona` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optionb` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optionc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optiond` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optione` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `answer` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `image` varchar(250) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contest_id` (`fun_n_learn_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_fun_n_learn_question`
--

LOCK TABLES `tbl_fun_n_learn_question` WRITE;
/*!40000 ALTER TABLE `tbl_fun_n_learn_question` DISABLE KEYS */;
INSERT INTO `tbl_fun_n_learn_question` VALUES (1,1,'Türk devletlerinde hükümdarın erkek çocuklarına verilen unvan nedir?',1,'Tigin','Şad','Yabgu','Atabey','Melik','a',''),(2,1,'Devlet işlerinin görüşülüp karara bağlandığı meclise ne ad verilir?',1,'Kurultay (Toy)','Divan','Pankuş','Senato','Meclis-i Mebusan','a','');
/*!40000 ALTER TABLE `tbl_fun_n_learn_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_guess_the_word`
--

DROP TABLE IF EXISTS `tbl_guess_the_word`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_guess_the_word` (
  `id` int NOT NULL AUTO_INCREMENT,
  `language_id` int NOT NULL,
  `category` int NOT NULL,
  `subcategory` int NOT NULL,
  `image` text COLLATE utf8mb4_general_ci NOT NULL,
  `question` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `answer` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category` (`category`),
  KEY `subcategory` (`subcategory`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_guess_the_word`
--

LOCK TABLES `tbl_guess_the_word` WRITE;
/*!40000 ALTER TABLE `tbl_guess_the_word` DISABLE KEYS */;
INSERT INTO `tbl_guess_the_word` VALUES (1,52,19,29,'','İslamiyet öncesi Türklerde devlet işlerinin görüşüldüğü meclis','KURULTAY'),(2,52,19,29,'','Osmanlı Devleti\'nde toprağa ve üretime bağlı askeri sistem','TIMAR'),(3,52,19,29,'','Gök Tanrı tarafından hükümdara verilen kutsal yönetim yetkisi','KUT'),(4,52,19,29,'','Milli Mücadele\'de vatanın sınırlarını çizen tarihi antlaşma kararları','MISAKIMILLI'),(5,52,20,30,'','Bir adanın kıyı oku ile karaya bağlanmasıyla oluşan saplı ada','TOMBOLO'),(6,52,20,30,'','Akdeniz bölgesinde kalkerli arazide suların eritmesiyle oluşan şekil','KARSTIK'),(7,52,20,30,'','Akarsuyun denize döküldüğü yerde biriktirdiği alüvyon ovası','DELTA'),(8,52,21,31,'','Toplum düzenini sağlayan ve devlet gücüyle desteklenen kurallar bütünü','HUKUK'),(9,52,21,31,'','Devletin en üstün ve bağlayıcı temel yazılı kanunu','ANAYASA'),(10,52,21,31,'','İdarede halkın şikayetlerini inceleyen Kamu Denetçiliği makamı','OMBUDSMAN'),(14,52,1,0,'','Osmanlı Devleti\'nde padişahın mutlak vekili ve sadrazam mührü','MÜHÜR'),(15,52,1,0,'','Kurtuluş Savaşı\'nda vatanın sınırlarını çizen milli antlaşma kararları','MISAKIMILLI'),(16,52,1,0,'','İslamiyet öncesi Türk mezarlarına verilen ad','KURGAN'),(18,52,2,0,'','Akdeniz bölgesinde kalkerli arazide suların eritmesiyle oluşan yeryüzü şekli','KARSTIK'),(21,52,3,0,'','Devletin en üstün ve bağlayıcı temel kanunu','ANAYASA'),(22,52,3,0,'','İdarede halkın şikayetlerini inceleyen kamu denetçiliği kurumu','OMBUDSMAN');
/*!40000 ALTER TABLE `tbl_guess_the_word` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_languages`
--

DROP TABLE IF EXISTS `tbl_languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_languages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `language` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `code` varchar(11) NOT NULL,
  `status` tinyint NOT NULL DEFAULT '0' COMMENT '1=Enabled, 0=Disabled',
  `type` tinyint NOT NULL DEFAULT '0' COMMENT '1=active, 0=deactive',
  `default_active` tinyint NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_languages`
--

LOCK TABLES `tbl_languages` WRITE;
/*!40000 ALTER TABLE `tbl_languages` DISABLE KEYS */;
INSERT INTO `tbl_languages` VALUES (1,'Amharic','am',0,0,0),(2,'Arabic','ar',0,0,0),(3,'Basque','eu',0,0,0),(4,'Bengali','bn',0,0,0),(5,'English (UK)','en-GB',0,0,0),(6,'Portuguese (Brazil)','pt-BR',0,0,0),(7,'Bulgarian','bg',0,0,0),(8,'Catalan','ca',0,0,0),(9,'Cherokee','chr',0,0,0),(10,'Croatian','hr',0,0,0),(11,'Czech','cs',0,0,0),(12,'Danish','da',0,0,0),(13,'Dutch','nl',0,0,0),(14,'English (US)','en',0,0,0),(15,'Estonian','et',0,0,0),(16,'Filipino','fil',0,0,0),(17,'Finnish','fi',0,0,0),(18,'French','fr',0,0,0),(19,'Greek','el',0,0,0),(20,'Gujarati','gu',0,0,0),(21,'Hebrew','iw',0,0,0),(22,'Hindi','hi',0,0,0),(23,'Hungarian','hu',0,0,0),(24,'Icelandic','is',0,0,0),(25,'Indonesian','id',0,0,0),(26,'German','de',0,0,0),(27,'Italian','it',0,0,0),(28,'Japanese','ja',0,0,0),(29,'Kannada','kn',0,0,0),(30,'Korean','ko',0,0,0),(31,'Latvian','lv',0,0,0),(32,'Lithuanian','lt',0,0,0),(33,'Malay','ms',0,0,0),(34,'Malayalam','ml',0,0,0),(35,'Marathi','mr',0,0,0),(36,'Norwegian','no',0,0,0),(37,'Polish','pl',0,0,0),(38,'Portuguese (Portugal)','pt-PT',0,0,0),(39,'Romanian','ro',0,0,0),(40,'Russian','ru',0,0,0),(41,'Serbian','sr',0,0,0),(42,'Chinese (PRC)','zh-CN',0,0,0),(43,'Slovak','sk',0,0,0),(44,'Slovenian','sl',0,0,0),(45,'Spanish','es',0,0,0),(46,'Swahili','sw',0,0,0),(47,'Swedish','sv',0,0,0),(48,'Tamil','ta',0,0,0),(49,'Telugu','te',0,0,0),(50,'Thai','th',0,0,0),(51,'Chinese (Taiwan)','zh-TW',0,0,0),(52,'KPSS Lisans (GY-GK)','kpss_lis',1,1,1),(53,'Urdu','ur',0,0,0),(54,'Ukrainian','uk',0,0,0),(55,'Vietnamese','vi',0,0,0),(56,'Welsh','cy',0,0,0),(57,'KPSS Ön Lisans & Lise','kpss_onl',1,1,0),(58,'KPSS Alan Bilgisi (A)','kpss_aln',1,1,0),(59,'Hakimlik & Savcılık','hakimlik',1,1,0),(60,'HMGS (Hukuk Giriş)','hmgs',1,1,0),(61,'İcra Müdürlüğü','icra_mud',1,1,0),(62,'Kaymakamlık Adaylığı','kaymakam',1,1,0),(63,'Görevde Yükselme (GYS)','gys',1,1,0),(64,'Polislik (PAEM/POMEM)','polislik',1,1,0),(65,'Akademik (ALES/YDS)','ales_yds',1,1,0);
/*!40000 ALTER TABLE `tbl_languages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_leaderboard_daily`
--

DROP TABLE IF EXISTS `tbl_leaderboard_daily`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_leaderboard_daily` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `score` int NOT NULL,
  `date_created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`,`date_created`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_leaderboard_daily`
--

LOCK TABLES `tbl_leaderboard_daily` WRITE;
/*!40000 ALTER TABLE `tbl_leaderboard_daily` DISABLE KEYS */;
INSERT INTO `tbl_leaderboard_daily` VALUES (1,2,4850,'2026-09-06 20:02:32'),(2,3,4620,'2026-09-06 20:02:32'),(3,1,4242,'2026-09-06 20:02:32'),(4,4,3980,'2026-09-06 20:02:32'),(5,5,3640,'2026-09-06 20:02:32'),(6,6,3410,'2026-09-06 20:02:32'),(7,7,3100,'2026-09-06 20:02:32'),(8,8,2890,'2026-09-06 20:02:32'),(9,9,2650,'2026-09-06 20:02:32'),(10,10,2320,'2026-09-06 20:02:32');
/*!40000 ALTER TABLE `tbl_leaderboard_daily` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_leaderboard_monthly`
--

DROP TABLE IF EXISTS `tbl_leaderboard_monthly`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_leaderboard_monthly` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `score` int NOT NULL,
  `last_updated` datetime NOT NULL,
  `date_created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`,`date_created`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_leaderboard_monthly`
--

LOCK TABLES `tbl_leaderboard_monthly` WRITE;
/*!40000 ALTER TABLE `tbl_leaderboard_monthly` DISABLE KEYS */;
INSERT INTO `tbl_leaderboard_monthly` VALUES (1,2,4850,'2026-09-06 20:02:32','2026-09-06 20:02:32'),(2,3,4620,'2026-09-06 20:02:32','2026-09-06 20:02:32'),(3,1,4242,'2026-09-06 23:17:05','2026-09-06 20:02:32'),(4,4,3980,'2026-09-06 20:02:32','2026-09-06 20:02:32'),(5,5,3640,'2026-09-06 20:02:32','2026-09-06 20:02:32'),(6,6,3410,'2026-09-06 20:02:32','2026-09-06 20:02:32'),(7,7,3100,'2026-09-06 20:02:32','2026-09-06 20:02:32'),(8,8,2890,'2026-09-06 20:02:32','2026-09-06 20:02:32'),(9,9,2650,'2026-09-06 20:02:32','2026-09-06 20:02:32'),(10,10,2320,'2026-09-06 20:02:32','2026-09-06 20:02:32');
/*!40000 ALTER TABLE `tbl_leaderboard_monthly` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_level`
--

DROP TABLE IF EXISTS `tbl_level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_level` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `category` int NOT NULL,
  `subcategory` int NOT NULL,
  `level` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `category` (`category`),
  KEY `subcategory` (`subcategory`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_level`
--

LOCK TABLES `tbl_level` WRITE;
/*!40000 ALTER TABLE `tbl_level` DISABLE KEYS */;
INSERT INTO `tbl_level` VALUES (1,1,1,1,2);
/*!40000 ALTER TABLE `tbl_level` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_maths_question`
--

DROP TABLE IF EXISTS `tbl_maths_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_maths_question` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` int NOT NULL,
  `subcategory` int NOT NULL,
  `language_id` int NOT NULL DEFAULT '0',
  `image` varchar(512) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `question` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `question_type` tinyint NOT NULL COMMENT '1=normal, 2=true/false',
  `optiona` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optionb` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optionc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optiond` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optione` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `answer` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `note` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category` (`category`),
  KEY `subcategory` (`subcategory`) USING BTREE,
  KEY `language_id` (`language_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_maths_question`
--

LOCK TABLES `tbl_maths_question` WRITE;
/*!40000 ALTER TABLE `tbl_maths_question` DISABLE KEYS */;
INSERT INTO `tbl_maths_question` VALUES (1,22,32,52,'','Ardışık 5 tek sayının toplamı 85 olduğuna göre bu sayıların en büyüğü kaçtır?',1,'21','19','17','23','25','a','Ortanca sayı 85 / 5 = 17. Sayılar: 13, 15, 17, 19, 21.'),(2,22,32,52,'','Bir sayının 3 katının 5 eksiği 40 olduğuna göre bu sayı kaçtır?',1,'15','12','18','20','14','a','3x - 5 = 40 => 3x = 45 => x = 15.'),(3,22,32,52,'','Bir sınıftaki öğrencilerin %60ı erkektir. 12 kız olduğuna göre sınıf mevcudu kaçtır?',1,'30','25','35','40','50','a','Kızlar %40. 0.40 * x = 12 => x = 30.'),(4,22,32,52,'','Bir babanın yaşı oğlunun yaşının 4 katıdır. 5 yıl sonra 3 katı olacağına göre çocuk bugün kaç yaşındadır?',1,'10','8','12','14','15','a','4x + 5 = 3(x + 5) => x = 10.'),(5,22,32,52,'','200 TL maliyetli bir ürün %30 kârla kaç TLye satılır?',1,'260 TL','230 TL','250 TL','270 TL','280 TL','a','200 * 1.30 = 260 TL.'),(6,22,32,52,'','Ardışık 5 tek sayının toplamı 85 olduğuna göre bu sayıların en büyüğü kaçtır?',1,'21','19','17','23','25','a','Ortanca sayı 85 / 5 = 17. Sayılar: 13, 15, 17, 19, 21.'),(7,22,32,52,'','Bir sayının 3 katının 5 eksiği 40 olduğuna göre bu sayı kaçtır?',1,'15','12','18','20','14','a','3x - 5 = 40 => 3x = 45 => x = 15.'),(8,22,32,52,'','Bir sınıftaki öğrencilerin %60ı erkektir. 12 kız olduğuna göre sınıf mevcudu kaçtır?',1,'30','25','35','40','50','a','Kızlar %40. 0.40 * x = 12 => x = 30.'),(9,22,32,52,'','Bir babanın yaşı oğlunun yaşının 4 katıdır. 5 yıl sonra 3 katı olacağına göre çocuk bugün kaç yaşındadır?',1,'10','8','12','14','15','a','4x + 5 = 3(x + 5) => x = 10.'),(10,22,32,52,'','200 TL maliyetli bir ürün %30 kârla kaç TLye satılır?',1,'260 TL','230 TL','250 TL','270 TL','280 TL','a','200 * 1.30 = 260 TL.');
/*!40000 ALTER TABLE `tbl_maths_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_month_week`
--

DROP TABLE IF EXISTS `tbl_month_week`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_month_week` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `type` int NOT NULL COMMENT '1=month,2=week',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_month_week`
--

LOCK TABLES `tbl_month_week` WRITE;
/*!40000 ALTER TABLE `tbl_month_week` DISABLE KEYS */;
INSERT INTO `tbl_month_week` VALUES (1,'January',1),(2,'February',1),(3,'March',1),(4,'April',1),(5,'May',1),(6,'June',1),(7,'July',1),(8,'August',1),(9,'September',1),(10,'October',1),(11,'November',1),(12,'December',1),(13,'Sunday',2),(14,'Monday',2),(15,'Tuesday',2),(16,'Wednesday',2),(17,'Thursday',2),(18,'Friday',2),(19,'Saturday',2);
/*!40000 ALTER TABLE `tbl_month_week` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_multi_match`
--

DROP TABLE IF EXISTS `tbl_multi_match`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_multi_match` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` int NOT NULL,
  `subcategory` int NOT NULL,
  `language_id` int NOT NULL DEFAULT '0',
  `image` varchar(250) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `question` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `question_type` tinyint NOT NULL COMMENT '1=normal, 2=true/false',
  `optiona` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optionb` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optionc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optiond` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optione` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `answer_type` tinyint NOT NULL COMMENT '1=multiselect,2=sequence',
  `answer` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `level` int NOT NULL,
  `note` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category` (`category`),
  KEY `subcategory` (`subcategory`) USING BTREE,
  KEY `language_id` (`language_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_multi_match`
--

LOCK TABLES `tbl_multi_match` WRITE;
/*!40000 ALTER TABLE `tbl_multi_match` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_multi_match` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_multi_match_level`
--

DROP TABLE IF EXISTS `tbl_multi_match_level`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_multi_match_level` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `category` int NOT NULL,
  `subcategory` int NOT NULL,
  `level` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `category` (`category`),
  KEY `subcategory` (`subcategory`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_multi_match_level`
--

LOCK TABLES `tbl_multi_match_level` WRITE;
/*!40000 ALTER TABLE `tbl_multi_match_level` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_multi_match_level` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_multi_match_question_reports`
--

DROP TABLE IF EXISTS `tbl_multi_match_question_reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_multi_match_question_reports` (
  `id` int NOT NULL AUTO_INCREMENT,
  `question_id` int NOT NULL,
  `user_id` int NOT NULL,
  `message` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `question_id` (`question_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_multi_match_question_reports`
--

LOCK TABLES `tbl_multi_match_question_reports` WRITE;
/*!40000 ALTER TABLE `tbl_multi_match_question_reports` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_multi_match_question_reports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_notifications`
--

DROP TABLE IF EXISTS `tbl_notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_notifications` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `users` varchar(8) NOT NULL DEFAULT 'all',
  `user_id` longtext,
  `type` varchar(250) NOT NULL,
  `type_id` int NOT NULL,
  `image` varchar(128) NOT NULL,
  `date_sent` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_notifications`
--

LOCK TABLES `tbl_notifications` WRITE;
/*!40000 ALTER TABLE `tbl_notifications` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_payment_request`
--

DROP TABLE IF EXISTS `tbl_payment_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_payment_request` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `uid` text COLLATE utf8mb4_general_ci NOT NULL,
  `payment_type` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `payment_address` varchar(225) COLLATE utf8mb4_general_ci NOT NULL,
  `payment_amount` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `coin_used` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `details` text COLLATE utf8mb4_general_ci NOT NULL,
  `status` tinyint NOT NULL COMMENT '0-pending, 1-completed, 2-invalid details',
  `date` datetime NOT NULL,
  `status_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_payment_request`
--

LOCK TABLES `tbl_payment_request` WRITE;
/*!40000 ALTER TABLE `tbl_payment_request` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_payment_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_question`
--

DROP TABLE IF EXISTS `tbl_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_question` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` int NOT NULL,
  `subcategory` int NOT NULL,
  `language_id` int NOT NULL DEFAULT '0',
  `image` varchar(512) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `question` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `question_type` tinyint NOT NULL COMMENT '1=normal, 2=true/false',
  `optiona` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optionb` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optionc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optiond` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `optione` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `answer` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `level` int NOT NULL,
  `note` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category` (`category`),
  KEY `subcategory` (`subcategory`) USING BTREE,
  KEY `language_id` (`language_id`)
) ENGINE=MyISAM AUTO_INCREMENT=257 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_question`
--

LOCK TABLES `tbl_question` WRITE;
/*!40000 ALTER TABLE `tbl_question` DISABLE KEYS */;
INSERT INTO `tbl_question` VALUES (1,1,1,52,'','İslamiyet öncesi Türk devletlerinde devlet işlerinin görüşülüp karara bağlandığı meclise ne ad verilir?',1,'Toy (Kurultay)','Tigin','Şad','Tamgacı','Yargu','a',1,'İslamiyet öncesi Türklerde hükümdar başkanlığında toplanan danışma ve karar meclisine Toy veya Kurultay adı verilir.'),(2,1,1,52,'','Tarihte bilinen ilk Türk devleti aşağıdakilerden hangisidir?',1,'Asya Hun Devleti','Göktürkler','Uygurlar','Avarlar','Hazarlar','a',1,'Tarihte teşkilatlı ilk Türk devleti Teoman önderliğinde kurulan Asya Hun Devleti dir.'),(3,1,3,52,'','Osmanlı Devleti\'nde ilk gümüş akçe hangi padişah döneminde bastırılmıştır?',1,'Osman Bey','Orhan Bey','I. Murad','Yıldırım Bayezid','Fatih Sultan Mehmet','b',1,'İlk bakır para Osman Bey, ilk gümüş akçe Orhan Bey, ilk altın para ise Fatih Sultan Mehmet döneminde bastırılmıştır.'),(4,1,5,52,'','Kurtuluş Savaşı\'nda Milli Mücadele\'nin amaç, gerekçe ve yöntemi ilk kez nerede ilan edilmiştir?',1,'Amasya Genelgesi','Erzurum Kongresi','Sivas Kongresi','Havza Genelgesi','Misak-ı Milli','a',1,'Amasya Genelgesi (22 Haziran 1919) ile milletin bağımsızlığını yine milletin azim ve kararının kurtaracağı vurgulanarak yöntem ve amaç belirlenmiştir.'),(5,1,6,52,'','Mustafa Kemal Paşa\'ya TBMM tarafından Gazilik unvanı ve Mareşallik rütbesi hangi zaferden sonra verilmiştir?',1,'Sakarya Meydan Muharebesi','I. İnönü Zaferi','Büyük Taarruz','Çanakkale Savaşı','II. İnönü Zaferi','a',1,'19 Eylül 1921 tarihinde Sakarya Zaferi sonrasında TBMM tarafından Mustafa Kemal Paşa ya Mareşallik ve Gazilik unvanı verilmiştir.'),(6,2,8,52,'','Türkiye\'nin en doğusu ile en batısı arasında kaç dakikalık yerel saat farkı vardır?',1,'76 dakika','56 dakika','60 dakika','80 dakika','90 dakika','a',1,'Türkiye 26° - 45° Doğu meridyenleri arasında yer alır. 45 - 26 = 19 meridyen x 4 dakika = 76 dakika yerel saat farkı bulunur.'),(7,2,9,52,'','Türkiye\'nin en yüksek zirvesi olan Ağrı Dağı jeolojik yapısı bakımından hangi tür dağdır?',1,'Volkanik Dağ','Kıvrım Dağı','Kırık Dağı (Horst)','Karstik Kütle','Buzul Kütlesi','a',1,'Ağrı Dağı (5137 m) sönmüş bir volkanik stratovolkandır.'),(8,2,10,52,'','Akdeniz iklim kuşağında kalkerli araziler üzerinde oluşan karakteristik kırmızı renkli toprak tipi hangisidir?',1,'Terra Rossa','Çernezyom','Podzol','Alüvyal','Regosol','a',1,'Terra Rossa, Akdeniz iklim bölgesinde kireçtaşları üzerinde çözünmeyle oluşan demir oksitçe zengin kırmızı renkli zonal topraktır.'),(9,3,13,52,'','1982 Anayasası\'na göre Türkiye Büyük Millet Meclisi üye tamsayısı kaçtır?',1,'600','550','500','450','650','a',1,'2017 anayasa değişikliği ile TBMM milletvekili sayısı 550 den 600 e çıkarılmıştır.'),(10,3,14,52,'','1982 Anayasası\'na göre Anayasa Mahkemesi kaç üyeden oluşmaktadır?',1,'15','17','11','12','21','a',1,'2017 anayasa değişikliği ile askeri mahkemeler kaldırılmış ve AYM üye sayısı 17 den 15 e düşürülmüştür.'),(11,3,14,52,'','Kanunlarda yürürlüğe giriş tarihi belirtilmemişse, Resmi Gazete\'de yayımlandığı tarihten itibaren ne zaman yürürlüğe girer?',1,'Yayımlandığı gün','45 gün sonra','30 gün sonra','Ertesi gün','15 gün sonra','a',1,'703 sayılı KHK uyarınca aksi belirtilmemişse kanunlar Resmi Gazete de yayımlandığı gün yürürlüğe girer.'),(12,4,18,52,'','Aşağıdaki cümlelerin hangisinde büyük harflerin yazımıyla ilgili bir yanlışlık yapılmıştır?',1,'Dicle nehri Güneydoğu ya bereket taşır.','Kurtuluş Savaşı tarihimizin dönüm noktasıdır.','Resmî Gazete de yayımlanan karar yürürlüğe girdi.','Van Gölü Türkiye nin en büyük gölüdür.','Ankara Kalesi tarihi bir mirastır.','a',1,'Özel ada dahil olan deniz, nehir, göl, dağ adları büyük harfle başlar: Dicle Nehri şeklinde yazılmalıdır.'),(13,4,19,52,'','\'Ayağını yorganına göre uzat\' atasözünün temel öğüdü aşağıdakilerden hangisidir?',1,'Giderlerini gelirine göre ayarlamak','Geleceğe yatırım yapmak','Başkalarına borç vermekten kaçınmak','Zor günlere hazırlıklı olmak','Tutumlu ve cimri olmak','a',1,'Ayağını yorganına göre uzat; giderini gelirine uydurmak, bütçeni aşmamak anlamında kullanılır.'),(14,6,0,61,'','İcra ve İflas Kanunu\'na göre ilamsız icra takibinde borçlunun ödeme emrine itiraz süresi kural olarak kaç gündür?',1,'7 gün','10 gün','15 gün','30 gün','5 gün','a',1,'İİK m. 62 uyarınca genel haciz yoluyla ilamsız takipte borçlu ödeme emrinin tebliğinden itibaren 7 gün içinde itiraz edebilir.'),(15,6,0,61,'','Kambiyo senetlerine özgü haciz yolunda borçlunun borca veya imzaya itiraz süresi kaç gündür?',1,'5 gün','7 gün','10 gün','15 gün','3 gün','a',1,'İİK m. 168 uyarınca kambiyo senetlerine mahsus haciz yolunda borca ve imzaya itiraz süresi tebliğden itibaren 5 gündür.'),(16,11,0,59,'','İdari Yargılama Usulü Kanunu\'na (İYUK) göre Danıştay ve İdare Mahkemelerinde genel dava açma süresi kaç gündür?',1,'Danıştay 60, İdare 60 gün','Danıştay 60, İdare 30 gün','Danıştay 30, İdare 60 gün','Her ikisinde de 30 gün','Her ikisinde de 90 gün','a',1,'İYUK m. 7 uyarınca genel dava açma süresi Danıştay da ve İdare Mahkemelerinde 60 gün, Vergi Mahkemelerinde ise 30 gündür.'),(17,1,1,52,'','İslamiyet öncesi Türk devletlerinde hükümdara yönetme yetkisinin Tanrı tarafından verildiğine inanılan anlayışa ne ad verilir?',1,'Kut Anlayışı','Töre','Kurultay','Yarlıg','Veraset','a',1,'Kut, Gök Tanrı tarafından hükümdara ve onun hanedanına verilen yönetme yetkisidir.'),(18,1,1,52,'','Türk tarihinde ilk kez düzenli ordu teşkilatını (onluk sistem) kuran Türk hükümdarı kimdir?',1,'Mete Han','Teoman','Bumin Kağan','Bilge Kağan','Atilla','a',1,'MÖ 209 yılında Asya Hun İmparatoru Mete Han onluk ordu sistemini kurmuştur.'),(19,1,1,52,'','İslamiyet öncesi Türk devletlerinde ölen kişinin ardından düzenlenen cenaze törenine ne ad verilir?',1,'Yuğ','Balbal','Kurgan','Uçmağ','Tamu','a',1,'Yuğ törenlerinde ölenin ardından sagu (ağıt) yakılırdı.'),(20,1,1,52,'','Türk tarihinde kendi adına para bastıran ilk Türk hükümdarı ve devleti aşağıdakilerden hangisidir?',1,'Baga Tarkan - Türgişler','Bumin Kağan - Kök Türkler','Mete Han - Asya Hun','Kutluk Bilge Kül Kağan - Uygurlar','İlteriş Kağan - II. Kök Türk','a',1,'Türgiş hükümdarı Baga Tarkan adına madeni para (yarmak) bastırmıştır.'),(21,1,1,52,'','Türk adıyla kurulan ilk Türk devleti aşağıdakilerden hangisidir?',1,'Kök Türk Devleti','Asya Hun Devleti','Uygur Devleti','Avarlar','Hazarlar','a',1,'Bumin Kağan tarafından 552 yılında kurulan I. Kök Türk Devleti, Türk adını resmi olarak kullanan ilk devlettir.'),(22,1,1,52,'','Orhun Yazıtları (Göktürk Kitabeleri) hangi hükümdar ve devlet adamları adına dikilmiştir?',1,'Bilge Kağan, Kül Tigin, Tonyukuk','Bumin Kağan, İstemi Yabgu, Mete Han','Mete Han, Teoman, Çiçi','Atilla, Bleda, Rua','Mukan Kağan, Tapo Kağan, Taspar Kağan','a',1,'Orhun Abideleri; Vezir Tonyukuk, Kül Tigin ve Bilge Kağan adına dikilmiştir.'),(23,1,1,52,'','Yerleşik hayata geçen, tarımla uğraşan ve Maniheizm dinini benimseyen ilk Türk devleti hangisidir?',1,'Uygurlar','Karluklar','Kırgızlar','Hazarlar','Peçenekler','a',1,'Bögü Kağan döneminde Maniheizmi kabul eden Uygurlar yerleşik hayata geçen ilk Türk devletidir.'),(24,1,1,52,'','Museviliği resmi din olarak kabul eden tek Türk devleti aşağıdakilerden hangisidir?',1,'Hazarlar','Avarlar','Macarlar','Kıpçaklar','Bulgarlar','a',1,'Kafkaslar ve Karadeniz\'in kuzeyinde hüküm süren Hazarlar Museviliği benimsemiştir.'),(25,1,1,52,'','Bizans ordusunda ücretli askerlik yaparken 1071 Malazgirt Savaşı\'nda Selçuklu tarafına geçen Türk toplulukları hangileridir?',1,'Peçenekler ve Uzlar','Avarlar ve Bulgarlar','Hazarlar ve Türgişler','Karluklar ve Yağmalar','Kıpçaklar ve Kumanlar','a',1,'Peçenekler ve Uzlar (Oğuzlar) Malazgirt Savaşı sırasında Büyük Selçuklu ordusuna katılmıştır.'),(26,1,1,52,'','Dünyanın en uzun destanı kabul edilen Manas Destanı hangi Türk topluluğuna aittir?',1,'Kırgızlar','Kazaklar','Uygurlar','Özbekler','Türkmenler','a',1,'Manas Destanı Kırgız Türklerine ait olup yaşayan en uzun destandır.'),(27,1,2,52,'','İslamiyeti kabul eden ilk Türk boyu aşağıdakilerden hangisidir?',1,'Karluklar','Yağmalar','Çiğiller','Tuhsiler','Oğuzlar','a',1,'Karluklar, 751 Talas Savaşı sonrası İslamiyeti topluca kabul eden ilk Türk boyudur.'),(28,1,2,52,'','Orta Asya\'da kurulan ilk Müslüman Türk devleti aşağıdakilerden hangisidir?',1,'Karahanlılar','Gazneliler','Büyük Selçuklular','Tolunoğulları','İhşidiler','a',1,'Satuk Buğra Han döneminde İslamiyeti kabul eden Karahanlılar, Orta Asya\'daki ilk Türk-İslam devletidir.'),(29,1,2,52,'','Kaşgarlı Mahmut tarafından yazılan ve ilk Türkçe sözlük niteliği taşıyan eser hangisidir?',1,'Divânu Lugâti\'t-Türk','Kutadgu Bilig','Atabetü\'l-Hakayık','Divan-ı Hikmet','Şehnâme','a',1,'Divânu Lugâti\'t-Türk, Araplara Türkçeyi öğretmek amacıyla Kaşgarlı Mahmut tarafından yazılmıştır.'),(30,1,2,52,'','Yusuf Has Hacip tarafından Karahanlı hükümdarı Tabgaç Buğra Han\'a sunulan \'mutluluk veren bilgi\' anlamına gelen siyasetname eseri hangisidir?',1,'Kutadgu Bilig','Divan-ı Hikmet','Atabetü\'l-Hakayık','Siyasetnâme','Risaletü\'n-Nushiyye','a',1,'Kutadgu Bilig, Türk-İslam edebiyatının ilk yazılı ve ilk siyasetname niteliğindeki eseridir.'),(31,1,2,52,'','Mısır\'da kurulan ilk Türk-İslam devleti aşağıdakilerden hangisidir?',1,'Tolunoğulları','İhşidiler (Akşitler)','Eyyubiler','Memlükler','Fatımiler','a',1,'Ahmet bin Tolun tarafından kurulan Tolunoğulları Mısır\'da kurulan ilk Türk devletidir.'),(32,1,2,52,'','Hicaz bölgesine (Mekke ve Medine) hakim olan ilk Türk devleti aşağıdakilerden hangisidir?',1,'İhşidiler (Akşitler)','Tolunoğulları','Eyyubiler','Büyük Selçuklular','Osmanlı Devleti','a',1,'Muhammed bin Toğaç tarafından kurulan İhşidiler Kutsal Topraklara hakim olan ilk Türk devletidir.'),(33,1,2,52,'','Sultan unvanını kullanan ilk Türk hükümdarı aşağıdakilerden hangisidir?',1,'Gazneli Mahmut','Alparslan','Tuğrul Bey','Satuk Buğra Han','Melikşah','a',1,'Gazneli Mahmut, Hindistan seferleri sonrası Abbasi halifesi tarafından Sultan unvanı verilen ilk Türk hükümdarıdır.'),(34,1,2,52,'','Anadolu\'nun kapılarını Türklere kesin olarak açan 1071 Malazgirt Savaşı hangi Selçuklu sultanı döneminde kazanılmıştır?',1,'Sultan Alparslan','Tuğrul Bey','Sultan Sencer','Melikşah','Çağrı Bey','a',1,'Sultan Alparslan, Bizans İmparatoru Romen Diyojen\'i mağlup ederek Anadolu\'nun fethini başlatmıştır.'),(35,1,2,52,'','Anadolu\'da kurulan ilk Türk beyliği aşağıdakilerden hangisidir?',1,'Saltuklular','Danişmentliler','Mengücekliler','Artuklular','Çaka Beyliği','a',1,'Erzurum ve çevresinde kurulan Saltuklular, Malazgirt sonrası kurulan ilk Türk beyliğidir.'),(36,1,2,52,'','Anadolu\'nun Türk yurdu olduğunu kesinleştiren ve Bizans\'ın Türkleri Anadolu\'dan atma ümidini bitiren savaş hangisidir?',1,'Miryokefalon Savaşı (1176)','Malazgirt Savaşı (1071)','Pasinler Savaşı (1048)','Dandanakan Savaşı (1040)','Yassıçemen Savaşı (1230)','a',1,'II. Kılıç Arslan komutasında kazanılan Miryokefalon Savaşı ile Anadolu kesin olarak Türk yurdu olmuştur.'),(37,1,3,52,'','Osmanlı Devleti\'nin Rumeli\'de fethettiği ilk toprak ve ilk askeri üs hangisidir?',1,'Çimpe Kalesi','Edirne','Gelibolu','Filibe','Varna','a',1,'Orhan Bey döneminde Bizans\'a yapılan yardım karşılığında Çimpe Kalesi üs olarak alınmıştır.'),(38,1,3,52,'','Osmanlı Devleti\'nde ilk düzenli ordu olan \'Yaya ve Müsellem\' teşkilatı hangi padişah zamanında kurulmuştur?',1,'Orhan Bey','Osman Bey','I. Murat','Yıldırım Bayezid','II. Murat','a',1,'Orhan Gazi döneminde fetihlerin hızlanmasıyla ilk düzenli ordu kurulmuştur.'),(39,1,3,52,'','Osmanlı tarihinde ilk kez Haçlı ordusuna karşı kazanılan savaş aşağıdakilerden hangisidir?',1,'Sırpsındığı Savaşı (1364)','I. Kosova Savaşı','Niğbolu Savaşı','Varna Savaşı','Koyunhisar Savaşı','a',1,'I. Murat döneminde 1364 yılında yapılan Sırpsındığı Savaşı ilk Osmanlı-Haçlı savaşıdır.'),(40,1,3,52,'','Osmanlı Devleti\'nin 1402 Ankara Savaşı sonrası girdiği 11 yıllık taht kavgaları dönemine ne ad verilir?',1,'Fetret Devri','Lale Devri','Duraklama Dönemi','Tanzimat Dönemi','Meşrutiyet Dönemi','a',1,'Çelebi Mehmet tahta çıkarak Fetret Devri\'ne son vermiş ve devletin ikinci kurucusu sayılmıştır.'),(41,1,3,52,'','İstanbul\'un fethinin dünya tarihi açısından en önemli sonucu aşağıdakilerden hangisidir?',1,'Orta Çağ\'ın kapanıp Yeni Çağ\'ın başlaması','İpek Yolu\'nun kontrolünün geçmesi','Fener Rum Patrikhanesi\'nin himaye edilmesi','Topların surları yıkabileceğinin görülmesi','Bizans\'ın yıkılması','a',1,'İstanbul\'un fethi evrensel ölçekte Orta Çağ\'ı bitirip Yeni Çağ\'ı başlatmıştır.'),(42,1,3,52,'','Osmanlı Devleti\'nde Halifelik makamı hangi padişahın Mısır Seferi (Mercidabık ve Ridaniye) sonucunda Osmanlı\'ya geçmiştir?',1,'Yavuz Sultan Selim','Fatih Sultan Mehmet','Kanuni Sultan Süleyman','II. Bayezid','II. Selim','a',1,'1516 Mercidabık ve 1517 Ridaniye Savaşları ile Memlük Devleti yıkılmış ve halifelik Osmanlı\'ya geçmiştir.'),(43,1,3,52,'','Akdeniz\'i bir Türk gölü haline getiren 1538 Preveze Deniz Zaferi\'ni kazanan ünlü Osmanlı kaptan-ı deryası kimdir?',1,'Barbaros Hayrettin Paşa','Piri Reis','Turgut Reis','Seydi Ali Reis','Oruç Reis','a',1,'Barbaros Hayrettin Paşa, Andrea Doria komutasındaki Haçlı donanmasını Preveze\'de bozguna uğratmıştır.'),(44,1,3,52,'','Avusturya Arşidükü\'nün protokolde Osmanlı Sadrazamına denk sayıldığı ve Osmanlı\'nın Avrupa\'da siyasi üstünlük kazandığı antlaşma hangisidir?',1,'1533 İstanbul (İbrahim Paşa) Antlaşması','1606 Zitvatorok Antlaşması','1699 Karlofça Antlaşması','1718 Pasarofça Antlaşması','1739 Belgrad Antlaşması','a',1,'1533 İstanbul Antlaşması ile Avusturya kralı Osmanlı sadrazamına denk kabul edilmiştir.'),(45,1,3,52,'','Osmanlı Devleti\'nin doğuda en geniş sınırlara ulaştığı antlaşma aşağıdakilerden hangisidir?',1,'1590 Ferhat Paşa Antlaşması','1639 Kasr-ı Şirin Antlaşması','1612 Nasuh Paşa Antlaşması','1618 Serav Antlaşması','1555 Amasya Antlaşması','a',1,'III. Murat döneminde Safevilerle imzalanan Ferhat Paşa Antlaşması doğudaki en geniş sınırlardır.'),(46,1,3,52,'','Bugünkü Türkiye-İran sınırının temelini büyük ölçüde belirleyen 1639 tarihli antlaşma hangisidir?',1,'Kasr-ı Şirin Antlaşması','Ferhat Paşa Antlaşması','Amasya Antlaşması','Nasuh Paşa Antlaşması','Bucaş Antlaşması','a',1,'IV. Murat\'ın Bağdat Seferi sonrası imzalanan Kasr-ı Şirin Antlaşması bugünkü sınırın temelidir.'),(47,1,4,52,'','Osmanlı Devleti\'nde padişahtan sonra en yetkili devlet adamı ve padişahın mutlak vekili kimdir?',1,'Sadrazam (Vezir-i Azam)','Şeyhülislam','Kazasker','Defterdar','Nişancı','a',1,'Sadrazam padişahın mührünü (mühr-i hümayun) taşır ve padişah adına devleti yönetir.'),(48,1,4,52,'','Divan-ı Hümayun\'da adalet ve eğitim işlerine bakan, kadı ve müderrislerin atamasını yapan görevli kimdir?',1,'Kazasker','Nişancı','Defterdar','Reisülküttap','Şeyhülislam','a',1,'Kazasker (Kadıasker) adalet ve eğitim teşkilatının başıdır, kadıları ve müderrisleri tayin eder.'),(49,1,4,52,'','Osmanlı Devleti\'nde fethedilen toprakların tahrir defterlerine kaydını yapan ve padişahın tuğrasını çeken divan üyesi kimdir?',1,'Nişancı','Defterdar','Reisülküttap','Kaptan-ı Derya','Sadrazam','a',1,'Nişancı iç ve dış yazışmaları yönetir, fermanlara tuğra çeker ve tahrir kayıtlarını tutar.'),(50,1,4,52,'','Osmanlı maliyesinin başında bulunan, gelir ve gider dengesini sağlayan ve bütçeyi hazırlayan divan üyesi kimdir?',1,'Defterdar','Nişancı','Sadrazam','Kazasker','Reisülküttap','a',1,'Defterdar devletin mali işlerini ve hazinesini yönetir.'),(51,1,4,52,'','Osmanlı Devleti\'nde Kapıkulu Ocaklarına asker yetiştirmek amacıyla gayrimüslim çocukların toplanıp eğitilmesi sistemine ne ad verilir?',1,'Devşirme Sistemi','Tımar Sistemi','İltizam Sistemi','Malikane Sistemi','Müsadere Sistemi','a',1,'Devşirme sistemi ile Acemi Ocağı ve Enderun Mektebi\'ne asker ve devlet adamı yetiştirilmiştir.'),(52,1,4,52,'','Devlet adamı yetiştirmek üzere Topkapı Sarayı içinde kurulan saray okuluna ne ad verilir?',1,'Enderun','Birun','Harem','Medrese','Darülfünun','a',1,'Enderun Mektebi, devşirmelerin üst düzey bürokrat ve yönetici olarak yetiştirildiği saray okuludur.'),(53,1,4,52,'','Geliri doğrudan padişah kızlarına ve hanımlarına ayrılan dirlik toprağına ne ad verilir?',1,'Paşmaklık','Malikane','Yurtluk','Ocaklık','Vakıf','a',1,'Paşmaklık arazisinin gelirleri saray kadınlarının masraflarına tahsis edilirdi.'),(54,1,4,52,'','Osmanlı Devleti\'nde devletin haksız kazanç sağlayan memurların mallarına el koyma usulüne ne ad verilir?',1,'Müsadere','İltizam','Mukataa','Ayanlık','Dirlik','a',1,'Müsadere usulü II. Mahmut döneminde kaldırılmış, Tanzimat Fermanı ile güvence altına alınmıştır.'),(55,1,4,52,'','Yeniçerilerin üç ayda bir aldıkları maaşa ne ad verilir?',1,'Ulufe','Cülus','İhsan','Dirlik','Bahşiş','a',1,'Yeniçeriler ve Kapıkulu askerleri üç ayda bir ulufe maaşı alırlardı.'),(56,1,4,52,'','Mimar Sinan\'ın \'Çıraklık, Kalfalık ve Ustalık\' eserleri sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',1,'Şehzade Camii - Süleymaniye Camii - Selimiye Camii','Süleymaniye Camii - Selimiye Camii - Şehzade Camii','Selimiye Camii - Süleymaniye Camii - Şehzade Camii','Sultanahmet Camii - Selimiye Camii - Süleymaniye Camii','Fatih Camii - Şehzade Camii - Selimiye Camii','a',1,'Sinan; Şehzade Camii\'ni çıraklık, Süleymaniye\'yi kalfalık, Edirne Selimiye\'yi ise ustalık eseri olarak nitelendirmiştir.'),(57,1,5,52,'','Milli Mücadele\'nin gerekçesi, amacı ve yönteminin ilk kez belirtildiği tarihi belge hangisidir?',1,'Amasya Genelgesi','Havza Genelgesi','Erzurum Kongresi','Sivas Kongresi','Misakımilli','a',1,'\'Milletin bağımsızlığını yine milletin azim ve kararı kurtaracaktır\' maddesi Amasya Genelgesi\'ndedir.'),(58,1,5,52,'','Toplanış amacı bakımından bölgesel ancak aldığı kararlar bakımından ulusal nitelik taşıyan kongre hangisidir?',1,'Erzurum Kongresi','Sivas Kongresi','Amasya Genelgesi','Balıkesir Kongresi','Alaşehir Kongresi','a',1,'Erzurum Kongresi Doğu illeri için toplanmış fakat tüm yurdu ilgilendiren kararlar almıştır.'),(59,1,5,52,'','Manda ve himayenin kesin olarak reddedildiği ve tüm cemiyetlerin tek çatı altında birleştirildiği kongre hangisidir?',1,'Sivas Kongresi','Erzurum Kongresi','Havza Genelgesi','Afyon Kongresi','Pozantı Kongresi','a',1,'Sivas Kongresi\'nde manda kesin reddedilmiş ve cemiyetler Anadolu ve Rumeli Müdafaa-i Hukuk Cemiyeti adıyla birleştirilmiştir.'),(60,1,5,52,'','İstanbul Hükümeti\'nin Temsil Heyeti\'ni ve Milli Mücadele\'yi hukuken ilk kez tanıdığı gelişme hangisidir?',1,'Amasya Görüşmeleri (Protokolü)','Bilecik Görüşmeleri','Mudanya Mütarekesi','Londra Konferansı','Gümrü Antlaşması','a',1,'Salih Paşa ile Mustafa Kemal arasındaki Amasya Görüşmeleri ile Temsil Heyeti hukuken tanınmıştır.'),(61,1,5,52,'','TBMM Hükümeti\'nin uluslararası alanda kazandığı ilk askeri ve siyasi zafer hangi antlaşma ile gerçekleşmiştir?',1,'Gümrü Antlaşması','Moskova Antlaşması','Ankara Antlaşması','Kars Antlaşması','Lozan Antlaşması','a',1,'Kazım Karabekir komutasında Ermenilere karşı kazanılan zafer sonrası 1920 Gümrü Antlaşması imzalanmıştır.'),(62,1,5,52,'','Düzenli ordunun Batı Cephesi\'nde kazandığı ilk askeri zafer aşağıdakilerden hangisidir?',1,'I. İnönü Savaşı','II. İnönü Savaşı','Sakarya Meydan Muharebesi','Büyük Taarruz','Kütahya-Eskişehir Savaşı','a',1,'Albay İsmet İnönü komutasındaki düzenli ordu Yunan ordusunu I. İnönü Savaşı\'nda durdurmuştur.'),(63,1,5,52,'','Mustafa Kemal Paşa\'ya \'Gazi\' unvanı ve \'Mareşal\' rütbesi hangi savaştan sonra TBMM tarafından verilmiştir?',1,'Sakarya Meydan Muharebesi','Büyük Taarruz','I. İnönü Savaşı','Çanakkale Savaşı','Trablusgarp Savaşı','a',1,'22 gün 22 gece süren Sakarya Meydan Muharebesi\'nden sonra Mustafa Kemal\'e Mareşallik ve Gazilik verilmiştir.'),(64,1,5,52,'','Türk ordusunun Sakarya Savaşı öncesinde ihtiyaçlarını karşılamak amacıyla yayımlanan milli emirler hangisidir?',1,'Tekalif-i Milliye Emirleri','Teşkilat-ı Esasiye','Hıyanet-i Vataniye','Misak-ı İktisadi','Takrir-i Sükun','a',1,'Başkomutan Mustafa Kemal 7-8 Ağustos 1921\'de Tekalif-i Milliye Emirleri\'ni yayımlamıştır.'),(65,1,5,52,'','Milli Mücadele\'nin silahlı dönemini sona erdiren ve Doğu Trakya\'nın savaşsız kurtarılmasını sağlayan mütareke hangisidir?',1,'Mudanya Ateşkes Antlaşması','Mondros Ateşkes Antlaşması','Lozan Barış Antlaşması','Gümrü Antlaşması','Ankara Antlaşması','a',1,'İsmet Paşa\'nın temsil ettiği Mudanya Mütarekesi ile İstanbul, Boğazlar ve Doğu Trakya savaşsız alınmıştır.'),(66,1,5,52,'','24 Temmuz 1923\'te imzalanan Lozan Barış Antlaşması\'nda Türkiye\'yi başdelege olarak temsil eden devlet adamı kimdir?',1,'İsmet İnönü','Rauf Orbay','Kazım Karabekir','Fevzi Çakmak','Ali Fuat Cebesoy','a',1,'Dışişleri Bakanı İsmet Paşa (İnönü) Lozan\'da Türk heyetinin başkanlığını yapmıştır.'),(67,1,6,52,'','Egemenliğin kayıtsız şartsız millete ait olduğunu savunan ve cumhuriyet rejimini temel alan Atatürk ilkesi hangisidir?',1,'Cumhuriyetçilik','Milliyetçilik','Halkçılık','Devletçilik','Laiklik','a',1,'Cumhuriyetçilik; milli egemenlik, seçim, meclis ve çok partili hayatı doğrudan kapsar.'),(68,1,6,52,'','Toplumda hiçbir sınıfa, zümreye veya aileye ayrıcalık tanınmamasını ve kanun önünde eşitliği savunan ilke hangisidir?',1,'Halkçılık','Devletçilik','Milliyetçilik','İnkılapçılık','Laiklik','a',1,'Halkçılık ilkesinin temeli sosyal adalet, eşitlik ve ayrıcalıksızlıktır.'),(69,1,6,52,'','Özel sektörün yetersiz kaldığı alanlarda büyük yatırımların devlet eliyle yapılmasını öngören ekonomik ilke hangisidir?',1,'Devletçilik','Cumhuriyetçilik','Halkçılık','Milliyetçilik','Laiklik','a',1,'1930\'lu yıllarda uygulanan 1. Beş Yıllık Sanayi Planı Devletçilik ilkesinin sonucudur.'),(70,1,6,52,'','Türk parasını korumak ve milli ticareti geliştirmek amacıyla Kabotaj Kanunu\'nun çıkarılması hangi ilkeyle doğrudan ilişkilidir?',1,'Milliyetçilik','Devletçilik','Halkçılık','Laiklik','Cumhuriyetçilik','a',1,'Türk karasularında ticaret ve taşıma hakkının Türk gemicilere verilmesi Milliyetçilik ilkesidir.'),(71,1,6,52,'','Eğitim ve öğretimin tek çatı altında birleştirilmesini sağlayan Tevhid-i Tedrisat Kanunu hangi tarihte kabul edilmiştir?',1,'3 Mart 1924','29 Ekim 1923','1 Kasım 1922','17 Şubat 1926','1 Kasım 1928','a',1,'3 Mart 1924\'te Hilafetin kaldırılmasıyla aynı gün Tevhid-i Tedrisat Kanunu çıkarılmıştır.'),(72,1,6,52,'','Medeni Kanun\'un kabul edilmesiyle (17 Şubat 1926) Türk kadınına aşağıdaki haklardan hangisi VERİLMEMİŞTİR?',1,'Seçme ve Seçilme Hakkı','Miras Eşitliği','Mahkemede Tanıklık Eşitliği','Boşanma Hakkı','İstediği Mesleğe Girme Hakkı','a',1,'Kadınlara siyasi haklar (seçme-seçilme) 1930 (Belediye), 1933 (Muhtar) ve 1934\'te (Milletvekili) verilmiştir.'),(73,1,6,52,'','Türkiye Cumhuriyeti\'nin ilk muhalefet partisi aşağıdakilerden hangisidir?',1,'Terakkiperver Cumhuriyet Fırkası','Serbest Cumhuriyet Fırkası','Demokrat Parti','Milli Kalkınma Partisi','Halk Fırkası','a',1,'1924 yılında Kazım Karabekir, Rauf Orbay ve Ali Fuat Cebesoy tarafından kurulmuştur.'),(74,1,6,52,'','1925 yılında çıkarılan ve Şeyh Sait İsyanı sonrası huzur ve güvenliği sağlamayı amaçlayan kanun hangisidir?',1,'Takrir-i Sükun Kanunu','Hıyanet-i Vataniye Kanunu','Firariler Kanunu','Men-i Müskirat Kanunu','Teşvik-i Sanayi Kanunu','a',1,'İsmet İnönü hükümeti döneminde çıkarılan Takrir-i Sükun Kanunu ile inkılaplar güvenceye alınmıştır.'),(75,1,6,52,'','Boğazlar Komisyonu\'nun kaldırılarak Boğazların yönetiminin ve güvenliğinin tamamen Türkiye\'ye bırakıldığı sözleşme hangisidir?',1,'1936 Montrö Boğazlar Sözleşmesi','1923 Lozan Boğazlar Sözleşmesi','1937 Sadabat Paktı','1934 Balkan Antantı','1921 Ankara Antlaşması','a',1,'Montrö Sözleşmesi ile Boğazlar üzerindeki Türk egemenliği tam olarak sağlanmıştır.'),(76,1,6,52,'','Mustafa Kemal Atatürk\'ün \'Şahsi meselemdir\' dediği ve 1939\'da anavatana katılan toprak parçası neresidir?',1,'Hatay','Musul','Batum','Boğazlar','Gökçeada','a',1,'Atatürk\'ün yoğun diplomatik çabaları sonucu Hatay Cumhuriyeti 1939\'da Türkiye\'ye katılmıştır.'),(77,2,8,52,'','Türkiye\'nin matematiksel (mutlak) konum koordinatları aşağıdakilerden hangisinde doğru verilmiştir?',1,'36° - 42° Kuzey Paralelleri / 26° - 45° Doğu Meridyenleri','26° - 45° Kuzey Paralelleri / 36° - 42° Doğu Meridyenleri','30° - 40° Kuzey Paralelleri / 20° - 40° Doğu Meridyenleri','36° - 42° Güney Paralelleri / 26° - 45° Batı Meridyenleri','35° - 45° Kuzey Paralelleri / 25° - 45° Doğu Meridyenleri','a',1,'Türkiye 36-42 Kuzey enlemleri ile 26-45 Doğu boylamları arasında yer alır.'),(79,2,8,52,'','Türkiye\'de güneyden kuzeye doğru gidildikçe aşağıdakilerden hangisi AZALMAZ?',1,'Gece ile gündüz arasındaki zaman farkı','Güneş ışınlarının geliş açısı','Sıcaklık ortalamaları','Çizgisel hız','Yerçekimi kuvveti','a',1,'Kutuplara doğru gidildikçe gece-gündüz süre farkı artar, azalmaz.'),(80,2,8,52,'','Türkiye\'de dağların güney yamaçlarının kuzey yamaçlarına göre daha fazla güneş alması ve ısınması ne ile açıklanır?',1,'Bakı Etkisi','Boylam Etkisi','Yükselti Etkisi','Karasallık','Rüzgar Yönü','a',1,'Türkiye Yengeç Dönencesi\'nin kuzeyinde yer aldığı için güney yamaçlar daima bakı durumundadır.'),(81,2,8,52,'','Türkiye\'nin ortak saat olarak kullandığı Iğdır meridyeni kaçıncı saat diliminde yer alır?',1,'+3. Saat Dilimi (45° Doğu)','+2. Saat Dilimi (30° Doğu)','+1. Saat Dilimi (15° Doğu)','+4. Saat Dilimi (60° Doğu)','0. Saat Dilimi (Greenwich)','a',1,'Türkiye tüm yıl boyunca 45° Doğu (Iğdır) boylamının yerel saatini ulusal saat (+3) olarak kullanır.'),(82,2,9,52,'','Türkiye\'de karstik şekillerin (polye, obruk, lapyalar) en yaygın görüldüğü coğrafi bölge hangisidir?',1,'Akdeniz Bölgesi (Teke ve Taşeli)','Güneydoğu Anadolu','İç Anadolu','Doğu Anadolu','Karadeniz Bölgesi','a',1,'Kalker (kireçtaşı) arazisinin yaygın olduğu Akdeniz Teke ve Taşeli platolarında karstik şekiller yoğundur.'),(83,2,9,52,'','Bir adanın kıyı oku ile karaya bağlanması sonucu oluşan yeryüzü şekline ne ad verilir (Örn: Kapıdağ Yarımadası)?',1,'Tombolo (Saplı Ada)','Lagün (Kıyı Set Gölü)','Falez (Yalıyar)','Delta Ovası','Haliç','a',1,'Kapıdağ ve Sinop İnceburun Türkiye\'nin en bilinen tombolo örnekleridir.'),(84,2,9,52,'','Türkiye\'nin en büyük delta ovası aşağıdakilerden hangisidir?',1,'Çukurova (Seyhan ve Ceyhan)','Bafra Ovası (Kızılırmak)','Çarşamba Ovası (Yeşilırmak)','Silifke Ovası (Göksu)','Menemen Ovası (Gediz)','a',1,'Seyhan ve Ceyhan nehirlerinin alüvyonlarıyla oluşan Çukurova en büyük delta ovamızdır.'),(85,2,9,52,'','Volkanik patlama sonucu oluşan krater, kaldera ve maar çukurlarına örnek olarak \'Dünya\'nın Nazar Boncuğu\' olarak bilinen göl hangisidir?',1,'Meke Maarı (Gölü)','Nemrut Krater Gölü','Gölcük Gölü','Van Gölü','Tuz Gölü','a',1,'Konya Karapınar\'da yer alan Meke Maarı volkanik gaz patlamasıyla oluşmuştur.'),(86,2,9,52,'','Türkiye\'de buzul aşındırma ve biriktirme şekillerine rastlanabilmesi ne ile açıklanır?',1,'Yüksek Dağlık Alanların Bulunması','Mutlak Konumunun Kutuplara Yakın Olması','Okyanus Kıyısında Yer Alması','Karasallık Şiddeti','Rüzgar Erozyonu','a',1,'Türkiye orta kuşaktadır; buzul şekilleri sadece yüksekliği 2500-3000 m üzerindeki dağlarda görülür.'),(87,2,10,52,'','Türkiye\'de yıllık yağış miktarının en fazla olduğu bölüm aşağıdakilerden hangisidir?',1,'Doğu Karadeniz Bölümü (Rize)','Batı Akdeniz (Antalya)','Yıldız Dağları Bölümü','Hakkari Yöresi','Güney Marmara','a',1,'Rize çevresi yıllık 2400 mm\'yi aşan yağış miktarıyla Türkiye\'nin en çok yağış alan yeridir.'),(88,2,10,52,'','Akdeniz ikliminin doğal bitki örtüsü olan makilerin tahrip edilmesiyle ortaya çıkan bodur çalı topluluğuna ne ad verilir?',1,'Garig (Frigana)','Psödomaki','Bozkır (Step)','Antropojen Bozkır','Tayga','a',1,'Makilerin tahribiyle garig, Karadeniz ormanlarının tahribiyle psödomaki oluşur.'),(89,2,10,52,'','Türkiye\'de kış mevsiminde Sibirya Termik Yüksek Basıncı etkili olduğunda hava durumu nasıl gerçekleşir?',1,'Aşırı Soğuk, Ayaz ve Kar Yağışlı','Ilık ve Yağmurlu','Sıcak ve Nemli','Fırtınalı ve Ilık','Sisli ve Ilık','a',1,'Sibirya yüksek basıncı Türkiye\'ye kışın girdiğinde kuru soğuk ve şiddetli ayaz yapar.'),(90,2,10,52,'','Yazları sıcak ve kurak, kışları ılık ve yağışlı olan Akdeniz ikliminde en fazla yağış hangi mevsimde düşer?',1,'Kış','İlkbahar','Yaz','Sonbahar','Yıl boyu eşit','a',1,'Akdeniz ikliminde cephesel kökenli kış yağışları hakimdir.'),(91,2,10,52,'','İç Anadolu Bölgesi\'nde ilkbaharda ısınan havanın yükselmesiyle oluşan konveksiyonel (kırkikindi) yağışlar en çok hangi ayda görülür?',1,'Nisan - Mayıs','Temmuz - Ağustos','Aralık - Ocak','Eylül - Ekim','Şubat - Mart','a',1,'İç kesimlerde ısınmaya bağlı konveksiyonel yağışlar ilkbahar aylarında görülür.'),(92,2,11,52,'','Türkiye\'de nüfus yoğunluğunun en az olduğu coğrafi bölge aşağıdakilerden hangisidir?',1,'Doğu Anadolu Bölgesi','İç Anadolu Bölgesi','Karadeniz Bölgesi','Güneydoğu Anadolu','Ege Bölgesi','a',1,'Yüz ölçümünün çok geniş ve arazinin engebeli, iklimin sert olması sebebiyle Doğu Anadolu en seyrektir.'),(93,2,11,52,'','Cumhuriyet tarihinde ilk genel nüfus sayımı hangi yılda yapılmıştır?',1,'1927','1923','1935','1940','1950','a',1,'Türkiye Cumhuriyeti\'nde ilk modern nüfus sayımı 1927 yılında yapılmıştır (13.6 milyon).'),(94,2,12,52,'','Dünya rezervlerinin yaklaşık \\%72\'si Türkiye\'de bulunan ve jet yakıtı, cam ve seramikte kullanılan stratejik maden hangisidir?',1,'Bor','Krom','Boksit','Bakır','Demir','a',1,'Balıkesir, Kütahya ve Eskişehir yörelerinde yoğunlaşan Bor madeninde Türkiye dünya lideridir.'),(95,2,12,52,'','Türkiye\'de taş kömürü yataklarının bulunması arazimizin hangi jeolojik zamanda oluştuğunun kanıtıdır?',1,'I. Jeolojik Zaman (Paleozoik)','II. Jeolojik Zaman (Mezozoik)','III. Jeolojik Zaman (Tersiyer)','IV. Jeolojik Zaman (Kuvaterner)','Prekambriyen','a',1,'Taş kömürü 1. Jeolojik zamanda, linyit ise 3. Jeolojik zamanda oluşmuştur.'),(96,2,12,52,'','Türkiye\'de fındık, incir, kayısı ve kiraz üretiminde dünya birincisi olmamız tarımsal potansiyelimizi gösterir. Malatya hangi ürünle özdeşleşmiştir?',1,'Kayısı','Fındık','İncir','Üzüm','Elma','a',1,'Malatya dünya kuru kayısı üretim ve ihracatında açık ara birinci sıradadır.'),(97,3,13,52,'','Yetkili bir makam tarafından konulmuş olan yazılı hukuk kurallarının tamamına ne ad verilir?',1,'Mevzu Hukuk','Müspet (Pozitif) Hukuk','Tabii (İdeal) Hukuk','Tarihi Hukuk','Örf ve Adet Hukuku','a',1,'Mevzu Hukuk sadece yetkili makamlarca konulan yazılı kuralları (kanun, yönetmelik vb.) kapsar.'),(98,3,13,52,'','Hukuk kurallarının yaptırımları (müeyyideleri) arasında aşağıdakilerden hangisi YER ALMAZ?',1,'Kınama ve Ayıplama','Ceza','Cebri İcra','Tazminat','Hükümsüzlük (İptal)','a',1,'Kınama ve ayıplama ahlak ve görgü kurallarının yaptırımıdır, maddi devlet gücü taşımaz.'),(99,3,13,52,'','Medeni Kanun\'a göre fiil ehliyetinin şartları arasında aşağıdakilerden hangisi yer almaz?',1,'Ergin (reşit) olmak, ayırt etme gücüne sahip olmak, kısıtlı olmamak','Evli olmak','Temyiz kudretine sahip olmak','Kısıtlı bulunmamak','18 yaşını doldurmuş olmak','b',1,'Evli olmak fiil ehliyetinin genel şartı değildir; ayırt etme gücü, erginlik ve kısıtlı olmamak şarttır.'),(100,3,13,52,'','Bir hakkın doğumunda veya kazanılmasında geçerli olan iyi niyet kuralı hangisidir?',1,'Subjektif İyi Niyet','Objektif İyi Niyet (Dürüstlük)','Hakkın Kötüye Kullanılması','Kuvvet Kullanma','Meşru Müdafaa','a',1,'Hakların kazanılmasında Subjektif İyi Niyet, kullanılmasında ise Dürüstlük Kuralı (Objektif) geçerlidir.'),(101,3,14,52,'','1982 Anayasası\'nın değiştirilemez ve değiştirilmesi teklif dahi edilemez maddeleri arasında hangisi YER ALMAZ?',1,'TBMM\'nin üye tamsayısının 600 olması','Devletin şeklinin Cumhuriyet olması (1. Madde)','Cumhuriyetin nitelikleri (Demokratik, laik, sosyal hukuk devleti - 2. Madde)','Devletin bütünlüğü, resmi dili Türkçe, bayrağı, marşı ve başkenti (3. Madde)','İlk 3 maddenin değiştirilemeyeceği hükmü (4. Madde)','a',1,'TBMM milletvekili sayısı anayasanın değiştirilemez ilk 4 maddesi kapsamında değildir.'),(102,3,14,52,'','1982 Anayasası\'na göre bir siyasi partinin TBMM seçimlerinde milletvekili çıkarabilmesi için ülke genelinde alması gereken seçim barajı yüzde kaçtır?',1,'\\%7','\\%10','\\%5','\\%3','\\%1','a',1,'Seçim kanununda yapılan son değişiklikle ülke barajı \\%7\'ye düşürülmüştür.'),(103,3,14,52,'','Siyasi partilerin kapatılması davalarına hangi mahkeme bakar ve karara bağlar?',1,'Anayasa Mahkemesi','Yargıtay','Danıştay','Uyuşmazlık Mahkemesi','Sayıştay','a',1,'Yargıtay Cumhuriyet Başsavcısı\'nın açtığı davada Anayasa Mahkemesi karar verir.'),(104,3,15,52,'','1982 Anayasası\'na göre Türkiye Büyük Millet Meclisi kaç milletvekilinden oluşur?',1,'600','550','450','500','650','a',1,'2017 anayasa değişikliği ile milletvekili sayısı 550\'den 600\'e çıkarılmıştır.'),(105,3,15,52,'','TBMM genel seçimleri kaç yılda bir Cumhurbaşkanlığı seçimi ile birlikte yapılır?',1,'5 Yılda Bir','4 Yılda Bir','3 Yılda Bir','6 Yılda Bir','2 Yılda Bir','a',1,'Anayasa Madde 77 gereğince TBMM ve Cumhurbaşkanlığı seçimleri 5 yılda bir aynı gün yapılır.'),(106,3,15,52,'','Cumhurbaşkanı seçilme yaşı 2017 değişikliği ile kaça indirilmiştir?',1,'40 Yaşını doldurmuş olmak','30 Yaşını doldurmuş olmak','35 Yaşını doldurmuş olmak','18 Yaşını doldurmuş olmak','25 Yaşını doldurmuş olmak','a',1,'Milletvekili seçilme yaşı 18\'e indirilmiş; Cumhurbaşkanı için 40 yaş ve yükseköğrenim şartı korunmuştur.'),(107,3,15,52,'','Anayasa Mahkemesi kaç üyeden oluşur ve üyelerin görev süresi kaç yıldır?',1,'15 Üye - 12 Yıl','17 Üye - 9 Yıl','12 Üye - 6 Yıl','15 Üye - 5 Yıl','21 Üye - 10 Yıl','a',1,'AYM 15 üyeden oluşur. Üyeler bir kez 12 yıllığına seçilir.'),(108,3,15,52,'','Adli yargı kolunun en üst temyiz mahkemesi aşağıdakilerden hangisidir?',1,'Yargıtay','Danıştay','Anayasa Mahkemesi','Sayıştay','Uyuşmazlık Mahkemesi','a',1,'Adli yargının temyiz mercii Yargıtay, idari yargının temyiz mercii Danıştay\'dır.'),(109,3,16,52,'','Türkiye\'de il ve ilçe kurulması, kaldırılması ve adlarının değiştirilmesi ne ile yapılır?',1,'Kanun ile','Cumhurbaşkanlığı Kararnamesi ile','İçişleri Bakanlığı Genelgesi ile','Yönetmelik ile','İl Genel Meclisi Kararı ile','a',1,'Anayasa m. 126 gereğince il ve ilçeler ancak kanunla kurulur, kaldırılır veya adları değiştirilir.'),(110,3,16,52,'','İl genel idaresinin başında bulunan ve hem devleti hem de Cumhurbaşkanını ilde temsil eden yetkili kimdir?',1,'Vali','Kaymakam','Büyükşehir Belediye Başkanı','İl Emniyet Müdürü','Garnizon Komutanı','a',1,'Vali istisnai memurdur ve ilde Cumhurbaşkanının temsilcisi ve idari yürütme vasıtasıdır.'),(111,3,16,52,'','Köyün tüzel kişiliğini temsil eden ve köy derneği tarafından seçilen köy yöneticisi kimdir?',1,'Muhtar','Kaymakam','İhtiyar Heyeti','İmam','Köy Katibi','a',1,'Muhtar köy idaresinin başıdır ve köy tüzel kişiliğini temsil eder.'),(112,3,17,52,'','Birleşmiş Milletler (BM) Genel Merkezi hangi şehirde yer almaktadır?',1,'New York (ABD)','Cenevre (İsviçre)','Brüksel (Belçika)','Paris (Fransa)','Viyana (Avusturya)','a',1,'BM Genel Merkezi New York\'tadır; Cenevre ise Avrupa merkezidir.'),(113,3,17,52,'','NATO\'ya (Kuzey Atlantik Antlaşması Örgütü) son katılan üye ülke aşağıdakilerden hangisidir?',1,'İsveç','Finlandiya','Kuzey Makedonya','Karadağ','Ukrayna','a',1,'İsveç 2024 yılında NATO\'nun 32. üye ülkesi olmuştur.'),(114,4,18,52,'','\'Ağır\' sözcüğü aşağıdaki cümlelerin hangisinde mecaz anlamda kullanılmıştır?',1,'Bu kadar ağır sözleri hiçbirimiz hak etmedik.','Ağır çuvalları taşırken beli incinmişti.','Kamyon ağır adımlarla yokuşu tırmanıyordu.','Gemi ağır bir yükle limandan ayrıldı.','Ağır metaller sanayide yoğun kullanılır.','a',1,'\'Ağır söz\' kırıcı, incitici anlamında mecazlaşmıştır.'),(115,4,18,52,'','Aşağıdaki cümlelerin hangisinde \'neden-sonuç (gerekçe)\' ilişkisi vardır?',1,'Yoğun kar yağışı nedeniyle köy yolları ulaşıma kapandı.','Sınavı kazanmak için gece gündüz durmadan çalışıyor.','Yarın erken kalkarsan birlikte yürüyüşe gideriz.','Konuyu anlasın diye tahtaya şekil çizdi.','Seninle görüşmek üzere Ankara\'ya gideceğim.','a',1,'Yolların kapanması sonuç, kar yağışı ise gerçekleşmiş nedendir.'),(116,4,18,52,'','Aşağıdaki atasözlerinden hangisi \'tutumlu olma ve birikim yapma\' ile ilgilidir?',1,'Ak akçe kara gün içindir.','Damlaya damlaya göl olur.','Ayağını yorganına göre uzat.','Sakla samanı gelir zamanı.','Hepsi','e',1,'Verilen tüm atasözleri tasarruf, tutumluluk ve tedbirli olmakla ilgilidir.'),(117,4,20,52,'','\'Genç adam, kütüphanedeki eski kitapları büyük bir dikkatle inceledi.\' cümlesinin öge dizilişi hangisidir?',1,'Özne - Belirtili Nesne - Zarf Tümleci - Yüklem','Özne - Dolaylı Tümleç - Belirtili Nesne - Yüklem','Özne - Zarf Tümleci - Nesne - Yüklem','Belirtili Nesne - Özne - Yüklem','Özne - Belirtisiz Nesne - Yüklem','a',1,'İnceledi (Yüklem), Genç adam (Özne), kütüphanedeki eski kitapları (Belirtili Nesne), büyük bir dikkatle (Zarf Tümleci).'),(118,4,20,52,'','Aşağıdaki cümlelerin hangisinde bir yazım yanlışı vardır?',1,'Bu konuyu Mehmet Bey\'de çok iyi biliyordu.','TBMM\'nin açılış törenine katıldık.','Tarih 29 Ekim 1923\'ü gösteriyordu.','O da bizimle sinemaya gelecek mi?','Türk Dil Kurumu Başkanlığına dilekçe verdik.','a',1,'\'Mehmet Bey de\' bağlacı ayrı yazılmalıdır, bitişik yazılamaz.'),(119,4,20,52,'','Aşağıdaki sözcüklerin hangisinde büyük ünlü uyumu (kalınlık-incelik kuralı) aranmaz?',1,'Tek heceli ve yabancı kökenli sözcüklerde','Türkçe kökenli türemiş sözcüklerde','Birleşik sözcüklerde','Üç heceli isimlerde','Fiil çekimlerinde','a',1,'Tek heceli sözcüklerde ve Türkçe kökenli olmayan yabancı sözcüklerde büyük ünlü uyumu aranmaz.'),(120,5,0,52,'','Ardışık 5 tek sayının toplamı 85 olduğuna göre bu sayıların en büyüğü kaçtır?',1,'21','19','17','23','25','a',1,'Ortanca sayı 85 / 5 = 17\'dir. Sayılar: 13, 15, 17, 19, 21. En büyüğü 21\'dir.'),(121,5,0,52,'','Bir sınıftaki öğrencilerin \\%60\'ı erkektir. Sınıfta 12 kız öğrenci olduğuna göre sınıf mevcudu kaçtır?',1,'30','25','40','35','50','a',1,'Kızların oranı \\%40\'tır. Sınıf mevcudu x olsun. 0.40 * x = 12 => x = 30.'),(122,5,0,52,'','Bir babanın yaşı, oğlunun yaşının 4 katıdır. 5 yıl sonra babanın yaşı oğlunun yaşının 3 katı olacağına göre çocuk bugün kaç yaşındadır?',1,'10','8','12','15','14','a',1,'Oğul x, baba 4x. 5 yıl sonra: 4x + 5 = 3(x + 5) => 4x + 5 = 3x + 15 => x = 10.'),(123,5,0,52,'','Bir araç A kentinden B kentine 60 km/s hızla gidip, 90 km/s hızla geri dönmüştür. Bu aracın gidiş-dönüşteki ortalama hızı saatte kaç km\'dir?',1,'72','75','70','80','65','a',1,'Ortalama hız harmonik ortalamadır: (2 * 60 * 90) / (60 + 90) = 10800 / 150 = 72 km/s.'),(124,5,0,52,'','200 TL maliyetle alınan bir ürün \\%30 karla kaç TL\'ye satılır?',1,'260 TL','230 TL','250 TL','280 TL','300 TL','a',1,'Kar: 200 * 0.30 = 60 TL. Satış fiyatı: 200 + 60 = 260 TL.'),(125,1,1,52,'','Türk tarihinde ilk yazılı anıtlar Orhun Abideleri (Göktürk Kitabeleri)\'dir.',2,'Doğru','Yanlış','','','','a',1,'Doğru. Orhun Yazıtları Türklerin bilinen ilk yazılı kaynaklarıdır.'),(126,1,1,52,'','Uygurlar Türk tarihinde kağıt ve matbaayı kullanan ilk devlettir.',2,'Doğru','Yanlış','','','','a',1,'Doğru. Uygurlar yerleşik hayata geçerek matbaa ve kağıt kullanmışlardır.'),(127,1,3,52,'','Osmanlı Devleti\'nde ilk altın para Fatih Sultan Mehmet döneminde basılmıştır.',2,'Doğru','Yanlış','','','','a',1,'Doğru. \'Sultani\' adı verilen ilk altın para Fatih döneminde basılmıştır.'),(128,1,5,52,'','Amasya Genelgesi\'nde milli egemenlik ilkesinden ilk kez üstü kapalı olarak bahsedilmiştir.',2,'Doğru','Yanlış','','','','a',1,'Doğru. \'Milletin bağımsızlığını milletin azim ve kararı kurtaracaktır.\''),(129,1,6,52,'','1924 Anayasası kabul edildiğinde devletin dini İslam\'dır maddesi yer almıyordu.',2,'Doğru','Yanlış','','','','b',1,'Yanlış! \'Devletin dini İslam\'dır\' maddesi 1928 yılında çıkarılmıştır.'),(130,2,8,52,'','Türkiye\'nin en doğu ucu ile en batı ucu arasında 76 dakikalık zaman farkı bulunur.',2,'Doğru','Yanlış','','','','a',1,'Doğru. 45 - 26 = 19 meridyen; 19 x 4 = 76 dakika.'),(131,2,9,52,'','Türkiye\'de aktif volkanik dağlar bulunmaktadır.',2,'Doğru','Yanlış','','','','b',1,'Yanlış. Türkiye\'deki volkanik dağlar sönmüş (uyuyan) durumdadır.'),(132,2,12,52,'','Bor madeni rezervlerinde Türkiye dünya birincisidir.',2,'Doğru','Yanlış','','','','a',1,'Doğru. Dünya rezervlerinin yaklaşık \\%72\'si Türkiye\'dedir.'),(133,3,14,52,'','1982 Anayasası\'na göre milletvekili seçilme yaşı 18\'dir.',2,'Doğru','Yanlış','','','','a',1,'Doğru. 2017 değişikliği ile seçilme yaşı 18\'e indirilmiştir.'),(134,3,15,52,'','Cumhurbaşkanı TBMM tarafından 7 yıllığına seçilir.',2,'Doğru','Yanlış','','','','b',1,'Yanlış. Cumhurbaşkanı halk tarafından 5 yıllığına seçilir.'),(135,3,16,52,'','İl ve ilçelerin kurulması veya kaldırılması kanun ile yapılır.',2,'Doğru','Yanlış','','','','a',1,'Doğru. Anayasa gereği il ve ilçeler ancak kanunla kurulabilir.'),(136,4,18,52,'','\'Damlaya damlaya göl olur\' atasözü tasarruf ve birikim ile ilgilidir.',2,'Doğru','Yanlış','','','','a',1,'Doğru.');
/*!40000 ALTER TABLE `tbl_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_question_reports`
--

DROP TABLE IF EXISTS `tbl_question_reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_question_reports` (
  `id` int NOT NULL AUTO_INCREMENT,
  `question_id` int NOT NULL,
  `user_id` int NOT NULL,
  `message` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `question_id` (`question_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_question_reports`
--

LOCK TABLES `tbl_question_reports` WRITE;
/*!40000 ALTER TABLE `tbl_question_reports` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_question_reports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_quiz_categories`
--

DROP TABLE IF EXISTS `tbl_quiz_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_quiz_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `type` int NOT NULL COMMENT '2-fun_n_learn, 3-guess_the_word, 4-audio_question',
  `type_id` int NOT NULL,
  `category` int NOT NULL,
  `subcategory` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `type` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_quiz_categories`
--

LOCK TABLES `tbl_quiz_categories` WRITE;
/*!40000 ALTER TABLE `tbl_quiz_categories` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_quiz_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_rooms`
--

DROP TABLE IF EXISTS `tbl_rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_rooms` (
  `id` int NOT NULL AUTO_INCREMENT,
  `room_id` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `entry_coin` int NOT NULL DEFAULT '0',
  `user_id` int NOT NULL,
  `room_type` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `category_id` int NOT NULL,
  `no_of_que` int NOT NULL,
  `questions` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `date_created` datetime NOT NULL,
  `set_user1` int NOT NULL DEFAULT '0',
  `set_user2` int NOT NULL DEFAULT '0',
  `set_user3` int NOT NULL DEFAULT '0',
  `set_user4` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `category_id` (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_rooms`
--

LOCK TABLES `tbl_rooms` WRITE;
/*!40000 ALTER TABLE `tbl_rooms` DISABLE KEYS */;
INSERT INTO `tbl_rooms` VALUES (1,'038139',20,1,'public',1,10,'[{\"id\":\"72\",\"category\":\"1\",\"subcategory\":\"6\",\"language_id\":\"52\",\"image\":\"\",\"question\":\"Medeni Kanun\'un kabul edilmesiyle (17 \\u015eubat 1926) T\\u00fcrk kad\\u0131n\\u0131na a\\u015fa\\u011f\\u0131daki haklardan hangisi VER\\u0130LMEM\\u0130\\u015eT\\u0130R?\",\"question_type\":\"1\",\"optiona\":\"Se\\u00e7me ve Se\\u00e7ilme Hakk\\u0131\",\"optionb\":\"Miras E\\u015fitli\\u011fi\",\"optionc\":\"Mahkemede Tan\\u0131kl\\u0131k E\\u015fitli\\u011fi\",\"optiond\":\"Bo\\u015fanma Hakk\\u0131\",\"optione\":\"\\u0130stedi\\u011fi Mesle\\u011fe Girme Hakk\\u0131\",\"answer\":\"a\",\"level\":\"1\",\"note\":\"Kad\\u0131nlara siyasi haklar (se\\u00e7me-se\\u00e7ilme) 1930 (Belediye), 1933 (Muhtar) ve 1934\'te (Milletvekili) verilmi\\u015ftir.\"},{\"id\":\"161\",\"category\":\"1\",\"subcategory\":\"3\",\"language_id\":\"52\",\"image\":\"\",\"question\":\"\\u0130stanbul\'un fethinin d\\u00fcnya tarihi a\\u00e7\\u0131s\\u0131ndan en \\u00f6nemli sonucu a\\u015fa\\u011f\\u0131dakilerden hangisidir?\",\"question_type\":\"1\",\"optiona\":\"Orta \\u00c7a\\u011f\'\\u0131n kapan\\u0131p Yeni \\u00c7a\\u011f\'\\u0131n ba\\u015flamas\\u0131\",\"optionb\":\"\\u0130pek Yolu\'nun kontrol\\u00fcn\\u00fcn ge\\u00e7mesi\",\"optionc\":\"Fener Rum Patrikhanesi\'nin himaye edilmesi\",\"optiond\":\"Toplar\\u0131n surlar\\u0131 y\\u0131kabilece\\u011finin g\\u00f6r\\u00fclmesi\",\"optione\":\"Bizans\'\\u0131n y\\u0131k\\u0131lmas\\u0131\",\"answer\":\"a\",\"level\":\"1\",\"note\":\"\\u0130stanbul\'un fethi evrensel \\u00f6l\\u00e7ekte Orta \\u00c7a\\u011f\'\\u0131 bitirip Yeni \\u00c7a\\u011f\'\\u0131 ba\\u015flatm\\u0131\\u015ft\\u0131r.\"},{\"id\":\"46\",\"category\":\"1\",\"subcategory\":\"3\",\"language_id\":\"52\",\"image\":\"\",\"question\":\"Bug\\u00fcnk\\u00fc T\\u00fcrkiye-\\u0130ran s\\u0131n\\u0131r\\u0131n\\u0131n temelini b\\u00fcy\\u00fck \\u00f6l\\u00e7\\u00fcde belirleyen 1639 tarihli antla\\u015fma hangisidir?\",\"question_type\":\"1\",\"optiona\":\"Kasr-\\u0131 \\u015eirin Antla\\u015fmas\\u0131\",\"optionb\":\"Ferhat Pa\\u015fa Antla\\u015fmas\\u0131\",\"optionc\":\"Amasya Antla\\u015fmas\\u0131\",\"optiond\":\"Nasuh Pa\\u015fa Antla\\u015fmas\\u0131\",\"optione\":\"Buca\\u015f Antla\\u015fmas\\u0131\",\"answer\":\"a\",\"level\":\"1\",\"note\":\"IV. Murat\'\\u0131n Ba\\u011fdat Seferi sonras\\u0131 imzalanan Kasr-\\u0131 \\u015eirin Antla\\u015fmas\\u0131 bug\\u00fcnk\\u00fc s\\u0131n\\u0131r\\u0131n temelidir.\"},{\"id\":\"171\",\"category\":\"1\",\"subcategory\":\"4\",\"language_id\":\"52\",\"image\":\"\",\"question\":\"Osmanl\\u0131 Devleti\'nde Kap\\u0131kulu Ocaklar\\u0131na asker yeti\\u015ftirmek amac\\u0131yla gayrim\\u00fcslim \\u00e7ocuklar\\u0131n toplan\\u0131p e\\u011fitilmesi sistemine ne ad verilir?\",\"question_type\":\"1\",\"optiona\":\"Dev\\u015firme Sistemi\",\"optionb\":\"T\\u0131mar Sistemi\",\"optionc\":\"\\u0130ltizam Sistemi\",\"optiond\":\"Malikane Sistemi\",\"optione\":\"M\\u00fcsadere Sistemi\",\"answer\":\"a\",\"level\":\"1\",\"note\":\"Dev\\u015firme sistemi ile Acemi Oca\\u011f\\u0131 ve Enderun Mektebi\'ne asker ve devlet adam\\u0131 yeti\\u015ftirilmi\\u015ftir.\"},{\"id\":\"73\",\"category\":\"1\",\"subcategory\":\"6\",\"language_id\":\"52\",\"image\":\"\",\"question\":\"T\\u00fcrkiye Cumhuriyeti\'nin ilk muhalefet partisi a\\u015fa\\u011f\\u0131dakilerden hangisidir?\",\"question_type\":\"1\",\"optiona\":\"Terakkiperver Cumhuriyet F\\u0131rkas\\u0131\",\"optionb\":\"Serbest Cumhuriyet F\\u0131rkas\\u0131\",\"optionc\":\"Demokrat Parti\",\"optiond\":\"Milli Kalk\\u0131nma Partisi\",\"optione\":\"Halk F\\u0131rkas\\u0131\",\"answer\":\"a\",\"level\":\"1\",\"note\":\"1924 y\\u0131l\\u0131nda Kaz\\u0131m Karabekir, Rauf Orbay ve Ali Fuat Cebesoy taraf\\u0131ndan kurulmu\\u015ftur.\"},{\"id\":\"155\",\"category\":\"1\",\"subcategory\":\"2\",\"language_id\":\"52\",\"image\":\"\",\"question\":\"Anadolu\'da kurulan ilk T\\u00fcrk beyli\\u011fi a\\u015fa\\u011f\\u0131dakilerden hangisidir?\",\"question_type\":\"1\",\"optiona\":\"Saltuklular\",\"optionb\":\"Dani\\u015fmentliler\",\"optionc\":\"Meng\\u00fccekliler\",\"optiond\":\"Artuklular\",\"optione\":\"\\u00c7aka Beyli\\u011fi\",\"answer\":\"a\",\"level\":\"1\",\"note\":\"Erzurum ve \\u00e7evresinde kurulan Saltuklular, Malazgirt sonras\\u0131 kurulan ilk T\\u00fcrk beyli\\u011fidir.\"},{\"id\":\"59\",\"category\":\"1\",\"subcategory\":\"5\",\"language_id\":\"52\",\"image\":\"\",\"question\":\"Manda ve himayenin kesin olarak reddedildi\\u011fi ve t\\u00fcm cemiyetlerin tek \\u00e7at\\u0131 alt\\u0131nda birle\\u015ftirildi\\u011fi kongre hangisidir?\",\"question_type\":\"1\",\"optiona\":\"Sivas Kongresi\",\"optionb\":\"Erzurum Kongresi\",\"optionc\":\"Havza Genelgesi\",\"optiond\":\"Afyon Kongresi\",\"optione\":\"Pozant\\u0131 Kongresi\",\"answer\":\"a\",\"level\":\"1\",\"note\":\"Sivas Kongresi\'nde manda kesin reddedilmi\\u015f ve cemiyetler Anadolu ve Rumeli M\\u00fcdafaa-i Hukuk Cemiyeti ad\\u0131yla birle\\u015ftirilmi\\u015ftir.\"},{\"id\":\"156\",\"category\":\"1\",\"subcategory\":\"2\",\"language_id\":\"52\",\"image\":\"\",\"question\":\"Anadolu\'nun T\\u00fcrk yurdu oldu\\u011funu kesinle\\u015ftiren ve Bizans\'\\u0131n T\\u00fcrkleri Anadolu\'dan atma \\u00fcmidini bitiren sava\\u015f hangisidir?\",\"question_type\":\"1\",\"optiona\":\"Miryokefalon Sava\\u015f\\u0131 (1176)\",\"optionb\":\"Malazgirt Sava\\u015f\\u0131 (1071)\",\"optionc\":\"Pasinler Sava\\u015f\\u0131 (1048)\",\"optiond\":\"Dandanakan Sava\\u015f\\u0131 (1040)\",\"optione\":\"Yass\\u0131\\u00e7emen Sava\\u015f\\u0131 (1230)\",\"answer\":\"a\",\"level\":\"1\",\"note\":\"II. K\\u0131l\\u0131\\u00e7 Arslan komutas\\u0131nda kazan\\u0131lan Miryokefalon Sava\\u015f\\u0131 ile Anadolu kesin olarak T\\u00fcrk yurdu olmu\\u015ftur.\"},{\"id\":\"1\",\"category\":\"1\",\"subcategory\":\"1\",\"language_id\":\"52\",\"image\":\"\",\"question\":\"\\u0130slamiyet \\u00f6ncesi T\\u00fcrk devletlerinde devlet i\\u015flerinin g\\u00f6r\\u00fc\\u015f\\u00fcl\\u00fcp karara ba\\u011fland\\u0131\\u011f\\u0131 meclise ne ad verilir?\",\"question_type\":\"1\",\"optiona\":\"Toy (Kurultay)\",\"optionb\":\"Tigin\",\"optionc\":\"\\u015ead\",\"optiond\":\"Tamgac\\u0131\",\"optione\":\"Yargu\",\"answer\":\"a\",\"level\":\"1\",\"note\":\"\\u0130slamiyet \\u00f6ncesi T\\u00fcrklerde h\\u00fck\\u00fcmdar ba\\u015fkanl\\u0131\\u011f\\u0131nda toplanan dan\\u0131\\u015fma ve karar meclisine Toy veya Kurultay ad\\u0131 verilir.\"},{\"id\":\"152\",\"category\":\"1\",\"subcategory\":\"2\",\"language_id\":\"52\",\"image\":\"\",\"question\":\"Hicaz b\\u00f6lgesine (Mekke ve Medine) hakim olan ilk T\\u00fcrk devleti a\\u015fa\\u011f\\u0131dakilerden hangisidir?\",\"question_type\":\"1\",\"optiona\":\"\\u0130h\\u015fidiler (Ak\\u015fitler)\",\"optionb\":\"Toluno\\u011fullar\\u0131\",\"optionc\":\"Eyyubiler\",\"optiond\":\"B\\u00fcy\\u00fck Sel\\u00e7uklular\",\"optione\":\"Osmanl\\u0131 Devleti\",\"answer\":\"a\",\"level\":\"1\",\"note\":\"Muhammed bin To\\u011fa\\u00e7 taraf\\u0131ndan kurulan \\u0130h\\u015fidiler Kutsal Topraklara hakim olan ilk T\\u00fcrk devletidir.\"}]','2026-09-06 23:06:50',0,0,0,0);
/*!40000 ALTER TABLE `tbl_rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_settings`
--

DROP TABLE IF EXISTS `tbl_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_settings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` varchar(512) NOT NULL,
  `message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=190 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_settings`
--

LOCK TABLES `tbl_settings` WRITE;
/*!40000 ALTER TABLE `tbl_settings` DISABLE KEYS */;
INSERT INTO `tbl_settings` VALUES (1,'about_us','<p><strong>Quiza</strong>\'ya HoÅŸ Geldiniz!</p><p>TÃ¼rkiye\'nin en keyifli bilgi yarÄ±ÅŸmasÄ± platformu.</p>'),(2,'contact_us','<p><strong>Lorem Ipsum</strong>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>\r\n<p><strong>Lorem Ipsum</strong>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>\r\n<p><strong>Lorem Ipsum</strong>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>\r\n<p><strong>Lorem Ipsum</strong>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>'),(3,'instructions','<p><strong>Instructions</strong></p>\r\n<p>Elite Quiz game has 4 or 5 options</p>\r\n<p>For each right answer 5 points will be given.</p>\r\n<p>Minus 2 points for each question.</p>\r\n<p>&nbsp;</p>\r\n<p><strong>Use of Lifeline</strong> : You can use only once per level</p>\r\n<p><strong>50 - 50</strong> : For remove two option out of four (deduct 4 coins).</p>\r\n<p><strong>Skip question</strong> : You can pass question without minus points(deduct 4 coins).</p>\r\n<p><strong>Audience poll</strong> : Use audience poll to&nbsp;check other users choose option(deduct 4&nbsp;coins).</p>\r\n<p><strong>Reset timer</strong> : Reset timer again if you needed more time score (deduct 4 coins).</p>\r\n<p>&nbsp;</p>\r\n<p><strong>Leaderboard</strong></p>\r\n<p>You can compare your score with other&nbsp;users of app.</p>\r\n<p>&nbsp;</p>\r\n<p><strong>Contest Rules</strong></p>\r\n<p>To provide fair and equal chance of winning to all Elite Quiz readers, the following are the official rules for all contests on Elite Quiz.</p>\r\n<p><strong>ELIGIBILITY: </strong>All player/users can play contest.</p>\r\n<p><strong>HOW TO ENTER: </strong>User can Play Contest&nbsp;by spending number of coins specified as an entry fees in contest details.</p>\r\n<p><strong>CHOICE OF LAW:&nbsp;</strong>All the Contest and Operations are belongs to WRTeam. and Apple is not involved in any way with the contest.&nbsp;</p>\r\n<p>&nbsp;</p>'),(4,'privacy_policy','<p><strong>Lorem Ipsum</strong>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>\r\n<p><strong>Lorem Ipsum</strong>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>\r\n<p><strong>Lorem Ipsum</strong>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>\r\n<p><strong>Lorem Ipsum</strong>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>'),(5,'terms_conditions','<p><strong>Lorem Ipsum</strong>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>\r\n<p><strong>Lorem Ipsum</strong>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>\r\n<p>&nbsp;</p>\r\n<p><strong>Lorem Ipsum</strong>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>\r\n<p><strong>Lorem Ipsum</strong>&nbsp;is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>'),(6,'answer_mode','1'),(7,'false_value','False'),(8,'true_value','True'),(9,'app_version','1.0.0+1'),(10,'reward_coin','4'),(11,'earn_coin','100'),(12,'refer_coin','50'),(13,'ios_more_apps',''),(14,'ios_app_link','https://testflight.apple.com'),(15,'more_apps',''),(16,'app_link','https://play.google.com/'),(17,'system_timezone_gmt','+03:00'),(18,'system_timezone','Europe/Istanbul'),(19,'language_mode','1'),(20,'option_e_mode','0'),(21,'quiz_zone_total_level_question','10'),(22,'quiz_zone_fix_level_question','1'),(23,'shareapp_text','Hello, This is a \'simple\' share \"text\". User will be happy to read '),(24,'contest_mode','1'),(25,'daily_quiz_mode','1'),(26,'force_update','0'),(27,'fcm_server_key',''),(28,'battle_mode_random_category','1'),(29,'battle_group_category_mode','1'),(30,'app_name','Quiza'),(31,'full_logo','1705488796.svg'),(32,'half_logo','17054887961.svg'),(33,'jwt_key','set_your_strong_jwt_secret_key'),(34,'system_version','2.3.9'),(35,'system_key','$2y$10$HzGScX/jWRc0MgE5SIN9Lu7MCpf2D1AV8W1rWbrOkgNRq36n3wjDC'),(36,'configuration_key','$2y$10$Ftv8MRLm5IfAkprJrcnSkelJMoY8uIUcB3RapZW0GopU0SrkkyFR.'),(38,'fun_n_learn_question','1'),(39,'guess_the_word_question','1'),(40,'audio_mode_question','1'),(41,'total_audio_time','10'),(42,'app_version_ios','1.0.0+1'),(43,'in_app_ads_mode','0'),(44,'ads_type','1'),(45,'android_banner_id','Android Banner Id'),(46,'android_interstitial_id','Android Interstitial Id'),(47,'android_rewarded_id','Android Rewarded Id'),(48,'ios_banner_id','IOS Banner Id'),(49,'ios_interstitial_id','IOS Interstitial Id'),(50,'ios_rewarded_id','IOS Rewarded Id'),(56,'ios_fb_banner_id','YOUR_PLACEMENT_ID'),(55,'android_fb_rewarded_id','YOUR_PLACEMENT_ID'),(54,'android_fb_interstitial_id','YOUR_PLACEMENT_ID'),(53,'android_fb_banner_id','YOUR_PLACEMENT_ID'),(57,'ios_fb_interstitial_id','YOUR_PLACEMENT_ID'),(58,'ios_fb_rewarded_id','YOUR_PLACEMENT_ID'),(59,'exam_module','1'),(60,'payment_mode','1'),(61,'payment_message',''),(62,'per_coin','10'),(63,'coin_amount','1'),(64,'coin_limit','100'),(65,'self_challenge_mode','1'),(66,'in_app_purchase_mode','0'),(67,'difference_hours','48'),(68,'app_maintenance','0'),(69,'maths_quiz_mode','1'),(71,'android_game_id','Android Game Id'),(72,'ios_game_id','IOS Game Id'),(73,'maximum_winning_coins','4'),(74,'minimum_coins_winning_percentage','70'),(75,'score','4'),(76,'quiz_zone_duration','30'),(77,'self_challenge_max_minutes','30'),(78,'guess_the_word_seconds','60'),(79,'maths_quiz_seconds','30'),(80,'fun_and_learn_time_in_seconds','60'),(81,'battle_mode_one','1'),(82,'battle_mode_group','1'),(83,'true_false_mode','1'),(84,'audio_quiz_seconds','30'),(85,'battle_mode_random_in_seconds','30'),(86,'welcome_bonus_coin','10'),(87,'quiz_zone_lifeline_deduct_coin','10'),(88,'battle_mode_random_entry_coin','5'),(89,'guess_the_word_max_winning_coin','10'),(90,'review_answers_deduct_coin','10'),(91,'currency_symbol','$'),(92,'daily_ads_visibility','0'),(93,'daily_ads_coins','5'),(94,'daily_ads_counter','1'),(95,'quiz_zone_mode','1'),(96,'quiz_winning_percentage','30'),(97,'quiz_zone_wrong_answer_deduct_score','4'),(98,'quiz_zone_correct_answer_credit_score','4'),(99,'guess_the_word_fix_question','0'),(100,'guess_the_word_total_question','10'),(101,'guess_the_word_max_hints','2'),(102,'guess_the_word_wrong_answer_deduct_score','4'),(103,'guess_the_word_correct_answer_credit_score','4'),(104,'audio_quiz_fix_question','1'),(105,'audio_quiz_total_question','10'),(106,'audio_quiz_wrong_answer_deduct_score','4'),(107,'audio_quiz_correct_answer_credit_score','4'),(108,'maths_quiz_fix_question','1'),(109,'maths_quiz_total_question','10'),(110,'maths_quiz_wrong_answer_deduct_score','4'),(111,'maths_quiz_correct_answer_credit_score','4'),(112,'fun_n_learn_quiz_fix_question','1'),(113,'fun_n_learn_total_question','10'),(114,'fun_n_learn_quiz_wrong_answer_deduct_score','4'),(115,'fun_n_learn_quiz_correct_answer_credit_score','4'),(116,'true_false_quiz_fix_question','1'),(117,'true_false_total_question','10'),(118,'true_false_quiz_in_seconds','30'),(119,'true_false_quiz_wrong_answer_deduct_score','4'),(120,'fun_n_learn_correct_answer_credit_score','4'),(121,'battle_mode_one_category','1'),(122,'battle_mode_one_fix_question','1'),(123,'battle_mode_one_total_question','10'),(124,'battle_mode_one_in_seconds','30'),(125,'battle_mode_one_wrong_answer_deduct_score','4'),(126,'battle_mode_one_correct_answer_credit_score','4'),(127,'battle_mode_one_quickest_correct_answer_extra_score','2'),(128,'battle_mode_one_second_quickest_correct_answer_extra_score','1'),(129,'battle_mode_one_code_char','1'),(130,'battle_mode_one_entry_coin','5'),(131,'battle_mode_group_category','1'),(132,'battle_mode_group_fix_question','1'),(133,'battle_mode_group_total_question','10'),(134,'battle_mode_group_in_seconds','30'),(135,'battle_mode_group_wrong_answer_deduct_score','10'),(136,'battle_mode_group_correct_answer_credit_score','10'),(137,'battle_mode_group_quickest_correct_answer_extra_score','10'),(138,'battle_mode_group_second_quickest_correct_answer_extra_score','10'),(139,'battle_mode_group_code_char','1'),(140,'battle_mode_group_entry_coin','5'),(141,'battle_mode_random_fix_question','1'),(142,'battle_mode_random_total_question','10'),(144,'battle_mode_random_correct_answer_credit_score','4'),(145,'battle_mode_random_quickest_correct_answer_extra_score','2'),(146,'battle_mode_random_second_quickest_correct_answer_extra_score','1'),(147,'battle_mode_random_search_duration','30'),(148,'self_challenge_max_questions','30'),(149,'exam_module_resume_exam_timeout','5'),(150,'question_shuffle_mode','1'),(151,'option_shuffle_mode','1'),(152,'battle_mode_random','1'),(153,'true_false_quiz_correct_answer_credit_score','4'),(154,'contest_mode_wrong_deduct_score','4'),(155,'contest_mode_correct_credit_score','4'),(156,'app_package_name',''),(157,'shared_secrets',''),(158,'fun_n_learn_quiz_total_question','10'),(159,'true_false_quiz_total_question','10'),(160,'latex_mode','0'),(161,'exam_latex_mode','0'),(162,'gmail_login','1'),(163,'email_login','1'),(164,'phone_login','1'),(165,'apple_login','1'),(166,'multi_match_mode','1'),(167,'multi_match_fix_level_question','1'),(168,'multi_match_total_level_question','10'),(169,'multi_match_duration','30'),(170,'multi_match_wrong_answer_deduct_score','10'),(171,'multi_match_correct_answer_credit_score','20'),(172,'guess_the_word_hint_deduct_coin','1'),(173,'footer_copyrights_text',''),(174,'theme_color','#F05387FF'),(175,'app_key_android_iron_source','Android Key'),(176,'app_key_ios_iron_source','IOS Key'),(177,'rewarded_id_android_iron_source','Android Rewarded Id'),(178,'rewarded_id_ios_iron_source','IOS Rewarded Id'),(179,'interstitial_id_android_iron_source','Android Interstitial Id'),(180,'interstitial_id_ios_iron_source','IOS Interstitial Id'),(181,'banner_id_android_iron_source','Android Banner Id'),(182,'banner_id_ios_iron_source','IOS Banner Id'),(183,'ai_provider','openai'),(184,'gemini_model',''),(185,'gemini_api_key',''),(186,'openai_model',''),(187,'openai_api_key',''),(188,'quiz_zone_total_question','10'),(189,'multi_match_total_question','10');
/*!40000 ALTER TABLE `tbl_settings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_slider`
--

DROP TABLE IF EXISTS `tbl_slider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_slider` (
  `id` int NOT NULL AUTO_INCREMENT,
  `language_id` int NOT NULL,
  `image` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `title` text COLLATE utf8mb4_general_ci NOT NULL,
  `description` text COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `language_id` (`language_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_slider`
--

LOCK TABLES `tbl_slider` WRITE;
/*!40000 ALTER TABLE `tbl_slider` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_slider` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_subcategory`
--

DROP TABLE IF EXISTS `tbl_subcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_subcategory` (
  `id` int NOT NULL AUTO_INCREMENT,
  `language_id` int NOT NULL DEFAULT '0',
  `maincat_id` int NOT NULL,
  `subcategory_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `slug` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `image` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `status` tinyint NOT NULL DEFAULT '1' COMMENT '1=Active, 0=Deactive',
  `is_premium` tinyint NOT NULL DEFAULT '0' COMMENT '0 - no , 1 - yes',
  `coins` int NOT NULL DEFAULT '0',
  `has_level` tinyint NOT NULL DEFAULT '1',
  `row_order` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `language_id` (`language_id`),
  KEY `maincat_id` (`maincat_id`),
  KEY `has_level` (`has_level`)
) ENGINE=MyISAM AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_subcategory`
--

LOCK TABLES `tbl_subcategory` WRITE;
/*!40000 ALTER TABLE `tbl_subcategory` DISABLE KEYS */;
INSERT INTO `tbl_subcategory` VALUES (26,52,16,'Osmanlı Önemli Antlaşmalar','fnl-osmanli-antlasmalar',NULL,1,0,0,1,2),(25,52,16,'İlk Türk Devletleri ve Teşkilat','fnl-ilk-turk-devletleri',NULL,1,0,0,1,1),(22,52,4,'Sözel Mantık ve Muhakeme','sozel-mantik','',1,0,0,1,5),(21,52,4,'Yazım Kuralları ve Noktalama İşaretleri','yazim-noktalama','',1,0,0,1,4),(19,52,4,'Paragrafta Anlam ve Ana Düşünce','paragrafta-anlam','',1,0,0,1,2),(20,52,4,'Dil Bilgisi ve Cümlenin Ögeleri','dil-bilgisi-ogeler','',1,0,0,1,3),(18,52,4,'Sözcük ve Cümlede Anlam','sozcuk-ve-cumlede-anlam','',1,0,0,1,1),(17,52,3,'Güncel Bilgiler ve Uluslararası Kuruluşlar','guncel-bilgiler-uluslararasi','',1,0,0,1,5),(16,52,3,'İdare Hukuku ve Türkiye İdari Teşkilatı','idare-hukuku-idari-teskilat','',1,0,0,1,4),(15,52,3,'Yasama, Yürütme ve Yargı Organları','yasama-yurutme-yargi','',1,0,0,1,3),(14,52,3,'1982 Anayasası ve Temel Esaslar','1982-anayasasi-temel-esaslar','',1,0,0,1,2),(13,52,3,'Temel Hukuk Kavramları','temel-hukuk-kavramlari','',1,0,0,1,1),(11,52,2,'Türkiye Nüfus ve Yerleşme','turkiye-nufus-yerlesme','',1,0,0,1,4),(12,52,2,'Türkiye Tarım, Hayvancılık ve Madenler','turkiye-tarim-madenler','',1,0,0,1,5),(10,52,2,'Türkiye İklimi ve Bitki Örtüsü','turkiye-iklim-bitki-ortusu','',1,0,0,1,3),(9,52,2,'Türkiye Yer Şekilleri, Dağlar ve Platolar','turkiye-yer-sekilleri','',1,0,0,1,2),(8,52,2,'Türkiye Coğrafi Konumu ve Etkileri','turkiye-cografi-konumu','',1,0,0,1,1),(7,52,1,'Çağdaş Türk ve Dünya Tarihi','cagdas-turk-dunya-tarihi','',1,0,0,1,7),(6,52,1,'Atatürk İlkeleri ve İnkılap Tarihi','ataturk-ilkeleri-inkilap-tarihi','',1,0,0,1,6),(5,52,1,'Kurtuluş Savaşı ve Cepheler','kurtulus-savasi-cepheler','',1,0,0,1,5),(4,52,1,'Osmanlı Kültür ve Medeniyeti','osmanli-kultur-medeniyet','',1,0,0,1,4),(3,52,1,'Osmanlı Devleti Kuruluş & Yükselme','osmanli-kurulus-yukselme','',1,0,0,1,3),(2,52,1,'İlk Türk-İslam Devletleri','ilk-turk-islam-devletleri','',1,0,0,1,2),(1,52,1,'İslamiyet Öncesi Türk Tarihi','islamiyet-oncesi-turk-tarihi','',1,0,0,1,1),(27,52,17,'Türkiye Dağları ve Gölleri','fnl-turkiye-daglari',NULL,1,0,0,1,1),(28,52,18,'1982 Anayasası Temel Maddeler','fnl-1982-anayasa',NULL,1,0,0,1,1),(29,52,19,'Eski Türk ve Osmanlı Terimleri','gtw-eski-turk-osmanli',NULL,1,0,0,1,1),(30,52,20,'Yeryüzü Şekilleri ve İklim Terimleri','gtw-yeryuzu-sekilleri',NULL,1,0,0,1,1),(31,52,21,'Temel Hukuk ve Anayasa Kavramları','gtw-temel-hukuk',NULL,1,0,0,1,1),(32,52,22,'Sayılar ve Dört İşlem','mq-sayilar-dort-islem',NULL,1,0,0,1,1),(33,52,22,'Rasyonel ve Ondalık Sayılar','mq-rasyonel-sayilar',NULL,1,0,0,1,2),(34,52,23,'Yaş ve Yüzde Problemleri','mq-yas-yuzde-problemleri',NULL,1,0,0,1,1),(35,52,23,'Hız ve Kar-Zarar Problemleri','mq-hiz-kar-zarar',NULL,1,0,0,1,2),(36,52,24,'Savaşlar ve Tarihleri','mm-savaslar-tarihleri',NULL,1,0,0,1,1),(37,52,24,'Hükümdarlar ve Olaylar','mm-hukumdar-olaylar',NULL,1,0,0,1,2),(38,52,25,'Dağlar ve Bulunduğu Bölgeler','mm-daglar-bolgeler',NULL,1,0,0,1,1),(39,52,26,'Uluslararası Örgütler ve Merkezleri','mm-orgutler-merkezleri',NULL,1,0,0,1,1),(40,52,16,'İlk Türk Devletleri ve Teşkilat','fnl-ilk-turk-devletleri',NULL,1,0,0,1,1),(41,52,16,'Osmanlı Önemli Antlaşmalar','fnl-osmanli-antlasmalar',NULL,1,0,0,1,2),(42,52,17,'Türkiye Dağları ve Gölleri','fnl-turkiye-daglari',NULL,1,0,0,1,1),(43,52,18,'1982 Anayasası Temel Maddeler','fnl-1982-anayasa',NULL,1,0,0,1,1),(44,52,19,'Eski Türk ve Osmanlı Terimleri','gtw-eski-turk-osmanli',NULL,1,0,0,1,1),(45,52,20,'Yeryüzü Şekilleri ve İklim Terimleri','gtw-yeryuzu-sekilleri',NULL,1,0,0,1,1),(46,52,21,'Temel Hukuk ve Anayasa Kavramları','gtw-temel-hukuk',NULL,1,0,0,1,1),(47,52,22,'Sayılar ve Dört İşlem','mq-sayilar-dort-islem',NULL,1,0,0,1,1),(48,52,22,'Rasyonel ve Ondalık Sayılar','mq-rasyonel-sayilar',NULL,1,0,0,1,2),(49,52,23,'Yaş ve Yüzde Problemleri','mq-yas-yuzde-problemleri',NULL,1,0,0,1,1),(50,52,23,'Hız ve Kar-Zarar Problemleri','mq-hiz-kar-zarar',NULL,1,0,0,1,2),(51,52,24,'Savaşlar ve Tarihleri','mm-savaslar-tarihleri',NULL,1,0,0,1,1),(52,52,24,'Hükümdarlar ve Olaylar','mm-hukumdar-olaylar',NULL,1,0,0,1,2),(53,52,25,'Dağlar ve Bulunduğu Bölgeler','mm-daglar-bolgeler',NULL,1,0,0,1,1),(54,52,26,'Uluslararası Örgütler ve Merkezleri','mm-orgutler-merkezleri',NULL,1,0,0,1,1);
/*!40000 ALTER TABLE `tbl_subcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_tracker`
--

DROP TABLE IF EXISTS `tbl_tracker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_tracker` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `uid` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `points` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `type` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `status` tinyint NOT NULL COMMENT '0-add, 1-deduct',
  `date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_tracker`
--

LOCK TABLES `tbl_tracker` WRITE;
/*!40000 ALTER TABLE `tbl_tracker` DISABLE KEYS */;
INSERT INTO `tbl_tracker` VALUES (1,1,'UCSfhMkMwIgE6NObaPEByjfxH7j1','5000','welcomeBonus',1,'2026-09-06'),(2,1,'UCSfhMkMwIgE6NObaPEByjfxH7j1','2','wonQuizZone',0,'2026-09-06'),(3,1,'UCSfhMkMwIgE6NObaPEByjfxH7j1','-10','reviewAnswerLbl',1,'2026-09-06'),(4,1,'UCSfhMkMwIgE6NObaPEByjfxH7j1','-10','fiftyFifty',1,'2026-09-06'),(5,1,'UCSfhMkMwIgE6NObaPEByjfxH7j1','-10','audiencePoll',1,'2026-09-06'),(6,1,'UCSfhMkMwIgE6NObaPEByjfxH7j1','-10','resetTime',1,'2026-09-06');
/*!40000 ALTER TABLE `tbl_tracker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_upload_languages`
--

DROP TABLE IF EXISTS `tbl_upload_languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_upload_languages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(512) COLLATE utf8mb4_general_ci NOT NULL,
  `title` varchar(512) COLLATE utf8mb4_general_ci NOT NULL,
  `app_version` varchar(100) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0',
  `web_version` varchar(100) COLLATE utf8mb4_general_ci NOT NULL DEFAULT '0',
  `app_rtl_support` tinyint NOT NULL DEFAULT '0',
  `web_rtl_support` tinyint NOT NULL DEFAULT '0',
  `app_status` tinyint NOT NULL DEFAULT '0',
  `web_status` tinyint NOT NULL DEFAULT '0',
  `app_default` tinyint NOT NULL DEFAULT '0',
  `web_default` tinyint NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_upload_languages`
--

LOCK TABLES `tbl_upload_languages` WRITE;
/*!40000 ALTER TABLE `tbl_upload_languages` DISABLE KEYS */;
INSERT INTO `tbl_upload_languages` VALUES (1,'english','English','0.0.1','0.0.1',0,0,1,1,0,0),(2,'turkce','TÃ¼rkÃ§e','1.0.0','1.0.0',0,0,1,1,1,1);
/*!40000 ALTER TABLE `tbl_upload_languages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_audio_quiz_session`
--

DROP TABLE IF EXISTS `tbl_user_audio_quiz_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_audio_quiz_session` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `questions` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `questions` (`questions`(768)),
  CONSTRAINT `tbl_user_audio_quiz_session_chk_1` CHECK (json_valid(`questions`))
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_audio_quiz_session`
--

LOCK TABLES `tbl_user_audio_quiz_session` WRITE;
/*!40000 ALTER TABLE `tbl_user_audio_quiz_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_user_audio_quiz_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_category`
--

DROP TABLE IF EXISTS `tbl_user_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_category`
--

LOCK TABLES `tbl_user_category` WRITE;
/*!40000 ALTER TABLE `tbl_user_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_user_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_contest_session`
--

DROP TABLE IF EXISTS `tbl_user_contest_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_contest_session` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `questions` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `questions` (`questions`(768)),
  CONSTRAINT `tbl_user_contest_session_chk_1` CHECK (json_valid(`questions`))
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_contest_session`
--

LOCK TABLES `tbl_user_contest_session` WRITE;
/*!40000 ALTER TABLE `tbl_user_contest_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_user_contest_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_daily_quiz_session`
--

DROP TABLE IF EXISTS `tbl_user_daily_quiz_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_daily_quiz_session` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `questions` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `questions` (`questions`(768)),
  CONSTRAINT `tbl_user_daily_quiz_session_chk_1` CHECK (json_valid(`questions`))
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_daily_quiz_session`
--

LOCK TABLES `tbl_user_daily_quiz_session` WRITE;
/*!40000 ALTER TABLE `tbl_user_daily_quiz_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_user_daily_quiz_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_fun_n_learn_session`
--

DROP TABLE IF EXISTS `tbl_user_fun_n_learn_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_fun_n_learn_session` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `questions` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `questions` (`questions`(768)),
  CONSTRAINT `tbl_user_fun_n_learn_session_chk_1` CHECK (json_valid(`questions`))
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_fun_n_learn_session`
--

LOCK TABLES `tbl_user_fun_n_learn_session` WRITE;
/*!40000 ALTER TABLE `tbl_user_fun_n_learn_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_user_fun_n_learn_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_guess_the_word_session`
--

DROP TABLE IF EXISTS `tbl_user_guess_the_word_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_guess_the_word_session` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `questions` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `questions` (`questions`(768)),
  CONSTRAINT `tbl_user_guess_the_word_session_chk_1` CHECK (json_valid(`questions`))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_guess_the_word_session`
--

LOCK TABLES `tbl_user_guess_the_word_session` WRITE;
/*!40000 ALTER TABLE `tbl_user_guess_the_word_session` DISABLE KEYS */;
INSERT INTO `tbl_user_guess_the_word_session` VALUES (1,1,'[{\"id\":\"2\",\"answer\":\"TIMAR\"},{\"id\":\"1\",\"answer\":\"KURULTAY\"},{\"id\":\"3\",\"answer\":\"KUT\"},{\"id\":\"4\",\"answer\":\"MISAKIMILLI\"}]','2026-09-06');
/*!40000 ALTER TABLE `tbl_user_guess_the_word_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_maths_quiz_session`
--

DROP TABLE IF EXISTS `tbl_user_maths_quiz_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_maths_quiz_session` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `questions` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `questions` (`questions`(768)),
  CONSTRAINT `tbl_user_maths_quiz_session_chk_1` CHECK (json_valid(`questions`))
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_maths_quiz_session`
--

LOCK TABLES `tbl_user_maths_quiz_session` WRITE;
/*!40000 ALTER TABLE `tbl_user_maths_quiz_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_user_maths_quiz_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_multi_match_session`
--

DROP TABLE IF EXISTS `tbl_user_multi_match_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_multi_match_session` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `questions` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `questions` (`questions`(768)),
  CONSTRAINT `tbl_user_multi_match_session_chk_1` CHECK (json_valid(`questions`))
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_multi_match_session`
--

LOCK TABLES `tbl_user_multi_match_session` WRITE;
/*!40000 ALTER TABLE `tbl_user_multi_match_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_user_multi_match_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_quiz_zone_session`
--

DROP TABLE IF EXISTS `tbl_user_quiz_zone_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_quiz_zone_session` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `questions` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `questions` (`questions`(768)),
  CONSTRAINT `tbl_user_quiz_zone_session_chk_1` CHECK (json_valid(`questions`))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_quiz_zone_session`
--

LOCK TABLES `tbl_user_quiz_zone_session` WRITE;
/*!40000 ALTER TABLE `tbl_user_quiz_zone_session` DISABLE KEYS */;
INSERT INTO `tbl_user_quiz_zone_session` VALUES (4,1,'[{\"id\":\"16\",\"answer\":\"a\",\"level\":\"1\"}]','2026-09-06');
/*!40000 ALTER TABLE `tbl_user_quiz_zone_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_user_true_false_session`
--

DROP TABLE IF EXISTS `tbl_user_true_false_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_user_true_false_session` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `questions` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `questions` (`questions`(768)),
  CONSTRAINT `tbl_user_true_false_session_chk_1` CHECK (json_valid(`questions`))
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user_true_false_session`
--

LOCK TABLES `tbl_user_true_false_session` WRITE;
/*!40000 ALTER TABLE `tbl_user_true_false_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_user_true_false_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_users`
--

DROP TABLE IF EXISTS `tbl_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `firebase_id` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '',
  `email` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `mobile` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `type` varchar(16) COLLATE utf8mb3_unicode_ci NOT NULL,
  `profile` varchar(128) COLLATE utf8mb3_unicode_ci NOT NULL,
  `fcm_id` varchar(1024) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `web_fcm_id` varchar(1024) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `coins` int NOT NULL DEFAULT '0',
  `refer_code` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `friends_code` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `remove_ads` tinyint NOT NULL DEFAULT '0',
  `daily_ads_counter` int NOT NULL DEFAULT '0' COMMENT 'Daily ads counter',
  `daily_ads_date` date NOT NULL DEFAULT '2023-10-19' COMMENT 'Daily ads date',
  `status` int unsigned DEFAULT '0',
  `date_registered` datetime NOT NULL,
  `api_token` longtext COLLATE utf8mb3_unicode_ci NOT NULL,
  `app_language` varchar(512) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `web_language` varchar(512) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `email` (`email`,`mobile`),
  KEY `firebase_id` (`firebase_id`(333)),
  KEY `fcm_id` (`fcm_id`(333)),
  KEY `web_fcm_id` (`web_fcm_id`(333))
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_users`
--

LOCK TABLES `tbl_users` WRITE;
/*!40000 ALTER TABLE `tbl_users` DISABLE KEYS */;
INSERT INTO `tbl_users` VALUES (1,'UCSfhMkMwIgE6NObaPEByjfxH7j1','Halil','halil@quiza.com','+905551234567','email','1788724225.svg','eGrNF2nWSDy_1OkFHjXsqe:APA91bHebFXz2XT0fruMe7o5NJ0Dh8VcRI0J4ahcOJl5S2U1xTuS35qmPS6m3h1cFGpPXpC9kcfLjKsKuOLjg1Ni69v8GAp__GHuM7C6MIFKxhO1durBGk8',NULL,4960,'QUIZA1','',0,0,'2026-09-06',1,'2026-09-06 19:00:13','eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3ODg3MjQyMTgsImlzcyI6IlF1aXoiLCJleHAiOjE3OTEzMTYyMTgsInVzZXJfaWQiOiIxIiwiZmlyZWJhc2VfaWQiOiJVQ1NmaE1rTXdJZ0U2Tk9iYVBFQnlqZnhIN2oxIiwic3ViIjoiUXVpeiBBdXRoZW50aWNhdGlvbiJ9.P2vkirDynSnlG3IopdOzpb89gNWUsk03ISTpw2PQf0o','turkce','turkce'),(2,'fb_2_kpss','Ahmet Yılmaz','ahmet@quiza.com','+905001112233','email','',NULL,NULL,2500,NULL,NULL,0,0,'2023-10-19',1,'2026-09-06 20:02:32','token_2','turkce','turkce'),(3,'fb_3_kpss','Elif Demir','elif@quiza.com','+905001112233','email','',NULL,NULL,2500,NULL,NULL,0,0,'2023-10-19',1,'2026-09-06 20:02:32','token_3','turkce','turkce'),(4,'fb_4_kpss','Merve Kaya','merve@quiza.com','+905001112233','email','',NULL,NULL,2500,NULL,NULL,0,0,'2023-10-19',1,'2026-09-06 20:02:32','token_4','turkce','turkce'),(5,'fb_5_kpss','Burak Şahin','burak@quiza.com','+905001112233','email','',NULL,NULL,2500,NULL,NULL,0,0,'2023-10-19',1,'2026-09-06 20:02:32','token_5','turkce','turkce'),(6,'fb_6_kpss','Zeynep Çelik','zeynep@quiza.com','+905001112233','email','',NULL,NULL,2500,NULL,NULL,0,0,'2023-10-19',1,'2026-09-06 20:02:32','token_6','turkce','turkce'),(7,'fb_7_kpss','Oğuzhan Koç','oguzhan@quiza.com','+905001112233','email','',NULL,NULL,2500,NULL,NULL,0,0,'2023-10-19',1,'2026-09-06 20:02:32','token_7','turkce','turkce'),(8,'fb_8_kpss','Fatma Yıldız','fatma@quiza.com','+905001112233','email','',NULL,NULL,2500,NULL,NULL,0,0,'2023-10-19',1,'2026-09-06 20:02:32','token_8','turkce','turkce'),(9,'fb_9_kpss','Emre Arslan','emre@quiza.com','+905001112233','email','',NULL,NULL,2500,NULL,NULL,0,0,'2023-10-19',1,'2026-09-06 20:02:32','token_9','turkce','turkce'),(10,'fb_10_kpss','Selin Aydın','selin@quiza.com','+905001112233','email','',NULL,NULL,2500,NULL,NULL,0,0,'2023-10-19',1,'2026-09-06 20:02:32','token_10','turkce','turkce');
/*!40000 ALTER TABLE `tbl_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_users_badges`
--

DROP TABLE IF EXISTS `tbl_users_badges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_users_badges` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `dashing_debut` int NOT NULL,
  `dashing_debut_counter` int NOT NULL,
  `combat_winner` int NOT NULL,
  `combat_winner_counter` int NOT NULL,
  `clash_winner` int NOT NULL,
  `clash_winner_counter` int NOT NULL,
  `most_wanted_winner` int NOT NULL,
  `most_wanted_winner_counter` int NOT NULL,
  `ultimate_player` int NOT NULL,
  `quiz_warrior` int NOT NULL,
  `quiz_warrior_counter` int NOT NULL,
  `super_sonic` int NOT NULL,
  `flashback` int NOT NULL,
  `brainiac` int NOT NULL,
  `big_thing` int NOT NULL,
  `elite` int NOT NULL,
  `thirsty` int NOT NULL,
  `thirsty_date` date DEFAULT NULL,
  `thirsty_counter` int NOT NULL,
  `power_elite` int NOT NULL,
  `power_elite_counter` int NOT NULL,
  `sharing_caring` int NOT NULL,
  `streak` int NOT NULL,
  `streak_date` date DEFAULT NULL,
  `streak_counter` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_users_badges`
--

LOCK TABLES `tbl_users_badges` WRITE;
/*!40000 ALTER TABLE `tbl_users_badges` DISABLE KEYS */;
INSERT INTO `tbl_users_badges` VALUES (1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,'0000-00-00',0,0,2,0,0,'2026-09-06',1);
/*!40000 ALTER TABLE `tbl_users_badges` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_users_in_app`
--

DROP TABLE IF EXISTS `tbl_users_in_app`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_users_in_app` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pay_from` tinyint NOT NULL COMMENT '1=android,2=ios',
  `uid` longtext NOT NULL,
  `user_id` int NOT NULL,
  `product_id` text NOT NULL,
  `amount` int NOT NULL,
  `status` varchar(50) NOT NULL,
  `transaction_id` text NOT NULL,
  `date` datetime NOT NULL,
  `purchase_token` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `responseData` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `uid` (`uid`(3072)),
  KEY `product_id` (`product_id`(3072))
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_users_in_app`
--

LOCK TABLES `tbl_users_in_app` WRITE;
/*!40000 ALTER TABLE `tbl_users_in_app` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_users_in_app` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_users_statistics`
--

DROP TABLE IF EXISTS `tbl_users_statistics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_users_statistics` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `questions_answered` int NOT NULL,
  `correct_answers` int NOT NULL,
  `strong_category` int NOT NULL,
  `ratio1` double NOT NULL,
  `weak_category` int NOT NULL,
  `ratio2` double NOT NULL,
  `best_position` int NOT NULL,
  `date_created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_users_statistics`
--

LOCK TABLES `tbl_users_statistics` WRITE;
/*!40000 ALTER TABLE `tbl_users_statistics` DISABLE KEYS */;
INSERT INTO `tbl_users_statistics` VALUES (1,1,2,1,0,0,1,50,0,'2026-09-06 22:50:54');
/*!40000 ALTER TABLE `tbl_users_statistics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_web_settings`
--

DROP TABLE IF EXISTS `tbl_web_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_web_settings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `language_id` int DEFAULT '14',
  `type` varchar(32) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_web_settings`
--

LOCK TABLES `tbl_web_settings` WRITE;
/*!40000 ALTER TABLE `tbl_web_settings` DISABLE KEYS */;
INSERT INTO `tbl_web_settings` VALUES (1,14,'favicon','favicon-1680233344.png'),(2,14,'header_logo','header_logo-1679987557.svg'),(3,14,'footer_logo','footer_logo-1679987557.svg'),(4,14,'sticky_header_logo','sticky_header_logo-1679987557.svg'),(5,14,'quiz_zone_icon','quiz_zone_icon-1680083222.svg'),(6,14,'daily_quiz_icon','daily_quiz_icon-1680083222.svg'),(7,14,'true_false_icon','true_false_icon-1680263423.svg'),(8,14,'fun_learn_icon','fun_learn_icon-1680083222.svg'),(9,14,'self_challange_icon','self_challange_icon-1680083222.svg'),(10,14,'contest_play_icon','contest_play_icon-1680083222.svg'),(11,14,'one_one_battle_icon','one_one_battle_icon-1680083222.svg'),(12,14,'group_battle_icon','group_battle_icon-1680083222.svg'),(13,14,'audio_question_icon','audio_question_icon-1680083222.svg'),(14,14,'math_mania_icon','math_mania_icon-1680083222.svg'),(15,14,'exam_icon','exam_icon-1680083222.svg'),(16,14,'guess_the_word_icon','guess_the_word_icon-1680083222.svg'),(17,14,'section1_heading','Why Choose Us Our Elite Quiz'),(18,14,'section1_heading','Why Choose Us Our Elite Quiz'),(19,14,'section1_title1','Life Lines'),(20,14,'section1_title2','Leaderboard'),(21,14,'section1_title3','Money Withdrawal'),(22,14,'section1_image1','section1_image1.svg'),(23,14,'section1_image2','section1_image2.svg'),(24,14,'section1_image3','section1_image3.svg'),(25,14,'section1_desc1','These lifelines are your secret weapons to help you secure the correct answers during gameplay. Use them wisely to boost your chances of winning!'),(26,14,'section1_desc2','Check out our Leaderboard to discover the top scorers in various quizzes. Join the competition and climb the ranks.'),(27,14,'section1_desc3','Unlock Money Withdrawal and transform quiz victories into tangible cash rewards. Earn while you quiz!'),(28,14,'section2_heading','Incredible Quiz Features'),(29,14,'section2_title1','Quizzes by category'),(30,14,'section2_title2','Quizzes by Language'),(31,14,'section2_title3','Battle Quiz'),(32,14,'section2_title4','Guess the Word'),(33,14,'section2_image1','section2_image1.svg'),(34,14,'section2_image2','section2_image2.svg'),(35,14,'section2_image3','section2_image3.svg'),(36,14,'section2_image4','section2_image4.svg'),(37,14,'section2_desc1','Dive into category-based quizzes for an engaging and informative challenge.'),(38,14,'section2_desc2','Explore quizzes tailored to your language preference for a personalized quiz experience.'),(39,14,'section2_desc3','Engage in epic quiz battles and prove your knowledge supremacy.'),(40,14,'section2_desc4','Put your vocabulary to the test with our challenging Guess the Word Quiz.'),(41,14,'section3_heading','Elite QuizBest Part'),(42,14,'section3_title1','Regular Udpates'),(43,14,'section3_title2','Competitive Fun'),(44,14,'section3_title3','Global Community'),(45,14,'section3_title4','All-age Inclusivity'),(46,14,'section3_image1','section3_image1.svg'),(47,14,'section3_image2','section3_image2.svg'),(48,14,'section3_image3','section3_image3.svg'),(49,14,'section3_image4','section3_image4.svg'),(50,14,'section3_desc1','Regularly Updated Quizzes for a Fresh and Exciting Learning Experience.'),(51,14,'section3_desc2','Test Your Knowledge and Challenge Others. Compete, Test, Challenge!'),(52,14,'section3_desc3','Join the Elite Quiz Global Community and Expand Your Knowledge Together!'),(53,14,'section3_desc4','Elite Quiz for Kids, Teens, & Adults - Fun Learning for Everyone!'),(54,14,'section_1_mode','1'),(55,14,'section_2_mode','1'),(56,14,'section_3_mode','1'),(57,14,'notification_title','Congratulations !'),(58,14,'notification_body','You have unlocked new badge.'),(59,14,'primary_color','#EF5388FF'),(60,14,'footer_color','#090029FF'),(61,14,'firebase_api_key',''),(62,14,'firebase_auth_domain',''),(63,14,'firebase_database_url',''),(64,14,'firebase_project_id',''),(65,14,'firebase_storage_bucket',''),(66,14,'firebase_messager_sender_id',''),(67,14,'firebase_app_id',''),(68,14,'firebase_measurement_id',''),(70,14,'company_name_footer','elite'),(71,14,'email_footer','xyz@gmail.com'),(72,14,'phone_number_footer','+91 9876543210'),(73,14,'web_link_footer','https://xyz.in/'),(74,14,'company_text','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'),(75,14,'address_text','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'),(76,14,'social_media','[{\"link\":\"https:\\/\\/www.facebook.com\\/\",\"icon\":\"social_media-1723629667.png\"}]'),(77,14,'multi_match_icon','multi_match_icon-1746608378.svg');
/*!40000 ALTER TABLE `tbl_web_settings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-09-07 14:00:57
