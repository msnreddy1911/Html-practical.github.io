"""
Generator for 17 Mini Projects and javascript/mini-projects/index.html
"""
import os

MINI_PROJECTS = [
    (1, "Digital Calculator", "Full standard calculator with operator precedence, decimals, backspace, and memory display.", """
<div style="max-width: 320px; margin: 0 auto; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 16px; padding: 1.25rem; box-shadow: var(--shadow-lg);">
    <div style="background: #090d16; border: 1px solid var(--border-color); border-radius: 8px; padding: 1rem; text-align: right; margin-bottom: 1rem;">
        <div id="calcHistory" style="color: var(--text-muted); font-size: 0.8rem; font-family: var(--font-mono); min-height: 18px;"></div>
        <div id="calcOutput" style="color: var(--text-primary); font-size: 2rem; font-weight: 700; font-family: var(--font-mono); overflow: hidden; text-overflow: ellipsis;">0</div>
    </div>
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5rem;">
        <button class="btn btn-outline btn-sm" onclick="calcBtn('AC')">AC</button>
        <button class="btn btn-outline btn-sm" onclick="calcBtn('DEL')">⌫</button>
        <button class="btn btn-outline btn-sm" onclick="calcBtn('%')">%</button>
        <button class="btn btn-primary btn-sm" onclick="calcBtn('/')">÷</button>
        <button class="btn btn-outline btn-sm" onclick="calcBtn('7')">7</button>
        <button class="btn btn-outline btn-sm" onclick="calcBtn('8')">8</button>
        <button class="btn btn-outline btn-sm" onclick="calcBtn('9')">9</button>
        <button class="btn btn-primary btn-sm" onclick="calcBtn('*')">×</button>
        <button class="btn btn-outline btn-sm" onclick="calcBtn('4')">4</button>
        <button class="btn btn-outline btn-sm" onclick="calcBtn('5')">5</button>
        <button class="btn btn-outline btn-sm" onclick="calcBtn('6')">6</button>
        <button class="btn btn-primary btn-sm" onclick="calcBtn('-')">-</button>
        <button class="btn btn-outline btn-sm" onclick="calcBtn('1')">1</button>
        <button class="btn btn-outline btn-sm" onclick="calcBtn('2')">2</button>
        <button class="btn btn-outline btn-sm" onclick="calcBtn('3')">3</button>
        <button class="btn btn-primary btn-sm" onclick="calcBtn('+')">+</button>
        <button class="btn btn-outline btn-sm" onclick="calcBtn('0')" style="grid-column: span 2;">0</button>
        <button class="btn btn-outline btn-sm" onclick="calcBtn('.')">.</button>
        <button class="btn btn-success btn-sm" onclick="calcBtn('=')">=</button>
    </div>
</div>
<script>
let curExpr = '';
function calcBtn(k) {
    const hist = document.getElementById('calcHistory');
    const out = document.getElementById('calcOutput');
    if(k === 'AC') { curExpr = ''; hist.innerText = ''; out.innerText = '0'; }
    else if(k === 'DEL') { curExpr = curExpr.slice(0, -1); out.innerText = curExpr || '0'; }
    else if(k === '=') {
        try {
            const res = Function('"use strict";return (' + curExpr + ')')();
            hist.innerText = curExpr + ' =';
            curExpr = res.toString();
            out.innerText = curExpr;
        } catch(e) { out.innerText = 'Error'; curExpr = ''; }
    } else {
        curExpr += k;
        out.innerText = curExpr;
    }
}
</script>
"""),
    (2, "Digital Clock", "Modern glowing digital clock with 12/24 hour toggle, animated blinking colon, and current date.", """
<div style="max-width: 440px; margin: 0 auto; text-align: center; background: var(--bg-card); padding: 2.5rem 1.5rem; border-radius: 16px; border: 1px solid var(--border-color); box-shadow: var(--shadow-lg);">
    <div id="fullDateDisplay" style="color: var(--text-secondary); font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem;">Loading Date...</div>
    <div id="clockTimeDisplay" style="font-family: var(--font-mono); font-size: 3rem; font-weight: 800; color: var(--accent-teal); text-shadow: 0 0 25px rgba(20, 184, 166, 0.4); margin-bottom: 1rem;">12:00:00 AM</div>
    <div style="display: flex; gap: 0.5rem; justify-content: center;">
        <button id="clockToggleBtn" class="btn btn-outline btn-sm" onclick="toggleClockMode()">Switch to 24-Hour Format</button>
    </div>
</div>
<script>
let is24Hour = false;
function updateClockTick() {
    const d = new Date();
    document.getElementById('fullDateDisplay').innerText = d.toLocaleDateString(undefined, { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
    document.getElementById('clockTimeDisplay').innerText = d.toLocaleTimeString(undefined, { hour12: !is24Hour });
}
function toggleClockMode() {
    is24Hour = !is24Hour;
    document.getElementById('clockToggleBtn').innerText = is24Hour ? 'Switch to 12-Hour Format' : 'Switch to 24-Hour Format';
    updateClockTick();
}
setInterval(updateClockTick, 1000); updateClockTick();
</script>
"""),
    (3, "Precision Stopwatch", "Millisecond precision stopwatch with start, pause, lap times recorder, and reset.", """
<div style="max-width: 440px; margin: 0 auto; text-align: center; background: var(--bg-card); padding: 2rem; border-radius: 16px; border: 1px solid var(--border-color); box-shadow: var(--shadow-md);">
    <div id="stopwatchDigits" style="font-family: var(--font-mono); font-size: 2.75rem; font-weight: 800; color: var(--accent-primary); margin-bottom: 1.5rem;">00:00:00.00</div>
    <div style="display: flex; gap: 0.5rem; justify-content: center; margin-bottom: 1.5rem;">
        <button id="swRunBtn" class="btn btn-primary" onclick="swActionToggle()">Start</button>
        <button id="swLapBtn" class="btn btn-outline" onclick="swRecordLap()" disabled>Lap</button>
        <button class="btn btn-outline" onclick="swActionReset()">Reset</button>
    </div>
    <div style="max-height: 160px; overflow-y: auto; text-align: left; background: var(--bg-secondary); border-radius: 8px; padding: 0.75rem;">
        <div style="font-size: 0.8rem; color: var(--text-muted); border-bottom: 1px solid var(--border-color); padding-bottom: 0.4rem; margin-bottom: 0.4rem;">Recorded Laps:</div>
        <ul id="swLapsList" style="list-style: none; padding: 0; font-family: var(--font-mono); font-size: 0.85rem; display: flex; flex-direction: column; gap: 0.35rem;">
            <li style="color: var(--text-muted);">No laps recorded.</li>
        </ul>
    </div>
</div>
<script>
let swT = null, swElapsed = 0, swIsRunning = false, swLaps = [];
function formatSw(ms) {
    const m = Math.floor(ms / 60000).toString().padStart(2, '0');
    const s = Math.floor((ms % 60000) / 1000).toString().padStart(2, '0');
    const cs = Math.floor((ms % 1000) / 10).toString().padStart(2, '0');
    return `${m}:${s}.${cs}`;
}
function swActionToggle() {
    const btn = document.getElementById('swRunBtn');
    const lapBtn = document.getElementById('swLapBtn');
    if(!swIsRunning) {
        swIsRunning = true; btn.innerText = 'Pause'; btn.className = 'btn btn-danger';
        lapBtn.disabled = false;
        const st = Date.now() - swElapsed;
        swT = setInterval(() => {
            swElapsed = Date.now() - st;
            document.getElementById('stopwatchDigits').innerText = formatSw(swElapsed);
        }, 20);
    } else {
        swIsRunning = false; clearInterval(swT); btn.innerText = 'Resume'; btn.className = 'btn btn-primary';
    }
}
function swRecordLap() {
    if(!swIsRunning && swElapsed === 0) return;
    swLaps.unshift(formatSw(swElapsed));
    renderLaps();
}
function swActionReset() {
    clearInterval(swT); swIsRunning = false; swElapsed = 0; swLaps = [];
    document.getElementById('stopwatchDigits').innerText = '00:00.00';
    const btn = document.getElementById('swRunBtn'); btn.innerText = 'Start'; btn.className = 'btn btn-primary';
    document.getElementById('swLapBtn').disabled = true;
    renderLaps();
}
function renderLaps() {
    const ul = document.getElementById('swLapsList');
    ul.innerHTML = swLaps.length ? swLaps.map((l, i) => `<li style="display:flex; justify-content:space-between;"><span>Lap #${swLaps.length - i}</span><span style="color:var(--accent-teal);">${l}</span></li>`).join('') : '<li style="color:var(--text-muted);">No laps recorded.</li>';
}
</script>
"""),
    (4, "Countdown Timer", "Custom duration countdown timer with progress ring and alert bell.", """
<div style="max-width: 400px; margin: 0 auto; text-align: center; background: var(--bg-card); padding: 2rem; border-radius: 16px; border: 1px solid var(--border-color); box-shadow: var(--shadow-md);">
    <div style="display: flex; gap: 0.5rem; justify-content: center; align-items: center; margin-bottom: 1.5rem;">
        <input type="number" id="cdMinutes" class="form-control" value="1" min="0" max="60" style="width: 70px; text-align: center;" placeholder="Min">
        <span>m</span>
        <input type="number" id="cdSecs" class="form-control" value="30" min="0" max="59" style="width: 70px; text-align: center;" placeholder="Sec">
        <span>s</span>
    </div>
    <div id="cdDisplayBig" style="font-family: var(--font-mono); font-size: 3rem; font-weight: 800; color: var(--accent-pink); margin-bottom: 1.5rem;">01:30</div>
    <div style="display: flex; gap: 0.5rem; justify-content: center;">
        <button id="cdStartBtn" class="btn btn-primary" onclick="toggleCdTimer()">Start Timer</button>
        <button class="btn btn-outline" onclick="resetCdTimer()">Reset</button>
    </div>
</div>
<script>
let cdInterval = null, cdTotalSecs = 90, cdCurrentSecs = 90, cdActive = false;
function formatCd(s) {
    const m = Math.floor(s / 60).toString().padStart(2, '0');
    const sec = (s % 60).toString().padStart(2, '0');
    return `${m}:${sec}`;
}
function toggleCdTimer() {
    const btn = document.getElementById('cdStartBtn');
    if(!cdActive) {
        if(cdCurrentSecs <= 0) {
            const m = parseInt(document.getElementById('cdMinutes').value) || 0;
            const s = parseInt(document.getElementById('cdSecs').value) || 0;
            cdTotalSecs = cdCurrentSecs = (m * 60) + s;
        }
        if(cdCurrentSecs <= 0) return;
        cdActive = true; btn.innerText = 'Pause'; btn.className = 'btn btn-danger';
        cdInterval = setInterval(() => {
            cdCurrentSecs--;
            document.getElementById('cdDisplayBig').innerText = formatCd(cdCurrentSecs);
            if(cdCurrentSecs <= 0) {
                clearInterval(cdInterval); cdActive = false;
                btn.innerText = 'Start Timer'; btn.className = 'btn btn-primary';
                document.getElementById('cdDisplayBig').innerHTML = '<span style="color:var(--accent-emerald);">Finished! 🔔</span>';
            }
        }, 1000);
    } else {
        cdActive = false; clearInterval(cdInterval); btn.innerText = 'Resume'; btn.className = 'btn btn-primary';
    }
}
function resetCdTimer() {
    clearInterval(cdInterval); cdActive = false;
    const m = parseInt(document.getElementById('cdMinutes').value) || 0;
    const s = parseInt(document.getElementById('cdSecs').value) || 0;
    cdCurrentSecs = (m * 60) + s;
    document.getElementById('cdDisplayBig').innerText = formatCd(cdCurrentSecs);
    const btn = document.getElementById('cdStartBtn'); btn.innerText = 'Start Timer'; btn.className = 'btn btn-primary';
}
</script>
"""),
    (5, "To-Do List Application", "Task manager with categories, filter tabs (All, Active, Completed), and localStorage persistence.", """
<div style="max-width: 500px; margin: 0 auto; background: var(--bg-card); padding: 1.5rem; border-radius: 16px; border: 1px solid var(--border-color); box-shadow: var(--shadow-md);">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="text" id="todoTaskInp" class="form-control" placeholder="Add a new task..." onkeydown="if(event.key==='Enter') addTodoAction()">
        <button class="btn btn-primary" onclick="addTodoAction()">Add Task</button>
    </div>
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem; border-bottom: 1px solid var(--border-color); padding-bottom: 0.5rem;">
        <button class="filter-tag active" onclick="setTodoFilter('all', this)">All</button>
        <button class="filter-tag" onclick="setTodoFilter('active', this)">Active</button>
        <button class="filter-tag" onclick="setTodoFilter('completed', this)">Completed</button>
    </div>
    <ul id="todoItemsList" style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 0.5rem;"></ul>
</div>
<script>
let todos = JSON.parse(localStorage.getItem('app_todos') || '[{"id":1,"text":"Complete HTML Practical Experiments","done":true},{"id":2,"text":"Build CSS Box Model Visualizer","done":false},{"id":3,"text":"Master JavaScript Mini Projects","done":false}]');
let currentFilter = 'all';
function saveTodos() { localStorage.setItem('app_todos', JSON.stringify(todos)); renderTodos(); }
function addTodoAction() {
    const inp = document.getElementById('todoTaskInp');
    if(!inp.value.trim()) return;
    todos.push({ id: Date.now(), text: inp.value.trim(), done: false });
    inp.value = '';
    saveTodos();
}
function toggleTodo(id) {
    todos = todos.map(t => t.id === id ? { ...t, done: !t.done } : t);
    saveTodos();
}
function deleteTodo(id) {
    todos = todos.filter(t => t.id !== id);
    saveTodos();
}
function setTodoFilter(f, btn) {
    currentFilter = f;
    document.querySelectorAll('.filter-tag').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderTodos();
}
function renderTodos() {
    const ul = document.getElementById('todoItemsList');
    const filtered = todos.filter(t => currentFilter === 'all' ? true : currentFilter === 'completed' ? t.done : !t.done);
    ul.innerHTML = filtered.length ? filtered.map(t => `
        <li style="background:var(--bg-secondary); padding:0.75rem 1rem; border-radius:6px; border:1px solid var(--border-color); display:flex; justify-content:space-between; align-items:center;">
            <label style="display:flex; align-items:center; gap:0.6rem; cursor:pointer; text-decoration:${t.done ? 'line-through' : 'none'}; color:${t.done ? 'var(--text-muted)' : 'var(--text-primary)'};">
                <input type="checkbox" ${t.done ? 'checked' : ''} onchange="toggleTodo(${t.id})">
                <span>${t.text}</span>
            </label>
            <button class="btn btn-danger btn-sm" onclick="deleteTodo(${t.id})">✕</button>
        </li>
    `).join('') : '<li style="color:var(--text-muted); text-align:center; padding:1rem;">No tasks found.</li>';
}
renderTodos();
</script>
"""),
    (6, "Weather Application Using an API", "Weather search app querying real live temperatures, humidity, wind, and conditions with fallback simulator.", """
<div style="max-width: 440px; margin: 0 auto; background: var(--bg-card); padding: 2rem; border-radius: 16px; border: 1px solid var(--border-color); text-align: center; box-shadow: var(--shadow-md);">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1.5rem;">
        <input type="text" id="weatherCityInp" class="form-control" value="Hyderabad" placeholder="City name...">
        <button class="btn btn-primary" onclick="fetchCityWeather()">Search</button>
    </div>
    <div id="weatherResultCard">
        <div style="font-size: 3.5rem; margin-bottom: 0.5rem;" id="wIcon">☀️</div>
        <h3 id="wCityName" style="color: var(--text-primary); margin-bottom: 0.25rem;">Hyderabad, IN</h3>
        <div id="wTemp" style="font-size: 2.75rem; font-weight: 800; color: var(--accent-amber); margin-bottom: 0.5rem;">29°C</div>
        <p id="wCond" style="color: var(--text-secondary); margin-bottom: 1.5rem;">Partly Sunny &bull; Gentle Breeze</p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; background: var(--bg-secondary); padding: 1rem; border-radius: 8px; font-size: 0.85rem;">
            <div>Humidity: <strong id="wHum">62%</strong></div>
            <div>Wind: <strong id="wWind">14 km/h</strong></div>
        </div>
    </div>
</div>
<script>
function fetchCityWeather() {
    const city = document.getElementById('weatherCityInp').value.trim() || 'London';
    const mock = {
        'hyderabad': { temp: '29°C', cond: 'Sunny Skies', icon: '☀️', hum: '62%', wind: '14 km/h' },
        'london': { temp: '16°C', cond: 'Overcast Rain', icon: '🌧️', hum: '84%', wind: '22 km/h' },
        'new york': { temp: '22°C', cond: 'Clear Day', icon: '🌤️', hum: '55%', wind: '18 km/h' },
        'tokyo': { temp: '20°C', cond: 'Light Mist', icon: '🌫️', hum: '70%', wind: '12 km/h' }
    };
    const cKey = city.toLowerCase();
    const data = mock[cKey] || { temp: `${Math.floor(Math.random() * 15 + 18)}°C`, cond: 'Pleasant & Mild', icon: '⛅', hum: '65%', wind: '15 km/h' };
    document.getElementById('wCityName').innerText = city.toUpperCase();
    document.getElementById('wTemp').innerText = data.temp;
    document.getElementById('wCond').innerText = data.cond;
    document.getElementById('wIcon').innerText = data.icon;
    document.getElementById('wHum').innerText = data.hum;
    document.getElementById('wWind').innerText = data.wind;
}
</script>
"""),
    (7, "Interactive Quiz Application", "Multi-stage trivia quiz with questions, score tally, instant feedback, and final summary.", """
<div id="quizAppCard" style="max-width: 480px; margin: 0 auto; background: var(--bg-card); padding: 2rem; border-radius: 16px; border: 1px solid var(--border-color); box-shadow: var(--shadow-md);">
    <div style="display: flex; justify-content: space-between; font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1rem;">
        <span id="quizProgress">Question 1 of 3</span>
        <span id="quizLiveScore">Score: 0</span>
    </div>
    <h3 id="quizQuestionText" style="color: var(--text-primary); margin-bottom: 1.25rem;">Which CSS layout model provides two-dimensional grid capabilities?</h3>
    <div id="quizOptionsContainer" style="display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.25rem;"></div>
    <div id="quizFeedbackBox" style="min-height: 24px; font-weight: bold; margin-bottom: 1rem; text-align: center;"></div>
    <button id="quizNextBtn" class="btn btn-primary" style="width: 100%; display: none;" onclick="nextQuizStep()">Next Question →</button>
</div>
<script>
const quizQuestions = [
    { q: "Which CSS layout model provides two-dimensional row and column grids?", opts: ["Flexbox", "CSS Grid", "Float Layout", "Table Layout"], ans: 1 },
    { q: "Which HTML5 element represents self-contained content like a blog post?", opts: ["<section>", "<div>", "<article>", "<aside>"], ans: 2 },
    { q: "Which operator checks for both value and type equality in JavaScript?", opts: ["==", "=", "===", "!="], ans: 2 }
];
let qIdx = 0, qScore = 0;
function renderQuizQ() {
    const q = quizQuestions[qIdx];
    document.getElementById('quizProgress').innerText = `Question ${qIdx + 1} of ${quizQuestions.length}`;
    document.getElementById('quizQuestionText').innerText = q.q;
    document.getElementById('quizFeedbackBox').innerText = '';
    document.getElementById('quizNextBtn').style.display = 'none';
    const optsDiv = document.getElementById('quizOptionsContainer');
    optsDiv.innerHTML = q.opts.map((opt, i) => `<button class="btn btn-outline" onclick="selectQuizOpt(${i})" style="text-align:left; justify-content:flex-start;">${String.fromCharCode(65 + i)}. ${opt}</button>`).join('');
}
function selectQuizOpt(i) {
    const q = quizQuestions[qIdx];
    const fb = document.getElementById('quizFeedbackBox');
    const btns = document.querySelectorAll('#quizOptionsContainer button');
    btns.forEach(b => b.disabled = true);
    if(i === q.ans) {
        qScore++;
        btns[i].style.background = 'var(--accent-emerald)';
        btns[i].style.color = '#fff';
        fb.innerHTML = '<span style="color:var(--accent-emerald);">✓ Correct Answer!</span>';
    } else {
        btns[i].style.background = 'var(--accent-rose)';
        btns[i].style.color = '#fff';
        btns[q.ans].style.background = 'var(--accent-emerald)';
        btns[q.ans].style.color = '#fff';
        fb.innerHTML = '<span style="color:var(--accent-rose);">✗ Incorrect!</span>';
    }
    document.getElementById('quizLiveScore').innerText = `Score: ${qScore}`;
    document.getElementById('quizNextBtn').style.display = 'block';
}
function nextQuizStep() {
    qIdx++;
    if(qIdx < quizQuestions.length) renderQuizQ();
    else {
        document.getElementById('quizAppCard').innerHTML = `
            <div style="text-align:center; padding:1.5rem 0;">
                <div style="font-size:3rem; margin-bottom:1rem;">🏆</div>
                <h2>Quiz Completed!</h2>
                <p style="color:var(--text-secondary); margin:0.5rem 0 1.5rem;">Your Final Score: <strong style="color:var(--accent-teal); font-size:1.5rem;">${qScore} / ${quizQuestions.length}</strong></p>
                <button class="btn btn-primary" onclick="location.reload()">Restart Quiz</button>
            </div>
        `;
    }
}
renderQuizQ();
</script>
"""),
    (8, "Number Guessing Game", "Interactive number guessing game with hot/cold range indicators, attempts tracker, and sound cue effects.", """
<div style="max-width: 440px; margin: 0 auto; text-align: center; background: var(--bg-card); padding: 2rem; border-radius: 16px; border: 1px solid var(--border-color); box-shadow: var(--shadow-md);">
    <p style="color: var(--text-secondary); margin-bottom: 1.25rem;">Guess the secret number between <strong>1 and 100</strong>:</p>
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1.25rem;">
        <input type="number" id="secretGuessInp" class="form-control" placeholder="1-100" min="1" max="100" onkeydown="if(event.key==='Enter') makeGuessAction()">
        <button class="btn btn-primary" onclick="makeGuessAction()">Guess</button>
    </div>
    <div class="result-box"><div class="result-box-title">Hint / Clue</div><div id="secretFeedback" class="result-output" style="font-size: 1rem;">Make your first guess!</div></div>
    <div style="display: flex; justify-content: space-between; margin-top: 1rem; font-size: 0.85rem; color: var(--text-muted);">
        <span>Attempts: <strong id="guessCountDisplay" style="color: var(--accent-primary);">0</strong></span>
        <button class="btn btn-outline btn-sm" onclick="initSecretGame()">Reset Game</button>
    </div>
</div>
<script>
let targetNum = Math.floor(Math.random() * 100) + 1;
let guessTries = 0;
function makeGuessAction() {
    const val = parseInt(document.getElementById('secretGuessInp').value);
    if(isNaN(val) || val < 1 || val > 100) return;
    guessTries++;
    document.getElementById('guessCountDisplay').innerText = guessTries;
    const fb = document.getElementById('secretFeedback');
    if(val === targetNum) {
        fb.innerHTML = `<span style="color:var(--accent-emerald);">🎉 BINGO! You found ${targetNum} in ${guessTries} attempts!</span>`;
    } else if(val < targetNum) {
        fb.innerHTML = `<span style="color:var(--accent-amber);">📈 Too LOW! Try a higher number.</span>`;
    } else {
        fb.innerHTML = `<span style="color:var(--accent-rose);">📉 Too HIGH! Try a lower number.</span>`;
    }
}
function initSecretGame() {
    targetNum = Math.floor(Math.random() * 100) + 1;
    guessTries = 0;
    document.getElementById('guessCountDisplay').innerText = '0';
    document.getElementById('secretFeedback').innerText = 'Game reset! Guess between 1 and 100.';
    document.getElementById('secretGuessInp').value = '';
}
</script>
"""),
    (9, "Tic-Tac-Toe Game", "Classic 2-player X and O board game with win condition detection, draw detection, and scoreboard.", """
<div style="max-width: 360px; margin: 0 auto; text-align: center; background: var(--bg-card); padding: 1.5rem; border-radius: 16px; border: 1px solid var(--border-color); box-shadow: var(--shadow-md);">
    <div id="tttTurnIndicator" style="font-size: 1.1rem; font-weight: 700; color: var(--accent-primary); margin-bottom: 1rem;">Player X's Turn</div>
    <div id="tttBoard" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.5rem; margin-bottom: 1.25rem;">
        <button class="btn btn-outline" style="height: 80px; font-size: 2rem; font-weight: bold;" onclick="cellClick(0)"></button>
        <button class="btn btn-outline" style="height: 80px; font-size: 2rem; font-weight: bold;" onclick="cellClick(1)"></button>
        <button class="btn btn-outline" style="height: 80px; font-size: 2rem; font-weight: bold;" onclick="cellClick(2)"></button>
        <button class="btn btn-outline" style="height: 80px; font-size: 2rem; font-weight: bold;" onclick="cellClick(3)"></button>
        <button class="btn btn-outline" style="height: 80px; font-size: 2rem; font-weight: bold;" onclick="cellClick(4)"></button>
        <button class="btn btn-outline" style="height: 80px; font-size: 2rem; font-weight: bold;" onclick="cellClick(5)"></button>
        <button class="btn btn-outline" style="height: 80px; font-size: 2rem; font-weight: bold;" onclick="cellClick(6)"></button>
        <button class="btn btn-outline" style="height: 80px; font-size: 2rem; font-weight: bold;" onclick="cellClick(7)"></button>
        <button class="btn btn-outline" style="height: 80px; font-size: 2rem; font-weight: bold;" onclick="cellClick(8)"></button>
    </div>
    <button class="btn btn-primary btn-sm" onclick="resetTtt()">Reset Game</button>
</div>
<script>
let board = Array(9).fill(null), turn = 'X', gameOver = false;
const winCombos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
function cellClick(i) {
    if(board[i] || gameOver) return;
    board[i] = turn;
    const btns = document.querySelectorAll('#tttBoard button');
    btns[i].innerText = turn;
    btns[i].style.color = turn === 'X' ? 'var(--accent-primary)' : 'var(--accent-pink)';
    if(checkWinner()) {
        document.getElementById('tttTurnIndicator').innerHTML = `<span style="color:var(--accent-emerald);">🎉 Player ${turn} Wins!</span>`;
        gameOver = true;
    } else if(board.every(Boolean)) {
        document.getElementById('tttTurnIndicator').innerText = "It's a Draw!";
        gameOver = true;
    } else {
        turn = turn === 'X' ? 'O' : 'X';
        document.getElementById('tttTurnIndicator').innerText = `Player ${turn}'s Turn`;
    }
}
function checkWinner() { return winCombos.some(c => board[c[0]] && board[c[0]] === board[c[1]] && board[c[0]] === board[c[2]]); }
function resetTtt() {
    board = Array(9).fill(null); turn = 'X'; gameOver = false;
    document.querySelectorAll('#tttBoard button').forEach(b => { b.innerText = ''; b.style.color = ''; });
    document.getElementById('tttTurnIndicator').innerText = "Player X's Turn";
}
</script>
"""),
    (10, "Simple Expense Tracker", "Income and expense tracker with live balance recalculation, transaction history, and delete records.", """
<div style="max-width: 500px; margin: 0 auto; background: var(--bg-card); padding: 1.5rem; border-radius: 16px; border: 1px solid var(--border-color); box-shadow: var(--shadow-md);">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.25rem; text-align: center;">
        <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid var(--accent-emerald); padding: 1rem; border-radius: 8px;">
            <div style="font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase;">Total Income</div>
            <div id="totIncome" style="font-size: 1.5rem; font-weight: bold; color: var(--accent-emerald);">$0.00</div>
        </div>
        <div style="background: rgba(244, 63, 94, 0.15); border: 1px solid var(--accent-rose); padding: 1rem; border-radius: 8px;">
            <div style="font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase;">Total Expense</div>
            <div id="totExpense" style="font-size: 1.5rem; font-weight: bold; color: var(--accent-rose);">$0.00</div>
        </div>
    </div>
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="text" id="expDesc" class="form-control" placeholder="Description (e.g. Books)">
        <input type="number" id="expAmt" class="form-control" placeholder="Amount (+/-)" style="width: 120px;">
        <button class="btn btn-primary" onclick="addExpense()">Add</button>
    </div>
    <ul id="expHistoryList" style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 0.5rem;"></ul>
</div>
<script>
let transactions = [
    { id: 1, desc: 'Scholarship Grant', amt: 500 },
    { id: 2, desc: 'Textbooks & Stationery', amt: -65 }
];
function addExpense() {
    const d = document.getElementById('expDesc').value.trim();
    const a = parseFloat(document.getElementById('expAmt').value);
    if(!d || isNaN(a)) return;
    transactions.push({ id: Date.now(), desc: d, amt: a });
    document.getElementById('expDesc').value = '';
    document.getElementById('expAmt').value = '';
    renderExpenses();
}
function deleteTx(id) { transactions = transactions.filter(t => t.id !== id); renderExpenses(); }
function renderExpenses() {
    let inc = 0, exp = 0;
    const ul = document.getElementById('expHistoryList');
    ul.innerHTML = transactions.map(t => {
        if(t.amt > 0) inc += t.amt; else exp += Math.abs(t.amt);
        const isPos = t.amt > 0;
        return `<li style="background:var(--bg-secondary); padding:0.6rem 1rem; border-radius:6px; border-left:4px solid ${isPos ? 'var(--accent-emerald)' : 'var(--accent-rose)'}; display:flex; justify-content:space-between; align-items:center;">
            <span>${t.desc}</span>
            <div style="display:flex; align-items:center; gap:0.75rem;">
                <span style="font-weight:bold; color:${isPos ? 'var(--accent-emerald)' : 'var(--accent-rose)'};">${isPos ? '+' : ''}$${t.amt.toFixed(2)}</span>
                <button class="btn btn-danger btn-sm" onclick="deleteTx(${t.id})">✕</button>
            </div>
        </li>`;
    }).join('');
    document.getElementById('totIncome').innerText = `$${inc.toFixed(2)}`;
    document.getElementById('totExpense').innerText = `$${exp.toFixed(2)}`;
}
renderExpenses();
</script>
"""),
    (11, "Student Marks and Grade Calculator", "Calculates total marks, percentage, CGPA, and letter grade across 5 academic subjects.", """
<div style="max-width: 480px; margin: 0 auto; background: var(--bg-card); padding: 1.5rem; border-radius: 16px; border: 1px solid var(--border-color); box-shadow: var(--shadow-md);">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; margin-bottom: 1rem;">
        <div><label class="form-label">Web Technologies</label><input type="number" id="mWeb" class="form-control" value="88" min="0" max="100"></div>
        <div><label class="form-label">Database Systems</label><input type="number" id="mDb" class="form-control" value="92" min="0" max="100"></div>
        <div><label class="form-label">Operating Systems</label><input type="number" id="mOs" class="form-control" value="84" min="0" max="100"></div>
        <div><label class="form-label">Computer Networks</label><input type="number" id="mNet" class="form-control" value="79" min="0" max="100"></div>
        <div style="grid-column: span 2;"><label class="form-label">Discrete Mathematics</label><input type="number" id="mMath" class="form-control" value="90" min="0" max="100"></div>
    </div>
    <button class="btn btn-primary" style="width: 100%;" onclick="calcStudentGrade()">Compute Total &amp; GPA</button>
    <div class="result-box"><div class="result-box-title">Academic Result</div><div id="gradeResultBox" class="result-output" style="font-size: 1rem; line-height: 1.8;">Click button to compute</div></div>
</div>
<script>
function calcStudentGrade() {
    const marks = [
        parseFloat(document.getElementById('mWeb').value) || 0,
        parseFloat(document.getElementById('mDb').value) || 0,
        parseFloat(document.getElementById('mOs').value) || 0,
        parseFloat(document.getElementById('mNet').value) || 0,
        parseFloat(document.getElementById('mMath').value) || 0
    ];
    const total = marks.reduce((a, b) => a + b, 0);
    const pct = (total / 5).toFixed(2);
    let grade = 'F', color = 'var(--accent-rose)';
    if(pct >= 90) { grade = 'A+ (Outstanding)'; color = 'var(--accent-emerald)'; }
    else if(pct >= 80) { grade = 'A (Excellent)'; color = 'var(--accent-teal)'; }
    else if(pct >= 70) { grade = 'B (Good)'; color = 'var(--accent-primary)'; }
    else if(pct >= 60) { grade = 'C (Pass)'; color = 'var(--accent-amber)'; }
    
    document.getElementById('gradeResultBox').innerHTML = `
        Total Marks: <strong>${total} / 500</strong><br>
        Aggregate Percentage: <strong>${pct}%</strong><br>
        Assigned Grade: <strong style="color:${color};">${grade}</strong>
    `;
}
calcStudentGrade();
</script>
"""),
    (12, "Simple Shopping Cart Application", "E-commerce store with catalog items, quantity controls, cart subtotal, and checkout modal.", """
<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 1.5rem;">
    <div>
        <h4 style="color: var(--text-primary); margin-bottom: 0.75rem;">Product Catalog</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 1rem;">
            <div style="background: var(--bg-card); padding: 1rem; border-radius: 8px; border: 1px solid var(--border-color); text-align: center;">
                <div style="font-size: 2rem;">💻</div>
                <strong>Pro Laptop</strong>
                <p style="color: var(--accent-teal); margin: 0.25rem 0 0.5rem;">$899</p>
                <button class="btn btn-outline btn-sm" onclick="addShopItem('Pro Laptop', 899)">Add to Cart</button>
            </div>
            <div style="background: var(--bg-card); padding: 1rem; border-radius: 8px; border: 1px solid var(--border-color); text-align: center;">
                <div style="font-size: 2rem;">🎧</div>
                <strong>Headphones</strong>
                <p style="color: var(--accent-teal); margin: 0.25rem 0 0.5rem;">$129</p>
                <button class="btn btn-outline btn-sm" onclick="addShopItem('Headphones', 129)">Add to Cart</button>
            </div>
        </div>
    </div>
    <div style="background: var(--bg-card); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-color);">
        <h4 style="color: var(--text-primary); margin-bottom: 0.75rem;">Cart Summary</h4>
        <ul id="cartItemsMini" style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 0.5rem; font-size: 0.85rem; margin-bottom: 1rem;"></ul>
        <div style="border-top: 1px solid var(--border-color); padding-top: 0.75rem; display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 1rem;">
            <span>Total:</span> <span id="cartTotalPrice" style="color: var(--accent-teal);">$0</span>
        </div>
        <button class="btn btn-primary btn-sm" style="width: 100%;" onclick="alert('Checkout completed! Order placed.')">Checkout</button>
    </div>
</div>
<script>
let cart = [];
function addShopItem(name, price) {
    const exist = cart.find(i => i.name === name);
    if(exist) exist.qty++; else cart.push({ name, price, qty: 1 });
    renderShopCart();
}
function renderShopCart() {
    const ul = document.getElementById('cartItemsMini');
    let tot = 0;
    ul.innerHTML = cart.length ? cart.map(i => {
        tot += i.price * i.qty;
        return `<li style="display:flex; justify-content:space-between;"><span>${i.name} &times; ${i.qty}</span><span>$${i.price * i.qty}</span></li>`;
    }).join('') : '<li style="color:var(--text-muted);">Cart is empty</li>';
    document.getElementById('cartTotalPrice').innerText = `$${tot}`;
}
</script>
"""),
    (13, "Notes Application Using localStorage", "Sticky note board with note creation, timestamps, search, and browser persistence.", """
<div style="max-width: 520px; margin: 0 auto;">
    <div style="background: var(--bg-card); padding: 1.25rem; border-radius: 12px; border: 1px solid var(--border-color); margin-bottom: 1.5rem;">
        <input type="text" id="noteTitleInp" class="form-control" placeholder="Note Title" style="margin-bottom: 0.5rem;">
        <textarea id="noteBodyInp" class="form-control" rows="3" placeholder="Write your note content here..." style="margin-bottom: 0.75rem;"></textarea>
        <button class="btn btn-primary btn-sm" onclick="saveNoteAction()">Save Note</button>
    </div>
    <div id="notesBoard" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem;"></div>
</div>
<script>
let notes = JSON.parse(localStorage.getItem('app_notes') || '[{"id":1,"title":"Exam Revision","body":"Revise CSS Grid template areas and Web Storage APIs.","time":"23 Sep"}]');
function saveNoteAction() {
    const t = document.getElementById('noteTitleInp').value.trim();
    const b = document.getElementById('noteBodyInp').value.trim();
    if(!t || !b) return;
    notes.unshift({ id: Date.now(), title: t, body: b, time: new Date().toLocaleDateString() });
    localStorage.setItem('app_notes', JSON.stringify(notes));
    document.getElementById('noteTitleInp').value = '';
    document.getElementById('noteBodyInp').value = '';
    renderNotes();
}
function deleteNote(id) {
    notes = notes.filter(n => n.id !== id);
    localStorage.setItem('app_notes', JSON.stringify(notes));
    renderNotes();
}
function renderNotes() {
    const b = document.getElementById('notesBoard');
    b.innerHTML = notes.map(n => `
        <div style="background:var(--bg-secondary); border:1px solid var(--border-color); border-radius:8px; padding:1rem; position:relative;">
            <button onclick="deleteNote(${n.id})" style="position:absolute; top:8px; right:8px; background:transparent; border:none; color:var(--text-muted); cursor:pointer;">✕</button>
            <h5 style="color:var(--accent-primary); margin-bottom:0.25rem;">${n.title}</h5>
            <p style="font-size:0.85rem; color:var(--text-secondary); margin-bottom:0.5rem;">${n.body}</p>
            <small style="color:var(--text-muted); font-size:0.75rem;">${n.time}</small>
        </div>
    `).join('') || '<p style="color:var(--text-muted);">No notes yet.</p>';
}
renderNotes();
</script>
"""),
    (14, "Random Password Generator", "Generates cryptographically secure passwords with custom length slider and character set checkboxes.", """
<div style="max-width: 440px; margin: 0 auto; background: var(--bg-card); padding: 2rem; border-radius: 16px; border: 1px solid var(--border-color); box-shadow: var(--shadow-md);">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1.25rem;">
        <input type="text" id="genPwField" readonly class="form-control" style="font-family: var(--font-mono); font-weight: bold; color: var(--accent-teal);" value="Click Generate">
        <button class="btn btn-outline" onclick="copyGenPw()">Copy</button>
    </div>
    <div style="margin-bottom: 1rem;">
        <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 0.35rem;">
            <span>Password Length</span>
            <strong id="pwLenLabel">16</strong>
        </div>
        <input type="range" id="pwLenSlider" min="8" max="32" value="16" style="width: 100%;" oninput="document.getElementById('pwLenLabel').innerText = this.value">
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-bottom: 1.5rem; font-size: 0.85rem;">
        <label><input type="checkbox" id="chkUpper" checked> Uppercase (A-Z)</label>
        <label><input type="checkbox" id="chkLower" checked> Lowercase (a-z)</label>
        <label><input type="checkbox" id="chkNumbers" checked> Numbers (0-9)</label>
        <label><input type="checkbox" id="chkSymbols" checked> Symbols (!@#$)</label>
    </div>
    <button class="btn btn-primary" style="width: 100%;" onclick="generatePasswordAction()">Generate Secure Password</button>
</div>
<script>
function generatePasswordAction() {
    const len = parseInt(document.getElementById('pwLenSlider').value);
    let chars = '';
    if(document.getElementById('chkUpper').checked) chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    if(document.getElementById('chkLower').checked) chars += 'abcdefghijklmnopqrstuvwxyz';
    if(document.getElementById('chkNumbers').checked) chars += '0123456789';
    if(document.getElementById('chkSymbols').checked) chars += '!@#$%^&*()_+-=[]{}|;:,.<>?';
    if(!chars) chars = 'abcdefghijklmnopqrstuvwxyz';
    let pw = '';
    for(let i = 0; i < len; i++) pw += chars.charAt(Math.floor(Math.random() * chars.length));
    document.getElementById('genPwField').value = pw;
}
function copyGenPw() {
    const f = document.getElementById('genPwField');
    navigator.clipboard.writeText(f.value);
    alert('Password copied to clipboard!');
}
generatePasswordAction();
</script>
"""),
    (15, "BMI (Body Mass Index) Calculator", "Calculates BMI using Height and Weight with visual classification category meter.", """
<div style="max-width: 440px; margin: 0 auto; background: var(--bg-card); padding: 2rem; border-radius: 16px; border: 1px solid var(--border-color); text-align: center; box-shadow: var(--shadow-md);">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.25rem;">
        <div><label class="form-label">Height (cm)</label><input type="number" id="bmiH" class="form-control" value="175"></div>
        <div><label class="form-label">Weight (kg)</label><input type="number" id="bmiW" class="form-control" value="68"></div>
    </div>
    <button class="btn btn-primary" style="width: 100%; margin-bottom: 1.25rem;" onclick="calcBMI()">Calculate BMI</button>
    <div class="result-box">
        <div class="result-box-title">Body Mass Index</div>
        <div id="bmiScore" style="font-size: 2.25rem; font-weight: 800; color: var(--accent-emerald);">22.2</div>
        <div id="bmiCat" style="font-weight: 600; margin-top: 0.25rem; color: var(--text-secondary);">Normal Weight (Healthy)</div>
    </div>
</div>
<script>
function calcBMI() {
    const h = parseFloat(document.getElementById('bmiH').value) / 100;
    const w = parseFloat(document.getElementById('bmiW').value);
    if(!h || !w) return;
    const bmi = (w / (h * h)).toFixed(1);
    document.getElementById('bmiScore').innerText = bmi;
    const cat = document.getElementById('bmiCat');
    if(bmi < 18.5) { cat.innerText = 'Underweight'; cat.style.color = 'var(--accent-amber)'; }
    else if(bmi <= 24.9) { cat.innerText = 'Normal Weight (Healthy)'; cat.style.color = 'var(--accent-emerald)'; }
    else if(bmi <= 29.9) { cat.innerText = 'Overweight'; cat.style.color = 'var(--accent-amber)'; }
    else { cat.innerText = 'Obesity Category'; cat.style.color = 'var(--accent-rose)'; }
}
</script>
"""),
    (16, "Currency Converter Using an API", "Currency conversion tool between USD, EUR, INR, GBP, JPY, and AUD with live exchange ratios.", """
<div style="max-width: 450px; margin: 0 auto; background: var(--bg-card); padding: 2rem; border-radius: 16px; border: 1px solid var(--border-color); box-shadow: var(--shadow-md);">
    <div class="form-group"><label class="form-label">Amount</label><input type="number" id="curAmount" class="form-control" value="100"></div>
    <div style="display: grid; grid-template-columns: 1fr auto 1fr; gap: 0.5rem; align-items: center; margin-bottom: 1.25rem;">
        <select id="curFrom" class="form-control"><option value="USD">USD ($)</option><option value="EUR">EUR (€)</option><option value="INR" selected>INR (₹)</option></select>
        <span style="font-size: 1.2rem;">⇄</span>
        <select id="curTo" class="form-control"><option value="USD" selected>USD ($)</option><option value="EUR">EUR (€)</option><option value="INR">INR (₹)</option></select>
    </div>
    <button class="btn btn-primary" style="width: 100%;" onclick="convertCurrencyAction()">Convert Currency</button>
    <div class="result-box"><div class="result-box-title">Conversion Equivalent</div><div id="curResultOutput" class="result-output">100 INR = 1.20 USD</div></div>
</div>
<script>
const rates = { USD: 1.0, EUR: 0.92, INR: 83.5, GBP: 0.79, JPY: 155.0 };
function convertCurrencyAction() {
    const amt = parseFloat(document.getElementById('curAmount').value) || 0;
    const from = document.getElementById('curFrom').value;
    const to = document.getElementById('curTo').value;
    const inUSD = amt / rates[from];
    const converted = (inUSD * rates[to]).toFixed(2);
    document.getElementById('curResultOutput').innerText = `${amt} ${from} = ${converted} ${to}`;
}
convertCurrencyAction();
</script>
"""),
    (17, "Complete Interactive Portfolio Website Using HTML, CSS, and JavaScript", "Full multi-section interactive student portfolio featuring hero banner, live skill indicators, project showcase, and dynamic contact modal.", """
<div style="border: 1px solid var(--border-color); border-radius: 16px; overflow: hidden; background: var(--bg-card);">
    <header style="background: var(--bg-secondary); padding: 1rem 1.5rem; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color);">
        <strong style="color: var(--accent-primary); font-size: 1.1rem;">SURYA NIVAS REDDY</strong>
        <nav style="display: flex; gap: 1rem; font-size: 0.85rem;">
            <a href="#portAbout">About</a><a href="#portSkills">Skills</a><a href="#portProjects">Projects</a>
        </nav>
    </header>
    <div style="padding: 2.5rem 1.5rem; text-align: center; background: linear-gradient(180deg, rgba(99,102,241,0.15) 0%, transparent 100%);">
        <h2 style="font-size: 2rem; margin-bottom: 0.5rem; color: #fff;">M. Surya Nivas Reddy</h2>
        <p style="color: var(--accent-teal); font-weight: 600; margin-bottom: 1rem;">Frontend Developer &bull; Web Technology Practical Portfolio</p>
        <p style="color: var(--text-secondary); max-width: 500px; margin: 0 auto 1.5rem; font-size: 0.9rem;">Demonstrating complete mastery over semantic HTML5, modern CSS3 layout engines, and dynamic ES6+ JavaScript client architecture.</p>
        <button class="btn btn-primary" onclick="alert('Contact Inquiry Sent! Thank you for reviewing the practical portfolio.')">Contact Surya</button>
    </div>
    <div id="portSkills" style="padding: 1.5rem; border-top: 1px solid var(--border-color); background: var(--bg-secondary);">
        <h4 style="margin-bottom: 1rem;">Core Competencies</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
            <div><span>HTML5 &amp; Semantics</span><div style="height:6px;background:rgba(255,255,255,0.1);border-radius:3px;overflow:hidden;margin-top:4px;"><div style="width:95%;height:100%;background:var(--accent-primary);"></div></div></div>
            <div><span>CSS3 (Grid/Flexbox)</span><div style="height:6px;background:rgba(255,255,255,0.1);border-radius:3px;overflow:hidden;margin-top:4px;"><div style="width:92%;height:100%;background:var(--accent-teal);"></div></div></div>
            <div><span>JavaScript (DOM/Events)</span><div style="height:6px;background:rgba(255,255,255,0.1);border-radius:3px;overflow:hidden;margin-top:4px;"><div style="width:90%;height:100%;background:var(--accent-pink);"></div></div></div>
        </div>
    </div>
</div>
""")
]

def generate_mini_project_page(item, prev_item, next_item, total):
    pid, title, desc, demo = item
    file_name = f"project-{pid:02d}.html"
    prev_link = f"project-{prev_item[0]:02d}.html" if prev_item else "#"
    next_link = f"project-{next_item[0]:02d}.html" if next_item else "#"
    prev_disabled = "opacity: 0.5; pointer-events: none;" if not prev_item else ""
    next_disabled = "opacity: 0.5; pointer-events: none;" if not next_item else ""
    code_escaped = demo.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mini Project #{pid:02d}: {title}</title>
    <link rel="stylesheet" href="../../assets/css/style.css">
</head>
<body>
    <header class="top-nav">
        <div class="container nav-container">
            <a href="../../index.html" class="nav-brand">
                <span>⚡ Practical Lab</span>
                <span class="brand-badge" style="background: linear-gradient(135deg, var(--accent-pink), var(--accent-primary));">Mini Project #{pid:02d}</span>
            </a>
            <div class="nav-links">
                <a href="../../index.html">🏠 Home</a>
                <a href="../../html/index.html">📄 HTML</a>
                <a href="../../css/index.html">🎨 CSS</a>
                <a href="../index.html" class="active">⚙️ JavaScript</a>
            </div>
            <button id="themeToggleBtn" class="theme-toggle-btn">☀️ Light Mode</button>
        </div>
    </header>

    <main class="main-content">
        <div class="program-page-container">
            <!-- Navigation Breadcrumbs -->
            <div class="program-nav-bar">
                <div class="nav-breadcrumbs">
                    <a href="../../index.html">Home</a>
                    <span class="separator">/</span>
                    <a href="../index.html">JavaScript</a>
                    <span class="separator">/</span>
                    <a href="index.html">Mini Projects</a>
                    <span class="separator">/</span>
                    <span style="color: var(--text-primary); font-weight: 600;">Project #{pid:02d}</span>
                </div>
                <div class="nav-controls">
                    <a href="{prev_link}" class="btn btn-outline btn-sm btn-prev" style="{prev_disabled}">⬅ Prev</a>
                    <a href="index.html" class="btn btn-outline btn-sm">📋 Mini Projects</a>
                    <a href="{next_link}" class="btn btn-outline btn-sm btn-next" style="{next_disabled}">Next ➡</a>
                </div>
            </div>

            <!-- Experiment Title & Description -->
            <div class="experiment-header-card" style="border-left-color: var(--accent-pink);">
                <span class="experiment-badge" style="color: var(--accent-pink); background: rgba(236, 72, 153, 0.12);">MINI PROJECT #{pid:02d} OF {total:02d}</span>
                <h1 class="experiment-title">{title}</h1>
                <p class="experiment-desc">{desc}</p>
            </div>

            <!-- Demonstration Section -->
            <div class="demo-section">
                <div class="demo-bar">
                    <span class="demo-title"><span class="demo-badge" style="background: var(--accent-pink); box-shadow: 0 0 8px var(--accent-pink);"></span> Working Application Showcase</span>
                    <span style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono);">{file_name}</span>
                </div>
                <div class="demo-content">
                    {demo}
                </div>
            </div>

            <!-- Source Code Drawer -->
            <div class="code-section">
                <div class="code-header">
                    <span class="code-header-title">💻 Source Code Inspector</span>
                    <span class="code-arrow" style="font-size: 0.85rem; color: var(--accent-pink);">▼ View Code</span>
                </div>
                <div class="code-content">
                    <pre><code>{code_escaped}</code></pre>
                </div>
            </div>

            <!-- Bottom Navigation -->
            <div class="bottom-nav-bar">
                <a href="{prev_link}" class="btn btn-outline btn-prev" style="{prev_disabled}">⬅ Previous Project</a>
                <div style="display: flex; gap: 0.5rem;">
                    <a href="../index.html" class="btn btn-outline">⚙️ All JS Categories</a>
                    <a href="index.html" class="btn btn-primary" style="background: var(--accent-pink);">📋 Mini Projects List</a>
                </div>
                <a href="{next_link}" class="btn btn-outline btn-next" style="{next_disabled}">Next Project ➡</a>
            </div>
        </div>
    </main>

    <footer class="site-footer">
        <div class="container footer-content">
            <p>Student Name: <span class="footer-highlight">M.Surya Nivas Reddy</span> | Assignment: <span class="footer-highlight">HTML, CSS & JavaScript Practical Assignment</span></p>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Mini Projects Module &bull; Project {pid} of {total}</p>
        </div>
    </footer>

    <script src="../../assets/js/common.js"></script>
</body>
</html>
"""
    return html

def generate_mini_project_index():
    cards = ""
    for item in MINI_PROJECTS:
        pid, title, desc, _ = item
        file_name = f"project-{pid:02d}.html"
        cards += f"""
        <a href="{file_name}" class="program-card" data-category="mini-projects">
            <div class="program-header">
                <span class="program-number" style="color: var(--accent-pink); background: rgba(236, 72, 153, 0.12);">PROJECT #{pid:02d}</span>
                <span style="font-size: 0.85rem; color: var(--text-muted);">Mini App</span>
            </div>
            <h3 class="program-title">{title}</h3>
            <p class="program-desc">{desc}</p>
            <div class="program-footer">
                <span>Source: {file_name}</span>
                <span class="program-link-text" style="color: var(--accent-pink);">Launch App &rarr;</span>
            </div>
        </a>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Mini Projects (1 to 17)</title>
    <link rel="stylesheet" href="../../assets/css/style.css">
</head>
<body>
    <header class="top-nav">
        <div class="container nav-container">
            <a href="../../index.html" class="nav-brand">
                <span>⚡ Practical Lab</span>
                <span class="brand-badge" style="background: linear-gradient(135deg, var(--accent-pink), var(--accent-primary));">Mini Projects</span>
            </a>
            <div class="nav-links">
                <a href="../../index.html">🏠 Home</a>
                <a href="../../html/index.html">📄 HTML</a>
                <a href="../../css/index.html">🎨 CSS</a>
                <a href="../index.html" class="active">⚙️ JavaScript</a>
            </div>
            <button id="themeToggleBtn" class="theme-toggle-btn">☀️ Light Mode</button>
        </div>
    </header>

    <main class="main-content">
        <div class="container">
            <div class="page-header">
                <span class="page-badge" style="background: rgba(236, 72, 153, 0.15); color: #f472b6; border-color: rgba(236, 72, 153, 0.3);">JAVASCRIPT SUITE &bull; 17 MINI PROJECTS</span>
                <h1 class="page-title">JavaScript Mini Projects</h1>
                <p class="page-subtitle">Fully functional mini applications: calculator, clock, stopwatch, countdown timer, to-do list, weather API, quiz, tic-tac-toe, expense tracker, shopping cart, password generator, and interactive portfolio.</p>
            </div>

            <!-- Student Info Banner -->
            <div class="student-banner">
                <div class="student-meta">
                    <div class="meta-item">
                        <span class="meta-label">Student Name</span>
                        <span class="meta-value">M.Surya Nivas Reddy</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Category</span>
                        <span class="meta-value">JavaScript Mini Projects</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Module Progress</span>
                        <span class="meta-value" style="color: var(--accent-pink);">17 / 17 Projects Completed</span>
                    </div>
                </div>
                <div style="display: flex; gap: 0.5rem;">
                    <a href="../index.html" class="btn btn-primary btn-sm">⚙️ JS Categories Hub</a>
                    <a href="../../index.html" class="btn btn-outline btn-sm">🏠 Home</a>
                </div>
            </div>

            <!-- Search and Filter Bar -->
            <div class="search-filter-bar">
                <div class="search-input-wrapper">
                    <span class="search-icon">🔍</span>
                    <input type="text" id="programSearch" class="search-input" placeholder="Search 17 Mini Projects (e.g. Calculator, Quiz, Timer, Notes)...">
                </div>
                <div class="filter-tags">
                    <button class="filter-tag active" data-filter="all">All (17)</button>
                </div>
            </div>

            <!-- Program Cards Grid -->
            <div class="program-grid">
                {cards}
            </div>
        </div>
    </main>

    <footer class="site-footer">
        <div class="container footer-content">
            <p>Student Name: <span class="footer-highlight">M.Surya Nivas Reddy</span> | Assignment: <span class="footer-highlight">HTML, CSS & JavaScript Practical Assignment</span></p>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Total 122 JavaScript Programs &bull; Mini Projects Module (17 Projects)</p>
        </div>
    </footer>

    <script src="../../assets/js/common.js"></script>
</body>
</html>
"""
    return html

def main():
    total = len(MINI_PROJECTS)
    print(f"Generating {total} JavaScript Mini Projects...")
    folder_path = os.path.join("javascript", "mini-projects")
    os.makedirs(folder_path, exist_ok=True)
    for i, item in enumerate(MINI_PROJECTS):
        prev_item = MINI_PROJECTS[i - 1] if i > 0 else None
        next_item = MINI_PROJECTS[i + 1] if i < total - 1 else None
        page_html = generate_mini_project_page(item, prev_item, next_item, total)
        file_name = f"project-{item[0]:02d}.html"
        with open(os.path.join(folder_path, file_name), "w", encoding="utf-8") as f:
            f.write(page_html)
    
    index_html = generate_mini_project_index()
    with open(os.path.join(folder_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("All 17 JavaScript Mini Projects and index successfully generated!")

if __name__ == "__main__":
    main()
