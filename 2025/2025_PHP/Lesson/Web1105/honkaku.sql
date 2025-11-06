-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- ホスト: 127.0.0.1
-- 生成日時: 2025-11-05 07:57:28
-- サーバのバージョン： 10.4.32-MariaDB
-- PHP のバージョン: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- データベース: `honkaku`
--

-- --------------------------------------------------------

--
-- テーブルの構造 `books`
--

CREATE TABLE `books` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `created` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `modified` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `title` varchar(255) NOT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `published` date DEFAULT NULL,
  `price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- テーブルのデータのダンプ `books`
--

INSERT INTO `books` (`id`, `created`, `modified`, `title`, `publisher`, `published`, `price`) VALUES
(2, '2025-10-30 00:14:42', '2025-10-30 00:14:42', 'オカリナで吹く　どうよう100選', 'こども出版社', '2018-01-15', 1500),
(3, '2025-10-30 00:46:23', '2025-10-30 00:46:23', 'あそぼう！micro:bit', 'こどものあそび協会', '2018-03-15', 1245),
(4, '2025-10-30 00:14:42', '2025-10-30 00:14:42', '薬膳料理　きほんの「き」', '料理評論社', '2018-03-21', 1100),
(5, '2025-10-30 00:14:42', '2025-10-30 00:14:42', '写真集～鳥取砂丘の花たち', '南国出版', '2018-04-01', 2400),
(6, '2025-10-30 00:14:42', '2025-10-30 00:14:42', '日本の名曲喫茶', 'クラシックアカデミー社', '2018-04-06', NULL),
(7, '2025-10-30 00:14:43', '2025-10-30 00:14:43', 'シンガポール料理50選', 'ワールド出版社', '2018-04-15', 2650),
(8, '2025-10-30 00:47:55', '2025-10-30 00:47:55', 'テナーのサックスの基本', NULL, NULL, 1400),
(9, '2025-10-30 00:49:22', '2025-10-30 00:49:22', 'ソプラノリコーダーの基本', NULL, NULL, 1030),
(10, '2025-10-30 01:34:21', '2025-10-30 01:34:21', 'たのしいバドミントン', NULL, NULL, 820),
(11, '2025-10-30 02:05:56', '2025-10-30 02:05:56', 'TEST BOOK 1(bindValue)', NULL, NULL, NULL),
(12, '2025-10-30 02:05:56', '2025-10-30 02:05:56', 'TEST BOOK 2(bindValue)', NULL, NULL, NULL),
(13, '2025-10-30 02:05:56', '2025-10-30 02:05:56', 'TEST BOOK 3(bindValue)', NULL, NULL, NULL),
(14, '2025-10-30 02:05:56', '2025-10-30 02:05:56', 'TEST BOOK 1(bindParam)', NULL, NULL, NULL),
(15, '2025-10-30 02:05:56', '2025-10-30 02:05:56', 'TEST BOOK 2(bindParam)', NULL, NULL, NULL),
(16, '2025-10-30 02:05:56', '2025-10-30 02:05:56', 'TEST BOOK 3(bindParam)', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- テーブルの構造 `collate_tests`
--

CREATE TABLE `collate_tests` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `value1` varchar(255) DEFAULT NULL,
  `value2` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `value3` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- テーブルのデータのダンプ `collate_tests`
--

INSERT INTO `collate_tests` (`id`, `value1`, `value2`, `value3`) VALUES
(1, 'abc', 'abc', 'abc'),
(2, 'xyz', 'xyz', 'xyz'),
(3, 'あいう', 'あいう', 'あいう'),
(4, 'ABC', 'ABC', 'ABC'),
(5, 'XYZ', 'XYZ', 'XYZ'),
(6, 'アイウ', 'アイウ', 'アイウ'),
(7, 'ＡＢＣ', 'ＡＢＣ', 'ＡＢＣ'),
(8, 'ＸＹＺ', 'ＸＹＺ', 'ＸＹＺ'),
(9, 'ｱｲｳ', 'ｱｲｳ', 'ｱｲｳ');

-- --------------------------------------------------------

--
-- テーブルの構造 `items`
--

CREATE TABLE `items` (
  `price` int(11) DEFAULT NULL,
  `tax_type` tinyint(4) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- テーブルの構造 `members`
--

CREATE TABLE `members` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `emp_num` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- ダンプしたテーブルのインデックス
--

--
-- テーブルのインデックス `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- テーブルのインデックス `collate_tests`
--
ALTER TABLE `collate_tests`
  ADD PRIMARY KEY (`id`);

--
-- テーブルのインデックス `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `emp_num` (`emp_num`);

--
-- ダンプしたテーブルの AUTO_INCREMENT
--

--
-- テーブルの AUTO_INCREMENT `books`
--
ALTER TABLE `books`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- テーブルの AUTO_INCREMENT `collate_tests`
--
ALTER TABLE `collate_tests`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- テーブルの AUTO_INCREMENT `members`
--
ALTER TABLE `members`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
