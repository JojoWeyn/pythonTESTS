
# Ответы на вопросы по Selenium и PyTest

## 1. Каковы основные возможности Selenium при использовании Python, и как они помогают в автоматизации тестирования различных аспектов веб-приложений?

**Selenium** — это популярная библиотека для автоматизации браузеров, которая предоставляет возможности для взаимодействия с веб-приложениями и их тестирования. С помощью Selenium можно:
- **Открывать веб-страницы** и взаимодействовать с элементами, такими как кнопки, поля ввода, выпадающие списки.
- **Использовать различные браузеры** (Chrome, Firefox, Safari, Edge).
- **Делать скриншоты** страницы и захватывать её состояние.
- **Тестировать функциональность** веб-страниц, включая формы, элементы интерфейса, а также проверку динамического контента.
- **Запускать тесты на различных платформах**.

Пример использования Selenium для автоматического тестирования входа в приложение:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://example.com/login")
driver.find_element(By.ID, "username").send_keys("user")
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.ID, "login").click()
assert "Welcome" in driver.page_source
driver.quit()
```

---

## 2. Как управлять различными браузерами с помощью Selenium на Python, и какие методы навигации доступны для перемещения между страницами?

Selenium предоставляет драйверы для различных браузеров. Чтобы управлять браузерами, нужно создать экземпляр соответствующего драйвера:

- **Chrome**: `webdriver.Chrome()`
- **Firefox**: `webdriver.Firefox()`
- **Edge**: `webdriver.Edge()`
- **Safari**: `webdriver.Safari()`

Методы навигации:
- **get(url)**: Открывает веб-страницу по указанному URL.
- **back()**: Возвращается на предыдущую страницу.
- **forward()**: Переходит на следующую страницу.
- **refresh()**: Перезагружает текущую страницу.
- **get_current_url()**: Получает URL текущей страницы.

Пример навигации:
```python
driver = webdriver.Chrome()
driver.get("http://example.com")
driver.get("http://example.com/next")
driver.back()  # Возвращение на предыдущую страницу
driver.forward()  # Переход на следующую
driver.quit()
```

---

## 3. Опишите процесс взаимодействия с элементами веб-страницы через Selenium на Python. Каковы основные методы для выполнения этих действий?

Selenium позволяет взаимодействовать с элементами страницы, используя различные локаторы (ID, name, XPath, CSS-селекторы). Основные методы:
- **find_element**: Находит один элемент.
- **find_elements**: Находит все элементы, соответствующие заданному локатору.
- **send_keys**: Вводит текст в поле ввода.
- **click**: Кликает по элементу.
- **clear**: Очищает поле ввода.
- **get_attribute**: Получает значение атрибута элемента.
- **get_text**: Получает текст элемента.

Пример взаимодействия:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://example.com")
driver.find_element(By.ID, "username").send_keys("user")
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.ID, "login").click()
assert "Welcome" in driver.page_source
driver.quit()
```

---

## 4. Что такое HTML-документ, какова его структура, и какие основные элементы составляют веб-страницу?

**HTML** (HyperText Markup Language) — это язык разметки, который используется для создания и структурирования веб-страниц. HTML-документ состоит из нескольких ключевых элементов:
- **`<html>`**: Корневой элемент документа.
- **`<head>`**: Содержит метаданные, такие как title, ссылки на стили и скрипты.
- **`<body>`**: Содержит основной контент страницы, включая заголовки, параграфы, изображения и ссылки.
- **`<div>`**: Контейнер, используемый для группировки элементов.
- **`<p>`**: Параграф текста.
- **`<a>`**: Гиперссылка.
- **`<img>`**: Изображение.
- **`<form>`**: Форма для ввода данных.

Пример структуры HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Example Page</title>
</head>
<body>
    <h1>Welcome to Example</h1>
    <p>This is a paragraph of text.</p>
    <a href="http://example.com">Click here</a>
</body>
</html>
```

---

## 5. Опишите, что такое XPath, как он работает для поиска элементов на веб-странице.

**XPath** — это язык запросов, который используется для навигации по элементам XML-документа (в том числе HTML). Он позволяет находить элементы на веб-странице, используя пути и условия. XPath выражения могут быть абсолютными (начинаются с корня документа) или относительными (начинаются с текущего узла).

Пример XPath выражений:
- `/html/body/div`: Абсолютный путь, начинающийся с корня.
- `//div[@id='main']`: Относительный путь, ищущий `div` с атрибутом `id="main"`.

Пример поиска элемента с использованием XPath:

```python
driver = webdriver.Chrome()
driver.get("http://example.com")
element = driver.find_element(By.XPATH, "//div[@id='main']")
print(element.text)
driver.quit()
```

---

## 6. Каковы основные отличия между использованием XPath и CSS-селекторов для поиска элементов. В каких ситуациях предпочтительнее использовать один метод над другим?

**XPath** и **CSS-селекторы** — это два распространенных метода для поиска элементов на веб-странице. Вот основные отличия:
- **XPath** предоставляет более гибкие возможности для поиска, поддерживает поиск по тексту, атрибутам и позициям элементов. Также позволяет использовать более сложные выражения, например, искать элементы по их содержимому или порядковому номеру.
- **CSS-селекторы** более быстрые и предпочтительны для простых случаев поиска, таких как поиск элементов по классу или ID. Однако они не поддерживают такую гибкость, как XPath, и не могут работать с текстом или иерархией элементов так, как XPath.

Пример:
```python
# XPath
driver.find_element(By.XPATH, "//div[@id='main']")

# CSS-селектор
driver.find_element(By.CSS_SELECTOR, "div#main")
```

Предпочтительно использовать CSS-селекторы для простых случаев, а XPath — когда требуется более сложный поиск.

---

## 7. Какие методы поиска элементов предоставляет Selenium, и каковы их особенности и области применения в автоматизации тестирования веб-приложений?

Selenium предоставляет несколько методов для поиска элементов:
- **find_element**: Ищет первый элемент, соответствующий локатору.
- **find_elements**: Ищет все элементы, соответствующие локатору.

Локаторы, которые можно использовать с этими методами:
- **By.ID**: Ищет элемент по ID.
- **By.NAME**: Ищет элемент по имени.
- **By.CLASS_NAME**: Ищет элемент по имени класса.
- **By.TAG_NAME**: Ищет элемент по тегу.
- **By.LINK_TEXT**: Ищет ссылку по точному тексту.
- **By.PARTIAL_LINK_TEXT**: Ищет ссылку по частичному тексту.
- **By.XPATH**: Ищет элемент по XPath.
- **By.CSS_SELECTOR**: Ищет элемент по CSS-селектору.

Пример использования:
```python
# Поиск по ID
element = driver.find_element(By.ID, "login-button")
```

---

## 8. Что такое CSS-селекторы, как они функционируют, и какие основные типы селекторов существуют, включая их особенности и применение для поиска элементов на веб-странице?

**CSS-селекторы** — это способ выбора элементов на веб-странице на основе их стилей и структуры. CSS-селекторы используются для поиска элементов по их атрибутам, тегам, классам, идентификаторам и отношениям между элементами.

Основные типы селекторов:
- **ID-селекторы**: Используются для поиска по уникальному идентификатору элемента. Пример: `#myId`.
- **Класс-селекторы**: Используются для поиска по имени класса элемента. Пример: `.myClass`.
- **Тег-селекторы**: Используются для поиска элементов по тегу. Пример: `div`.
- **Комбинированные селекторы**: Используются для поиска по комбинации нескольких атрибутов. Пример: `div.myClass`.

Пример использования:
```python
# Поиск по ID
driver.find_element(By.CSS_SELECTOR, "#myId")
# Поиск по классу
driver.find_element(By.CSS_SELECTOR, ".myClass")
```
CSS-селекторы являются быстрыми и эффективными, но они менее гибкие, чем XPath.

---

## 9. Опишите процесс создания сложных CSS-селекторов для точного выбора элементов на странице.

Для создания сложных **CSS-селекторов** можно комбинировать различные атрибуты и структуры элементов. Вот несколько примеров:
- **Поиск по тегу и классу**: `div.myClass` — выбирает все `div` с классом `myClass`.
- **Поиск по атрибутам**: `input[type='text']` — выбирает все элементы `input` с атрибутом `type="text"`.
- **Поиск по вложенности**: `div > p` — выбирает все элементы `p`, которые являются прямыми дочерними элементами `div`.
- **Поиск по порядковому номеру**: `div:nth-child(2)` — выбирает второй элемент `div` в родительском контейнере.

Пример сложного селектора:
```python
driver.find_element(By.CSS_SELECTOR, "div.myClass > p:nth-child(2)")
```

---

## 10. Как обрабатывать окна подтверждений, предупреждения и другие диалоговые окна в Selenium на Python? Опишите методы взаимодействия с такими окнами.

Selenium позволяет взаимодействовать с модальными окнами (диалогами) с помощью интерфейса **Alert**. Методы работы с окнами подтверждений и предупреждений:
- **accept()**: Принять окно (нажать "OK" или "Accept").
- **dismiss()**: Отклонить окно (нажать "Cancel" или "Dismiss").
- **send_keys()**: Ввести текст в окно (например, в поле для ввода).
- **get_text()**: Получить текст из окна.

Пример работы с alert:
```python
from selenium.webdriver.common.alert import Alert

# Перехват окна подтверждения
alert = Alert(driver)
alert.accept()  # Принять
```

---


## 11. Загрузка файлов

Настройка пути для загрузки файлов:
```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": "/path/to/download"
})
```

---

## 12. Управление окнами и вкладками

### 1. Получение дескрипторов окон (window handles)
Каждое окно или вкладка в браузере имеет уникальный дескриптор (идентификатор), который можно получить с помощью:

```python
window_handles = driver.window_handles
```

- `driver.current_window_handle` — дескриптор текущего окна.
- `driver.window_handles` — список всех доступных дескрипторов окон.

---

### 2. Переключение между окнами
Чтобы переключиться на другое окно или вкладку, используйте метод `switch_to.window` с указанием дескриптора окна:

```python
driver.switch_to.window(window_handles[index])
```

#### Пример:
```python
from selenium import webdriver

driver = webdriver.Chrome()

# Открытие первой вкладки
driver.get("https://example.com")

# Открытие новой вкладки
driver.execute_script("window.open('https://google.com', '_blank');")

# Получение всех дескрипторов окон
window_handles = driver.window_handles

# Переключение на вторую вкладку
driver.switch_to.window(window_handles[1])

print("Текущий URL:", driver.current_url)
```

---

### 3. Закрытие ненужного окна
Чтобы закрыть текущее окно, используйте метод:

```python
driver.close()
```

После закрытия окна нужно переключиться на оставшееся окно, иначе Selenium потеряет контекст.

#### Пример:
```python
# Закрытие текущего окна
driver.close()

# Переключение на другое окно (например, первое)
driver.switch_to.window(window_handles[0])
```

---

### 4. Обработка окон в цикле
Если необходимо закрыть определённые окна или обработать каждую вкладку, можно использовать цикл:

```python
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    print("Текущий URL:", driver.current_url)

    if "example.com" not in driver.current_url:
        driver.close()
```

---

### 5. Ожидание появления новой вкладки
Если новая вкладка открывается не мгновенно, рекомендуется использовать `WebDriverWait` для ожидания:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Дожидаемся появления новой вкладки
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

# Переключаемся на новую вкладку
driver.switch_to.window(driver.window_handles[-1])
```

---

### 6. Возвращение к основной вкладке
Чтобы вернуться к основной (первой) вкладке:

```python
main_window = driver.window_handles[0]
driver.switch_to.window(main_window)
```

---

## Полный пример: работа с несколькими окнами
```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

# Открытие основной вкладки
driver.get("https://example.com")
main_window = driver.current_window_handle

# Открытие новой вкладки
driver.execute_script("window.open('https://google.com', '_blank');")

# Ожидание появления новой вкладки
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

# Переключение на новую вкладку
for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        break

print("Текущий URL:", driver.current_url)

# Закрытие новой вкладки
driver.close()

# Возвращение к основной вкладке
driver.switch_to.window(main_window)

print("Текущий URL после возвращения:", driver.current_url)

driver.quit()
```

---

## Часто используемые методы для работы с окнами/вкладками

- **`driver.window_handles`**: возвращает список всех открытых окон.
- **`driver.current_window_handle`**: возвращает дескриптор текущего окна.
- **`driver.switch_to.window(handle)`**: переключается на окно с указанным дескриптором.
- **`driver.close()`**: закрывает текущее окно.
- **`driver.quit()`**: закрывает все окна браузера.

Эти методы позволяют гибко управлять окнами и вкладками при тестировании сложных веб-приложений.



---

## 13. Поведение вкладок

# Отличия в поведении браузера при открытии вкладок через JavaScript и Selenium

## 1. Открытие вкладок через JavaScript (`window.open()`):
- Вкладка открывается в контексте текущей веб-страницы.
- Управление вкладкой возможно только через JavaScript на открывшей вкладку странице, но доступ к содержимому может быть ограничен политикой Same-Origin Policy.
- У Selenium нужно вручную переключаться на новую вкладку, используя дескрипторы окон.
- Если открыть множество вкладок, управление ими вручную становится сложным.

## 2. Открытие вкладок через Selenium:
- Открытие вкладки осуществляется через выполнение JavaScript (как в примерах выше) или через настройку браузера.
- Selenium автоматически отслеживает все открытые вкладки/окна и предоставляет уникальные идентификаторы (`window_handles`) для переключения между ними.
- При работе с Selenium вкладки и окна контролируются как независимые элементы браузера, что дает полное управление вкладками независимо от политики безопасности.

## 3. Контекст управления:
- При открытии через JavaScript новый контекст (DOM, история браузера) становится доступен только из той же страницы.
- Selenium позволяет переключаться между вкладками и окнами, что обеспечивает полный доступ к любому их содержимому, включая возможность выполнения действий.

## 4. Закрытие вкладок:
- Вкладки, открытые через JavaScript, можно закрыть программно, если у текущей страницы есть к ним доступ.
- Selenium позволяет закрывать любую вкладку или окно, даже если оно было открыто вручную пользователем, используя `driver.close()`.

## Когда использовать один подход вместо другого:
- **JavaScript**: Если требуется лишь тестировать поведение вкладок внутри одной страницы и доступ к DOM нового окна не нужен.
- **Selenium**: Для тестирования поведения браузера, переключения между вкладками и окон или работы с контентом, находящимся за пределами текущего домена.



---

## 14. Закрытие браузеров
# Как правильно закрывать браузеры и вкладки в автоматизированных тестах

Закрытие браузеров и вкладок в тестах необходимо для предотвращения утечек ресурсов и ошибок в последующих тестах. Рассмотрим основные практики:

## 1. Закрытие текущей вкладки
Для закрытия текущей вкладки используется метод:

```python
driver.close()
```

После закрытия вкладки нужно переключиться на другую активную вкладку, чтобы продолжить работу:

```python
# Закрываем текущую вкладку
driver.close()

# Переключаемся на оставшуюся вкладку (например, первую)
driver.switch_to.window(driver.window_handles[0])
```

---

## 2. Закрытие всех вкладок и завершение работы браузера
Для полного завершения работы браузера, включая закрытие всех вкладок, используется метод:

```python
driver.quit()
```

Этот метод освобождает все системные ресурсы, связанные с браузером.

---

## 3. Использование `try-finally` для гарантированного закрытия
Чтобы гарантировать закрытие браузера даже при возникновении ошибок, рекомендуется использовать блок `try-finally`:

```python
from selenium import webdriver

try:
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    # Ваши тестовые действия
finally:
    driver.quit()
```

---

## 4. Использование фикстур в тестовых фреймворках
При использовании фреймворков, таких как `pytest`, можно применять фикстуры для автоматического управления жизненным циклом браузера:

```python
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Пример теста
def test_example(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
```

---

## 5. Закрытие неиспользуемых вкладок
Если открыто много вкладок, можно закрыть все ненужные:

```python
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "example.com" not in driver.current_url:
        driver.close()

# Переключение на оставшуюся вкладку
driver.switch_to.window(driver.window_handles[0])
```

---

## 6. Устранение ошибок "No such window"
Если попытаться выполнить действия в уже закрытом окне, возникает ошибка `No such window`. Для её предотвращения проверяйте количество оставшихся вкладок:

```python
if len(driver.window_handles) > 0:
    driver.switch_to.window(driver.window_handles[0])
```

---

## Рекомендации:
- Всегда завершайте работу браузера с помощью `driver.quit()` в конце теста.
- Используйте `try-finally` или фикстуры для автоматизации закрытия.
- Убедитесь, что все окна и вкладки закрыты перед запуском нового теста.



---

## 15. Проверка видимости элемента

- **Методы**:
  - `is_displayed()`: Возвращает `True`, если элемент видим.
  - `is_enabled()`: Проверяет, доступен ли элемент для взаимодействия.

---

## 16. Явные и неявные ожидания

- **Неявные ожидания**: Задают глобальное время ожидания для всех элементов:
  ```python
  driver.implicitly_wait(10)
  ```
- **Явные ожидания**: Используются для конкретных условий:
  ```python
  from selenium.webdriver.common.by import By
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC

  element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "element_id"))
  )
  ```

---

## 17. Когда использовать явные ожидания

- Используйте явные ожидания, если требуется ждать конкретное условие, например, видимость элемента или доступность для клика.
- Неявные ожидания лучше подходят для менее специфичных задержек.

---

## 18. Обработка задержек

- Используйте `WebDriverWait` с разными условиями из `expected_conditions`.
- Пример ожидания появления текста:
  ```python
  from selenium.webdriver.support import expected_conditions as EC

  WebDriverWait(driver, 10).until(
      EC.text_to_be_present_in_element((By.ID, "status"), "Complete")
  )
  ```

---

## 19. PyTest

PyTest — это мощный фреймворк для тестирования, который поддерживает параметризацию, фикстуры и плагины. Его основные преимущества:
- Простота синтаксиса.
- Автоматическое обнаружение тестов.
- Большое количество плагинов.

---

## 20. Преимущества PyTest

- Удобство написания тестов благодаря минималистичному синтаксису.
- Поддержка сложных тестовых сценариев.
- Расширяемость за счет плагинов.

---

## 21. Фикстуры в PyTest

Что такое фикстуры в PyTest, как они используются для настройки окружения тестов перед их выполнением?
Фикстуры в PyTest — это механизм, который позволяет настроить окружение тестов (например, подготовить данные, создать объекты, настроить соединение с базой данных, создать временные файлы и т. д.) и выполнить очистку после их завершения.

Пример использования фикстуры:
```python
import pytest

@pytest.fixture
def setup_database():
    # Код для настройки базы данных
    db = create_test_database()
    yield db  # Возвращаем объект базы данных
    # Очистка после выполнения тестов
    db.close()

def test_query_database(setup_database):
    db = setup_database
    result = db.query("SELECT * FROM table")
    assert len(result) > 0
```

---

## 22. Параметризация тестов

PyTest поддерживает проверку нескольких наборов данных:
```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (4, 5, 9),
    (10, 20, 30)
])
def test_addition(a, b, expected):
    assert a + b == expected
```

---

## 23. Отчеты PyTest

Для формирования отчетов можно использовать плагин pytest-html, который генерирует отчеты в формате HTML.

Пример команды для создания HTML-отчета:
```bash
pytest --html=report.html
```

---

## 24. CI/CD

CI/CD (Continuous Integration/Continuous Delivery) — это практика автоматизации процесса тестирования и деплоя. В CI/CD пайплайне тесты запускаются автоматически каждый раз, когда код изменяется.

Инструменты для CI/CD:
- Jenkins: Один из самых популярных инструментов для CI/CD.
- GitLab CI: Интегрированный инструмент для CI/CD, работающий с репозиториями на GitLab.
- Travis CI: Сервис для интеграции и доставки, популярный в open-source проектах.
- CircleCI: Облачный сервис для CI/CD.
- GitHub Actions: Встроенный инструмент для автоматизации процессов прямо в GitHub.

---

## 25. Тестирование API

Типичные сценарии тестирования API:
- Проверка доступности API (статус код 200).
- Проверка правильности структуры данных (JSON, XML).
- Проверка авторизации и аутентификации (например, тестирование токенов или сессий).
- Тестирование ошибок API (например, правильный статус код для несуществующих маршрутов).

Библиотеки для тестирования API:
- `requests`: Простая и мощная библиотека для HTTP-запросов.
- `pytest` с плагином pytest-requests.
- `requests-mock`: Для мокирования ответов от сервера.
- `httpx`: Асинхронная библиотека для HTTP-запросов

Для тестирования API часто используются:
- `Postman`: Для создания сценариев API.

---

## 26. Плагины для отчетов

Плагины для PyTest:
- `pytest-html`: Генерация HTML-отчетов.
- `pytest-junitxml`: Генерирует XML-отчеты в формате JUnit.

---

## 27. Анализ производительности

- **Библиотеки**: `locust`, `JMeter`.
- **Применение**: Нагрузка на веб-сервисы, тестирование отказоустойчивости.

Пример команды для запуска locust:
```bash
locust -f file.py --host=http://example.com
```

Пример файла locust.py
```python
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def read_root(self):
        self.client.get("/")

    @task
    def create_user(self):
        user_data = {
            "index": 1,
            "name": "Test User",
            "role": "admin"
        }
        self.client.post("/user", json=user_data)

    @task
    def get_users(self):
        self.client.get("/user")

    @task
    def get_user(self):
        self.client.get("/user/1")

    @task
    def delete_user(self):
        self.client.delete("/user/1")
```
---

## 28. Page Object Model
Page Object Model (POM) — это шаблон проектирования для автоматизированных тестов, при котором каждый веб-страница представляется как отдельный объект (класс), инкапсулирующий все взаимодействия с ней.
- **Преимущества**:
  - Уменьшение дублирования кода.
  - Улучшение читаемости и поддерживаемости тестов.
  - Упрощение изменений в тестах при изменениях в UI.
  - Централизованное управление элементами страниц.
  - Легкость поддержки тестов.

---

## 29. Реализация Page Object Model

Пример:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = driver.find_element(By.NAME, 'username')
        self.password_field = driver.find_element(By.NAME, 'password')
        self.submit_button = driver.find_element(By.NAME, 'submit')

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.submit_button.click()

class TestLogin:
    def test_valid_login(self):
        driver = webdriver.Chrome()
        login_page = LoginPage(driver)
        login_page.login('user', 'password')
        assert "Welcome" in driver.page_source
        driver.quit()

```

---

## 30. Преимущества Page Object Model
**Преимущества:**
- Упрощение поддержки: Легко изменять тесты при изменении структуры страницы или элементов.
- Чистота кода: Разделение тестов и логики взаимодействия с веб-страницей.
- Переиспользуемость: Переиспользование кода для разных тестов и страниц.
- Удобство для тестировщиков: Меньше дублирования кода и меньше ошибок при обновлениях UI.
- Улучшение читаемости кода.
- Упрощение поддержки тестов.
- Разделение логики тестов и структуры страниц.
---

# Продолжение следует в следующем сообщении