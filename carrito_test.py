from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

def test_total_carrito_bug_482():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app_package = "com.mercamovil"
    options.app_activity = ".ui.SplashActivity"
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(5)
    try:
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "campo-usuario").send_keys("qa@mercamovil.test")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "campo-clave").send_keys("Demo123")
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "btn-ingresar").click()
        driver.execute_script("mobile: swipeGesture", {"left": 100, "top": 500, "width": 800, "height": 1200, "direction": "up", "percent": 0.75})
        driver.find_element(AppiumBy.ID, "Seleccionar Audífonos BT").click()
        driver.find_element(AppiumBy.ID, "Botón Agregar al carrito").click()
        driver.find_element(AppiumBy.ID, "Botón + (aumentar cantidad a 2)").click()
        assert driver.find_element(AppiumBy.ID, "Carrito").text == "$59.98"
    finally:
        driver.quit()
