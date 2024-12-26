[задачи](/tasks.md)
---
## 1. React. Понятие компонента. Вызов компонента и передача параметров. Механизм рендера. Варианты запуска.

### Понятие компонента
В React, **компонент** — это базовый строительный блок приложения. Он представляет собой часть пользовательского интерфейса, которую можно переиспользовать. Компоненты бывают двух типов:

- **Функциональные компоненты** — это обычные JavaScript-функции, которые принимают параметры (называемые props) и возвращают элементы React (JSX).
- **Классовые компоненты** — это классы, наследующие `React.Component`, которые имеют дополнительные возможности, например, работу с состоянием (state) и методами жизненного цикла.

Пример функционального компонента:
```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}!</h1>;
}
```

Пример вызова компонента:
```jsx
<Welcome name="John" />
```
Здесь мы передаем параметр `name` со значением "John" в компонент `Welcome` через props.

### Механизм рендера
React использует Virtual DOM — абстрактное представление реального DOM. Это позволяет минимизировать операции с реальным DOM, что делает React очень производительным. 

Алгоритм работы:
1. React создает виртуальное дерево DOM (Virtual DOM).
2. При изменениях React сравнивает новое дерево с предыдущим (diffing algorithm).
3. Реальный DOM обновляется только там, где есть изменения.

### Варианты запуска
1. **Create React App**: официальный инструмент для быстрого создания React-приложений.
   ```bash
   npx create-react-app my-app
   cd my-app
   npm start
   ```

---

## 2. React. Работа с props. Вложенные компоненты. Узлы JSX. Вывод списков. Работа с условиями.

### Работа с props
**Props** — это данные, которые передаются от родительского компонента к дочернему. Props являются неизменяемыми внутри компонента.

Пример передачи props:
```jsx
function Greeting(props) {
  return <p>Hello, {props.user}!</p>;
}

function App() {
  return <Greeting user="Alice" />;
}
```
Здесь `user` — это пропс, переданный в компонент `Greeting`.

### Вложенные компоненты
Компоненты можно вкладывать друг в друга для создания сложных интерфейсов.
```jsx
function Header() {
  return <h1>My App</h1>;
}

function App() {
  return (
    <div>
      <Header />
      <p>Welcome to my application!</p>
    </div>
  );
}
```

### Узлы JSX
**JSX** — это синтаксис, позволяющий писать HTML-подобный код внутри JavaScript. JSX преобразуется в вызовы `React.createElement`.

Пример JSX:
```jsx
const element = <div className="container">Hello, world!</div>;
```
Важно помнить:
1. В JSX используется camelCase для атрибутов (например, `className` вместо `class`).
2. Все теги должны быть закрыты.

### Вывод списков
Для отображения списков элементов используется метод `map`.
```jsx
const items = ["Apple", "Banana", "Cherry"];

function ItemList() {
  return (
    <ul>
      {items.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </ul>
  );
}
```
Каждый элемент должен иметь уникальный `key` для оптимизации.

### Работа с условиями
Условный рендеринг позволяет отображать элементы на основе логики.
```jsx
function Greeting(props) {
  if (props.isLoggedIn) {
    return <h1>Welcome back!</h1>;
  } else {
    return <h1>Please sign in.</h1>;
  }
}
```
Сокращенная форма с тернарным оператором:
```jsx
function Greeting(props) {
  return props.isLoggedIn ? <h1>Welcome back!</h1> : <h1>Please sign in.</h1>;
}
```

---

## 3. React. FC vs Class. Жизненный цикл компонента. Хуки и правила их вызова. useState, useEffect, useRef.

### Functional Component (FC) vs Class Component

**Функциональные компоненты**:
- Легче писать и тестировать.
- Используют хуки для работы с состоянием и жизненным циклом.

Пример:
```jsx
function MyComponent() {
  return <div>Hello, world!</div>;
}
```

**Классовые компоненты**:
- Обладают собственными методами жизненного цикла.
- Могут быть сложнее для понимания и поддержки.

Пример:
```jsx
class MyComponent extends React.Component {
  render() {
    return <div>Hello, world!</div>;
  }
}
```

### Жизненный цикл компонента
Жизненный цикл — это этапы, через которые проходит компонент:
1. **Монтирование**: компонент создается и добавляется в DOM.
   - `componentDidMount`
2. **Обновление**: компонент обновляется при изменении props или state.
   - `componentDidUpdate`
3. **Размонтирование**: компонент удаляется из DOM.
   - `componentWillUnmount`

Функциональные компоненты используют хуки вместо методов жизненного цикла:
- `useEffect` — выполняется при монтировании, обновлении и размонтировании.

### useState
Хук `useState` позволяет добавлять состояние в функциональные компоненты.
```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

### useEffect
Хук `useEffect` используется для выполнения побочных эффектов, таких как запросы к API или настройка подписок.
```jsx
useEffect(() => {
  console.log("Component mounted");

  return () => console.log("Component unmounted");
}, []); // Пустой массив означает, что эффект выполняется только при монтировании.
```

### useRef
`useRef` позволяет сохранять мутируемое значение, которое не вызывает перерендеринг.
```jsx
const inputRef = useRef();

function focusInput() {
  inputRef.current.focus();
}

<input ref={inputRef} />
```

Без useRef
```jsx
import React, { useState } from "react";
function Piska() {
  const [piska, setPiska] = useState([]);
  const [input, setInput] = useState("");
  const [filter, setFilter] = useState("");

  function add() {
    const number = Number(input);
    setPiska([...piska, number]);
    setInput("");
  }

  const filtredPiska = filter ? piska.slice(0, filter) : piska;
  return (
    <div>
      <ul>
        {filtredPiska.map((number) => (
          <li>{number}</li>
        ))}
      </ul>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="number"
      />
      <input
        type="text"
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
        placeholder="filter"
      />
      <button onClick={add}>+</button>
    </div>
  );
}

export default Piska;
```

с useRef
```jsx
import React, { useState, useRef } from "react";
function Piska() {
  const piskaRef = useRef([]);
  const [render, setRender] = useState(false);
  const [input, setInput] = useState("");
  const [filter, setFilter] = useState("");

  function add() {
    const number = Number(input);
    piskaRef.current.push(number);
    setRender(!render);

    setInput("");
  }

  const filtredPiska = filter
    ? piskaRef.current.slice(0, filter)
    : piskaRef.current;
  return (
    <div>
      <ul>
        {filtredPiska.map((number) => (
          <li>{number}</li>
        ))}
      </ul>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="number"
      />
      <input
        type="text"
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
        placeholder="filter"
      />
      <button onClick={add}>+</button>
    </div>
  );
}

export default Piska;

```
---

## 4. Другие хуки (useCallback, useContext, useReducer). Работа с контекстом в React.

### useCallback
Мемоизация функции для предотвращения ее создания при каждом рендере.
```jsx
const memoizedCallback = useCallback(() => {
  doSomething(a, b);
}, [a, b]);
```

### useContext
Хук `useContext` используется для доступа к значениям контекста.
```jsx
const MyContext = React.createContext();

function MyComponent() {
  const value = useContext(MyContext);
  return <div>{value}</div>;
}
```

### useReducer
`useReducer` — это альтернатива `useState`, подходящая для более сложной логики состояния.
```jsx
import React, { useReducer } from "react";

// Шаг 1: Определим редьюсер
const piskaReducer = (state, action) => {
  switch (action.type) {
    case "INCREMENT":
      return { piska: state.piska + 1 };
    case "DECREMENT":
      return { piska: state.piska > 0 ? state.piska - 1 : 0 };
    default:
      return state;
  }
};

function PiskaLogin() {
  // Шаг 2: Используем useReducer
  const [state, dispatch] = useReducer(piskaReducer, { piska: 0 });

  // Шаг 3: Диспатчинг действий
  const plus = () => dispatch({ type: "INCREMENT" });
  const minus = () => dispatch({ type: "DECREMENT" });

  return (
    <div>
      <p style={{ color: state.piska % 2 === 0 ? "green" : "red" }}>
        piska {state.piska}
      </p>
      <button onClick={minus}>-</button>
      <button onClick={plus}>+</button>
    </div>
  );
}

export default PiskaLogin;

```

без useReducer
```jsx
import React, { useState } from "react";
function PiskaLogin() {
  let [piska, setPiska] = useState(0);
  function plus() {
    setPiska(piska + 1);
  }

  function minus() {
    setPiska(piska > 0 ? piska - 1 : 0);
  }
  return (
    <div>
      <p style={{ color: piska % 2 == 0 ? "green" : "red" }}>piska {piska}</p>
      <button onClick={minus}>-</button>
      <button onClick={plus}>+</button>
    </div>
  );
}

export default PiskaLogin;

```
---
## 5. React. Управляемые и неуправляемые компоненты и контролы. Работа с событиями и вмешательство в их работу. 
### Управляемые компоненты
Управляемые компоненты — это компоненты, состояние которых полностью контролируется React. Значения этих компонентов хранятся в состоянии и обновляются с помощью событий (например, onChange). Когда пользователь взаимодействует с компонентом, React обновляет состояние компонента, а затем компонент рендерится заново с новыми данными.

Пример
```jsx
import React, { useState } from 'react';

function ControlledForm() {
  // Управление состоянием формы через React
  const [value, setValue] = useState('');

  // Обработчик изменения значения
  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return (
    <div>
      <label>
        Name:
        <input
          type="text"
          value={value} // Состояние управляет значением поля
          onChange={handleChange} // Обновление состояния при изменении
        />
      </label>
    </div>
  );
}

export default ControlledForm;
```
Объяснение:
- Состояние `value` управляет значением поля ввода.
- Событие `onChange` отслеживает изменения и обновляет состояние.
- Так как React контролирует это состояние, значение в поле ввода всегда синхронизировано с состоянием.

Преимущества управляемых компонентов:
- **Гибкость:** Полный контроль за состоянием и данными формы.
- **Преобразование данных:** Легко обрабатывать и валидировать данные при вводе.
- **Отслеживание состояния:** Поскольку значение компонента хранится в состоянии, React может отслеживать изменения и делать с ними что угодно (например, отправка данных формы).

Недостатки:
- Требует больше кода для обработки состояния и событий.
- Может быть избыточным для простых форм.


### Неуправляемые компоненты (Uncontrolled Components)
Неуправляемые компоненты — это компоненты, состояние которых не контролируется React. Вместо этого значениями управляет DOM, и React использует ссылки (ref), чтобы взаимодействовать с ними напрямую. Это похоже на традиционное поведение HTML-форм, где элементы управления (например, `<input>`) самостоятельно хранят своё значение.

```jsx
import React, { useRef } from 'react';

function UncontrolledForm() {
  // Ссылка для доступа к полю ввода
  const inputRef = useRef();

  // Обработчик отправки формы
  const handleSubmit = (event) => {
    event.preventDefault();
    alert('Value: ' + inputRef.current.value); // Получаем значение через ref
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input type="text" ref={inputRef} /> {/* Здесь нет контроля за значением */}
      </label>
      <button type="submit">Submit</button>
    </form>
  );
}

export default UncontrolledForm;
```

Объяснение:
- Мы используем хук `useRef` для создания ссылки на элемент `<input>`, чтобы затем получить его значение.
- При отправке формы мы получаем значение поля ввода через `inputRef.current.value`.
- Здесь React не контролирует состояние поля ввода — оно управляется непосредственно DOM.

Преимущества неуправляемых компонентов:
- **Меньше кода:** Легче и быстрее реализовать, особенно если нужно просто получить значение из формы.
- **Быстродействие:** Можно избежать дополнительных перерендеров, связанных с обновлением состояния.

Недостатки:
- **Меньше гибкости:** Без использования состояния трудно реализовать обработку или валидацию данных на лету.
- **Трудности с синхронизацией:** Без состояния трудно следить за состоянием формы или делать какие-либо изменения до отправки.

### Работа с событиями в React
В React события обрабатываются немного иначе, чем в обычном DOM. Вот ключевые моменты:
- **Обработчики событий:** В React события передаются как атрибуты в JSX (например, onClick, onChange и т. д.). События в React работают через систему виртуального DOM.
- **Синтетические события:** В React все события — это синтетические события, которые оборачивают нативные события браузера, чтобы обеспечить кросс-браузерную совместимость.
- **Предотвращение поведения по умолчанию:** В React для предотвращения стандартного поведения события (например, для submit или click), используем event.preventDefault().
```jsx
import React from 'react';

function ButtonClick() {
  // Обработчик события onClick
  const handleClick = (event) => {
    event.preventDefault(); // Предотвращаем стандартное поведение (например, отправку формы)
    console.log('Button was clicked!');
  };

  return <button onClick={handleClick}>Click me</button>;
}

export default ButtonClick;
```

### Вмешательство в работу событий
Иногда нужно вмешиваться в стандартное поведение событий. Например:

- **Предотвращение действия по умолчанию:** Используем event.preventDefault(), чтобы отменить стандартные действия (например, отправку формы).
- **Остановка распространения события:** Используем event.stopPropagation(), чтобы событие не "путешествовало" дальше по DOM-дереву (например, не срабатывал обработчик на родительском элементе).

```jsx
import React from 'react';

function StopEventPropagation() {
  const handleParentClick = () => {
    alert('Parent clicked');
  };

  const handleChildClick = (event) => {
    event.stopPropagation(); // Останавливаем распространение события
    alert('Child clicked');
  };

  return (
    <div onClick={handleParentClick}>
      <button onClick={handleChildClick}>Click me</button>
    </div>
  );
}

export default StopEventPropagation;
```

- **Управляемые компоненты** — это более "реактивный" подход, при котором React полностью управляет состоянием. Это делает код более предсказуемым, но может требовать дополнительных усилий.
- Неуправляемые компоненты подходят для случаев, когда вам не нужно вмешательство в данные формы на лету, и вы просто хотите получить значения в какой-то момент времени.
- Взаимодействие с событиями в React немного отличается от стандартного DOM, и важно помнить о методах предотвращения стандартного поведения и остановки распространения событий, чтобы гибко управлять поведением приложений.
---

## 8. Библиотеки готовых компонентов. Примеры актуальных библиотек. Установка и подключение. Особенности отдельных компонентов библиотеки (работа с датами, таблицами и другие примеры «продвинутых» компонентов). CSS-фреймворки в разных стилях.

**Популярные библиотеки компонентов для React**
- Material-UI (MUI)
- Ant Design
- React Bootstrap
- Chakra UI
- Semantic UI React
- BlueprintJS

**CSS-фреймворки**
- Bootstrap
- Tailwind CSS


Использование готовых библиотек компонентов в React позволяет значительно ускорить процесс разработки и обеспечивает согласованный и современный дизайн. Такие библиотеки, как Material-UI, Ant Design, Chakra UI, React Bootstrap и другие, предлагают множество компонентов для работы с формами, таблицами, датами и прочими элементами интерфейса. Каждая из них имеет свои особенности, и выбор зависит от ваших предпочтений и особенностей проекта.


## 9,

**SPA (Single Page Application)** — это тип веб-приложения или сайта, который работает в рамках одной HTML-страницы. В отличие от традиционных многоконтентных сайтов, где при каждом переходе между страницами браузер загружает новую HTML-страницу с сервера, в SPA приложение все необходимые данные и компоненты загружаются только один раз при начальной загрузке страницы, а затем динамически обновляются по мере взаимодействия пользователя с приложением.

Когда пользователь переходит по ссылке или выполняет какие-либо действия, например, отправляет форму или нажимает на кнопки, приложение не загружает новую страницу, а меняет только нужную часть интерфейса. Это позволяет добиться более быстрого отклика и плавного взаимодействия с пользователем.

- BrowserRouter: Использует HTML5 history.pushState для управления маршрутом и обновления URL. Это самый распространенный вариант маршрутизации.
- HashRouter: Использует хеши в URL (например, /#/about), что полезно в случае, когда сервер не поддерживает историю браузера (например, на старых веб-серверах или при отсутствии серверной настройки).
- MemoryRouter: Управляет состоянием маршрута в памяти, а не в URL. Используется в тестах или в случае, когда не нужно синхронизировать URL с состоянием маршрута.

### Вложенные маршруты (Nested Routes)
React Router поддерживает вложенные маршруты, которые позволяют создавать компоненты, которые отображаются в зависимости от дочерних маршрутов.
```jsx
import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

function Dashboard() {
  return (
    <div>
      <h2>Dashboard</h2>
      <nav>
        <Link to="profile">Profile</Link> | <Link to="settings">Settings</Link>
      </nav>
      <Routes>
        <Route path="profile" element={<h3>Profile Page</h3>} />
        <Route path="settings" element={<h3>Settings Page</h3>} />
      </Routes>
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link> | <Link to="/dashboard">Dashboard</Link>
      </nav>
      <Routes>
        <Route path="/" element={<h2>Home Page</h2>} />
        <Route path="/dashboard/*" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

## 10
**Программный переход на нужный роут**
Для программного перехода между маршрутам используется хук useNavigate. Это позволяет вам менять маршрут программно, без использования компонента `<Link />`.

```jsx
import "./styles.css";
import { useNavigate, useLocation } from "react-router-dom";

function Layout({ children }) {
  const navigate = useNavigate();
  const location = useLocation();

  const handleNavigation = () => {
    if (location.pathname === "/") {
      navigate("/1");
    } else {
      navigate("/");
    }
  };

  return (
    <div>
      <header className="header">
        <div>
          <p>Piska Test</p>
          <nav>
            <a onClick={handleNavigation}>
              {location.pathname === "/login" ? "Go To Home" : "Go To Login"}
            </a>
          </nav>
        </div>
      </header>
      <main className="main">{children}</main>
      <footer>
        <div className="footer">
          <p>piska piska piska</p>
        </div>
      </footer>
    </div>
  );
}

export default Layout;
```

```jsx
import "./styles.css";
import Layout from "./Layout";
import Piska from "./Piska";
import PiskaLogin from "./PiskaLogin";
import Three from "./Three";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Piska />} />
          <Route path="/1" element={<PiskaLogin />} />
          <Route path="/3" element={<Three name="Piska props" />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
```


## 11

В React для выполнения сетевых запросов и работы с данными, полученными от серверов, можно использовать несколько вариантов. Наиболее популярными инструментами для выполнения запросов являются:

- Fetch API
- Axios (популярная библиотека для работы с HTTP запросами)
- GraphQL (если используется GraphQL API, можно использовать библиотеки, такие как Apollo Client)

### Fetch
Get
```jsx
useEffect(() => {
// Выполнение GET запроса при монтировании компонента
fetch("https://api.example.com/data")
  .then((response) => response.json())
  .then((data) => setData(data))
  .catch((error) => console.error("Ошибка при загрузке данных:", error));
}, []);
```
Post
```jsx
const data = { name };
// Выполнение POST запроса
fetch("https://api.example.com/submit", {
  method: "POST", // Метод запроса
  headers: {
    "Content-Type": "application/json", // Указываем, что отправляем данные в формате JSON
  },
  body: JSON.stringify(data), // Преобразуем объект в JSON строку
})
  .then((response) => response.json())
  .then((data) => console.log("Ответ от сервера:", data))
  .catch((error) => console.error("Ошибка при отправке данных:", error));
};
```
Post с cookie
```jsx
const data = { name };
// Выполнение POST запроса с cookies
fetch("https://api.example.com/submit", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(data),
  credentials: "include", // Включаем cookies (если они должны быть отправлены с запросом)
})
  .then((response) => response.json())
  .then((data) => console.log("Ответ от сервера:", data))
  .catch((error) => console.error("Ошибка при отправке данных:", error));
};
```

## 12

CommonJS и ES6-формат модулей
В Node.js существуют два основных формата для работы с модулями:

CommonJS (CJS) — стандарт, использующий require и module.exports:

Это формат, который Node.js использует по умолчанию.

Пример:

```javascript
// commonjs-example.js
module.exports = function() {
  console.log("Hello from CommonJS");
};
```
Для импорта:
```javascript
const greet = require('./commonjs-example');
greet(); // Hello from CommonJS
```
ES6 модули (ESM) — это новый стандарт модулей в JavaScript, использующий import и export:

В ES6 модулях используется синтаксис import и export.

Пример:
```javascript
// es6-example.js
export function greet() {
  console.log("Hello from ES6 module");
}
```
Для импорта:
```javascript
import { greet } from './es6-example.js';
greet(); // Hello from ES6 module
```