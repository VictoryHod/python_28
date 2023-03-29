valid_email = "kusya040593@mail.ru"
valid_pass = "Asd12345!"

invalid_email = 'kusya@gmail.com'
invalid_pass = 'Zxc12345'

name = 'Виктория'
surname = 'Ходосевич'
region = 'Москва г'
email = 'kusya040593@mail.ru'
password = 'Asd12345!'

false_email = '123456'
false_mobile_max = '891178945236'
false_mobile_mini = '8911789452'
false_name_mini = 'А'
name_two_letters = "Он"
thirty_letters = 'Пыльпополюлетитскозьтопоткопыт'
thirty_one_letters = 'Пыльпополюлетит-скозьтопоткопыт'

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    #Заголовки названий элементов
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    ENTRY_VK = 'Войти'
    OK = 'Одноклассники'
    CHOICE_ACCOUNT = 'Вход'
    MM = 'Войти и разрешить'