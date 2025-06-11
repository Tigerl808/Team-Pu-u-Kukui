-- MySQL scripts
-- @author Tiger Li 2024
-- Database hacc2024
DROP DATABASE IF EXISTS hacc2024;
CREATE DATABASE IF NOT EXISTS hacc2024;
USE hacc2024;
--  Table broadbcover_by_city
CREATE TABLE `broadbcover_by_city` (
  `cid` INT NOT NULL PRIMARY KEY AUTO_INCREMENT ,
  `City` VARCHAR(50),
  `BroadbandCoverage` FLOAT,
  `Providers` INT DEFAULT NULL,
  `Latitude` FLOAT,	
  `Longitude` FLOAT,
  `County` VARCHAR(25),
  `RecordYear` SMALLINT,
  `DateUpdate` DATETIME DEFAULT now()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Data from DBEDT
INSERT INTO `hacc2024`.`broadbcover_by_city`
(`cid`,
`City`,
`BroadbandCoverage`,
`Providers`,
`Latitude`,
`Longitude`,
`County`,
`RecordYear`
)
 VALUES
(1, 'Aiea', 0.944, 13, 21.3858, -157.9333, 'Honolulu', 2023 ),
(2, 'Anahola', 0.962, 12, 22.1476, -159.3133, 'Kauai', 2023 ),
(3, 'Captain Cook', 0.989, 14, 19.4953, -155.9212, 'Hawaii', 2023 ),
(4, 'Eleele', 0.992, 10, 21.9156, -159.5869, 'Kauai', 2023 ),
(5, 'Ewa Beach', 0.867, 13, 21.3156, -158.0072, 'Honolulu', 2023 ),
(6, 'Haiku', 0.978, 12, 20.9247, -156.3103, 'Maui', 2023 ),
(7, 'Hakalau', 0.685, 11, 19.8953, -155.1239, 'Hawaii', 2023 ),
(8, 'Haleiwa', 0.973, 12, 21.5887, -158.1031, 'Honolulu', 2023 ),
(9, 'Hana', 0.955, 9, 20.7556, -155.9844, 'Maui', 2023 ),
(10, 'Hanalei', 0.973, 10, 22.2034, -159.5011, 'Kauai', 2023 ),
(11, 'Hanapepe', 0.957, 11, 21.9126, -159.5908, 'Kauai', 2023 ),
(12, 'Hauula', 0.973, 10, 21.6139, -157.9094, 'Honolulu', 2023 ),
(13, 'Hawi', 0.972, 10, 20.2394, -155.8378, 'Hawaii', 2023 ),
(14, 'Hilo', 0.963, 13, 19.7075, -155.085, 'Hawaii', 2023 ),
(15, 'Holualoa', 0.996, 12, 19.6195, -155.9342, 'Hawaii', 2023 ),
(16, 'Honaunau', 1, 11, 19.4174, -155.904, 'Hawaii', 2023 ),
(17, 'Honokaa', 0.97, 11, 20.0792, -155.4683, 'Hawaii', 2023 ),
(18, 'Honolulu', 0.899, 19, 21.3069, -157.8583, 'Honolulu', 2023 ),
(19, 'Hoolehua', 0.482, 11, 21.1524, -157.0822, 'Molokai', 2023 ),
(20, 'Kaaawa', 0.897, 11, 21.5547, -157.8587, 'Honolulu', 2023 ),
(21, 'Kahuku', 0.802, 12, 21.6802, -157.9538, 'Honolulu', 2023 ),
(22, 'Kahului', 0.991, 12, 20.8895, -156.4743, 'Maui', 2023 ),
(23, 'Kailua', 0.858, 14, 21.4022, -157.7394, 'Honolulu', 2023 ),
(24, 'Kailua Kona', 0.991, 16, 19.6391, -155.9969, 'Hawaii', 2023 ),
(25, 'Kalaheo', 0.993, 10, 21.9225, -159.5258, 'Kauai', 2023 ),
(26, 'Kamuela', 0.95, 15, 20.0205, -155.6691, 'Hawaii', 2023 ),
(27, 'Kaneohe', 0.974, 15, 21.409, -157.7986, 'Honolulu', 2023 ),
(28, 'Kapaa', 0.993, 11, 22.0781, -159.3389, 'Kauai', 2023 ),
(29, 'Kapaau', 0.937, 13, 20.2358, -155.8008, 'Hawaii', 2023 ),
(30, 'Kapolei', 0.941, 13, 21.3359, -158.0608, 'Honolulu', 2023 ),
(31, 'Kaunakakai', 0.959, 12, 21.0956, -157.0222, 'Molokai', 2023 ),
(32, 'Keaau', 0.976, 13, 19.6214, -155.0361, 'Hawaii', 2023 ),
(33, 'Kealakekua', 1, 11, 19.5403, -155.9194, 'Hawaii', 2023 ),
(34, 'Kekaha', 0.953, 12, 21.9697, -159.7161, 'Kauai', 2023 ),
(35, 'Kihei', 0.999, 12, 20.7644, -156.445, 'Maui', 2023 ),
(36, 'Kilauea', 0.976, 11, 22.2138, -159.4033, 'Kauai', 2023 ),
(37, 'Koloa', 0.981, 11, 21.9067, -159.4697, 'Kauai', 2023 ),
(38, 'Kualapuu', 0.981, 9, 21.1589, -157.0269, 'Molokai', 2023 ),
(39, 'Kula', 0.969, 13, 20.7981, -156.3266, 'Maui', 2023 ),
(40, 'Kurtistown', 0.766, 11, 19.5725, -155.0808, 'Hawaii', 2023 ),
(41, 'Lahaina', 0.99, 13, 20.8783, -156.6825, 'Maui', 2023 ),
(42, 'Laie', 0.786, 11, 21.6463, -157.9239, 'Honolulu', 2023 ),
(43, 'Lanai City', 0.953, 9, 20.8278, -156.9217, 'Lanai', 2023 ),
(44, 'Lawai', 1, 10, 21.9181, -159.5114, 'Kauai', 2023 ),
(45, 'Lihue', 0.974, 12, 21.9811, -159.3711, 'Kauai', 2023 ),
(46, 'Makawao', 0.991, 12, 20.8561, -156.3139, 'Maui', 2023 ),
(47, 'Maunaloa', 0.833, 10, 21.1401, -157.2289, 'Molokai', 2023 ),
(48, 'Mililani', 0.957, 13, 21.4513, -158.0158, 'Honolulu', 2023 ),
(49, 'Mountain View', 0.9, 10, 19.5389, -155.125, 'Hawaii', 2023 ),
(50, 'Naalehu', 0.898, 11, 19.0697, -155.5828, 'Hawaii', 2023 ),
(51, 'Ocean View', 0.863, 12, 19.0894, -155.7714, 'Hawaii', 2023 ),
(52, 'Paauilo', 0.688, 10, 20.0431, -155.3747, 'Hawaii', 2023 ),
(53, 'Pahala', 0.961, 10, 19.2028, -155.4797, 'Hawaii', 2023 ),
(54, 'Pahoa', 0.819, 13, 19.4947, -154.945, 'Hawaii', 2023 ),
(55, 'Paia', 0.988, 12, 20.9031, -156.3697, 'Maui', 2023 ),
(56, 'Papaaloa', 0.854, 10, 20.0078, -155.2428, 'Hawaii', 2023 ),
(57, 'Pearl City', 0.888, 14, 21.3972, -157.9753, 'Honolulu', 2023 ),
(58, 'Pepeekeo', 0.941, 12, 19.8322, -155.1042, 'Hawaii', 2023 ),
(59, 'Princeville', 0.976, 11, 22.2235, -159.4852, 'Kauai', 2023 ),
(60, 'Volcano', 0.887, 12, 19.4269, -155.2386, 'Hawaii', 2023 ),
(61, 'Wahiawa', 0.576, 12, 21.5021, -158.0236, 'Honolulu', 2023 ),
(62, 'Waialua', 0.902, 11, 21.5739, -158.1317, 'Honolulu', 2023 ),
(63, 'Waianae', 0.879, 14, 21.4472, -158.1833, 'Honolulu', 2023 ),
(64, 'Waikoloa', 0.996, 12, 19.9256, -155.8828, 'Hawaii', 2023 ),
(65, 'Wailuku', 0.995, 14, 20.8911, -156.5025, 'Maui', 2023 ),
(66, 'Waimanalo', 0.924, 13, 21.3312, -157.7111, 'Honolulu', 2023 ),
(67, 'Waimea', 0.968, 11, 20.0219, -155.6714, 'Hawaii', 2023 ),
(68, 'Waipahu', 0.987, 15, 21.3867, -158.0092, 'Honolulu', 2023 );

-- Table use_pc_internet_by_county
CREATE TABLE `use_pc_internet_by_county` (
  `uid` int NOT NULL PRIMARY KEY AUTO_INCREMENT ,
  `Use_pc_internet` varchar (150),
  `County` varchar (50),
  `Estimate` int DEFAULT NULL,
  `Margin_Error` int DEFAULT NULL,
   `Estimate_Perccent` float,
  `Margin_Error_Percent` float,
  `YearRecord` int DEFAULT NULL,
  `DateUpdate` datetime default now()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `hacc2024`.`use_pc_internet_by_county`
(`uid`,
`Use_pc_internet`,
`County`,
`Estimate`,
`Margin_Error`,
`Estimate_Perccent`,
`Margin_Error_Percent`,
`YearRecord`)
VALUES
(1, 'Total households', 'HawaiiState', 483906, 1934, 483906, 0, 2022 ),
(2, 'With a computer', 'HawaiiState', 457131, 2261, 0.945, 0.2, 2022 ),
(3, 'With a broadband Internet subscription', 'HawaiiState', 434531, 2497, 0.898, 0.3, 2022 ),
(4, 'Total households', 'Hawaii County', 72468, 941, 72468, 0, 2022 ),
(5, 'With a computer', 'Hawaii County', 67249, 963, 0.928, 0.6, 2022 ),
(6, 'With a broadband Internet subscription', 'Hawaii County', 62806, 1083, 0.867, 1, 2022 ),
(7, 'Total households', 'Honolulu County', 333700, 1329, 333700, 0, 2022 ),
(8, 'With a computer', 'Honolulu County', 316525, 1649, 0.949, 0.3, 2022 ),
(9, 'With a broadband Internet subscription', 'Honolulu County', 302597, 1883, 0.907, 0.4, 2022 ),
(10, 'Total households', 'Kalawao County', 32, 20, 32, 0, 2022 ),
(11, 'With a computer', 'Kalawao County', 30, 21, 0.938, 8, 2022 ),
(12, 'With a broadband Internet subscription', 'Kalawao County', 28, 21, 0.875, 12.6, 2022 ),
(13, 'Total households', 'Kauai County', 22978, 512, 22978, 0, 2022 ),
(14, 'With a computer', 'Kauai County', 21706, 535, 0.945, 1.1, 2022 ),
(15, 'With a broadband Internet subscription', 'Kauai County', 21207, 550, 0.923, 1.3, 2022 ),
(16, 'Total households', 'Maui County', 54728, 796, 54728, 0, 2022 ),
(17, 'With a computer', 'Maui County', 51621, 864, 0.943, 0.8, 2022 ),
(18, 'With a broadband Internet subscription', 'Maui County', 47893, 904, 0.875, 1.1, 2022 );

-- Table readiness_by_dimensions
CREATE TABLE `readiness_by_dimensions` (
  `rid` int NOT NULL PRIMARY KEY AUTO_INCREMENT ,
  `Dimension` varchar (100),
  `Details` varchar (250),
  `Unprepared` float,
  `Old_Guard` float,
   `Social_Users` float,
  `Technical` float,
  `Digital` float,
  `YearRecord` int DEFAULT NULL,
  `DateUpdate` datetime default now()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

#--rid	Dimension	Details	Unprepared (17%)	Old Guard 	Social Users (19%)	Technical 	Digital 	YearRecord
#select * from `hacc2024`.`readiness_by_dimensions`
INSERT INTO `hacc2024`.`readiness_by_dimensions`
(`rid`,
`Dimension`,
`Details`,
`Unprepared`,
`Old_Guard`,
`Social_Users`,
`Technical`,
`Digital`,
`YearRecord`)
VALUES
(1, 'Overall', 'OverallPercent', 17, 23, 19, 15, 26, 2022 ),
(2, 'COUNTY', 'Oahu', 58, 67, 66, 78, 78, 2022 ),
(3, 'COUNTY', 'Hawaii County', 21, 16, 10, 10, 11, 2022 ),
(4, 'COUNTY', 'Maui County', 16, 9, 14, 9, 9, 2022 ),
(5, 'COUNTY', 'Kauai County', 5, 7, 10, 2, 2, 2022 ),
(6, 'GENDER', 'Male', 34, 62, 47, 52, 48, 2022 ),
(7, 'GENDER', 'Female ', 34, 62, 47, 52, 52, 2022 ),
(8, 'AGE', '18-34', 13, 21, 55, 61, 42, 2022 ),
(9, 'AGE', '35-54', 48, 41, 31, 29, 36, 2022 ),
(10, 'AGE', '55-65', 39, 37, 14, 10, 22, 2022 ),
(11, 'AGE', 'Average (in years)', 48.3, 47.6, 34.9, 33.5, 39.7, 2022 ),
(12, 'EDUCATION', 'HS Graduate or less', 53, 28, 41, 24, 23, 2022 ),
(13, 'EDUCATION', 'Business/Trade School/Some Col', 27, 53, 34, 49, 42, 2022 ),
(14, 'EDUCATION', 'College Graduate/Post-Graduate', 20, 19, 25, 27, 35, 2022 ),
(15, 'HOUSEHOLD INCOME', 'Less than $50,000', 41, 23, 27, 29, 18, 2022 ),
(16, 'HOUSEHOLD INCOME', '$50,000 but less than $100,000', 41, 46, 53, 26, 30, 2022 ),
(17, 'HOUSEHOLD INCOME', '$100,000 but less than $150,000', 12, 21, 9, 36, 27, 2022 ),
(18, 'HOUSEHOLD INCOME', '$150,000 and over', 6, 10, 11, 10, 25, 2022 ),
(19, 'YEARS IN HAWAII', 'Born in Hawaii', 55, 55, 59, 65, 72, 2022 ),
(20, 'YEARS IN HAWAII', 'Not Born in Hawai‘i (Net)', 45, 45, 41, 35, 28, 2022 ),
(21, 'YEARS IN HAWAII', '1 to 20 years', 11, 24, 26, 24, 13, 2022 ),
(22, 'YEARS IN HAWAII', '20 years or more', 35, 21, 15, 11, 14, 2022 ),
(23, 'ETHNICITY', 'Caucasian', 22, 18, 20, 18, 14, 2022 ),
(24, 'ETHNICITY', 'Japanese', 10, 18, 9, 32, 27, 2022 ),
(25, 'ETHNICITY', 'Hawaiian/part Hawaiian', 23, 29, 20, 28, 25, 2022 ),
(26, 'ETHNICITY', 'Filipino', 16, 5, 9, 10, 8, 2022 ),
(27, 'ETHNICITY', 'Other Asian', 7, 6, 27, 3, 4, 2022 ),
(28, 'ETHNICITY', 'Mixed', 14, 4, 2, 7, 13, 2022 ),
(29, 'ETHNICITY', 'Other', 9, 18, 13, 1, 7, 2022 ),
(30, 'HOUSEHOLD SIZE', '1-2', 45, 41, 23, 42, 37, 2022 ),
(31, 'HOUSEHOLD SIZE', '3-4', 34, 40, 57, 42, 40, 2022 ),
(32, 'HOUSEHOLD SIZE', '5+', 21, 19, 20, 16, 23, 2022 ),
(33, 'HOUSEHOLD SIZE', 'Average', 3.5, 3.2, 3.6, 3.1, 3.3, 2022 );


-- Table `Campaign_Fund`
-- Please note that this is a subset of the 150,000 lines of campaign records
-- due to the limitation of the online testing mysql host, local stage tables were used to extract the result
-- SELECT   CandidateName, sum(Amount) as subTotal FROM dedb.campaign group by CandidateName order by subTotal Desc limit 25;
CREATE TABLE `Campaign_Fund` (
  `cid` int NOT NULL PRIMARY KEY AUTO_INCREMENT ,
  `CandidateName` varchar (250),
  `CampaignTotal` float,
  `YearRecord` int DEFAULT NULL,
  `DateUpdate` datetime default now()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


INSERT INTO `hacc2024`.`Campaign_Fund`
(`cid`,
`CandidateName` ,
`CampaignTotal` ,
`YearRecord`)
VALUES
(1, 'Amemiya, Keith', 1248751, 2020 ),
(2, 'Pine, Kymberly', 759993, 2020 ),
(3, 'Hanabusa, Colleen', 617937, 2020 ),
(4, 'Dela Cruz, Donovan', 556851, 2020 ),
(5, 'Blangiardi, Rick', 512145, 2020 ),
(6, 'Hannemann, Mufi', 473957, 2020 ),
(7, 'Tupola, Andria', 305787, 2020 ),
(8, 'Kouchi, Ron', 235478, 2020 ),
(9, 'Alm, Steve', 224119, 2020 ),
(10, 'Keith-Agaran, Gilbert', 192296, 2020 ),
(11, 'Roth, Mitchell', 175008, 2020 ),
(12, 'Luke, Sylvia', 142260, 2020 ),
(13, 'Wakai, Glenn', 141748, 2020 ),
(14, 'Chang, Stanley', 140355, 2020 ),
(15, 'Kau, Megan', 135358, 2020 ),
(16, 'Akina, William', 113465, 2020 ),
(17, 'Say, Calvin', 98923, 2020 ),
(18, 'Rhoads, Karl', 97527, 2020 ),
(19, 'Texeira, Alan', 93200, 2020 ),
(20, 'Saiki, Scott', 86340, 2020 ),
(21, 'Cordero, Radiant', 85677, 2020 ),
(22, 'DeCoite, Lynn', 80195, 2020 ),
(23, 'Higa, Stacy', 76350, 2020 ),
(24, 'Tsuneyoshi, Earl', 67650, 2020 ),
(25, 'Kitagawa, Lisa', 65010, 2020 );