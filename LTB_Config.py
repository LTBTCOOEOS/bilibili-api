
class LTB_Config:
    UDP_IP = "127.0.0.1"
    UDP_PORT = 60013
    myRoom = 3645373

    topThreeEnable = False
    multiProxyEnable = False
    getFaceEnable = False
    getNormalDataEnable = False
    writePresistData = False

    presist_data_file_name = "presist_file.csv"
    # 代理服务器(产品官网 www.16yun.cn)
    proxyHost = "u7713.20.tn.16yun.cn"
    proxyPort = "6227"

    # 代理验证信息
    proxyUser = "16PADDGK"
    proxyPass = "649418"
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host" : proxyHost,
        "port" : proxyPort,
        "user" : proxyUser,
        "pass" : proxyPass,
    }




