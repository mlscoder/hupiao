

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for rent_info
-- ----------------------------
DROP TABLE IF EXISTS `rent_info`;
CREATE TABLE `rent_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `h_id` int(11) NULL DEFAULT NULL COMMENT '租房信息id',
  `url` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '帖子链接',
  `station` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '地铁站点',
  `identity` int(11) NULL DEFAULT NULL COMMENT '身份预测',
  `price` int(10) NULL DEFAULT NULL COMMENT '价格',
  `pay` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '支付方式',
  `rent_type` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '出租方式',
  `only_girl` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '性别限制',
  `count` int(11) NULL DEFAULT NULL COMMENT '发布次数',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2789 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '租房分类信息表' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
