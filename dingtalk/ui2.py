# coding: utf-8
from time import sleep

import uiautomator2 as u2

from dingsend import dingrobot

d = u2.connect('CMLFPZCU596HH6Z9')
appPackage = "com.alibaba.android.rimet:id/"


def open_dingtalk(account="13507922019", passwd="dj1522833718"):
    d.app_clear("com.alibaba.android.rimet")
    d.app_start("com.alibaba.android.rimet")  # 启动dingdingAPP
    elem = ['btn_agree', 'et_phone', 'll_container', 'cb_privacy', 'btn_next', 'et_password', 'tv']
    num = 0
    for e in elem:
        if num == 1 or num == 5:
            if num == 1:
                keys = account
            else:
                keys = passwd
            d(resourceId=appPackage + e).wait()
            d(resourceId=appPackage + e).send_keys(keys)
        else:
            d(resourceId=appPackage + e).wait()
            d(resourceId=appPackage + e).click()
        num += 1


def switch_organizations():
    # 组织名
    d(resourceId=appPackage + 'tv_org_name').wait()
    tv_org_name = d(resourceId=appPackage + 'tv_org_name').get_text()
    if tv_org_name == '上海一橙网络科技股份有限公司九江分公司':
        """
        执行换组织操作
        """
        d(resourceId=appPackage + 'tv_org_name').click()
        # 江西中铁服务公司
        d(resourceId=appPackage + "tv_title", text="江西中铁服务公司").wait()
        d(resourceId=appPackage + "tv_title", text="江西中铁服务公司").click()
    elif tv_org_name == '江西中铁服务公司':
        pass


def Options_one(timu):
    d.xpath(timu).wait()
    d.xpath(timu).click()
    sleep(1)
    while True:
        cen = d.xpath('//*[@text="暂无内容"]').center()
        print(cen)
        if cen[1] >= 1500:
            d.swipe(355, 1234, 355, 1000)
            sleep(0.5)
        else:
            break
    Op = ['A', 'B', 'C', 'D']
    nu = 0
    for i in Op:
        if nu == 0:
            d.xpath('//*[@text="请选择"]').wait()
            d.xpath('//*[@text="请选择"]').click()
        else:
            d.xpath('//*[@text="{}"]'.format(Op[nu - 1])).wait()
            d.xpath('//*[@text="{}"]'.format(Op[nu - 1])).click()
        nu += 1
        d(text=i).wait()
        d(text=i).click()
        sleep(1)
        if d.xpath('//*[@text="答案正确"]').exists is True:
            print('答案正确')
            sleep(0.5)
            d.xpath('//*[@text="收起"]').click()
            return True
        else:
            pass


def Options_all():
    timu1 = '//*[@resource-id="root"]/android.view.View[1]/android.view.View[3]/android.view.View[' \
            '1]/android.view.View[1]/android.view.View[1]/android.view.View[6]/android.view.View[' \
            '3]/android.view.View[1]/android.view.View[1]'
    timu2 = '//*[@resource-id="root"]/android.view.View[1]/android.view.View[1]/android.view.View[' \
            '3]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[' \
            '6]/android.view.View[3]/'
    ti = 0
    for i in range(5):
        if ti == 0:
            # 第一个展开
            timu = timu1
        else:
            timu = timu2 + 'android.view.View[{}]/android.view.View[1]/android.view.View[1]'.format(str(ti + 1))
            print(str(ti + 1))
        ti += 1
        Options_one(timu)


def Answer_questions_safely():
    # 办公
    d.xpath('//*[@resource-id="com.alibaba.android.rimet:id/recycler_view"]/android.widget.RelativeLayout[3]').wait()
    d.xpath('//*[@resource-id="com.alibaba.android.rimet:id/recycler_view"]/android.widget.RelativeLayout[3]').click()
    # 安全答题
    d(text="安全答题").wait()
    d(text="安全答题").click()
    # 安全答题文件夹
    d.xpath(
        '//*[@resource-id="root"]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[1]').wait()
    d.xpath(
        '//*[@resource-id="root"]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[1]').click()
    # 安全答题文件
    d.xpath(
        '//*[@resource-id="root"]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View['
        '2]/android.view.View[1]/android.view.View[3]').wait()
    d.xpath(
        '//*[@resource-id="root"]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View['
        '2]/android.view.View[1]/android.view.View[3]').click()
    Options_all()
    d.xpath('//*[@text="提交"]').click()
    while True:
        if d.xpath('//*[@text="今日已作答，请明日再答题！"]').exists:
            print('今日已作答，请明日再答题！')
            d(resourceId="com.alibaba.android.rimet:id/back_icon").wait()
            d(resourceId="com.alibaba.android.rimet:id/back_icon").click()
            d(resourceId="android:id/button2").wait()
            d(resourceId="android:id/button2").click()
            return '今日已作答，请明日再答题！'
        elif d(text="您已完成今日作答，得分100，再接再厉！").exists:
            d(resourceId="com.alibaba.android.rimet:id/back_icon").wait()
            d(resourceId="com.alibaba.android.rimet:id/back_icon").click()
            d(resourceId="com.alibaba.android.rimet:id/close_layout").wait()
            d(resourceId="com.alibaba.android.rimet:id/close_layout").click()
            return '今日作答完成！'
        else:
            pass


def Security_self_check():
    d.xpath('//*[@resource-id="com.alibaba.android.rimet:id/recycler_view"]/android.widget.RelativeLayout[3]').wait()
    d.xpath('//*[@resource-id="com.alibaba.android.rimet:id/recycler_view"]/android.widget.RelativeLayout[3]').click()
    d.xpath('//*[@text="每日安全自查"]').wait()
    d.xpath('//*[@text="每日安全自查"]').click()
    f = '//*[@resource-id="root"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[' \
        '1]/android.view.View[1]/'
    fa = '//*[@resource-id="root"]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[' \
         '1]/android.view.View[1]/android.view.View[1]/'

    values = {2: "九江", 3: "濂溪区", 5: "维护条线", 6: "集客"}
    for key, value in values.items():
        # print(key, value)
        if key == 2:
            a = f
        else:
            a = fa
        d.xpath(a + 'android.view.View[{}]/android.view.View[3]'.format(str(key))).wait()
        d.xpath(a + 'android.view.View[{}]/android.view.View[3]'.format(str(key))).click()
        d(text=value).wait()
        d(text=value).click()
    sleep(1)
    d.swipe(355, 1234, 355, 280)
    d.xpath(fa + 'android.view.View[8]/android.view.View[4]').wait()
    d.xpath(fa + 'android.view.View[8]/android.view.View[4]').set_text(str(36))
    Vi = 9
    for i in range(12):
        if Vi <= 14:
            x = 1
        else:
            x = 3
        if Vi == 12:
            d.swipe(355, 1234, 355, 280)
        elif Vi == 14:
            pass
        elif Vi == 16:
            d.xpath(fa + 'android.view.View[16]/android.view.View[3]/android.view.View[{}]'.format(x)).wait()
            d.xpath(fa + 'android.view.View[16]/android.view.View[3]/android.view.View[{}]'.format(x)).click()
            d.swipe(355, 1234, 355, 280)
        else:
            d.xpath(fa + 'android.view.View[{}]/android.view.View[3]/android.view.View[{}]'.format(str(Vi), x)).wait()
            d.xpath(fa + 'android.view.View[{}]/android.view.View[3]/android.view.View[{}]'.format(str(Vi), x)).click()
        # print(Vi)
        Vi += 1
    d.xpath('//*[@text="提交"]').click()
    while True:
        if d.xpath('//*[@text="此项内容已存在，不允许重复提交"]').exists:
            return '今日已自查，请明日再自查！'
        elif d.xpath('//*[@text="提交成功"]').exists:
            return '今日自查完成！'
        else:
            pass


def dingtalk_task():
    # 打开程序
    open_dingtalk()
    # 切换组织判断
    switch_organizations()
    # 安全答题
    Answer = Answer_questions_safely()
    dingrobot('安全答题', Answer, pic='https://img2.baidu.com/it/u=2879694884,3288412488&fm=253')
    # 安全自查
    Security = Security_self_check()
    dingrobot('安全自查', Security, pic='https://img2.baidu.com/it/u=2879694884,3288412488&fm=253')

    d.app_stop("com.alibaba.android.rimet")  # 停止应用


dingtalk_task()
