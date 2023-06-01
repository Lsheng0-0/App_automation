# 导入webdriver
import os
import sys
from time import sleep
# 初始化参数
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait

caps = {}
caps["appium:platformName"] = "Android"
caps["appium:platformVersion"] = "10"
caps["appium:deviceName"] = "CMLFPZCU596HH6Z9"
caps["appium:appPackage"] = "com.alibaba.android.rimet"
caps["appium:appActivity"] = ".biz.LaunchHomeActivity"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://192.168.0.101:4723/wd/hub", caps)


def get_coordinate(value):
    """
    获取中心点坐标
    :param value: 元素的id
    :return: 元素中心点坐标
    """
    ele_size = driver.find_element(by=AppiumBy.ID, value=value).size
    ele_loc = driver.find_element(by=AppiumBy.ID, value=value).location
    # 元素的宽、高
    width = ele_size['width']
    height = ele_size['height']
    # 元素左上角坐标
    x = ele_loc['x']
    y = ele_loc['y']
    return x + width / 2, y + height / 2  # 元素中心点坐标


def element_swipe(x1, y1, width=0, high=0):
    """
    滑动屏幕
    :param x1:
    :param y1:
    :param width: 正负右左
    :param high: 正负下上
    :return: 动作
    """
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x1, y1)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(x1 + width, y1 + high)
    actions.w3c_actions.pointer_action.release()
    actions.perform()


def element_click(ele, by_away='id'):
    """
    :param by_away:
    :param ele:
    :return:
    """

    if by_away == 'id':
        element = driver.find_element(by=AppiumBy.ID, value=ele)
        element.click()
    elif by_away == 'xpath':
        element = driver.find_element(by=AppiumBy.XPATH, value=ele)
        element.click()
    elif by_away == 'class_name':
        element = driver.find_element(by=AppiumBy.CLASS_NAME, value=ele)
        element.click()
    return True


def element_send(ele, keys, by_away='id'):
    """
    :param ele:
    :param keys:
    :return:
    """
    if by_away == 'id':
        element = driver.find_element(by=AppiumBy.ID, value=ele)
        element.send_keys(keys)
    elif by_away == 'xpath':
        element = driver.find_element(by=AppiumBy.XPATH, value=ele)
        element.send_keys(keys)
    elif by_away == 'class_name':
        element = driver.find_element(by=AppiumBy.CLASS_NAME, value=ele)
        element.send_keys(keys)


def is_element(element, timeout=1):
    """
    # 判断元素是否存在
    :param element:
    :param timeout:
    :return:
    """
    count = 0
    while count < timeout:
        souce = driver.page_source
        if element in souce:
            return True
        else:
            count += 1
            sleep(1)
    return False


def isElement(identifyBy, c):
    """
    Determine whether elements exist
    Usage:
    isElement(By.XPATH,"//a")
    """
    sleep(1)
    flag = None
    try:
        if identifyBy == "id":
            WebDriverWait(driver, timeout=20, poll_frequency=1).until(
                lambda x: x.find_element(by=AppiumBy.ID, value=c),
                message='id定位超时')
        elif identifyBy == "xpath":
            WebDriverWait(driver, timeout=20, poll_frequency=1).until(
                lambda x: x.find_element(by=AppiumBy.XPATH, value=c),
                message='xpath定位超时')
        elif identifyBy == "class_name":
            WebDriverWait(driver, timeout=20, poll_frequency=1).until(
                lambda x: x.find_element(by=AppiumBy.CLASS_NAME, value=c),
                message='class_name定位超时')
        elif identifyBy == "link_text":
            WebDriverWait(driver, timeout=20, poll_frequency=1).until(
                lambda x: x.find_element(by=AppiumBy.LINK_TEXT, value=c),
                message='link_text定位超时')
        elif identifyBy == "partial_link_text":
            WebDriverWait(driver, timeout=20, poll_frequency=1).until(
                lambda x: x.find_element(by=AppiumBy.PARTIAL_LINK_TEXT, value=c),
                message='partial_link_text定位超时')
        elif identifyBy == "name":
            WebDriverWait(driver, timeout=20, poll_frequency=1).until(
                lambda x: x.find_element(by=AppiumBy.NAME, value=c),
                message='name定位超时')
        elif identifyBy == "tag_name":
            WebDriverWait(driver, timeout=20, poll_frequency=1).until(
                lambda x: x.find_element(by=AppiumBy.TAG_NAME, value=c),
                message='tag_name定位超时')
            driver.find_element(by=AppiumBy.TAG_NAME, value=c)
        elif identifyBy == "css_selector":
            WebDriverWait(driver, timeout=20, poll_frequency=1).until(
                lambda x: x.find_element(by=AppiumBy.CSS_SELECTOR, value=c),
                message='css_selector定位超时')
        flag = True
    except NoSuchElementException as e:
        flag = False
    finally:
        return flag


def get_text(ele):
    """
    获取元素的text
    :param ele:
    :return:
    """
    element = driver.find_element(by=AppiumBy.ID, value=ele)
    text = element.__getattribute__("text")
    return text


def login_dingtalk(account, passwd):
    """
    登录操作
    """
    appPackage = "com.alibaba.android.rimet:id/"
    # 点击同意,输入账号,点击下一步,点击同意,点击继续,输入密码.点击登录 1、5输入
    login_object = ['btn_agree', 'et_phone', 'll_container', 'cb_privacy', 'btn_next', 'et_password', 'tv']
    num = 0
    for ob in login_object[:]:
        is_el = is_element(appPackage + ob, timeout=15)
        if is_el is True:
            print(appPackage + ob)
            if num == 1 or num == 5:
                if num == 1:
                    keys = account
                else:
                    keys = passwd
                element_send(appPackage + ob, keys)
            else:
                element_click(appPackage + ob)
            num += 1
            sleep(1)
        else:
            print("登录失败！！！")
    print("登录成功")


def detect():
    """
    检测弹窗
    :return:
    """
    # 检测是否有更新
    mes = is_element('android:id/message', timeout=15)
    if mes is True:
        message = get_text('android:id/message')
        if message == '修复了一些已知问题，提升了用户体验。':
            element_click('android:id/button2')
        else:
            pass
    else:
        pass


def restart():
    # 重启此程序
    os.execv(__file__, *sys.argv[1:])


def switch_organizations():
    # 组织名
    is_element('com.alibaba.android.rimet:id/tv_org_name', timeout=15)
    tv_org_name = get_text('com.alibaba.android.rimet:id/tv_org_name')
    if tv_org_name == '上海一橙网络科技股份有限公司九江分公司':
        """
        执行换组织操作
        """
        element_click('com.alibaba.android.rimet:id/tv_org_name')
        sleep(1)
        # 江西中铁服务公司
        element_click("//*[@text='江西中铁服务公司']", by_away='xpath')
    elif tv_org_name == '工作台':
        """
        工作台就重启
        """
        driver.quit()
        sleep(1)
        restart()
    else:
        pass


# 安全答题
def answer_questions_safely():
    element_click("//*[@text='安全答题']", by_away='xpath')
    is_element("com.alibaba.android.rimet:id/title")
    element_click("com.alibaba.android.rimet:id/title")
    element_click("//*[@text='安全答题']" and "//*[@index='2']", by_away='xpath')
    # 安全答题
    element_click('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
                  '.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                  '/android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                  '/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view'
                  '.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/com.uc.webview.export.WebView'
                  '/com.uc.webkit.bb/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android'
                  '.view.View/android.view.View[4]/android.view.View[2]/android.view.View[1]', by_away='xpath')


login_dingtalk(account="13507922019", passwd="dj1522833718")
is_element('com.alibaba.android.rimet:id/action_bar_root', timeout=15)
# 检测更新敞口
detect()
# 是否更换组织
switch_organizations()
# 安全自查
frame = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget' \
        '.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android' \
        '.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android' \
        '.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android' \
        '.widget.RelativeLayout/android.widget.RelativeLayout/com.uc.webview.export.WebView/com.uc.webkit.bb/android' \
        '.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[' \
        '3]/android.view.View/android.view.View/android.view.View[1]'
isElement('xpath', "//*[@text='每日安全自查']")
q = element_click("//*[@text='每日安全自查']", by_away='xpath')
print(q)
pa = [2, 3, 5, 6]
for p in pa:
    sleep(1)
    fil_in = '/android.view.View[{}]/android.view.View[3]/android.view.View'.format(str(p))
    print(frame + fil_in)
    isElement('xpath', frame + fil_in)
    sleep(1)
    w =  element_click(frame + fil_in, by_away='xpath')
    print(w)
    if p == 2:
        isElement('xpath', "//*[@text='九江']")
        element_click("//*[@text='九江']", by_away='xpath')
    elif p == 3:
        isElement('xpath', "//*[@text='濂溪区']")
        element_click("//*[@text='濂溪区']", by_away='xpath')
    elif p == 5:
        isElement('xpath', "//*[@text='维护条线']")
        element_click("//*[@text='维护条线']", by_away='xpath')
    elif p == 6:
        isElement('xpath', "//*[@text='集客']")
        element_click("//*[@text='集客']", by_away='xpath')

# 上划
element_swipe(379, 1175, high=-675)
isElement('class_name', "android.widget.EditText")
element_send("android.widget.EditText", keys='36', by_away='class_name')

frame_sel = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget' \
            '.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android' \
            '.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget' \
            '.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget' \
            '.RelativeLayout/android.widget.RelativeLayout/com.uc.webview.export.WebView/com.uc.webkit.bb/android.webkit' \
            '.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[' \
            '3]/android.view.View/android.view.View/android.view.View[1]/'
pa2 = [9, 10, 11, 13, 15, 16, 17, 18, 19, 20]
for i in pa2:
    sleep(1)
    ge = 'android.view.View[{}]/android.view.View[3]/android.view.View[1]/android.view.View[2]'.format(str(i))
    isElement('xpath', frame_sel + ge)
    element_click(frame_sel + ge, by_away='xpath')
    if i == 11 or i == 15 or i == 18:
        element_swipe(379, 1175, high=-675)
sleep(1)
isElement('xpath', "//*[@text='提交']")
element_click("//*[@text='提交']", by_away='xpath')
if is_element("com.alibaba.android.rimet:id/webview_frame", timeout=15) is True:
    print('完成自查')
else:
    print('重复自查')

element_click('com.alibaba.android.rimet:id/back_icon')
sleep(5)
driver.quit()