dict_sh_sz = {
        '最新': 'lastPrice',
        '均价': 'averageValue',
        '涨幅': 'changeRate',
        '涨跌': 'change',
        '总手': 'volume',
        '金额': 'amount',
        '换手': 'turnoverRate',
        '量比': 'volumeRatio',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '涨停': 'limitUp',
        '跌停': 'limitDown',
        '外盘': 'buyVolume',
        '内盘': 'sellVolume',
        '委比': 'orderRatio',
        '振幅': 'amplitudeRate',
        '市盈率(动) right': 'pe',
        '市盈率(静) right': 'pe2',
        '每股净资产': 'netAsset',
        '市净率': 'pb',
        '总股本': 'capitalization',
        '总值': 'totalValue',
        '流通股': 'circulatingShares',
        '流值': 'flowValue'
    }

dict_sci_tech = {
        '最新': 'lastPrice',
        '均价': 'averageValue',
        '涨幅': 'changeRate',
        '涨跌': 'change',
        '总手': 'volume',
        '金额': 'amount',
        '换手': 'turnoverRate',
        '量比': 'volumeRatio',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '涨停': 'limitUp',
        '跌停': 'limitDown',
        '外盘': 'buyVolume',
        '内盘': 'sellVolume',
        '委比': 'orderRatio',
        '振幅': 'amplitudeRate',
        '盘后量': 'afterHoursVolume',
        '盘后额': 'afterHoursAmount',
        '盘后成交笔数': 'afterHoursTransactionNumber',
        '盘后撤单数量': 'afterHoursWithdrawBuyCount',
        '盘后撤单笔数': 'afterHoursWithdrawBuyVolume',
        '市盈率(动) right': 'pe',
        '市盈率(静) right': 'pe2',
        '每股净资产': 'netAsset',
        '市净率': 'pb',
        '是否同股同权': 'vote',
        '总股本': 'capitalization',
        '总值': 'totalValue',
        '流通股': 'circulatingShares',
        '流值': 'flowValue',
        '发行股本': 'issuedCapital',
        '是否盈利': 'upf'
    } #市盈率有所改动 #TODO L2账号盘后成交笔数查看

dict_hk = {
        '最新': 'lastPrice',
        '均价': 'averageValue',
        '涨幅': 'changeRate',
        '涨跌': 'change',
        '总手': 'volume',
        '金额': 'amount',
        '换手': 'turnoverRate',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '外盘': 'buyVolume',
        '内盘': 'sellVolume',
        '市盈率(TTM)': 'pe',
        '每股净资产': 'netAsset',
        '市净率': 'pb',
        '总股本': 'capitalization',
        '总值': 'totalValue',
        '港股本': 'hs',
        '港值': 'HKTotalValue'
    }

dict_hk_wl = {
        '最新': 'lastPrice',
        '均价': 'averageValue',
        '涨幅': 'changeRate',
        '涨跌': 'change',
        '总手': 'volume',
        '金额': 'amount',
        '换手': 'turnoverRate',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '外盘': 'buyVolume',
        '内盘': 'sellVolume',
    }


dict_fund = {
        '最新': 'lastPrice',
        '均价': 'averageValue',
        '涨幅': 'changeRate',
        '涨跌': 'change',
        '总手': 'volume',
        '金额': 'amount',
        '换手': 'turnoverRate',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '外盘': 'buyVolume',
        '内盘': 'sellVolume'
    }

dict_fund_ETF = {
        '最新': 'lastPrice',
        '涨跌': 'change',
        '涨幅': 'changeRate',
        '换手': 'turnoverRate',
        '涨停': 'limitUp',
        '跌停': 'limitDown',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '量比': 'volumeRatio',
        '总手': 'volume',
        '金额': 'amount',
        '实时净值': 'IOPV'
}

#债券
dict_bond = {
        '最新': 'lastPrice',
        '涨跌': 'change',
        '涨幅': 'changeRate',
        '总手': 'volume',
        '量比': 'volumeRatio',
        '金额': 'amount',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '外盘': 'buyVolume',
        '内盘': 'sellVolume'
}

dict_bond_sh_sz = {
        '最新': 'lastPrice',
        '涨跌': 'change',
        '涨幅': 'changeRate',
        '总手': 'volume',
        '量比': 'volumeRatio',
        '金额': 'amount',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '正股代码': 'zgConvertCodes',
        '外盘': 'buyVolume',
        '内盘': 'sellVolume'
}
#沪国债
dict_bond_sh_gz = {
        '最新': 'lastPrice',
        '涨跌': 'change',
        '涨幅': 'changeRate',
        '总手': 'volume',
        '量比': 'volumeRatio',
        '金额': 'amount',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '资金可用日': 'rpd',
        '资金可取日': 'cdd',
        '占款天数': 'cd',
        '借用天数': 'rp',
        '外盘': 'buyVolume',
        '内盘': 'sellVolume'
}

#深国债
dict_bond_sz_gz = {
        '最新': 'lastPrice',
        '涨跌': 'change',
        '涨幅': 'changeRate',
        '总手': 'volume',
        '量比': 'volumeRatio',
        '金额': 'amount',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '今加权': 'add_option_avg_price',
        '昨加权': 'add_option_avg_close',
        '涨跌BP': 'add_option_avg_pb',
        '资金可用日': 'rpd',
        '资金可取日': 'cdd',
        '占款天数': 'cd',
        '借用天数': 'rp',
        '外盘': 'buyVolume',
        '内盘': 'sellVolume'
}

dict_newOTCmarket = {
        '最新': 'lastPrice',
        '均价': 'averageValue',
        '涨幅': 'changeRate',
        '涨跌': 'change',
        '总手': 'volume',
        '金额': 'amount',
        '换手': 'turnoverRate',
        '量比': 'volumeRatio',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '涨停': 'limitUp',
        '跌停': 'limitDown',
        '外盘': 'buyVolume',
        '内盘': 'sellVolume',
        '委比': 'orderRatio',
        '振幅': 'amplitudeRate',
        '市盈率（动）': 'pe',
        '市盈率（静）': 'pe2',
        '每股净资产': 'netAsset',
        '市净率': 'pb',
        '总股本': 'capitalization',
        '总值': 'totalValue',
        '流通股': 'circulatingShares',
        '流值': 'flowValue'
}

# 上证期权
dict_option = {
        '最新': 'lastPrice',
        '均价': 'averageValue',
        '涨幅': 'changeRate',
        '涨跌': 'change',
        '总量': 'volume',
        '金额': 'amount',
        '持仓': 'openInterest',
        '日增': 'position_chg',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '结算': 'setPrice',
        '今开': 'openPrice',
        '前结': 'presetPrice',
        '合约单位': 'stockUnit',
        '涨停': 'limitUp',
        '跌停': 'limitDown',
        '行权价': 'excercisePx',
        '剩余期限': 'remainDate',
        '内在价值': 'inValue',
        '折溢价率': 'premiumRate',
        '隐含波动': 'impliedVolatility',
        'Delta': 'delta',
        'Gamma': 'gramma',
        'Theta': 'theta',
        'Vega': 'vega',
        'Rho': 'rho'
}

#期货 中金所
dict_future_zjs= {
        '最新': 'lastPrice',
        '涨跌': 'change',
        '涨幅': 'changeRate',
        '换手': 'turnoverRate',
        '涨停': 'limitUp',
        '跌停': 'limitDown',
        '今开': 'openPrice',
        '昨结': 'preSettlement',
        '量比': 'volumeRatio',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '总手': 'volume',
        '金额': 'amount',
        '持仓': 'openInterest',
        '外盘': 'buy_vol',
        '内盘': 'sell_vol',
}
# 期货、期权-大商所 郑商所 上期所
dict_option_future = {
        '最新': 'lastPrice',
        '均价': 'averageValue',
        '涨跌': 'change',
        '涨幅': 'changeRate',
        '今开': 'openPrice',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '总手': 'volume',
        '金额': 'amount',
        '外盘': 'buy_vol',
        '内盘': 'sell_vol',
        '持仓': 'openInterest',
        '结算': 'settlement',
        '仓差': 'posDiff',
        '前结': 'preSettlement',
        '日增': 'position_chg'
}

# 全球 、外汇（收盘行情）
dict_after = {
        '最新': 'lastPrice',
        '涨幅': 'changeRate',
        '涨跌': 'change',
        '今开': 'openPrice',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '昨收': 'preClosePrice',
        '振幅': 'amplitudeRate',
        '总手': 'volume'
}

dict_sh_sz_index = {
        '最新': 'lastPrice',
        '涨幅': 'changeRate',
        '涨跌': 'change',
        '今开': 'openPrice',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '昨收': 'preClosePrice',
        '总手': 'volume',
        '换手': 'turnoverRate',
        '量比': 'volumeRatio',
        '上涨家数': 'upCount',
        '平盘家数': 'sameCount',
        '下跌家数': 'downCount'
}

dict_hk_index = {
        '最新': 'lastPrice',
        '涨幅': 'changeRate',
        '涨跌': 'change',
        '今开': 'openPrice',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '昨收': 'preClosePrice',
        '振幅': 'amplitudeRate',
        '总手': 'volume'
}


dict_newOTCmarket_index = {
        '最新': 'lastPrice',
        '涨幅': 'changeRate',
        '涨跌': 'change',
        '今开': 'openPrice',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '昨收': 'preClosePrice',
        '振幅': 'amplitudeRate',
        '总手': 'volume',
        '换手': 'turnoverRate',
        '量比': 'volumeRatio',
        '上涨家数': 'upCount',
        '平盘家数': 'sameCount',
        '下跌家数': 'downCount',
        '均价': 'averageValue',
        '委比': 'orderRatio',
        '外盘': 'buyVolume',
        '内盘': 'sellVolume'
}

# L1权限下，除期货、期权、沪深港、新三板指数及全球、外汇，其他股票 TickRequest
dict_TickRequest = {
        '时间': 'getTransactionTime()',
        '成交价': 'getTransactionPrice()',
        '成交量': 'getSingleVolume()'

}

# L1权限下，期货、期权（中金所、大商所、郑商所、上期所、上期所原油） TickRequest
dict_TickRequest_option_future = {
        '时间': 'getTransactionTime()',
        '成交价': 'getTransactionPrice()',
        '成交量': 'getSingleVolume()',
        '仓差': 'getOpenInterestDiff()',
        '性质': 'getType()'
}

# L2权限下，沪深港股票，包含AB股、基金、债券 L2TickDetailRequestV2
dict_TickDetailRequest_L2 = {
        '时间': 'getTransactionTime()',
        '成交价': 'getTransactionPrice()',
        '成交量': 'getSingleVolume()'
}

def get_dict(type):
    dict = {
        "sh_sz": dict_sh_sz,
        "sci_tech": dict_sci_tech,
        "hk": dict_hk,
        "hk_wl": dict_hk_wl,
        "fund": dict_fund,
        "fund_ETF": dict_fund_ETF,
        "bond": dict_bond,
        "bond_sh_sz": dict_bond_sh_sz,
        "bond_sh_gz": dict_bond_sh_gz,
        "bond_sz_gz": dict_bond_sz_gz,
        "newOTCmarket": dict_newOTCmarket,
        "option": dict_option,
        "future_zjs": dict_future_zjs,
        "option_future": dict_option_future,
        "after": dict_after,
        "sh_sz_index": dict_sh_sz_index,
        "hk_index": dict_hk_index,
        "newOTCmarket_index": dict_newOTCmarket_index,
        "TickRequest": dict_TickRequest,
        "TickRequest_option_future": dict_TickRequest_option_future,
        "TickDetailRequest_L2": dict_TickDetailRequest_L2
    }
    return dict[type]
