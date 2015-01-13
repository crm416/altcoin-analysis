"""
    Market capitalization data as of January 9, 2015.
"""

_coins = ['BTC', 'XRP', 'LTC', 'XPY', 'BTS', 'STR', 'NXT', 'DOGE', 'PPC', 'DRK', 'XCP', 'NMC', 'NSR', 'FC2', 'BANX', 'YBC', 'XMR', 'NBT', 'BLK', 'BCN', 'MSC', 'BTCD', 'ETC', 'QRK', 'MTC', 'NOTE', 'FTC', 'RDD', 'XTC', 'CLAM', 'XPM', 'WDC', 'IXC', 'VIA', 'NVC', 'MEC', 'UNO', 'XDN', 'PTS', 'SDC', 'MONA', 'IFC', 'SYS', 'POT', 'XC', 'BILS', 'URO', 'GRC', 'VRC', 'PND', 'ANC', 'ZET', 'UTC', 'NLG', 'CURE', 'I0C', 'BURST', 'CANN', 'EMC', 'QORA', 'APC', 'MAX', 'NOO', 'ARCH', 'SPR', 'DGC', 'SLR', 'BAY', 'CZC', 'HYPER', 'VTC', 'XST', 'SWIFT', 'NODE', 'XCR', 'FIMK', 'DMD', 'OPAL', 'ZCC', 'GLD', 'DGB', 'BTM', 'START', 'VPN', 'BOST', 'XDP', 'TRC', 'USDe', 'CCN', 'DVC', 'BLU', 'MOON', 'SYNC', 'DEM', 'VIOR', 'LXC', 'HBN', 'MZC', 'BBR', 'JPC', 'FRC', 'NAUT', 'M', 'PINK', 'XCH', 'FLT', 'WC', 'MYR', 'MINT', 'HZ', 'GSX', 'NAV', 'SMBR', 'UNC', 'ZEIT', 'EAC', 'DIEM', 'RIC', 'FIBRE', 'CLR', 'HYP', 'TAG', 'BITS', 'NET', 'AUR', 'WATER', 'GAIA', 'HTML5', 'RBY', 'MLS', 'EMC2', 'NOBL', 'MED', 'CARBON', 'CKC', 'EFL', 'TIPS', 'CXC', 'ABY', 'QSLV', 'BOOM', 'AC', 'KARM', 'PTC', 'XQN', 'XAI', 'TTC', 'DOGED', 'SRC', 'TEK', 'SLG', 'MMC', 'CRYPT', 'OCUPY', 'CLOAK', 'TES', 'GHC', 'BYC', 'LTCD', 'CINNI', 'XMG', 'CAP', 'SUPER', 'NFD', 'VTA', 'SEED', 'IOC', 'BCX', 'SBIT', 'CSC', 'EXCL', 'NEOS', 'VDO', 'DIME', 'MIN', 'BQC', 'FLAP', 'SFR', 'MNE', 'XDQ', 'AERO', 'BALLS', 'PIGGY', 'MWC', 'MARYJ', 'JBS', 'SSD', 'XCN', 'BLC', 'COMM', 'CHASH', 'QTL', 'QBK', 'SXC', 'OC', 'FST', 'XCASH', 'YAC', 'NKT', 'BTB', 'GLC', 'GMC', 'TIT', 'WKC', 'FCC', 'FLO', 'TRUST', 'OMC', 'NRS', 'SILK', 'ENRG', 'MRY', 'APEX', 'MNC', 'TCO', 'UFO', 'PIMP', 'NYAN', 'GDC', 'TRK', 'DIO', 'GML', 'NTX', 'KEY', 'LOT', 'THC', 'DTC', 'ULTC', 'UTIL', 'ACOIN', 'BSTY', 'HUC', 'GRS', 'BUN', 'FRK', 'GUE', 'DP', 'LEAF', 'BET', 'EXE', 'VOOT', 'PLC2', 'GUA', 'TRI', 'PLNC', 'VGC', 'CAGE', 'PFC', 'ARG', 'VMC', 'GRE', 'MUE', 'JKC', 'JUDGE', 'NYC', 'CGA', 'PXI', 'GHOST', 'LMR', 'GLYPH', 'CASH', 'MAL', '42', 'BRIT', 'CRT', 'ESC', 'DSB', 'AXR', 'TAK', 'ETD', 'BELA', 'FAIR', 'ORO', 'CHA', 'XWT', 'TIX', 'NAS', 'CGB', 'RIN', 'KORE', 'COL', 'LKY', 'FAIL', 'ORB', 'PHS', 'DTC', 'PRT', 'ROOT', 'EVENT', 'BUK', 'ECC', 'DRKC', 'FRSH', 'QBC', 'RZR', 'RED', 'ZED', 'NTR', 'HLC', 'TRL', 'COOL', 'HVC', 'RBBT', 'KING', 'CRW', 'LTB', 'MEOW', 'CTM', 'CAIx', 'XBC', 'C2', 'SAT2', 'DOPE', 'QB', 'SPA', 'FCN', 'ALN', 'ELT', 'UNB', 'PXC', 'XLB', 'RPC', 'ASC', 'SHA', 'KTK', 'SBC', 'SPARK', 'ABC2', 'XPD', 'GRW', 'SMC', 'EMD', 'ISR', 'GB', 'CHILD', 'HAM', 'MCN', 'DSH', 'SHIBE', 'FRAC', 'XXX', 'CAT', 'BTCS', 'XJO', 'MRC2', 'PYC', 'KDC', 'CRAIG', 'ELC', 'CESC', 'XSI', 'CAPT', 'BTG', 'GCN', 'XGR', 'ICG', 'ROX', 'HAL', 'PMP', 'AID', 'FOOD', 'SOL', 'PROZ', 'ICB', 'FLEX', 'MOTO', 'LTS', 'GNS', 'LGD', 'OSC', 'XCLD', 'ROS', 'TOR', 'SHLD', 'RIPO', 'BEN', 'PSEUD', 'ZS', 'GUN', 'ADN', 'QCN', 'EMU', 'DOGEBC', 'BCF', 'TECH', 'FFC', 'CNL', 'LSD', 'ONE', 'PES', 'CFC2', 'GROW', 'PRC', 'LYC', 'CATC', 'SOLE', 'SPT', 'CRACK', 'PHO', 'XBOT', 'NEC', 'SHADE', 'CND', 'BOB', 'IPC', 'CORG', 'RAW', 'PHC', 'RT2', 'KUMA', 'CYC', 'NRB', 'NMB', 'SPUDS', 'MUGA', 'BLZ', 'FUD', 'MNTA', 'KRN', 'BNCR', 'KRYP', 'FETISH', 'HEX', 'UNAT', 'BAT', 'HIRO', 'BDSM', 'GRN', 'CAC', 'TAC', 'GDN', 'U', 'DIG', 'DANK', 'CDN', 'BVC', 'UROD', 'CFN', 'XSTC', 'CACH', 'DPC', 'LIT', 'GRA', 'DON', 'DRS', 'BST', 'WLF', 'GOOD', 'LION', '66', 'RBT', 'BLOCK', 'EXC', 'LAT', 'DS', 'BTE', 'CRC', '2015', 'J', 'LAB', 'VTR', 'DBL', 'CNC', 'AGS', 'NBL', 'TGC', 'STV', 'DT', 'EZC', 'SCSY', 'AMC', 'SSV', 'NAN', 'ALF', 'SKC', 'KGC', 'CNO', 'STR', 'MEM', 'BTMI', 'ELP', 'GME', 'XNC', 'CENT']
_caps = [3921315210.0, 636283468.993, 70269867.8525, 48889237.8626, 35720775.1565, 19638122.8836, 16624651.7219, 16376696.3391, 10054250.9322, 8537818.8276, 8042625.72895, 6641439.1536, 5614400.08946, 4254680.53897, 3256470.53688, 3074250.0, 2372391.74602, 2270740.18812, 2002119.83602, 1575393.71441, 1449021.45762, 1248971.7159, 1187640.00056, 1123252.15834, 1002658.30072, 986144.565755, 958431.57131, 861320.928048, 842079.0, 716621.292037, 665051.40948, 550968.823573, 522938.19245, 516761.486867, 446907.513705, 441088.99399, 440403.757779, 432056.734717, 429280.933754, 365170.389995, 363276.005876, 361637.971345, 350207.943314, 345617.376068, 334323.936141, 322836.0, 320215.074144, 294491.753165, 292593.596644, 288017.430681, 283947.429658, 275467.028083, 274634.293226, 268217.835395, 243864.29353, 243248.017507, 242469.780132, 236503.472782, 230296.0, 219432.948265, 207455.102152, 207291.559023, 205111.288283, 200203.77888, 186150.916723, 185517.431618, 182809.502533, 180274.213615, 180179.895959, 178773.957184, 166292.275402, 165641.061143, 160991.45893, 157355.0, 153915.0, 149016.900885, 145911.623847, 145840.827745, 137232.053718, 134428.654084, 130554.512718, 130262.13098, 129576.410892, 129376.412953, 126839.287788, 121133.192462, 115009.387122, 113469.471562, 111043.912192, 109444.899191, 97088.7116603, 96341.8403762, 95843.0375322, 95657.2768706, 92499.7621554, 91596.2284851, 89666.3455253, 85558.0238438, 82329.8288127, 81519.6561323, 80042.9381991, 77225.3476696, 69670.6004242, 69421.9919257, 66703.9837117, 65674.9311516, 63763.5720959, 63104.7194406, 61494.1435762, 61411.5350169, 61232.611779, 59823.7153894, 59579.1655731, 59106.7242356, 56992.4484253, 56828.78475, 56343.7165637, 56255.4537522, 52423.5121016, 52255.1267506, 51580.702468, 49286.9994709, 48604.5203631, 46442.4783477, 45810.8283969, 45165.0247797, 44888.9389504, 44041.0238147, 43847.328375, 43111.6560514, 42640.0919152, 42500.0551056, 42455.9383516, 41576.7182646, 39551.8953932, 39365.8638134, 39033.0797603, 38971.9207686, 38544.4371247, 38541.086293, 38514.3507603, 38410.2130214, 38397.3979789, 38254.763042, 38093.19828, 37523.5283075, 37395.545775, 36073.0607492, 34771.6691, 33388.746551, 33291.8178961, 33227.8554097, 33059.256138, 32912.1993848, 32480.4116837, 31822.2827405, 31758.7510999, 31679.6430732, 30558.3556399, 29889.2073616, 29845.8462541, 29246.0977166, 29029.5424083, 28891.4209285, 28610.0, 28563.0534966, 28178.576951, 27598.8473873, 27569.174979, 27192.55497, 26748.4265863, 26524.2340588, 26103.7803385, 26064.3662818, 25239.690236, 24600.0442039, 23758.2724633, 23250.6174644, 21992.2888242, 21622.5542893, 20924.0938264, 20503.6952942, 20337.3102821, 20333.4469399, 19883.8305536, 19755.9672568, 19031.7191152, 18424.7387084, 18260.3667523, 18159.2097167, 18150.3824788, 18070.6340966, 17866.1700969, 17737.48475, 17422.0991615, 17293.0336975, 16648.2087547, 15730.3207745, 15664.5472, 15246.6689634, 13954.934708, 13568.6702893, 12490.7328, 12362.8171207, 11999.2146625, 11789.283408, 11727.4460341, 11663.382396, 11410.7862365, 11061.0590161, 10972.802088, 10716.926221, 10571.3774439, 10478.1863933, 10135.0482171, 9889.90364386, 9874.5070615, 9769.80486295, 9638.31345821, 9305.08147291, 9267.03882362, 8863.2, 8583.0, 8147.89517197, 8031.45635975, 7917.07475149, 7903.77645972, 7849.96091, 7587.84526218, 7423.20387111, 7270.743322, 7126.960733, 7054.0858629, 6981.46698044, 6712.80959115, 6611.6218668, 6444.57107783, 5964.7326585, 5772.19640313, 5717.26688176, 5619.55446791, 5538.390396, 5229.08882437, 4852.36076982, 4777.62609975, 4439.8863372, 4219.67533748, 4054.6229328, 3570.40234339, 3456.50829397, 3368.77816481, 3097.39312905, 2977.67132785, 2457.55732914, 2399.0850918, 2397.12190025, 2302.80396539, 1958.6006968, 1902.93273785, 1858.52, 1843.2512975, 1645.93292522, 1328.33325149, 1320.64803937, 1297.08474026, 1285.37360826, 1190.63995439, 991.128972893, 856.531669006, 646.411479, 287.096612445, 157.5555561, 196934.882104, 156967.602676, 102885.256658, 93467.7119877, 75579.5606772, 55005.6, 52272.199448, 28744.5206815, 26061.1351527, 24928.4023491, 24549.4997862, 23262.6785117, 22867.0939614, 16734.2027609, 16219.0215536, 15479.146671, 14501.1787701, 13508.9260582, 13468.5079328, 13332.4092475, 13043.8471431, 12498.6202751, 12464.2856048, 12324.7162324, 11599.7802026, 11445.0181109, 10805.9591348, 10546.7400968, 10121.1364966, 10103.9451363, 9962.3386561, 9926.96512498, 9104.30038187, 9050.525033, 8848.64397144, 8776.93935932, 8725.61567941, 8709.5866616, 8580.96780309, 8553.7260781, 8298.19056426, 7651.99842997, 7402.86953176, 7310.42367622, 7222.34256161, 6940.14497842, 6760.109364, 6575.14004317, 6261.86372932, 6077.00491922, 5972.01274738, 5907.75845583, 5548.90499466, 5459.93013271, 5435.87362437, 5287.82038349, 5140.02096939, 5117.12692683, 5002.83251853, 4751.33515112, 4597.09205475, 4397.13638662, 4346.00863716, 4334.48332987, 4205.97919729, 4186.96673172, 4167.337815, 4150.84108075, 4060.1606844, 4010.1251156, 3991.48079873, 3958.47639854, 3942.40549231, 3940.6719113, 3775.6028557, 3747.37068246, 3678.41111443, 3650.02721125, 3596.18255873, 3593.35492334, 3578.01285525, 3553.78810478, 3530.78100678, 3428.5038144, 3322.87792794, 3256.95981991, 3158.79812474, 3157.92426472, 2997.9015279, 2993.62175043, 2973.48007631, 2901.16502141, 2757.23930496, 2751.81676684, 2746.18540458, 2652.26621921, 2508.89664417, 2449.06754592, 2385.09978615, 2355.61109638, 2299.90285737, 2234.8585789, 2211.4537788, 2193.18389801, 2148.6025191, 2099.11028699, 2042.91404925, 2021.3158513, 1974.30465393, 1957.50071716, 1923.4584432, 1883.93524096, 1857.0556452, 1835.80935361, 1797.1416681, 1664.25312341, 1663.40548915, 1657.6848912, 1568.6628708, 1428.64711353, 1416.62124437, 1414.93226307, 1374.22572468, 1365.02175587, 1329.55870148, 1249.31864424, 1248.15991902, 1186.82234807, 1177.5116265, 1160.2101036, 1157.19788318, 1154.15809659, 1131.5476615, 1096.37864364, 1058.0538756, 1044.5041796, 1044.33618082, 1016.03681873, 936.870471021, 925.711670595, 829.979402016, 774.550417536, 766.557487966, 747.111856689, 737.66247548, 700.8151106, 662.230677888, 660.160878522, 634.054823716, 524.935792573, 521.324867758, 514.654411696, 511.1393936, 497.170061177, 488.78941482, 486.22763664, 448.958026304, 392.489191341, 364.79111836, 268.496481093, 264.207728965, 257.545994251, 215.57217636, 179.659810226, 139.52258727, 133.8644734, 127.729817285, 116.01225291, 114.518303142, 102.447472584, 96.4588692259, 92.26539035, 49.300752, 42.614466255, 32.9014096781, 23.6650824279, 4.30086406851, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def cap_for_ticker(ticker):
    idx = rank_for_ticker(ticker)
    if idx != None:
        return _caps[idx]

def rank_for_ticker(ticker):
    ticker = ticker.upper()
    if ticker in _coins:
        return _coins.index(ticker.upper())
