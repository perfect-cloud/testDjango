--
-- Create model UserBaseInfo
--
-- (no-op)
--
-- Create model DepartInfo
--
CREATE TABLE `app4_departinfo` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `departname` varchar(30) NOT NULL, `createDate` datetime(6) NOT NULL);
--
-- Create model UserExtraInfo
--
CREATE TABLE `app4_userextrainfo` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `username` varchar(30) NOT NULL, `truename` varchar(30) NOT NULL, `sex` integer NOT NULL, `salary` numeric(8, 2) NOT NULL, `age` integer NOT NULL, `department` varchar(20) NOT NULL, `status` varchar(1) NOT NULL, `createDate` datetime(6) NOT NULL, `memo` longtext NULL, `depart_id` integer NOT NULL, `user_id` integer NOT NULL UNIQUE);
--
-- Create model SkillInfo
--
CREATE TABLE `app4_skillinfo` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `skillname` varchar(30) NOT NULL, `createDate` datetime(6) NOT NULL);
CREATE TABLE `user_skill` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `skillinfo_id` integer NOT NULL, `userextrainfo_id` integer NOT NULL);
ALTER TABLE `app4_userextrainfo` ADD CONSTRAINT `app4_userextrainfo_depart_id_14e70e1a_fk_app4_departinfo_id` FOREIGN KEY (`depart_id`) REFERENCES `app4_departinfo` (`id`);
ALTER TABLE `app4_userextrainfo` ADD CONSTRAINT `app4_userextrainfo_user_id_2c1ed931_fk_UserBaseInfo4_id` FOREIGN KEY (`user_id`) REFERENCES `UserBaseInfo4` (`id`);
ALTER TABLE `user_skill` ADD CONSTRAINT `user_skill_skillinfo_id_userextrainfo_id_bb402257_uniq` UNIQUE (`skillinfo_id`, `userextrainfo_id`);
ALTER TABLE `user_skill` ADD CONSTRAINT `user_skill_skillinfo_id_c8628996_fk_app4_skillinfo_id` FOREIGN KEY (`skillinfo_id`) REFERENCES `app4_skillinfo` (`id`);
ALTER TABLE `user_skill` ADD CONSTRAINT `user_skill_userextrainfo_id_c88b7530_fk_app4_userextrainfo_id` FOREIGN KEY (`userextrainfo_id`) REFERENCES `app4_userextrainfo` (`id`);
