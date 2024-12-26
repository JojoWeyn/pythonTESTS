### 1 Кликер с кнопками [+] и [-]:
```jsx
import React, { useState } from 'react';

const Clicker = () => {
  const [count, setCount] = useState(0);

  const handleIncrement = () => {
    setCount(count + 1);
  };

  const handleDecrement = () => {
    if (count > 0) setCount(count - 1);
  };

  return (
    <div>
      <button onClick={handleDecrement}>-</button>
      <span style={{ color: count % 2 === 0 ? 'green' : 'red' }}>{count}</span>
      <button onClick={handleIncrement}>+</button>
    </div>
  );
};
```
### 2 Список чисел с фильтрацией:

```jsx
import React, { useState } from 'react';

const NumberList = () => {
  const [numbers, setNumbers] = useState([]);
  const [input, setInput] = useState('');
  const [filter, setFilter] = useState('all');

  const handleAddNumber = () => {
    setNumbers([...numbers, parseInt(input)]);
    setInput('');
  };

  const filteredNumbers = numbers.filter(num => {
    if (filter === 'even') return num % 2 === 0;
    if (filter === 'odd') return num % 2 !== 0;
    return true;
  });

  return (
    <div>
      <input
        type="number"
        value={input}
        onChange={e => setInput(e.target.value)}
      />
      <button onClick={handleAddNumber}>+</button>
      <select onChange={e => setFilter(e.target.value)}>
        <option value="all">All</option>
        <option value="even">Even</option>
        <option value="odd">Odd</option>
      </select>
      <ul>
        {filteredNumbers.map((num, index) => (
          <li key={index}>{num}</li>
        ))}
      </ul>
    </div>
  );
};
```

### 3 Калькулятор систем счисления:

```jsx
import React, { useState } from 'react';

const BaseConverter = () => {
  const [number, setNumber] = useState('');
  const [fromBase, setFromBase] = useState(10);
  const [toBase, setToBase] = useState(10);
  const [converted, setConverted] = useState('');

  const handleChange = () => {
    const decimalValue = parseInt(number, fromBase);
    setConverted(decimalValue.toString(toBase));
  };

  return (
    <div>
      <input
        type="number"
        value={number}
        onChange={e => setNumber(e.target.value)}
        onBlur={handleChange}
      />
      <select value={fromBase} onChange={e => setFromBase(Number(e.target.value))}>
        <option value={2}>Binary</option>
        <option value={8}>Octal</option>
        <option value={10}>Decimal</option>
        <option value={16}>Hexadecimal</option>
      </select>
      <select value={toBase} onChange={e => setToBase(Number(e.target.value))}>
        <option value={2}>Binary</option>
        <option value={8}>Octal</option>
        <option value={10}>Decimal</option>
        <option value={16}>Hexadecimal</option>
      </select>
      <div>Converted: {converted}</div>
    </div>
  );
};
```
### 4 Калькулятор перевода температур:

```jsx
import React, { useState } from 'react';

const TemperatureConverter = () => {
  const [celsius, setCelsius] = useState('');
  const [fahrenheit, setFahrenheit] = useState('');

  const handleCelsiusChange = (e) => {
    const value = e.target.value;
    setCelsius(value);
    setFahrenheit((value * 9/5) + 32);
  };

  const handleFahrenheitChange = (e) => {
    const value = e.target.value;
    setFahrenheit(value);
    setCelsius((value - 32) * 5/9);
  };

  return (
    <div>
      <input
        type="number"
        value={celsius}
        onChange={handleCelsiusChange}
        placeholder="Celsius"
      />
      <input
        type="number"
        value={fahrenheit}
        onChange={handleFahrenheitChange}
        placeholder="Fahrenheit"
      />
    </div>
  );
};
```

### 5 Обратный таймер:

```jsx
import React, { useState, useEffect } from 'react';

const Timer = () => {
  const [time, setTime] = useState(10); // время в секундах
  const [running, setRunning] = useState(false);

  useEffect(() => {
    let interval;
    if (running && time > 0) {
      interval = setInterval(() => setTime(prev => prev - 1), 1000);
    }
    return () => clearInterval(interval);
  }, [running, time]);

  const startTimer = () => setRunning(true);
  const stopTimer = () => setRunning(false);

  return (
    <div>
      <div>{time}</div>
      <button onClick={startTimer} disabled={running}>Start</button>
      <button onClick={stopTimer} disabled={!running}>Stop</button>
    </div>
  );
};
```

### 6 Частотный словарь:
```jsx
import React, { useState, useEffect } from 'react';

const WordFrequency = () => {
  const [input, setInput] = useState('');
  const [wordCount, setWordCount] = useState({});

  useEffect(() => {
    const words = input.split(/\s+/);
    const count = words.reduce((acc, word) => {
      acc[word] = (acc[word] || 0) + 1;
      return acc;
    }, {});
    setWordCount(count);
  }, [input]);

  const sortedWords = Object.entries(wordCount).sort((a, b) => b[1] - a[1]);

  return (
    <div>
      <textarea value={input} onChange={e => setInput(e.target.value)} />
      <ul>
        {sortedWords.map(([word, count], index) => (
          <li key={index}>{word}: {count}</li>
        ))}
      </ul>
    </div>
  );
};
```

### 7 Кнопка смены фона:
```jsx
import React, { useState } from 'react';

const BackgroundChanger = () => {
  const [isRed, setIsRed] = useState(true);

  const toggleBackground = () => setIsRed(!isRed);

  return (
    <div style={{ backgroundColor: isRed ? 'red' : 'green', padding: '20px' }}>
      <button onClick={toggleBackground}>Change Background</button>
    </div>
  );
};
```

### 8 Среднее арифметическое:
```jsx

import React, { useState } from 'react';

const AverageCalculator = () => {
  const [numbers, setNumbers] = useState([]);
  const [input, setInput] = useState('');

  const handleAddNumber = () => {
    setNumbers([...numbers, parseInt(input)]);
    setInput('');
  };

  const average = numbers.length ? numbers.reduce((a, b) => a + b, 0) / numbers.length : 0;

  return (
    <div>
      <input
        type="number"
        value={input}
        onChange={e => setInput(e.target.value)}
      />
      <button onClick={handleAddNumber}>Add Number</button>
      <div>Average: {average}</div>
    </div>
  );
};
```

### 9 Alert:
```jsx
import React, { useState, useEffect } from 'react';

const Alert = ({ message, delay }) => {
  const [visible, setVisible] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => setVisible(false), delay * 1000);
    return () => clearTimeout(timer);
  }, [delay]);

  return visible ? <div>{message}</div> : null;
};
```

### 10 Обратная строка:
```jsx
import React, { useState } from 'react';

const ReverseString = ({ text }) => {
  const [reversed, setReversed] = useState('');

  const reverseText = () => setReversed(text.split('').reverse().join(''));

  return (
    <div>
      <div>{text}</div>
      <button onClick={reverseText}>Reverse</button>
      <div>{reversed}</div>
    </div>
  );
};
```

### 11 Светофор:
```jsx
import React, { useState, useEffect } from 'react';

const TrafficLight = () => {
  const [color, setColor] = useState('red');

  useEffect(() => {
    const interval = setInterval(() => {
      setColor(prev => (prev === 'red' ? 'green' : prev === 'green' ? 'yellow' : 'red'));
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return <div>{color === 'red' ? '🔴' : color === 'green' ? '🟢' : '🟡'}</div>;
};
```

### 12 Счётчик с переменным шагом:
```jsx
import React, { useState } from 'react';

const CounterWithStep = () => {
  const [count, setCount] = useState(0);
  const [step, setStep] = useState(1);

  return (
    <div>
      <input type="range" min="1" max="10" value={step} onChange={e => setStep(Number(e.target.value))} />
      <div>Step: {step}</div>
      <button onClick={() => setCount(count + step)}>+</button>
      <div>Count: {count}</div>
    </div>
  );
};
```

### 13 Обращение к сети:
```jsx
import React, { useState } from 'react';

const FetchData = () => {
  const [id, setId] = useState('');
  const [data, setData] = useState(null);

  const fetchData = async () => {
    const response = await fetch(`https://jsonplaceholder.typicode.com/todos/${id}`);
    const result = await response.json();
    setData(result);
  };

  return (
    <div>
      <input type="text" value={id} onChange={e => setId(e.target.value)} />
      <button onClick={fetchData}>Get</button>
      {data && <div>{data.title}</div>}
    </div>
  );
};
```

### 14 PIN-код:
```jsx
import React, { useState } from 'react';

const PinCode = () => {
  const [pin, setPin] = useState('');
  const correctPin = '9999';

  const handlePinChange = (e) => {
    const newPin = (pin + e.target.value).slice(-4);
    setPin(newPin);
  };

  return (
    <div>
      <input type="number" maxLength={1} onChange={handlePinChange} />
      <input type="number" maxLength={1} onChange={handlePinChange} />
      <input type="number" maxLength={1} onChange={handlePinChange} />
      <input type="number" maxLength={1} onChange={handlePinChange} />
      {pin === correctPin && <div>Correct PIN</div>}
    </div>
  );
};
```

### 15 Калькулятор систем счисления (2, 8, 16):
```jsx
import React, { useState } from 'react';

const BaseConverter = () => {
  const [number, setNumber] = useState('');
  const [fromBase, setFromBase] = useState(10);
  const [toBase, setToBase] = useState(10);
  const [converted, setConverted] = useState('');

  const handleChange = () => {
    const decimalValue = parseInt(number, fromBase);
    setConverted(decimalValue.toString(toBase));
  };

  return (
    <div>
      <input
        type="number"
        value={number}
        onChange={e => setNumber(e.target.value)}
        onBlur={handleChange}
      />
      <select value={fromBase} onChange={e => setFromBase(Number(e.target.value))}>
        <option value={2}>Binary</option>
        <option value={8}>Octal</option>
        <option value={10}>Decimal</option>
        <option value={16}>Hexadecimal</option>
      </select>
      <select value={toBase} onChange={e => setToBase(Number(e.target.value))}>
        <option value={2}>Binary</option>
        <option value={8}>Octal</option>
        <option value={10}>Decimal</option>
        <option value={16}>Hexadecimal</option>
      </select>
      <div>Converted: {converted}</div>
    </div>
  );
};
```

### 16 Список чисел с фильтрацией (дополнено):
```jsx
import React, { useState } from 'react';

const NumberList = () => {
  const [numbers, setNumbers] = useState([]);
  const [input, setInput] = useState('');
  const [filter, setFilter] = useState('all');

  const handleAddNumber = () => {
    setNumbers([...numbers, parseInt(input)]);
    setInput('');
  };

  const filteredNumbers = numbers.filter(num => {
    if (filter === 'even') return num % 2 === 0;
    if (filter === 'odd') return num % 2 !== 0;
    return true;
  });

  return (
    <div>
      <input
        type="number"
        value={input}
        onChange={e => setInput(e.target.value)}
      />
      <button onClick={handleAddNumber}>+</button>
      <select onChange={e => setFilter(e.target.value)}>
        <option value="all">All</option>
        <option value="even">Even</option>
        <option value="odd">Odd</option>
      </select>
      <ul>
        {filteredNumbers.map((num, index) => (
          <li key={index}>{num}</li>
        ))}
      </ul>
    </div>
  );
};
```

### 17 Лайк:
```jsx
import React, { useState } from 'react';

const LikeButton = () => {
  const [liked, setLiked] = useState(false);
  let lastClick = 0;

  const handleClick = () => {
    const now = Date.now();
    if (now - lastClick < 800) {
      setLiked(!liked);
    }
    lastClick = now;
  };

  return (
    <button onClick={handleClick}>
      {liked ? '❤️' : '🖤'}
    </button>
  );
};
```

### 18 Градусник:
```jsx
import React from 'react';

const Thermometer = ({ temperature }) => {
  return (
    <div style={{ color: temperature < 0 ? 'blue' : 'red' }}>
      {temperature}°C
    </div>
  );
};
```

### 19 Минимальный сервер на Express.js:
```js
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
```

### 20 Минимальный сервер на Node.js:
```js
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World');
});

server.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});
```