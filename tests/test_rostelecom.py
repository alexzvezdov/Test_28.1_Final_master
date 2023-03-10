import pytest

from pages.auth_page import AuthPage
from pages.config_page import RegPage

# Тест-кейс EXP-001
# Корректное отображение "Главной страницы авторизации"
def test_head_page(web_browser):
    page = AuthPage(web_browser)
    phone_tab_class = page.phone_tab.get_attribute("class")
    assert page.auth_title.get_text() == "Авторизация"
    assert phone_tab_class == "rt-tab rt-tab--small rt-tab--active"
    assert page.phone.is_clickable()
    assert page.password.is_clickable()
    assert page.btn_login.is_clickable()
    assert page.registration_link.is_clickable()
    assert page.logo_lk.get_text() == "Личный кабинет"


# Тест-кейс EXP-002 (Bug: ROS-001)
# Проверка расположения элементов в левом и правом блоке страницы
@pytest.mark.xfail(reason="Расположение элементов на странице не соответствует Требованиям")
def test_elements_of_auth(web_browser):
    page = AuthPage(web_browser)
    assert page.auth_form.find(timeout=20)
    assert page.lk_form.find(timeout=20)


# Тест-кейс EXP-003(Bug: ROS-002)
# Проверка названия "Номер"
@pytest.mark.xfail(reason="Название 'Номер' не соответствует Требованиям")
def test_phone_tab(web_browser):
    page = AuthPage(web_browser)
    assert page.phone_tab.get_text() == "Номер"


# Тест-кейс EXP-004(Bug: ROS-003)
# Проверка названия кнопки "Продолжить" в форме "Регистрация"
@pytest.mark.xfail(reason="Кнопка должна иметь название 'Продолжить'")
def test_registration_page_use_continue_button(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    assert reg_page.name_field_text.get_text() == "Имя"
    assert reg_page.last_name_field_text.get_text() == "Фамилия"
    assert reg_page.region_field_text.get_text() == "Регион"
    assert reg_page.email_or_mobile_phone_field_text.get_text() == "E-mail или мобильный телефон"
    assert reg_page.password_field_text.get_text() == "Пароль"
    assert reg_page.password_confirmation_field_text.get_text() == "Подтверждение пароля"
    assert reg_page.continue_button.get_text() == "Продолжить"


# Тест-кейс EXP-005
# Регистрация пользователя с пустым полем "Имя", появления текста с подсказкой об ошибке
def test_registration_page_with_empty_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('')
    reg_page.last_name_field.send_keys("Звездов")
    reg_page.email_or_mobile_phone_field.send_keys("sten@mail.ru")
    reg_page.password_field.send_keys("Sten2022")
    reg_page.password_confirmation_field.send_keys("Sten2022")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс EXP-006
# Регистрация пользователя с пустым полем "Фамилия", появления текста с подсказкой об ошибке
def test_registration_page_with_empty_last_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Алекс")
    reg_page.last_name_field.send_keys('')
    reg_page.email_or_mobile_phone_field.send_keys("sten@mail.ru")
    reg_page.password_field.send_keys("Sten2022")
    reg_page.password_confirmation_field.send_keys("Sten2022")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс EXP-007
# Регистрация пользователя с пустым полем "E-mail или мобильный телефон", появления текста с подсказкой об ошибке
def test_registration_page_with_empty_email_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Алекс")
    reg_page.last_name_field.send_keys("Звездов")
    reg_page.email_or_mobile_phone_field.send_keys("")
    reg_page.password_field.send_keys("Sten2022")
    reg_page.password_confirmation_field.send_keys("Sten2022")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.message_empty_email_field.get_text() == "Введите телефон в формате +7ХХХХХХХХХХ или" \
                                                            " +375XXXXXXXXX, или email в формате example@email.ru"
# Тест-кейс EXP-008
# Регистрация пользователя с некорректным вводом электронной почты в поле "E-mail или мобильный телефон", появления текста с подсказкой об ошибке
def test_registration_page_with_incorrect_email(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Алекс")
    reg_page.last_name_field.send_keys("Звездов")
    reg_page.email_or_mobile_phone_field.send_keys("stenmail.ru")
    reg_page.password_field.send_keys("Sten2022")
    reg_page.password_confirmation_field.send_keys("Sten2022")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.message_enter_with_incorrect_email.get_text() == "Введите телефон в формате +7ХХХХХХХХХХ или" \
                                                                     " +375XXXXXXXXX, или email в формате example@email.ru"


# Тест-кейс EXP-009
# Регистрация пользователя со значением в поле "Имя" меньше 2 символов, появление текста с подсказкой об ошибке
def test_registration_with_an_incorrect_value_in_the_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('А')
    reg_page.last_name_field.send_keys("Звездов")
    reg_page.email_or_mobile_phone_field.send_keys("sten@mail.ru")
    reg_page.password_field.send_keys("Sten2022")
    reg_page.password_confirmation_field.send_keys("Sten2022")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс EXP-010
# Регистрация пользователя со значением в поле "Имя" превышающим 30 символов, появление текста с подсказкой об ошибке
def test_registration_with_an_incorrect_value_in_the_name_field_more_30symbols(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('Афвыфрпрдлджлжджэджывапврапролфы')
    reg_page.last_name_field.send_keys("Звездов")
    reg_page.email_or_mobile_phone_field.send_keys("sten@mail.ru")
    reg_page.password_field.send_keys("Sten2022")
    reg_page.password_confirmation_field.send_keys("Sten2022")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс EXP-011
# Регистрация пользователя со значением в поле "Фамилия" меньше 2 символов, появление текста с подсказкой об ошибке
def test_registration_with_an_incorrect_value_in_the_last_name_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Алекс")
    reg_page.last_name_field.send_keys("З")
    reg_page.email_or_mobile_phone_field.send_keys("sten@mail.ru")
    reg_page.password_field.send_keys("Sten2022")
    reg_page.password_confirmation_field.send_keys("Sten2022")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс EXP-012
# Регистрация пользователя со значением в поле "Фамилия" превышающим 30 символов, появление текста с подсказкой об ошибке
def test_registration_with_an_incorrect_value_in_the_last_name_field_more_30symbols(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Алекс")
    reg_page.last_name_field.send_keys('Афвыфрпрдлджлжджэджывапврапролфы')
    reg_page.email_or_mobile_phone_field.send_keys("sten@mail.ru")
    reg_page.password_field.send_keys("Sten2022")
    reg_page.password_confirmation_field.send_keys("Sten2022")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс EXP-013
# Регистрация пользователя со значением в поле "Подтверждение пароля" значения отличного от значения введенного в поле «Пароль»
def test_registration_with_an_incorrect_value_in_the_Password_confirmation_field(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Алекс")
    reg_page.last_name_field.send_keys('Звездов')
    reg_page.email_or_mobile_phone_field.send_keys("sten@mail.ru")
    reg_page.password_field.send_keys("Sten2022")
    reg_page.password_confirmation_field.send_keys("Sten20")
    reg_page.continue_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Пароли не совпадают"


# Тест-кейс EXP-014
# Регистрация пользователя с уже зарегистрированной почтой, появление оповещения, что пользователь существует
def test_registration_already_registered_user(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Алекс")
    reg_page.last_name_field.send_keys("Звездов")
    reg_page.email_or_mobile_phone_field.send_keys("sten@mail.ru")
    reg_page.password_field.send_keys("Sten2022")
    reg_page.password_confirmation_field.send_keys("Sten2022")
    reg_page.continue_button.click()
    assert reg_page.notification_form.is_visible


# Тест-кейс EXP-015(Bug: ROS-004)
# Проверка значка "х" - закрыть всплывающее окно оповещения
@pytest.mark.xfail(reason="Должен быть значок закрыть 'х'")
def test_notification_form(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Алекс")
    reg_page.last_name_field.send_keys("Звездов")
    reg_page.email_or_mobile_phone_field.send_keys("sten@mail.ru")
    reg_page.password_field.send_keys("Sten2022")
    reg_page.password_confirmation_field.send_keys("Sten2022")
    reg_page.continue_button.click()
    assert reg_page.login_button.get_text() == 'Войти'
    assert reg_page.recover_password_button.get_text() == 'Восстановить пароль'
    assert reg_page.close_button.get_text() == 'x'


# Тест-кейс EXP-016
#  При регистрации пользователя введен пароль содержащий менее 8 символов, появление текста с подсказкой об ошибке
def test_incorrect_password_field_value_less_8symbols(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Алекс")
    reg_page.last_name_field.send_keys("Звездов")
    reg_page.email_or_mobile_phone_field.send_keys("sten@mail.ru")
    reg_page.password_field.send_keys("Sten20")
    reg_page.password_confirmation_field.send_keys("Sten20")
    reg_page.continue_button.click()
    assert reg_page.error_message_password.get_text() == "Длина пароля должна быть не менее 8 символов"


# Тест-кейс EXP-017
# При регистрации пользователя в поле "Фамилия" введено значение, содержащее недопустимые символы вместо кириллицы
def test_instead_of_cyrillic_invalid_characters(web_browser):
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Алекс")
    reg_page.last_name_field.send_keys("»:?*()_")
    reg_page.email_or_mobile_phone_field.send_keys("sten@mail.ru")
    reg_page.password_field.send_keys("Sten2022")
    reg_page.password_confirmation_field.send_keys("Sten2022*")
    reg_page.continue_button.click()
    assert reg_page.message_must_be_filled_in_cyrillic.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс EXP-018
# Вход по неправильному логину в форме "Авторизация" уже зарегистрированного пользователя, надпись "Забыл пароль" перекрашивается
@pytest.mark.xfail(reason="Неверный логин или пароль")
def test_authorization_user_with_an_invalid_login(web_browser):
    page = AuthPage(web_browser)
    page.login_tab.click()
    page.login.send_keys('Error')
    page.password.send_keys("Sten2022")
    page.btn_login.click()
    assert page.message_invalid_username_or_password.get_text() == "Неверный логин или текст с картинки"
    assert "rt-link--orange" in page.the_element_forgot_the_password.get_attribute('class')


# Тест-кейс EXP-019
# Вход по неправильному паролю в форме "Авторизация" уже зарегистрированного пользователя, надпись "Забыл пароль" перекрашивается
@pytest.mark.xfail(reason="Неверный логин или пароль")
def test_authorization_user_with_an_invalid_password(web_browser):
    page = AuthPage(web_browser)
    page.email.send_keys('Sten@mail.ru')
    page.password.send_keys("Error")
    page.btn_login.click()
    assert page.message_invalid_username_or_password.get_text() == "Неверный логин или текст с картинки"
    assert "rt-link--orange" in page.the_element_forgot_the_password.get_attribute('class')


# Тест-кейс EXP-020
# Тестирование аутентификации зарегистрированного пользователя по номеру телефона
def test_authorisation_valid_phone_number(web_browser):
    page = AuthPage(web_browser)
    page.phone.send_keys("+7916*******")
    page.password.send_keys("Sten2022")
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() \
           and '&client_id=account_b2c#/' in page.get_current_url()


# Тест-кейс EXP-021
# Тестирование аутентификации зарегистрированного пользователя по адресу электронной почты
def test_authorisation_valid_email(web_browser):
    page = AuthPage(web_browser)
    page.email.send_keys("sten@mail.ru")
    page.password.send_keys("Sten2022")
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() \
           and '&client_id=account_b2c#/' in page.get_current_url()

# Тест-кейс EXP-022
# После нажатия на кнопку «Почта» на странице «Восстановление пароля», появляется окно ввода электронной почты
def test_email_tab_when_password_recovery(web_browser):
    page = AuthPage(web_browser)
    page.fogot_the_password.click()
    page.phone.send_keys("+7916********")
    page.btn_reset.click()
    assert "rt-tab rt-tab--small rt-tab--active" in page.email_tab.get_attribute("class")
