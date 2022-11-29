import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = 'SM-G531H'
options.app_package = 'com.sec.android.app.launcher'
options.app_activity = 'com.android.launcher2.Launcher'
options.automation_name = 'UiAutomator1'
options.full_reset = 'false'
options.no_reset = 'true'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
driver.implicitly_wait(15)
    
def test_OpenApkChat():
    e11 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Aplikasi")
    e11.click()
    e12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Teamgram Beta")
    e12.click()
    assert 'android.widget.ImageView' in driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Open navigation menu').tag_name
def test_NewMessage():
    e13 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@content-desc=\"New Message\"]/android.widget.ImageView")
    e13.click()
    assert 'New Message' in driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]/android.widget.TextView').text
def test_SearchContact():
    e14 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageButton[@content-desc=\"Search\"]/android.widget.ImageView")
    e14.click()
    el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
    el5.click()
    el5.send_keys("Juan Fernando")
    e16 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[2]/android.view.View/android.view.View[1]")
    e16.click()
def test_Chat():
    e17 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.EditText")
    e17.click()
    e18 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.EditText")
    e18.send_keys('Halo Test')
    e19 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc=\"Emoji, stickers, and GIFs\"]")
    e19.click()
    e20 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="👍")
    e20.click()
    e21 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"Send\"]")
    e21.click()
    assert 'Message' in driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.EditText').text
#def test_Reply():
    #e22 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.View[6]")
    #e22.click()
    #e23 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]")
    #e23.click()
    #e24 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.EditText")
    #e24.send_keys('Test Reply')
    #e25 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"Send\"]")
    #e25.click()
#def test_Copy():
    #e26 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.View[6]")
    #e26.click()
    #e27 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]")
    #e27.click()
def test_Forward():
    e28 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.View[6]")
    e28.click()
    assert 'Forward' in driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.TextView').text
    e29 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.TextView")
    e29.click()
    e30 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageButton[@content-desc=\"Search\"]/android.widget.ImageView")
    e30.click()
    e31 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView")
    e31.send_keys('Juan Fernando')
    e32 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View[1]")
    e32.click()
    e33 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"Send\"]")
    e33.click()
#def test_Pin():
    #e34 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.View[6]")
    #e34.click()
    #e35 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[4]")
    #e35.click()
    #e36 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.TextView[2]")
    #e36.click()
def test_Delete():
    e37 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.view.View[6]")
    e37.click()
    e38 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[5]")
    e38.click()
    e39 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.TextView[2]")
    e39.click()
def test_SendGambar():
    e40 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc=\"Attach media\"]")
    e40.click()
    e41 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.CheckBox")
    e41.click()
    e42 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.Button/android.widget.ImageView")
    e42.click()
def test_SendConctact():
    e43 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc=\"Attach media\"]")
    e43.click()
    e44 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.View[3]/android.widget.FrameLayout[4]")
    e44.click()
    e45 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout")
    e45.click()
    e46 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView")
    e46.click()
def test_SendFile():
    e47 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc=\"Attach media\"]")
    e47.click()
    e48 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.View[3]/android.widget.FrameLayout[2]")
    e48.click()
    e49 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[4]")
    e49.click()
    e50 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.Button/android.widget.ImageView")
    e50.click()
def test_SendLocation():
    e51 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc=\"Attach media\"]")
    e51.click()
    e52 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.View[3]/android.widget.FrameLayout[3]")
    e52.click()
    time.sleep(3)
    e53 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.View/android.widget.FrameLayout[2]")
    e53.click()
def test_SendMusic():
    e54 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc=\"Attach media\"]")
    e54.click()
    e55 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.View[3]/android.widget.FrameLayout[5]")
    e55.click()
    e56 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout")
    e56.click()
    e57 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.Button/android.widget.ImageView")
    e57.click()
def test_Call():
    e58 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageButton[@content-desc=\"Call\"]/android.widget.ImageView")
    e58.click()
    time.sleep(1)
def test_VideoCall():
    e59 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageButton[@content-desc=\"More options\"]/android.widget.ImageView")
    e59.click()
    e60 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[3]")
    e60.click()
    time.sleep(1)
def test_Search():
    e61 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageButton[@content-desc=\"More options\"]/android.widget.ImageView")
    e61.click()
    e62 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[4]")
    e62.click()
    e63 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
    e63.click()
    e63.send_keys('Halo Test 1')
    e64 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageView[@content-desc=\"Go back\"]")
    e64.click()
def test_ClearHistory():
    e65 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageButton[@content-desc=\"More options\"]/android.widget.ImageView")
    e65.click()
    e66 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[5]")
    e66.click()
    e67 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView[2]")
    e67.click()
    time.sleep(1)
def test_Undo():
    e68 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout[4]/android.widget.LinearLayout")
    e68.click()
    e69 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Go back")
    e69.click()
#def test_DeleteChat():
    #driver.find_element(by=AppiumBy.XPATH, value="//android.widget.ImageButton[@content-desc=\"More options\"]/android.widget.ImageView")
    #.click()
    #driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[7]")
    #.click()
    #driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView[2]")
    #.click()
def test_NewGroup():
    e70 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Open navigation menu")
    e70.click()
    e71 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.View/android.widget.TextView[1]")
    e71.click()
    e72 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.view.View/android.widget.ScrollView/android.view.View/android.widget.EditText")
    e72.click()
    e72.send_keys("Juan Fernando")
    assert 'New Group' in driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.TextView[1]').text
    e73 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.view.View/android.view.View/android.widget.FrameLayout")
    e73.click()
    e74 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next")
    e74.click()
    e75 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Choose photo")
    e75.click()
    e76 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.view.View/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View")
    e76.click()
    e77 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Send")
    e77.click()
    e78 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.EditText")
    e78.click()
    e78.send_keys("Group 1")
    e79 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@content-desc=\"Done\"]/android.widget.ImageView")
    e79.click()
    time.sleep(1)
    assert 'Profile picture' in driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Profile picture"]').text
    e80 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.EditText")
    e80.click()
    e80.send_keys("Halo Guys")
    e81 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Send")
    e81.click()
    

























