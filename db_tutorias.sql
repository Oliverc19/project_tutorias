-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: db_tutorias
-- ------------------------------------------------------
-- Server version	8.0.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add materia',7,'add_materia'),(26,'Can change materia',7,'change_materia'),(27,'Can delete materia',7,'delete_materia'),(28,'Can view materia',7,'view_materia'),(29,'Can add persona',8,'add_persona'),(30,'Can change persona',8,'change_persona'),(31,'Can delete persona',8,'delete_persona'),(32,'Can view persona',8,'view_persona'),(33,'Can add estudiante',9,'add_estudiante'),(34,'Can change estudiante',9,'change_estudiante'),(35,'Can delete estudiante',9,'delete_estudiante'),(36,'Can view estudiante',9,'view_estudiante'),(37,'Can add Tutor',10,'add_tutor'),(38,'Can change Tutor',10,'change_tutor'),(39,'Can delete Tutor',10,'delete_tutor'),(40,'Can view Tutor',10,'view_tutor'),(41,'Can add Tutoría',11,'add_tutoria'),(42,'Can change Tutoría',11,'change_tutoria'),(43,'Can delete Tutoría',11,'delete_tutoria'),(44,'Can view Tutoría',11,'view_tutoria');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$NwHBB5id3YauA70m7xgPGE$uQ1NaNHfxnZbpNA4VcgCnU5tY7e17nC4y8+G+n6IdJQ=','2026-06-16 19:43:55.654068',1,'admin','','','',1,1,'2026-06-16 19:43:11.655752');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2026-06-16 20:19:53.722073','10235435','10235435 - Rodrigo Escobar Silva (rodri99@gmail.com) - matematicas',1,'[{\"added\": {}}]',10,1),(2,'2026-06-16 20:20:36.048830','1364686','1364686 - Sergio Poma Perez (serg@gmail.com)',1,'[{\"added\": {}}]',8,1),(3,'2026-06-16 20:20:52.181441','89012345','89012345 - Daniela Vargas Laime (daniela.vargas@ucb.edu.bo)',2,'[{\"changed\": {\"fields\": [\"Rol\"]}}]',8,1),(4,'2026-06-16 20:20:58.664406','78901234','78901234 - Roberto Apaza Poma (roberto.apaza@ucb.edu.bo)',2,'[{\"changed\": {\"fields\": [\"Rol\"]}}]',8,1),(5,'2026-06-16 20:21:04.319089','67890123','67890123 - Valeria Choque Vargas (valeria.choque@ucb.edu.bo)',2,'[{\"changed\": {\"fields\": [\"Rol\"]}}]',8,1),(6,'2026-06-16 20:21:10.292405','45678901','45678901 - María Flores Huanca (maria.flores@ucb.edu.bo)',2,'[{\"changed\": {\"fields\": [\"Rol\"]}}]',8,1),(7,'2026-06-16 20:21:15.613664','23456789','23456789 - Ana Quispe Flores (ana.quispe@ucb.edu.bo)',2,'[{\"changed\": {\"fields\": [\"Rol\"]}}]',8,1),(8,'2026-06-16 20:21:28.188684','45678901','45678901 - María Flores Huanca (maria.flores@ucb.edu.bo) - medicina',1,'[{\"added\": {}}]',10,1),(9,'2026-06-16 20:21:39.653480','1364686','1364686 - Sergio Poma Perez (serg@gmail.com) - Informatica (700312)',1,'[{\"added\": {}}]',9,1),(10,'2026-06-16 20:21:52.780796','67890123','67890123 - Valeria Choque Vargas (valeria.choque@ucb.edu.bo) - medicina (78646)',1,'[{\"added\": {}}]',9,1),(11,'2026-06-16 20:22:13.266720','78901234','78901234 - Roberto Apaza Poma (roberto.apaza@ucb.edu.bo) - mecatronica (56798)',1,'[{\"added\": {}}]',9,1),(12,'2026-06-16 20:22:38.515322','1','matematicas',1,'[{\"added\": {}}]',7,1),(13,'2026-06-16 20:22:50.201883','2','cirugia',1,'[{\"added\": {}}]',7,1),(14,'2026-06-16 20:23:11.797743','1','matematicas - pendiente',1,'[{\"added\": {}}]',11,1),(15,'2026-06-16 20:23:29.742149','2','cirugia - rechazada',1,'[{\"added\": {}}]',11,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(9,'gestion_tutorias','estudiante'),(7,'gestion_tutorias','materia'),(8,'gestion_tutorias','persona'),(10,'gestion_tutorias','tutor'),(11,'gestion_tutorias','tutoria'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-06-16 19:40:02.774258'),(2,'auth','0001_initial','2026-06-16 19:40:20.972484'),(3,'admin','0001_initial','2026-06-16 19:40:24.199152'),(4,'admin','0002_logentry_remove_auto_add','2026-06-16 19:40:24.299092'),(5,'admin','0003_logentry_add_action_flag_choices','2026-06-16 19:40:24.466958'),(6,'contenttypes','0002_remove_content_type_name','2026-06-16 19:40:26.711865'),(7,'auth','0002_alter_permission_name_max_length','2026-06-16 19:40:27.933927'),(8,'auth','0003_alter_user_email_max_length','2026-06-16 19:40:28.241997'),(9,'auth','0004_alter_user_username_opts','2026-06-16 19:40:28.367923'),(10,'auth','0005_alter_user_last_login_null','2026-06-16 19:40:29.595295'),(11,'auth','0006_require_contenttypes_0002','2026-06-16 19:40:29.652739'),(12,'auth','0007_alter_validators_add_error_messages','2026-06-16 19:40:29.750687'),(13,'auth','0008_alter_user_username_max_length','2026-06-16 19:40:31.190049'),(14,'auth','0009_alter_user_last_name_max_length','2026-06-16 19:40:33.868576'),(15,'auth','0010_alter_group_name_max_length','2026-06-16 19:40:34.204310'),(16,'auth','0011_update_proxy_permissions','2026-06-16 19:40:34.425724'),(17,'auth','0012_alter_user_first_name_max_length','2026-06-16 19:40:36.223943'),(18,'gestion_tutorias','0001_initial','2026-06-16 19:40:49.350608'),(19,'sessions','0001_initial','2026-06-16 19:40:50.446851');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('wdwvdz47w9nmxwruwqbsshpgxasrjcau','.eJxVjDEOwjAMAP_iGUXYSUjTkZ03VE7s0AJKpaadEH9HlTrAene6Nwy8reOwNV2GSaAHhNMvS5yfWnchD6732eS5rsuUzJ6YwzZzm0Vf16P9G4zcRuiBkFxRXxLZs1hPHXofvItRqEMsmZyIXBJpjGgZo4RgOWFXgouKovD5Ar4hN0s:1wZZhT:qaUgC_OGM5-On29ezPFcNs5-zi1p1_pgQWMWB1iZ_iM','2026-06-30 19:43:55.932594');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestion_tutorias_estudiante`
--

DROP TABLE IF EXISTS `gestion_tutorias_estudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestion_tutorias_estudiante` (
  `persona_id` varchar(15) NOT NULL,
  `carrera` varchar(100) NOT NULL,
  `codigo_estudiante` varchar(20) NOT NULL,
  PRIMARY KEY (`persona_id`),
  UNIQUE KEY `codigo_estudiante` (`codigo_estudiante`),
  CONSTRAINT `gestion_tutorias_est_persona_id_62e51eea_fk_gestion_t` FOREIGN KEY (`persona_id`) REFERENCES `gestion_tutorias_persona` (`ci`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestion_tutorias_estudiante`
--

LOCK TABLES `gestion_tutorias_estudiante` WRITE;
/*!40000 ALTER TABLE `gestion_tutorias_estudiante` DISABLE KEYS */;
INSERT INTO `gestion_tutorias_estudiante` VALUES ('1364686','Informatica','700312'),('67890123','medicina','78646'),('78901234','mecatronica','56798');
/*!40000 ALTER TABLE `gestion_tutorias_estudiante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestion_tutorias_materia`
--

DROP TABLE IF EXISTS `gestion_tutorias_materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestion_tutorias_materia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `codigo` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestion_tutorias_materia`
--

LOCK TABLES `gestion_tutorias_materia` WRITE;
/*!40000 ALTER TABLE `gestion_tutorias_materia` DISABLE KEYS */;
INSERT INTO `gestion_tutorias_materia` VALUES (1,'matematicas','456'),(2,'cirugia','388');
/*!40000 ALTER TABLE `gestion_tutorias_materia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestion_tutorias_persona`
--

DROP TABLE IF EXISTS `gestion_tutorias_persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestion_tutorias_persona` (
  `ci` varchar(15) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `paterno` varchar(50) NOT NULL,
  `materno` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `rol` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ci`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestion_tutorias_persona`
--

LOCK TABLES `gestion_tutorias_persona` WRITE;
/*!40000 ALTER TABLE `gestion_tutorias_persona` DISABLE KEYS */;
INSERT INTO `gestion_tutorias_persona` VALUES ('01234567','Patricia','Laime','Condori','patricia.laime@ucb.edu.bo','estudiante'),('10235435','Rodrigo','Escobar','Silva','rodri99@gmail.com','TUT'),('12345678','Carlos','Mamani','Quispe','carlos.mamani@ucb.edu.bo','tutor'),('1364686','Sergio','Poma','Perez','serg@gmail.com','EST'),('23456789','Ana','Quispe','Flores','ana.quispe@ucb.edu.bo','EST'),('34567890','Luis','Condori','Apaza','luis.condori@ucb.edu.bo','tutor'),('45678901','María','Flores','Huanca','maria.flores@ucb.edu.bo','TUT'),('56789012','Jorge','Huanca','Choque','jorge.huanca@ucb.edu.bo','tutor'),('67890123','Valeria','Choque','Vargas','valeria.choque@ucb.edu.bo','EST'),('78901234','Roberto','Apaza','Poma','roberto.apaza@ucb.edu.bo','EST'),('89012345','Daniela','Vargas','Laime','daniela.vargas@ucb.edu.bo','EST'),('90123456','Sergio','Poma','Mamani','sergio.poma@ucb.edu.bo','estudiante');
/*!40000 ALTER TABLE `gestion_tutorias_persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestion_tutorias_tutor`
--

DROP TABLE IF EXISTS `gestion_tutorias_tutor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestion_tutorias_tutor` (
  `persona_id` varchar(15) NOT NULL,
  `especialidad` varchar(100) NOT NULL,
  PRIMARY KEY (`persona_id`),
  CONSTRAINT `gestion_tutorias_tut_persona_id_0df035d1_fk_gestion_t` FOREIGN KEY (`persona_id`) REFERENCES `gestion_tutorias_persona` (`ci`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestion_tutorias_tutor`
--

LOCK TABLES `gestion_tutorias_tutor` WRITE;
/*!40000 ALTER TABLE `gestion_tutorias_tutor` DISABLE KEYS */;
INSERT INTO `gestion_tutorias_tutor` VALUES ('10235435','matematicas'),('45678901','medicina');
/*!40000 ALTER TABLE `gestion_tutorias_tutor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestion_tutorias_tutoria`
--

DROP TABLE IF EXISTS `gestion_tutorias_tutoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestion_tutorias_tutoria` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `materia_id` int NOT NULL,
  `estudiante_id` varchar(15) NOT NULL,
  `tutor_id` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gestion_tutorias_tut_materia_id_c3087a35_fk_gestion_t` (`materia_id`),
  KEY `gestion_tutorias_tut_estudiante_id_774e21aa_fk_gestion_t` (`estudiante_id`),
  KEY `gestion_tutorias_tut_tutor_id_cd132e58_fk_gestion_t` (`tutor_id`),
  CONSTRAINT `gestion_tutorias_tut_estudiante_id_774e21aa_fk_gestion_t` FOREIGN KEY (`estudiante_id`) REFERENCES `gestion_tutorias_estudiante` (`persona_id`),
  CONSTRAINT `gestion_tutorias_tut_materia_id_c3087a35_fk_gestion_t` FOREIGN KEY (`materia_id`) REFERENCES `gestion_tutorias_materia` (`id`),
  CONSTRAINT `gestion_tutorias_tut_tutor_id_cd132e58_fk_gestion_t` FOREIGN KEY (`tutor_id`) REFERENCES `gestion_tutorias_tutor` (`persona_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestion_tutorias_tutoria`
--

LOCK TABLES `gestion_tutorias_tutoria` WRITE;
/*!40000 ALTER TABLE `gestion_tutorias_tutoria` DISABLE KEYS */;
INSERT INTO `gestion_tutorias_tutoria` VALUES (1,'2026-06-16 20:23:07.000000','pendiente',1,'1364686','10235435'),(2,'2026-06-16 20:23:26.000000','rechazada',2,'67890123','45678901');
/*!40000 ALTER TABLE `gestion_tutorias_tutoria` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-16 15:27:32
