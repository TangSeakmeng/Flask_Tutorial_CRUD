/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80013
 Source Host           : localhost:3309
 Source Schema         : flask_tutorial

 Target Server Type    : MySQL
 Target Server Version : 80013
 File Encoding         : 65001

 Date: 28/06/2020 17:18:28
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tblcategory
-- ----------------------------
DROP TABLE IF EXISTS `tblcategory`;
CREATE TABLE `tblcategory`  (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `categoryname` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tblcategory
-- ----------------------------
INSERT INTO `tblcategory` VALUES (1, 'Extended Stay America, Inc.');
INSERT INTO `tblcategory` VALUES (2, 'Extended Stay America, Inc.');
INSERT INTO `tblcategory` VALUES (3, 'Mercer International Inc.');
INSERT INTO `tblcategory` VALUES (4, 'Lifeway Foods, Inc.');
INSERT INTO `tblcategory` VALUES (5, 'CenturyLink, Inc.');
INSERT INTO `tblcategory` VALUES (6, 'Newell Brands Inc.');
INSERT INTO `tblcategory` VALUES (7, 'Rave Restaurant Group, Inc.');
INSERT INTO `tblcategory` VALUES (8, 'Two Harbors Investments Corp');
INSERT INTO `tblcategory` VALUES (9, 'U.S. Bancorp');
INSERT INTO `tblcategory` VALUES (10, 'Koss Corporation');
INSERT INTO `tblcategory` VALUES (11, 'computer');
INSERT INTO `tblcategory` VALUES (12, 'computer');
INSERT INTO `tblcategory` VALUES (13, 'phone');

-- ----------------------------
-- Table structure for tblproduct
-- ----------------------------
DROP TABLE IF EXISTS `tblproduct`;
CREATE TABLE `tblproduct`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `description` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `categoryid` int(11) NULL DEFAULT NULL,
  `quantity` int(11) NULL DEFAULT NULL,
  `price` float NULL DEFAULT NULL,
  `image` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `categoryid`(`categoryid`) USING BTREE,
  CONSTRAINT `tblproduct_ibfk_1` FOREIGN KEY (`categoryid`) REFERENCES `tblcategory` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 52 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tblproduct
-- ----------------------------
INSERT INTO `tblproduct` VALUES (3, 'Rhyloo', 'usnews.com', 6, 58, 235, 'SollicitudinUt.png');
INSERT INTO `tblproduct` VALUES (4, 'Meezzy', 'homestead.com', 4, 29, 263, 'PellentesqueQuisque.jpeg');
INSERT INTO `tblproduct` VALUES (5, 'Twimm', 'goodreads.com', 10, 77, 260, 'Nibh.tiff');
INSERT INTO `tblproduct` VALUES (6, 'Avaveo', 'edublogs.org', 2, 55, 708, 'Sed.png');
INSERT INTO `tblproduct` VALUES (7, 'Edgeblab', 'freewebs.com', 2, 9, 103, 'ArcuAdipiscing.tiff');
INSERT INTO `tblproduct` VALUES (8, 'Devcast', 'google.nl', 8, 7, 820, 'VariusIntegerAc.jpeg');
INSERT INTO `tblproduct` VALUES (9, 'Midel', 'sciencedaily.com', 10, 45, 47, 'Nascetur.png');
INSERT INTO `tblproduct` VALUES (10, 'Jabbersphere', 'linkedin.com', 8, 58, 109, 'MorbiVestibulum.png');
INSERT INTO `tblproduct` VALUES (11, 'Feedfire', 'stanford.edu', 4, 32, 288, 'Sagittis.jpeg');
INSERT INTO `tblproduct` VALUES (12, 'Photofeed', 'dailymotion.com', 8, 39, 557, 'Luctus.png');
INSERT INTO `tblproduct` VALUES (13, 'Eayo', 'goo.gl', 9, 58, 866, 'Egestas.jpeg');
INSERT INTO `tblproduct` VALUES (14, 'Trupe', 'wikia.com', 4, 83, 50, 'Orci.tiff');
INSERT INTO `tblproduct` VALUES (15, 'Browsecat', 'smugmug.com', 1, 36, 250, 'EstCongueElementum.png');
INSERT INTO `tblproduct` VALUES (16, 'Tekfly', 'dedecms.com', 7, 25, 109, 'AtNulla.tiff');
INSERT INTO `tblproduct` VALUES (17, 'Jabbersphere', 'soundcloud.com', 3, 97, 36, 'Volutpat.tiff');
INSERT INTO `tblproduct` VALUES (18, 'Thoughtstorm', 'businessinsider.com', 3, 39, 591, 'OrciNullamMolestie.tiff');
INSERT INTO `tblproduct` VALUES (19, 'Teklist', 'sciencedaily.com', 8, 31, 661, 'TempusVivamusIn.jpeg');
INSERT INTO `tblproduct` VALUES (20, 'Feedfish', 'mozilla.org', 3, 1, 575, 'NuncCommodo.jpeg');
INSERT INTO `tblproduct` VALUES (21, 'Skipstorm', 'hp.com', 8, 82, 637, 'Ac.tiff');
INSERT INTO `tblproduct` VALUES (22, 'Riffpedia', 'meetup.com', 2, 89, 815, 'PedeLibero.tiff');
INSERT INTO `tblproduct` VALUES (23, 'Voonte', 'sciencedaily.com', 4, 82, 831, 'JustoLaciniaEget.gif');
INSERT INTO `tblproduct` VALUES (24, 'Zoombox', 'mapquest.com', 6, 23, 438, 'Id.gif');
INSERT INTO `tblproduct` VALUES (25, 'Yata', 'cdc.gov', 8, 65, 888, 'CrasIn.jpeg');
INSERT INTO `tblproduct` VALUES (26, 'Buzzster', 'gizmodo.com', 1, 59, 926, 'DuiLuctus.png');
INSERT INTO `tblproduct` VALUES (27, 'Skippad', 'virginia.edu', 2, 35, 484, 'Vel.jpeg');
INSERT INTO `tblproduct` VALUES (28, 'Skiba', 'angelfire.com', 8, 64, 643, 'PellentesqueQuisquePorta.tiff');
INSERT INTO `tblproduct` VALUES (29, 'Ainyx', 'unblog.fr', 9, 43, 955, 'Mauris.png');
INSERT INTO `tblproduct` VALUES (30, 'Dabjam', 'cloudflare.com', 6, 32, 534, 'EgetTinciduntEget.png');
INSERT INTO `tblproduct` VALUES (31, 'Gigazoom', 'google.de', 2, 32, 158, 'PedeJustoLacinia.jpeg');
INSERT INTO `tblproduct` VALUES (32, 'LiveZ', 'sohu.com', 1, 86, 104, 'LaciniaErat.jpeg');
INSERT INTO `tblproduct` VALUES (33, 'Brainsphere', 'google.de', 2, 32, 631, 'EratCurabitur.jpeg');
INSERT INTO `tblproduct` VALUES (34, 'Linktype', 'ucsd.edu', 3, 57, 600, 'Interdum.png');
INSERT INTO `tblproduct` VALUES (35, 'Zoomzone', 'technorati.com', 10, 29, 808, 'Sed.jpeg');
INSERT INTO `tblproduct` VALUES (36, 'Topiczoom', 'exblog.jp', 2, 10, 107, 'AcEnim.jpeg');
INSERT INTO `tblproduct` VALUES (37, 'Blogpad', 'hubpages.com', 2, 10, 330, 'VelIpsum.png');
INSERT INTO `tblproduct` VALUES (38, 'Oyonder', 'stumbleupon.com', 3, 31, 154, 'Rhoncus.tiff');
INSERT INTO `tblproduct` VALUES (39, 'Miboo', 'umich.edu', 5, 86, 660, 'InFelisDonec.jpeg');
INSERT INTO `tblproduct` VALUES (40, 'Jazzy', 'newsvine.com', 6, 95, 380, 'DuiLuctus.tiff');
INSERT INTO `tblproduct` VALUES (41, 'Dynabox', 'tinypic.com', 1, 22, 508, 'ElementumPellentesque.jpeg');
INSERT INTO `tblproduct` VALUES (42, 'Jaxspan', 'shutterfly.com', 1, 47, 869, 'SapienCursus.tiff');
INSERT INTO `tblproduct` VALUES (43, 'Flipopia', 'zdnet.com', 3, 72, 613, 'EtiamPretiumIaculis.tiff');
INSERT INTO `tblproduct` VALUES (44, 'Yamia', 'home.pl', 2, 87, 733, 'Potenti.tiff');
INSERT INTO `tblproduct` VALUES (45, 'Jabbersphere', 'reverbnation.com', 1, 23, 343, 'MorbiNon.tiff');
INSERT INTO `tblproduct` VALUES (46, 'Flipopia', 'opera.com', 6, 70, 432, 'Id.jpeg');
INSERT INTO `tblproduct` VALUES (47, 'Livetube', 'yelp.com', 2, 84, 234, 'Amet.tiff');
INSERT INTO `tblproduct` VALUES (48, 'Skajo', 'tiny.cc', 9, 93, 21, 'EratId.tiff');
INSERT INTO `tblproduct` VALUES (49, 'bro oupor', 'oupor', 8, 5, 10, 'Conor.jpg');
INSERT INTO `tblproduct` VALUES (50, 'chhorn phallabot', 'kilonoob', 9, 50, 2000, '4k-wallpapers-phone-Is-4K-Wallpaper.jpg');
INSERT INTO `tblproduct` VALUES (51, 'jeff', 'mage', 10, 50, 500, '1.jpg');

SET FOREIGN_KEY_CHECKS = 1;
