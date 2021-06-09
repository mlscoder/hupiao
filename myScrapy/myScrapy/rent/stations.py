# -- coding: utf-8 --
stations = ['五莲路', '打浦桥', '上海动物园', '马陆', '上海游泳馆', '宝杨路', '宋园路', '莲溪路 ', '市光路', '潘广路', '灵岩南路', '老西门', '中兴路', '丰庄', '淞虹路',
            '华夏东路', '顾戴路', '龙柏新村', '元江路', '共康路', '镇坪路', '友谊路', '衡山路', '野生动物园', '三林', '港城路', '吴中路', '世纪大道', '金沙江路', '塘桥',
            '徐家汇', '新闸路', '上海南站', '伊犁路', '远东大道', '迪士尼', '曲阳路', '上海马戏城', '台儿庄路', '东宝兴路', '真北路', '浦电路', '望园路', '外高桥保税区北站',
            '祁华路',
            '南京西路', '北新泾', '南翔', '常熟路', '复兴岛', '芳甸路', '江湾镇', '曲阜路', '环城东路', '莲花路', '提篮桥', '周浦东', '岚皋路', '赤峰路', '松江体育中心',
            '铁力路', '芳华路',
            '枫桥路', '航津路', '鹤沙航城', '沈梅路', '上海科技馆', '上海体育馆', '安亭', '祁连山南路', '顾唐路', '张江高科', '龙漕路', '通河新村', '巨峰路', '临港大道',
            '高桥',
            '朱梅路', '上海汽车城', '姚虹路', '嫩江路', '民雷路', '杨高南路', '金科路', '金京路', '浦东国际机场', '豫园', '虹桥路', '新场', '张华浜', '佘山', '静安寺',
            '锦绣路',
            '闵行开发区', '中科路', '永德路', '杨思', '周浦', '洲海路', '国际客运中心', '金海路', '虹口足球场', '新江湾城', '中春路', '七宝', '虹莘路', '下南路',
            '东兰路', '水城路',
            '蓝村路', '大木桥路', '航头东', '翔殷路', '花木路', '淞发路', '江月路', '上海大学', '龙华中路', '华夏中路', '源深体育中心', '江浦路', '广兰路', '九亭',
            '七莘路',
            '铜川路', '商城路', '江川路', '北桥', '世博会博物馆', '鞍山新村', '大场镇', '中华艺术宫', '宁国路', '红宝石路', '顾村公园', '华夏西路', '张江路', '金平路',
            '后滩',
            '虹桥2号航站楼', '华宁路', '萧塘', '东昌路', '杨树浦路', '金桥路', '闵瑞路', '大连路', '紫竹高新区', '古浪路', '高桥西', '高科西路', '民生路', '世博大道',
            '大柏树', '光明路', '威宁路', '东川路', '虹桥1号航站楼', '四平路', '殷高东路 ', '富锦路', '曙建路', '祁连山路', '下沙', '金吉路', '大渡河路', '嘉定北',
            '武威路', '临沂新村 ',
            '汉中路', '文井路', '南大路', '南京东路', '彭浦新村', '新天地', '南陈路', '桂林路', '北蔡', '江浦公园', '虹桥火车站', '梅岭北路', '秀沿路', '云山路',
            '南浦大桥',
            '杨高中路', '东靖路', '美兰湖', '三林东', '凌兆新村', '银都路', '浦电路 ', '天潼路', '中潭路', '嘉善路', '临平路', '康桥', '鹤涛路', '锦江乐园', '嘉定西',
            '春申路', '延长路',
            '新村路', '川沙', '华鹏路 ', '陆家浜路', '陆家嘴', '桂林公园', '景西路', '学林路 ', '刘行', '马当路', '江湾体育场', '剑川路', '合川路', '外环路', '花桥',
            '长寿路', '大世界',
            '御桥', '上海体育场', '昌吉东路', '徐泾东', '漕溪路', '汶水路', '武宁路', '漕宝路', '曹杨路', '成山路', '康新公路', '兆丰路', '虹漕路', '五洲大道', '李子园',
            '漕河泾开发区', '中山北路', '江苏路', '外高桥保税区南站', '呼兰路', '上海西站', '邮电新村', '石龙路', '松江大学城', '江杨北路', '西渡', '殷高西路', '真如',
            '大华三路',
            '延吉中路', '世纪公园', '友谊西路', '宝山路', '书院', '莘庄', '国权路', '唐镇', '沈杜公路', '上南路', '云锦路', '东城一路', '龙耀路', '淮海中路', '繁荣路',
            '人民广场', '申江路',
            '同济大学', '博兴路', '紫藤路', '凌空路', '东明路', '交通大学', '锦秋路', '长风公园', '奉浦大道', '西藏北路', '上大路', '江宁路', '淞滨路', '三门路',
            '航中路',
            '上海火车站', '醉白池', '罗南新村', '上海儿童医学中心', '奉贤新城', '黄陂南路', '龙华', '虹梅南路', '东方体育中心', '浦三路', '星中路', '中山公园', '白银路',
            '延安西路', '小南门',
            '北洋泾路', '洞泾', '上海赛车场', '浦航路', '惠南东', '隆德路', '云台路', '创新中路', '杨高北路', '宝安公路', '金桥', '东安路', '隆昌路', '场中路', '昌平路',
            '虹梅路', '双柏路',
            '华泾西', '上海图书馆', '华东理工大学', '武威东路', '浦东大道', '龙阳路', '肇嘉浜路', '浦江镇', '陈春路 ', '金运路', '黄兴路', '娄山关路', '蓝天路', '长清路',
            '罗山路',
            '惠南', '嘉定新城', '耀华路', '罗秀路', '汇臻路', '海伦路', '金沙江西路', '西藏南路', '陕西南路', '五角场', '龙溪路', '颛桥', '泗泾', '国帆路', '芦恒路',
            '自然博物馆', '东陆路', '航头', '共富新村', '金海湖', '陈翔公路', '松江南站', '桃浦新村', '基隆路', '三鲁公路', '爱国路', '滴水湖', '行知路', '双江路',
            '曹路', '鲁班路', '四川北路',
            '宜山路', '海天三路', '松江新城', '丰翔路', '高青路', '祁安路', '德平路', '联航路', '长江南路', '水产路', '黄兴公园']

business_station = ['南京东路', '南京西路', '人民广场', '新天地', '静安寺', '世纪大道', '打浦桥', '陕西南路', '豫园', '徐家汇']

beijing_station = ['军事博物馆', '褡裢坡', '旧宫', '车公庄西', '双桥', '惠新西街南口', '育新', '亮马桥', '六道口', '东管头南', '天坛东门', '天通苑', '良乡大学城北',
                   '奥体中心', '和平门', '昌平东关', '青年路', '珠市口', '七里庄', '白盆窑', '清华东路西口', '北海北', '建国门', '育知路', '百子湾', '双井', '十里河',
                   '立水桥南', '达官营', '巴沟', '虎坊桥', '天桥', '草桥', '北苑', '泥洼', '西钓鱼台', '石门', '大钟寺', '常营', '北沙滩', '苏州街', '小红门',
                   '亦庄桥', '什刹海', '古城', '六里桥', '安立路', '中国美术馆', '焦化厂', '3号航站楼', '东高地', '广阳城', '草房', '通州北关', '西土城', '大望路',
                   '后沙峪', '三元桥', '张自忠路', '分钟寺', '西局', '巩华城', '东夏园', '梨园', '南邵', '南锣鼓巷', '柳芳', '北京西站', '劲松', '南礼士路',
                   '双合', '团结湖', '望京东', '回龙观东大街', '北运河东', '关庄', '阜成门', '经海路', '四惠东', '农业展览馆', '王府井', '崇文门', '南法信', '宣武门',
                   '湾子', '灯市口', '永定门外', '2号航站楼', '海户屯', '管庄', '磁器口', '八里桥', '北京站', '欢乐谷景区', '角门西', '平西府', '天安门东',
                   '丰台东大街', '长椿街', '复兴门', '万源街', '黄渠', '花园桥', '安德里北街', '莲花桥', '丰台科技园', '朱辛庄', '角门东', '成寿寺', '潞城', '木樨园',
                   '五道口', '垡头', '大屯路东', '芍药居', '西直门', '北苑路北', '桥湾', '良乡南关', '西二旗', '西单', '宋家庄', '安贞门', '九龙山', '知春里',
                   '金台夕照', '六里桥东', '肖村', '崔各庄', '传媒大学', '亦庄火车站', '郭公庄', '和平西桥', '瀛海', '光熙门', '俸伯', '马泉营', '荣京东街', '和义',
                   '西黄村', '白石桥南', '玉泉路', '北邵洼', '菜市口', '广渠门外', '金安桥', '知春路', '石榴庄', '果园', '八角游乐园', '立水桥', '廖公庄', '长阳',
                   '丰台南路', '稻田', '丰台站', '科怡路', '苏庄', '田村', '长春桥', '阎村东', '十里堡', '国贸', '木樨地', '健德门', '西小口', '火器营', '德茂',
                   '五棵松', '车道沟', '朝阳门', '东直门', '鼓楼大街', '通州北苑', '五福堂', '天安门西', '荣昌东街', '永泰庄', '林萃桥', '海淀五路居', '车公庄',
                   '森林公园南门', '良乡大学城西', '花乡东桥', '奥林匹克公园', '次渠', '安定门', '刘家窑', '金台路', '孙河', '大红门南', '昌平西山口', '上地', '昌平',
                   '杨庄', '土桥', '化工', '呼家楼', '和平里北街', '临河里', '次渠南', '万寿路', '北土城', '回龙观', '大葆台', '篱笆房', '蒲黄榆', '纪家庙',
                   '海淀黄庄', '大郊亭', '白堆子', '国展', '大红门', '广渠门内', '亦庄文化园', '望京', '东单', '龙泽', '永安里', '北运河西', '十三陵景区', '高碑店',
                   '慈寿寺', '花梨坎', '首经贸', '九棵树', '雍和宫', '南楼梓庄', '平安里', '天通苑南', '东大桥', '苹果园', '广安门内', '沙河', '火箭万源', '郝家府',
                   '物资学院路', '霍营', '顺义', '生命科学园', '望京西', '国家图书馆', '安华桥', '沙河高教园', '同济南路', '良乡大学城', '前门', '东四十条', '潘家园',
                   '东四', '八宝山', '太阳宫', '四惠', '天通苑北', '公主坟', '北新桥', '惠新西街北口']

beijing_station_business = ['天安门东', '天安门西', '王府井', '西直门', '中关村', '望京西', ]

guangzhou_station = ['海心沙', '神岗', '小北', '竹料', '飞沙角', '猎德', '聚龙', '梅花园', '澜石', '芳村', '华林寺', '亭岗', '东风', '猎德大桥南',
                     '滘心', '广州塔', '暹岗', '小坪', '长湴', '凤岗', '琶洲', '中新', '花城大道', '桂城', '沙园', '新城东', '广州塔',
                     '凤凰新村', '山田', '马鞍山公园', '上步', '团一大广场', '会展东', '黄花岗', '东山口', '科学城', '公园前', '石壁', '沙河顶',
                     '棠东', '赤草', '番禺广场', '菊树', '黄埔大道', '南海神庙', '车陂南', '车陂', '体育西路', '庆盛', '从化客运站', '大观南路',
                     '南岗', '花城路', '长平', '科韵路', '赤岗', '沙河', '妇儿中心', '清塘', '员村', '东涌', '太和', '东平', '广州南站', '金坑',
                     '中大', '嘉禾望岗', '新造', '官桥', '客村', '金融高新区', '新南', '南桂路', '珠江新城', '世纪莲', '沙贝', '京溪南方医院', '香雪',
                     '广州东站', '机场北', '新沙', '朱村', '白云公园', '晓港', '滘口', '新港东', '魁奇路', '五羊邨', '飞鹅岭', '鹅掌坦',
                     '苏元', '官洲', '厦滘', '植物园', '高塘石', '金峰', '江泰路', '西村', '万胜围', '华师', '大学城北', '千灯湖', '石牌桥',
                     '钟村', '黄村', '神舟路', '三元里', '杨箕', '机场南', '石潭', '人和', '广州塔东', '石溪', '萧岗', '镇龙西',
                     '花都广场', '马沥', '海珠广场', '裕丰围', '镇龙', '谢村', '西门口', '同德', '高增', '南村万博', '琶洲塔', '水西', '燕岗',
                     '钟岗', '汉溪长隆', '虫雷岗', '夏园', '岗顶', '一德路', '普君北路', '白云大道北', '天平架', '飞翔公园', '会展中', '黄沙',
                     '知识城', '季华园', '沙村', '黄边', '祖庙', '东湖', '大沙东', '江夏', '东圃', '镇龙北', '双岗', '北京路', '大剧院', '琶醍',
                     '横沙', '员岗', '市桥', '五山', '潭村', '鹭江', '广州火车站', '体育中心南', '琶洲大桥南', '三溪', '夏良', '文化公园', '鹤洞',
                     '何棠下', '南洲', '清㘵', '红卫', '西场', '低涌', '林和西', '同济路', '大学城南', '广州北站', '蕉门', '会展西', '黄阁',
                     '花果山公园', '龙溪', '塘坑', '钟落潭', '永泰', '西塱', '旺村', '天河智慧城', '花都汽车城', '增城广场', '万胜围', '大石',
                     '大沙地', '同和', '枫下', '太平', '朝安', '宝岗大道', '南浦', '汤村', '龙归', '燕塘', '南风', '陈家祠', '萝岗', '坑贝',
                     '中山八', '白云东平', '南横', '会江', '沙涌', '文冲', '大涌', '天河公园', '黄陂', '天河南', '南沙客运港', '磨碟沙', '越秀公园',
                     '东晓南', '河沙', '广隆', '纪念堂', '长寿路', '洛溪', '板桥', '石碁', '金洲', '大塘', '白云文化广场', '市二宫', '昌岗',
                     '黄阁汽车城', '坑口', '淘金', '石井', '如意坊', '浔峰岗', '烈士陵园', '柯木塱', '海傍', '动物园', '新和', '体育中心', '同福西',
                     '花地湾', '新塘', '坦尾', '龙洞', '白江', '官湖', '江南西', '沥滘', '天河客运站', '农讲所', '鱼珠', '区庄', '莲塘']

guangzhou_station_business = ['机场北', '嘉禾望岗', '珠江新城', '岗顶', '石牌桥', '天河南', '体育西路', '广州南站 ']

shenzhen_station = ['市民中心', '太子湾', '田贝', '禾花', '臣田北', '公明广场', '松岗', '华侨城', '华新', '科苑', '留仙洞', '会展北', '新秀', '深康', '大剧院',
                    '红树湾', '车公庙', '双拥街', '宝安中学', '龙城西', '水贝', '孖岭', '罗湖', '光明', '长圳', '官田', '向西村', '黄田', '坂田北', '宝安中心',
                    '沙头角', '粤海门', '侨香', '西丽湖', '东角头', '深大南', '安托山', '益田', '薯田埔', '华南城', '前湾', '横塘', '天健花园', '前海湾',
                    '龙城广场', '仙湖路', '洪浪北', '农林', '侨城北', '机场', '通新岭', '莲花北', '光雅园', '文锦', '茶光', '笋岗', '坪洲', '茜坑', '福民',
                    '深圳北站', '会展南', '固戍', '长岭陂', '梅林关', '大运北', '布心', '元芬', '梧桐山南', '桃源居', '下梅林', '石厦', '莲花西', '凤凰城',
                    '横岗', '洲石路', '四海', '阳台山东', '后海', '宝安', '新安', '桃园', '竹子林', '上芬', '赤尾', '深大', '田头', '晒布', '观澜', '机场东',
                    '湖贝', '蛇口港', '海山', '皇岗村', '深湾', '桃源村', '坪山中学', '爱联', '大芬', '梦海', '铁路公园', '购物公园', '坪山围', '西丽',
                    '会展中心', '香蜜', '莲塘口岸', '红岭', '松岗公园', '福田口岸', '南坑', '新屋', '清湖北', '后亭', '华强南', '平湖', '景田', '民治', '沙井',
                    '西乡', '高新园', '大运', '桥头', '水湾', '皇岗口岸', '左炮台', '双龙', '坂田', '南联', '塘朗', '南油西', '文化中心', '上沙',
                    '流塘宝安客运中心', '银湖', '中山公园', '红花山', '杨美', '太安', '翠岗工业园', '兴东', '江岭', '红树湾南', '香梅北', '工业六路', '机场北',
                    '数码城', '上梅林', '南山', '马安山', '香蜜湖', '白石洲', '上李朗', '溪头', '福永', '东纵', '南山书城', '黄贝岭', '翻身', '老街', '红山',
                    '雅宝', '丹竹头', '六联村', '塘尾', '创业路', '上屋', '回龙埔', '龙平', '五和', '下沙', '布吉', '上川', '六约', '冬瓜岭', '海上田园东',
                    '龙东村', '华为', '福保', '永湖', '鲤鱼门', '翠竹', '海月', '白石龙', '人民南', '高新南', '灵芝', '临海', '木古', '福田', '盐田路',
                    '宝华', '深外高中', '民乐', '龙南', '同富', '南油', '燕南', '梅村', '合水口', '世界之窗', '红岭南', '南头古城', '荷坳', '科学公园', '长龙',
                    '怀德', '龙城中路', '观澜湖', '赤湾', '桂湾', '长湖', '八卦岭', '贝尔路', '龙岗汽车站', '红岭北', '臣田南', '后瑞', '下水径', '和平', '吉祥',
                    '坪山', '楼村', '上塘', '大学城', '莲花村', '光明大街', '科学馆', '华强北', '梅景', '凉帽山', '塘坑', '莲塘', '侨城东', '百鸽笼', '沙尾',
                    '碧海湾', '龙华', '上水径', '大新', '登良', '怡景', '竹村', '黄木岗', '科技馆', '岗头', '甘坑', '海上世界', '湾厦', '国贸', '松元厦',
                    '龙井', '深云', '木棉湾', '体育中心', '少年宫', '碧头', '岗厦', '盐田港西', '洪湖', '草埔', '珠光', '田心', '香梅', '龙胜', '牛湖',
                    '翰岭', '泥岗', '深圳湾公园', '雪象', '宝体', '怡海', '清湖', '岗厦北', '鹿丹村', '前湾公园', '妈湾', '荔湾', '园岭', '凯成二路', '荔林',
                    '华强路', '同乐村', '同乐']

shenzhen_station_business = ['购物公园']

hangzhou_station = ['人民广场', '滨康路', '潘水', '九堡', '景芳', '良睦路', '湘湖', '高沙路', '江东二路', '诚业路', '新塘', '浙大紫金港', '育才北路', '凤起路',
                    '近江', '港城大道', '下沙江滨', '建设一路', '市民中心', '永福', '萍水街', '金家渡', '南峰', '墩祥街', '闸弄口', '浦沿', '金沙湖', '杭发厂',
                    '临平', '霞鸣街', '蒋村', '明星路', '钱江路', '江锦路', '西湖文化广场', '文泽路', '新街', '人民路', '中泰', '曹家桥', '中河路', '新风',
                    '金星', '南星桥', '音乐学院', '南阳', '保俶路', '中医药大学', '虾龙圩', '新港', '虎啸杏', '下宁桥', '婺江路', '西兴', '建业路', '飞虹路',
                    '钱江世纪城', '南湖', '姑娘桥', '高桥', '振宁路', '江陵路', '农林大学', '双桥', '博奥路', '长河', '星民', '火车东站', '江汉路', '龙翔桥',
                    '南苑', '禹航路', '九和路', '武林广场', '科海路', '凤新路', '新兴路', '云水', '朝阳', '建国路', '伟业路', '杨家墩', '公望街', '城站',
                    '余杭高铁站', '中村', '庆菱路', '绿汀路', '火车南站', '盈中', '向阳路', '武林门', '双浦', '定安路', '复兴路', '五常', '银湖', '兴议', '善贤',
                    '彭埠', '乔司南', '野生动物园东', '青六中路', '三坝', '受降', '新镇路', '博览中心', '文新', '青山湖', '义蓬', '打铁关', '良渚', '水澄桥',
                    '翁梅', '建国北路', '西浦路', '九州街', '青山湖科技城', '学院路', '客运中心', '滨和路', '通惠中路', '启成路', '候潮门', '枫桦西路', '塘新线',
                    '坎山', '新汉路', '城星路', '葛巷', '七堡', '创景路', '萧山国际机场', '文海南路', '丰潭路', '杭氧', '西文街', '奥体中心', '八百里', '金鸡路',
                    '甬江路', '盈丰路', '三墩', '沈塘桥', '杭师大仓前', '白洋', '临安广场', '乔司', '桂花西路', '文三路', '杜甫村', '富阳客运中心', '大运河',
                    '下沙西', '江城路', '江晖路', '联庄', '新桥', '拱宸桥东', '古翠路', '聚才路', '香积寺路', '和睦', '永盛路', '庆春广场', '万安桥', '建设三路',
                    '合欢路', '美院象山', '杭州大会展中心', '中河北路']

hangzhou_station_business = ['武林广场', '人民广场', '武林门']

nanjing_station = ['天印大道', '仙林中心', '南庆', '东大成贤学院', '卸甲甸', '百家湖', '红河路', '灵山', '栖霞', '石碛河', '林山', '光华门', '中保', '吴侯街',
                   '云锦路', '泉都大街', '梦都大街', '中山湖', '大校场', '万安', '板桥', '集庆门大街', '西岗桦墅', '临江.青奥体育公园', '生态科技园', '西安门',
                   '营苑南路', '秣陵', '清水亭', '华阳', '苜蓿园', '大明路', '文德路', '句容', '文靖路', '富贵山', '虹桥', '农贸中心', '溧水', '禄口机场',
                   '天隆寺', '小市', '江心洲', '大校场路', '铜山', '红山动物园', '三山街', '蒋王庙', '崇明', '大厂', '古泉', '兴隆大街', '金桥市场', '云南路',
                   '白象', '龙潭', '上海路', '羊山公园', '莫愁湖', '春江路', '侯家塘', '浮桥', '珠江路', '石湫', '南京林业大学·新庄', '吉印大道', '常府街', '南京站',
                   '龙华路', '幸庄', '康安里', '南京南站', '管子桥', '恒河路', '黄里', '万安路', '空港新城江宁', '黄河路', '雨润大街', '南京猿人洞', '大行宫',
                   '清凉山', '汤山', '成山路', '竹山路', '沈桥', '保税物流中心', '油坊桥', '桥林新城', '聚宝山', '化工园', '新港开发区', '孟北', '兴梅路', '奥体东',
                   '白下科技园', '佛城西路', '元通', '龙池', '迈皋桥', '中胜', '双龙大道', '兰花塘', '星火路', '万寿村', '玉带', '汤泉', '花神庙', '大里墅',
                   '柘塘', '南医大·江苏经贸学院', '仙鹤门', '胜利村', '上峰', '学则路', '信息工程大学', '将军路', '杨家圩', '永初路', '金牛湖', '孝陵卫', '宏运大道',
                   '正德学院', '湾营路', '金马路', '上元门', '仙新路', '上坊', '麒麟镇', '东郊小镇', '群力', '仙林湖', '岔路口', '贾西', '静淮街', '景明佳园',
                   '南京工业大学', '经天路', '翔凤路', '杨庄', '天润城', '明故宫', '武定门', '平良大街', '江宁', '清河路', '黄梅', '雄州', '方州广场', '山西路',
                   '金箔路', '安德门', '六合开发区', '凤台南路', '南京交院', '卡子门', '凤凰山公园', '东大九龙湖校区', '汉中门大街', '定淮门', '西善桥', '沧波门', '鼓楼',
                   '小龙湾', '夫子庙', '天元西路', '奥体中心', '雨山路', '马骡圩', '高庙路', '葛塘', '翔宇路南', '小天堂', '新生圩', '板桥北', '盐仓桥', '滨江村',
                   '团结圩', '汉中门', '五塘广场', '长芦', '高淳', '南大仙林校区', '机场路', '泰冯路', '胜太路', '城北路', '秣周东路', '王家湾', '林东', '运河路',
                   '上元大街', '天保', '雨花门', '明觉', '九华山', '建宁路', '大桥南路', '马标', '玄武门', '铁心桥', '大里村', '定林', '浦口万汇城', '双垅',
                   '铜井', '陈家庄', '中国药科大学', '林场', '双拜岗', '城河村', '八百桥', '鸡鸣寺', '河定桥', '龙眠大道', '翔宇路北', '苏宁总部·徐庄', '大中桥',
                   '七桥瓮', '桥林', '嫩江路', '麒麟工业园', '长巷', '童世界', '胜太西路', '麒麟门', '正方中路', '雄州东路', '省经干院', '六合机场', '朝天宫',
                   '岗子村', '春江新城', '广州路', '小行', '明发广场', '绿博园', '空港新城溧水', '下关', '南艺·二师·草场门', '月牙湖', '宝华', '新模范马路', '新街口',
                   '马群', '泰山新村', '长途东站', '仙林', '汇通路', '刘村', '高家冲', '方家营', '禄口新城', '上坊工业园', '建南', '软件大道', '东流', '卧龙湖',
                   '新亭路', '板桥南', '九龙湖', '芝嘉路', '柳洲东路', '后标营', '曹后村', '科宁路', '高新开发区', '雄州西路', '无想山', '翠屏山', '河海大学佛城西路',
                   '龙江', '诚信大道', '钟灵街', '鼓楼科技园', '福建路', '五台山', '下马坊', '乐山路', '张府园', '灵岩山', '仙林东', '夹岗', '中华门', '铁心桥大街',
                   '百水桥']
nanjing_station_business = ['夫子庙', '新街口']

chengdu_station = ['郫筒', '黄石', '玉双路', '天府三街', '晨光', '东郊记忆', '杭州路', '马超西路', '凤溪河', '蜀新大道', '幸福桥', '茶店子', '西博城', '广福',
                   '观东', '郫县西站', '国宁', '升仙湖', '华府大道', '杨柳河', '花照壁', '兴业北街', '高升桥', '双桥路', '迎春桥', '蔡桥', '钓鱼嘴', '五根松',
                   '金科北路', '植物园', '茶店子客运站', '天河路', '大丰', '万年路', '理工大学', '新南门', '大源', '民乐', '庆安', '龙泉驿', '康强四路', '省骨科医院',
                   '陆肖', '华兴', '九兴大道', '双流机场1航站楼', '簇桥', '犀浦', '双流西', '天源路', '成都西站', '石羊', '四河', '红星桥', '应天寺',
                   '塔子山公园', '望丛祠', '牛市口', '西南交大', '新业路', '成都行政学院', '十里店', '莲花', '金星', '洞子口', '二江寺', '红旗大道', '大田', '来龙',
                   '文殊院', '石犀公园', '文化宫', '文星', '桐梓林', '蒲草塘', '军区总医院', '羊犀立交', '钟楼', '红牌楼', '高新', '建设北路', '九里堤', '双林村',
                   '新川路', '万年场', '明蜀王陵', '百草路', '川大望江校区', '人民北路', '抚琴', '芳草街', '迎宾大道', '锦城学院', '迎晖路', '松林', '天府广场',
                   '世纪城', '檬梓', '省体育馆', '沙湾', '西河', '天宇路', '孵化园', '新鸿路', '青羊宫', '尚锦路', '蜀新大道', '金周路', '永丰', '龙爪堰',
                   '金融城', '西华大学', '福宁路', '狮子山', '锦城大道', '兴隆湖', '草堂北路', '青岛路', '金府', '警官学院', '大禹东路', '新通大道', '太升南路',
                   '心岛', '明光', '红高路', '侯家桥', '龙吟', '倪家桥', '市二医院', '合信路', '西北桥', '光华公园', '殷家林', '锦城湖', '团结新区', '安泰二路',
                   '三官堂', '龙灯山', '天河路', '兴隆', '市一医院', '武汉路', '廖家湾', '新津', '机投桥', '动物园', '双店路', '市五医院', '中医大省医院',
                   '锦城广场', '回龙', '双流机场2航站楼', '火车南站', '西南财大', '杉板桥', '望丛祠', '花源', '涌泉', '衣冠庙', '崔家店', '仁和', '梓潼宫',
                   '骡马市', '神仙树', '龙马路', '春熙路', '麓湖', '槐树店', '合作路', '德富大道', '东升', '磨子桥', '天府五街', '广州路', '太平园', '泉水路',
                   '犀安路', '两河路', '武侯大道', '顺江路', '马厂坝', '兴盛', '沈阳路', '柏水场', '熊猫大道', '天映路', '金华寺东路', '华阳', '川藏立交', '天欣路',
                   '东湖公园', '昌公堰', '九江北', '昭觉寺南路', '科园', '琉璃场', '土龙路', '花石', '净居寺', '新达路', '西南交大犀浦', '三里坝', '星河', '双流广场',
                   '安埠', '南熏大道', '技师学院', '杜家碾', '三岔', '锦江宾馆', '五津', '大面铺', '八里庄', '龙平路', '万盛', '东大路', '花牌坊', '天府机场北',
                   '成都大学', '一品天下', '成都医学院', '成都东客站', '通惠门', '科学城', '牛王庙', '凤凰大街', '武侯立交', '韦家碾', '清淳', '天府商务区', '府青路',
                   '清江西路', '骑龙', '人民公园', '电子科大', '麓山大道', '九道堰', '北部商贸城', '前锋路', '何公路', '金土', '青杠', '皇花园', '惠王陵', '火车北站',
                   '大观', '白果林', '秦皇寺', '西华大道', '宽窄巷子', '海昌路', '航都大街', '簇锦', '李家沱', '二仙桥', '华桂路', '梁家巷', '赛云台', '兰家沟',
                   '川大江安校区', '高朋大道', '金沙博物馆', '双凤桥', '琉三路', '连山坡', '广都', '东光', '三瓦窑', '安泰五路', '北站西二路', '太平寺', '刘家碾',
                   '红石公园', '石油大学', '石羊立交', '芦角', '五块石', '金融城东', '珠江路', '黄田坝', '培风', '蜀汉路东', '顺风', '温泉大道', '锦水河', '白佛桥',
                   '万安', '金花', '书房', '非遗博览园', '东坡路', '东门大桥', '百叶路', '和平街', '华西坝', '南湖立交', '龙桥路', '中坝', '金石路', '天府公园',
                   '驷马桥', '张家寺', '梨园路', '十陵', '花桥', '黄水', '联工', '交子大道', '四川师大', '界牌', '锦城广场东', '陆家桥', '成渝立交', '红展东路',
                   '儒林路', '洪河', '新平', '成都西站', '三河场', '武青南路', '怡心湖', '三元', '中和']

chengdu_station_business = ['人民公园', '成都西站', '金融城']

wuhan_station = ['三阳路', '五环大道', '武汉东站', '新荣', '六渡桥', '北华街', '幸福湾', '钟家村', '柏林', '广埠屯', '百步亭花园路', '塔子湖', '常青城', '珞雄路',
                 '水果湖', '高车', '长港路', '朱家河', '洪山路', '杨家湾', '云飞路', '建安街', '新路村', '东风公司', '小东门', '沌阳大道', '武湖', '崇仁路',
                 '光谷广场', '徐家棚', '汉口北', '黄龙山路', '双墩', '仁和路', '古田四路', '阳逻', '孟家铺', '谭鑫培公园', '宗关', '秀湖', '徐家棚',
                 '天河机场', '金融港北', '市民之家', '古田三路', '光谷大道', '头道街', '友谊路', '滕子岗', '东吴大道', '三眼桥', '前进村', '江城大道', '湖工大',
                 '佛祖岭', '汉正街', '金台', '金银湖', '汉西一路', '兴业路', '工业四路', '新农', '舵落口', '建港', '中南路', '江夏客厅', '汪家墩', '阳逻开发区',
                 '七里庙', '小洪山', '首义路', '蔡甸广场', '园林路', '二七小路', '板桥', '金银潭', '永安堂', '梅苑小区', '凤凰路', '军运村', '中山公园', '宋家岗',
                 '华中科技大学', '径河', '复兴路', '长岭山', '新天', '金潭路', '国博中心南', '园博园', '中一路', '武昌火车站', '青鱼嘴', '轻工大学', '武泰闸', '堤角',
                 '园博园北', '三店', '武汉火车站', '玉龙路', '汉阳客运站', '藏龙东街', '青龙', '临嶂大道', '江汉路', '三角湖', '苗栗路', '罗家港', '武汉商务区',
                 '龙阳村', '马房山', '老关村', '中南医院', '沙口', '武胜路', '光谷生物园', '琴台', '滠口新城', '太平洋', '马湖', '唐家墩', '罗家庄', '宝通寺',
                 '未来三路', '青年路', '徐州新村', '楚河汉街', '纸坊大街', '车城东路', '航空总部', '二七路', '光谷六路', '黄金口', '积玉桥', '宏图大道', '马鹦路',
                 '后湖大道', '知音', '杨春湖', '徐东', '铁机路', '洪山广场', '施岗', '梨园', '利济北路', '国博中心北', '大智路', '佳园路', '汉口火车站', '石桥',
                 '瑞安街', '杨汊湖', '码头潭公园', '取水楼', '武生院', '古田一路', '王家墩东', '常码头', '王家湾', '硚口路', '黄浦路', '小龟山', '黄家湖地铁小镇',
                 '丹水池', '赵家条', '野芷湖', '竹叶山', '东亭', '湖北大学', '新河街', '岳家嘴', '螃蟹岬', '古田二路', '文治街', '光谷五路', '红钢城', '盘龙城',
                 '体育中心', '拦江路', '十里铺', '五里墩', '省农科院', '集贤', '汉阳火车站', '新荣客运站', '菱角湖', '惠济二路', '陶家岭', '巨龙大道', '虎泉', '豹澥',
                 '竹叶海', '常青花园', '金银湖公园', '省博湖北日报', '左岭', '光谷七路', '未来一路', '光谷四路', '光谷同济医院', '四新大道', '葛店南', '湖口', '大花岭',
                 '范湖', '街道口', '新庙村', '循礼门', '文昌路', '谌家矶', '军民村', '青龙山地铁小镇', '额头湾', '香港路']

wuhan_station_business = ['汉阳客运站', '武汉商务区']

chongqing_station = ['华岩中心', '唐家院子', '动步公园', '黄花园', '中央公园西', '杨家坪', '石桥铺', '大坪', '国博中心', '高堡湖', '礼嘉', '鹅岭',
                     '白居寺', '巴山', '嘉州路', '王家庄', '翠云', '上新街', '鲤鱼池', '石新路', '建桥', '大学城', '六公里', '大剧院', '黄泥塝',
                     '丹鹤', '新山村', '金渝', '大江', '两路口', '冉家坝', '五里店', '金家湾', '状元碑', '陈家桥', '人和', '刘家坝', '洪湖东路',
                     '袁家岗', '工贸', '学堂湾', '跳磴', '较场口', '中央公园', '狮子坪', '马家岩', '动物园', '天星桥', '重庆北站北广场', '华龙',
                     '石油路', '郑家院子', '鸳鸯', '铜元局', '长生桥', '大堰村', '华岩寺', '凤鸣山', '陈家坪', '小什字', '头塘', '唐家沱', '南桥寺',
                     '中梁山', '金山寺', '刘家坪', '沙河坝', '九曲河', '黄茅坪', '寸滩', '双龙', '海棠溪', '和睦路', '体育公园', '牛角沱', '赖家桥',
                     '江北机场T2航站楼', '湖霞街', '茶园', '民心佳园', '观音桥', '环山公园', '清溪河', '彩云湖', '龙头寺公园', '石井坡', '大渡口',
                     '园博园', '佛图关', '上湾路', '小龙坎', '重庆大学', '金竹', '红旗河沟', '奥体中心', '半山', '红土地', '五公里', '重光', '微电园',
                     '华成路', '康庄', '鱼胡路', '杨公桥', '平安', '大溪沟', '九公里', '太平冲', '渝鲁', '保税港', '大山村', '长河', '蔡家',
                     '幸福广场', '罗家坝', '复兴', '上桥', '二塘', '江北机场T3航站楼', '长福路', '沙坪坝', '中央公园东', '马王场', '金建路', '欢乐谷',
                     '龙头寺', '花卉园', '海峡路', '烈士墓', '碧津', '李子坝', '曹家湾', '玉带山', '龙凤溪', '尖顶坡', '鱼洞', '弹子石', '天堂堡',
                     '歇台子', '高庙村', '重庆北站南广场', '光电园', '金童路', '观月路', '重庆西站', '花溪', '民安大道', '思源', '四公里', '华新街',
                     '南湖', '大石坝', '空港广场', '悦来', '仁济', '鹿山', '璧山', '七星岗', '曾家岩', '谢家湾', '红岩坪', '渝北广场', '磁器口',
                     '上浩', '黑石子', '南坪', '天生', '江北城', '双碑', '麒龙', '举人坝', '北碚', '大龙山', '大竹林', '双凤桥', '莲花', '回兴',
                     '涂山', '朝天门', '凤西路', '园博中心', '童家院子', '八公里', '邱家湾', '高义口', '重庆图书馆', '三亚湾', '向家岗', '刘家院子',
                     '二郎', '岔路口', '临江门']

chongqing_station_business = ['较场口', '李子坝', '中央公园']


# 动态获取城市地铁站
def getCityStations(city):
    # 地铁映射
    cityDict = {
        "sh": stations,
        "sh_b": business_station,
        "bj": beijing_station,
        "bj_b": beijing_station_business,
        "gz": guangzhou_station,
        "gz_b": guangzhou_station_business,
        "sz": shenzhen_station,
        "sz_b": shenzhen_station_business,
        "hz": hangzhou_station,
        "hz_b": hangzhou_station_business,
        "nj": nanjing_station,
        "nj_b": nanjing_station_business,
        "cd": chengdu_station,
        "cd_b": chengdu_station_business,
        "wh": wuhan_station,
        "wh_b": wuhan_station_business,
        "cq": chongqing_station,
        "cq_b": chongqing_station_business
    }
    return cityDict.get(city, stations)
