# Проект автоматизации тестирования приложения для заказа самокатов
* Основа для написания автотестов — фреймворки pytest и selenium.
* Команда для запуска — pytest -v.
* Страницы описаны в pages/
* В data.py содержатся данные для тестового заказа, а также текста для проверки секции вопрос-ответ
* Собрать отчёт о тестировании - pytest tests\*test_name.py --alluredir=allure_results
* Посмотреть наглядно отчёт можно с помощью команды allure serve allure_results 
