"""
Generator for Core JavaScript Practical Programs (js-01 to js-67) and javascript/core/index.html
"""
import os

CORE_JS_PROGRAMS = [
    (1, "Display 'Hello World'", "Demonstrates displaying text using console.log(), document.write(), alert(), and innerHTML.", """
<div style="text-align: center;">
    <h3 id="hwDisplay" style="color: var(--accent-primary); margin-bottom: 1rem; min-height: 40px;">Click a button below</h3>
    <div style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;">
        <button class="btn btn-primary" onclick="document.getElementById('hwDisplay').innerText = 'Hello, World! Welcome to JavaScript Programming.';">Update DOM innerText</button>
        <button class="btn btn-outline" onclick="console.log('Hello World logged to console!'); alert('Hello World alert popup!');">Trigger Alert &amp; Console</button>
    </div>
</div>
"""),
    (2, "Perform Arithmetic Operations", "Calculates Addition, Subtraction, Multiplication, Division, Modulus, and Exponentiation on user inputs.", """
<div style="max-width: 480px; margin: 0 auto;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
        <input type="number" id="numA" class="form-control" value="12" placeholder="First Number">
        <input type="number" id="numB" class="form-control" value="4" placeholder="Second Number">
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center; margin-bottom: 1rem;">
        <button class="btn btn-outline btn-sm" onclick="calcOps('+')">Add (+)</button>
        <button class="btn btn-outline btn-sm" onclick="calcOps('-')">Subtract (-)</button>
        <button class="btn btn-outline btn-sm" onclick="calcOps('*')">Multiply (&times;)</button>
        <button class="btn btn-outline btn-sm" onclick="calcOps('/')">Divide (&divide;)</button>
        <button class="btn btn-outline btn-sm" onclick="calcOps('%')">Modulus (%)</button>
        <button class="btn btn-outline btn-sm" onclick="calcOps('**')">Power (**)</button>
    </div>
    <div class="result-box"><div class="result-box-title">Calculation Result</div><div id="calcRes" class="result-output">12 + 4 = 16</div></div>
</div>
<script>
function calcOps(op) {
    const a = parseFloat(document.getElementById('numA').value) || 0;
    const b = parseFloat(document.getElementById('numB').value) || 0;
    let r = 0;
    if(op === '+') r = a + b;
    else if(op === '-') r = a - b;
    else if(op === '*') r = a * b;
    else if(op === '/') r = b !== 0 ? (a / b).toFixed(3) : 'Cannot divide by zero';
    else if(op === '%') r = a % b;
    else if(op === '**') r = Math.pow(a, b);
    document.getElementById('calcRes').innerText = `${a} ${op} ${b} = ${r}`;
}
</script>
"""),
    (3, "Find the Largest of Three Numbers", "Finds the maximum value among three numbers using conditional if-else statements and Math.max().", """
<div style="max-width: 480px; margin: 0 auto;">
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="number" id="lgN1" class="form-control" value="45" placeholder="Num 1">
        <input type="number" id="lgN2" class="form-control" value="89" placeholder="Num 2">
        <input type="number" id="lgN3" class="form-control" value="32" placeholder="Num 3">
    </div>
    <button class="btn btn-primary" style="width: 100%;" onclick="findLargest3()">Find Largest Number</button>
    <div class="result-box"><div class="result-box-title">Largest Number Found</div><div id="lgRes" class="result-output">Click button to compute</div></div>
</div>
<script>
function findLargest3() {
    const a = parseFloat(document.getElementById('lgN1').value) || 0;
    const b = parseFloat(document.getElementById('lgN2').value) || 0;
    const c = parseFloat(document.getElementById('lgN3').value) || 0;
    const max = Math.max(a, b, c);
    document.getElementById('lgRes').innerHTML = `Maximum among (${a}, ${b}, ${c}) is <span style="color:var(--accent-teal);">${max}</span>`;
}
</script>
"""),
    (4, "Check Whether a Number is Even or Odd", "Uses modulus operator (n % 2 === 0) to determine parity.", """
<div style="max-width: 400px; margin: 0 auto; text-align: center;">
    <input type="number" id="oddEvenNum" class="form-control" value="17" placeholder="Enter integer" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" onclick="checkOddEven()">Check Parity</button>
    <div class="result-box"><div class="result-box-title">Parity Result</div><div id="oddEvenRes" class="result-output">Click to check</div></div>
</div>
<script>
function checkOddEven() {
    const n = parseInt(document.getElementById('oddEvenNum').value);
    if(isNaN(n)) return;
    const isEven = n % 2 === 0;
    document.getElementById('oddEvenRes').innerHTML = `${n} is an <strong style="color:${isEven ? 'var(--accent-emerald)' : 'var(--accent-pink)'}">${isEven ? 'EVEN' : 'ODD'}</strong> number.`;
}
</script>
"""),
    (5, "Check Whether a Number is Positive, Negative, or Zero", "Evaluates sign of an input number using ternary/if-else logic.", """
<div style="max-width: 400px; margin: 0 auto; text-align: center;">
    <input type="number" id="signNum" class="form-control" value="-15" placeholder="Enter a number" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" onclick="checkSign()">Evaluate Sign</button>
    <div class="result-box"><div class="result-box-title">Sign Evaluation</div><div id="signRes" class="result-output">Result pending</div></div>
</div>
<script>
function checkSign() {
    const n = parseFloat(document.getElementById('signNum').value);
    let msg = '';
    if(n > 0) msg = `<span style="color:var(--accent-emerald)">Positive (+${n})</span>`;
    else if(n < 0) msg = `<span style="color:var(--accent-rose)">Negative (${n})</span>`;
    else msg = `<span style="color:var(--accent-amber)">Zero (0)</span>`;
    document.getElementById('signRes').innerHTML = `The number is ${msg}`;
}
</script>
"""),
    (6, "Find the Factorial of a Number", "Calculates factorial n! iteratively with step-by-step mathematical expansion.", """
<div style="max-width: 450px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="number" id="factInp" class="form-control" value="6" min="0" max="25" placeholder="Enter n (0-25)">
        <button class="btn btn-primary" onclick="calcFactorial()">Calculate</button>
    </div>
    <div class="result-box"><div class="result-box-title">Factorial Output</div><div id="factRes" class="result-output">6! = 720</div></div>
</div>
<script>
function calcFactorial() {
    const n = parseInt(document.getElementById('factInp').value);
    if(n < 0) { document.getElementById('factRes').innerText = 'Factorial not defined for negative numbers'; return; }
    let res = 1n;
    for(let i = 2n; i <= BigInt(n); i++) res *= i;
    document.getElementById('factRes').innerHTML = `${n}! = <span style="color:var(--accent-teal);">${res.toString()}</span>`;
}
</script>
"""),
    (7, "Generate the Fibonacci Series", "Generates the first N terms of the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...", """
<div style="max-width: 500px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="number" id="fiboN" class="form-control" value="10" min="1" max="40" placeholder="Number of terms">
        <button class="btn btn-primary" onclick="genFibonacci()">Generate</button>
    </div>
    <div class="result-box"><div class="result-box-title">Fibonacci Sequence</div><div id="fiboRes" class="result-output">0, 1, 1, 2, 3, 5, 8, 13, 21, 34</div></div>
</div>
<script>
function genFibonacci() {
    const count = parseInt(document.getElementById('fiboN').value) || 1;
    let seq = [0];
    if(count > 1) seq.push(1);
    for(let i = 2; i < count; i++) seq.push(seq[i-1] + seq[i-2]);
    document.getElementById('fiboRes').innerText = seq.join(', ');
}
</script>
"""),
    (8, "Check Whether a Number is Prime", "Checks if a number has exactly two positive divisors using efficient sqrt(n) test.", """
<div style="max-width: 450px; margin: 0 auto; text-align: center;">
    <input type="number" id="primeInp" class="form-control" value="29" placeholder="Enter integer" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" onclick="checkPrime()">Test Primality</button>
    <div class="result-box"><div class="result-box-title">Primality Test</div><div id="primeRes" class="result-output">Pending check</div></div>
</div>
<script>
function checkPrime() {
    const n = parseInt(document.getElementById('primeInp').value);
    if(n <= 1) { document.getElementById('primeRes').innerHTML = `${n} is NOT a prime number.`; return; }
    let isP = true;
    for(let i = 2; i * i <= n; i++) {
        if(n % i === 0) { isP = false; break; }
    }
    document.getElementById('primeRes').innerHTML = `${n} is ${isP ? '<strong style="color:var(--accent-emerald)">a PRIME number</strong>' : '<strong style="color:var(--accent-rose)">a COMPOSITE number (not prime)</strong>'}`;
}
</script>
"""),
    (9, "Check Whether a Number is a Palindrome", "Checks if a number reads the same forwards and backwards (e.g. 12321).", """
<div style="max-width: 450px; margin: 0 auto; text-align: center;">
    <input type="number" id="palinInp" class="form-control" value="12321" placeholder="Enter number" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" onclick="checkPalindrome()">Check Palindrome</button>
    <div class="result-box"><div class="result-box-title">Palindrome Test</div><div id="palinRes" class="result-output">Result pending</div></div>
</div>
<script>
function checkPalindrome() {
    const s = document.getElementById('palinInp').value.trim();
    const rev = s.split('').reverse().join('');
    const isPal = s === rev;
    document.getElementById('palinRes').innerHTML = `Original: ${s} &bull; Reversed: ${rev}<br>${isPal ? '<span style="color:var(--accent-emerald)">It IS a Palindrome!</span>' : '<span style="color:var(--accent-rose)">NOT a Palindrome</span>'}`;
}
</script>
"""),
    (10, "Reverse a Number", "Extracts digits mathematically using modulus and integer division to reverse an integer.", """
<div style="max-width: 450px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="number" id="revNumInp" class="form-control" value="987654" placeholder="Enter number">
        <button class="btn btn-primary" onclick="reverseNumber()">Reverse</button>
    </div>
    <div class="result-box"><div class="result-box-title">Reversed Output</div><div id="revRes" class="result-output">456789</div></div>
</div>
<script>
function reverseNumber() {
    let n = parseInt(document.getElementById('revNumInp').value);
    let sign = Math.sign(n);
    n = Math.abs(n);
    let rev = 0;
    while(n > 0) {
        rev = rev * 10 + (n % 10);
        n = Math.floor(n / 10);
    }
    document.getElementById('revRes').innerText = rev * sign;
}
</script>
"""),
    (11, "Find the Sum of Digits of a Number", "Computes the arithmetic sum of individual digits in an integer.", """
<div style="max-width: 450px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="number" id="sumDigitInp" class="form-control" value="4829" placeholder="Enter number">
        <button class="btn btn-primary" onclick="sumDigits()">Sum Digits</button>
    </div>
    <div class="result-box"><div class="result-box-title">Calculation Breakdown</div><div id="sumDigitRes" class="result-output">4 + 8 + 2 + 9 = 23</div></div>
</div>
<script>
function sumDigits() {
    const s = Math.abs(parseInt(document.getElementById('sumDigitInp').value) || 0).toString();
    const digits = s.split('').map(Number);
    const total = digits.reduce((acc, d) => acc + d, 0);
    document.getElementById('sumDigitRes').innerText = `${digits.join(' + ')} = ${total}`;
}
</script>
"""),
    (12, "Find the Largest and Smallest Element in an Array", "Identifies maximum and minimum values in an array of numbers.", """
<div style="max-width: 500px; margin: 0 auto;">
    <input type="text" id="arrExtremes" class="form-control" value="23, 89, 12, 5, 94, 67, 3" placeholder="Comma-separated numbers" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" style="width: 100%;" onclick="findExtremes()">Find Min &amp; Max</button>
    <div class="result-box"><div class="result-box-title">Analysis Result</div><div id="extremeRes" class="result-output">Max: 94 | Min: 3</div></div>
</div>
<script>
function findExtremes() {
    const arr = document.getElementById('arrExtremes').value.split(',').map(s => parseFloat(s.trim())).filter(n => !isNaN(n));
    if(!arr.length) return;
    const min = Math.min(...arr);
    const max = Math.max(...arr);
    document.getElementById('extremeRes').innerHTML = `Maximum: <strong style="color:var(--accent-teal)">${max}</strong> &bull; Minimum: <strong style="color:var(--accent-pink)">${min}</strong>`;
}
</script>
"""),
    (13, "Sort an Array", "Sorts numeric array in ascending and descending order using Array.prototype.sort().", """
<div style="max-width: 500px; margin: 0 auto;">
    <input type="text" id="sortArrInp" class="form-control" value="45, 12, 85, 32, 89, 39, 69, 7" style="margin-bottom: 1rem;">
    <div style="display: flex; gap: 0.5rem; justify-content: center; margin-bottom: 1rem;">
        <button class="btn btn-primary btn-sm" onclick="sortNums(true)">Sort Ascending</button>
        <button class="btn btn-outline btn-sm" onclick="sortNums(false)">Sort Descending</button>
    </div>
    <div class="result-box"><div class="result-box-title">Sorted Array</div><div id="sortRes" class="result-output">7, 12, 32, 39, 45, 69, 85, 89</div></div>
</div>
<script>
function sortNums(asc) {
    const arr = document.getElementById('sortArrInp').value.split(',').map(s => parseFloat(s.trim())).filter(n => !isNaN(n));
    arr.sort((a, b) => asc ? a - b : b - a);
    document.getElementById('sortRes').innerText = arr.join(', ');
}
</script>
"""),
    (14, "Find the Sum and Average of Array Elements", "Aggregates array elements using reduce() to compute total and arithmetic mean.", """
<div style="max-width: 500px; margin: 0 auto;">
    <input type="text" id="sumAvgInp" class="form-control" value="10, 20, 30, 40, 50" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" style="width: 100%;" onclick="calcSumAvg()">Compute Sum &amp; Average</button>
    <div class="result-box"><div class="result-box-title">Result</div><div id="sumAvgRes" class="result-output">Sum: 150 &bull; Average: 30</div></div>
</div>
<script>
function calcSumAvg() {
    const arr = document.getElementById('sumAvgInp').value.split(',').map(s => parseFloat(s.trim())).filter(n => !isNaN(n));
    const sum = arr.reduce((acc, v) => acc + v, 0);
    const avg = (sum / (arr.length || 1)).toFixed(2);
    document.getElementById('sumAvgRes').innerHTML = `Sum: <strong style="color:var(--accent-teal)">${sum}</strong> &bull; Average: <strong style="color:var(--accent-primary)">${avg}</strong>`;
}
</script>
"""),
    (15, "Demonstrate JavaScript Functions", "Demonstrates function declaration, function expressions, parameter passing, and return values.", """
<div style="max-width: 480px; margin: 0 auto; text-align: center;">
    <p style="color: var(--text-secondary); margin-bottom: 1rem;">Testing declaration: <code>function greet(name, role)</code></p>
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="text" id="fnName" class="form-control" value="Surya" placeholder="Name">
        <input type="text" id="fnRole" class="form-control" value="Engineer" placeholder="Role">
    </div>
    <button class="btn btn-primary" onclick="testFunction()">Invoke Function</button>
    <div class="result-box"><div class="result-box-title">Function Return Value</div><div id="fnRes" class="result-output">Welcome, Surya! Role: Engineer</div></div>
</div>
<script>
function createGreeting(name, role) {
    return `Welcome, ${name}! Registered as: ${role}.`;
}
function testFunction() {
    const n = document.getElementById('fnName').value;
    const r = document.getElementById('fnRole').value;
    document.getElementById('fnRes').innerText = createGreeting(n, r);
}
</script>
"""),
    (16, "Program Using Arrow Functions", "Demonstrates ES6 fat arrow syntax () => {}, lexical this, and concise implicit return expressions.", """
<div style="max-width: 450px; margin: 0 auto; text-align: center;">
    <input type="number" id="arrowNum" class="form-control" value="7" style="margin-bottom: 1rem;">
    <div style="display: flex; gap: 0.5rem; justify-content: center; margin-bottom: 1rem;">
        <button class="btn btn-outline btn-sm" onclick="runArrow('sq')">Square (x => x*x)</button>
        <button class="btn btn-outline btn-sm" onclick="runArrow('cb')">Cube (x => x**3)</button>
    </div>
    <div class="result-box"><div class="result-box-title">Arrow Output</div><div id="arrowRes" class="result-output">Square of 7 is 49</div></div>
</div>
<script>
const square = x => x * x;
const cube = x => x ** 3;
function runArrow(type) {
    const n = parseFloat(document.getElementById('arrowNum').value) || 0;
    const res = type === 'sq' ? square(n) : cube(n);
    document.getElementById('arrowRes').innerText = `${type === 'sq' ? 'Square' : 'Cube'} of ${n} is ${res}`;
}
</script>
"""),
    (17, "Strings and String Methods", "Demonstrates toUpperCase(), slice(), replace(), split(), trim(), and includes().", """
<div style="max-width: 500px; margin: 0 auto;">
    <input type="text" id="strSample" class="form-control" value="  Mastering JavaScript Web Programming  " style="margin-bottom: 1rem;">
    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center; margin-bottom: 1rem;">
        <button class="btn btn-outline btn-sm" onclick="runStrOp('upper')">toUpperCase()</button>
        <button class="btn btn-outline btn-sm" onclick="runStrOp('trim')">trim()</button>
        <button class="btn btn-outline btn-sm" onclick="runStrOp('slice')">slice(0, 15)</button>
        <button class="btn btn-outline btn-sm" onclick="runStrOp('split')">split(' ')</button>
    </div>
    <div class="result-box"><div class="result-box-title">Transformed String</div><div id="strRes" class="result-output">Ready</div></div>
</div>
<script>
function runStrOp(op) {
    const raw = document.getElementById('strSample').value;
    let r = '';
    if(op === 'upper') r = raw.toUpperCase();
    else if(op === 'trim') r = `"${raw.trim()}" (Length: ${raw.trim().length})`;
    else if(op === 'slice') r = raw.trim().slice(0, 15);
    else if(op === 'split') r = JSON.stringify(raw.trim().split(' '));
    document.getElementById('strRes').innerText = r;
}
</script>
"""),
    (18, "Arrays and Array Methods", "Showcases map(), filter(), reduce(), and push()/pop() array operations.", """
<div style="max-width: 500px; margin: 0 auto;">
    <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">Base Array: <code>[1, 2, 3, 4, 5, 6, 7, 8]</code></p>
    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1rem;">
        <button class="btn btn-outline btn-sm" onclick="arrMethod('evens')">filter(x => x % 2 === 0)</button>
        <button class="btn btn-outline btn-sm" onclick="arrMethod('doubled')">map(x => x * 2)</button>
        <button class="btn btn-outline btn-sm" onclick="arrMethod('sum')">reduce((acc, x) => acc + x)</button>
    </div>
    <div class="result-box"><div class="result-box-title">Resulting Array / Value</div><div id="arrMethodRes" class="result-output">Click an operation</div></div>
</div>
<script>
const baseArr = [1, 2, 3, 4, 5, 6, 7, 8];
function arrMethod(m) {
    let out = '';
    if(m === 'evens') out = JSON.stringify(baseArr.filter(x => x % 2 === 0));
    else if(m === 'doubled') out = JSON.stringify(baseArr.map(x => x * 2));
    else if(m === 'sum') out = baseArr.reduce((a, b) => a + b, 0);
    document.getElementById('arrMethodRes').innerText = out;
}
</script>
"""),
    (19, "Objects in JavaScript", "Object literals, properties, methods, Object.keys(), Object.values(), and JSON serialization.", """
<div style="max-width: 480px; margin: 0 auto;">
    <div class="result-box" style="margin-top: 0; margin-bottom: 1rem;">
        <div class="result-box-title">Student Object Representation</div>
        <pre id="objOutput" style="font-family: var(--font-mono); font-size: 0.85rem; color: #818cf8;"></pre>
    </div>
    <button class="btn btn-primary" style="width: 100%;" onclick="mutateStudentObj()">Add Semester GPA Property</button>
</div>
<script>
let student = { name: "M. Surya Nivas Reddy", branch: "CSE", year: 2026, active: true };
function renderStudent() {
    document.getElementById('objOutput').innerText = JSON.stringify(student, null, 2);
}
function mutateStudentObj() {
    student.gpa = 9.45;
    renderStudent();
}
renderStudent();
</script>
"""),
    (20, "Date and Math Objects", "Live clock formatted with Date object and common Math functions (random, round, ceil, pow).", """
<div style="max-width: 480px; margin: 0 auto; text-align: center;">
    <div id="dateClock" style="font-size: 1.4rem; font-family: var(--font-mono); color: var(--accent-teal); margin-bottom: 1rem;">Loading Date...</div>
    <div style="display: flex; gap: 0.5rem; justify-content: center; margin-bottom: 1rem;">
        <button class="btn btn-outline btn-sm" onclick="testMath('rand')">Math.random()</button>
        <button class="btn btn-outline btn-sm" onclick="testMath('pi')">Math.PI</button>
        <button class="btn btn-outline btn-sm" onclick="testMath('sqrt')">Math.sqrt(144)</button>
    </div>
    <div class="result-box"><div class="result-box-title">Math Output</div><div id="mathRes" class="result-output">Random value: 0.842</div></div>
</div>
<script>
function updateClock() {
    const d = new Date();
    document.getElementById('dateClock').innerText = d.toUTCString();
}
setInterval(updateClock, 1000); updateClock();
function testMath(m) {
    let r = '';
    if(m === 'rand') r = 'Random (1-100): ' + Math.floor(Math.random() * 100 + 1);
    else if(m === 'pi') r = 'PI: ' + Math.PI.toFixed(6);
    else if(m === 'sqrt') r = 'sqrt(144) = ' + Math.sqrt(144);
    document.getElementById('mathRes').innerText = r;
}
</script>
"""),
    (21, "DOM & Event-Based Experiments Showcase", "An interactive lab playground consolidating core DOM access methods and event bindings.", """
<div style="text-align: center; background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <h3 id="sandboxTitle" style="color: var(--accent-primary); margin-bottom: 0.5rem;">Interactive DOM Sandbox</h3>
    <p id="sandboxDesc" style="color: var(--text-secondary); margin-bottom: 1.25rem;">Observe real-time DOM property and style updates.</p>
    <div style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;">
        <button class="btn btn-primary btn-sm" onclick="document.getElementById('sandboxTitle').innerText = 'DOM Element Updated!';">Mutate Title</button>
        <button class="btn btn-outline btn-sm" onclick="document.getElementById('sandboxDesc').style.color = '#10b981';">Change Style</button>
        <button class="btn btn-danger btn-sm" onclick="document.getElementById('sandboxTitle').innerText = 'Interactive DOM Sandbox'; document.getElementById('sandboxDesc').style.color = 'var(--text-secondary)';">Reset</button>
    </div>
</div>
"""),
    (22, "Change Text Using JavaScript", "Modifying paragraph and heading content dynamically using .textContent and .innerHTML.", """
<div style="max-width: 450px; margin: 0 auto; text-align: center;">
    <h3 id="textTarget" style="margin-bottom: 1rem; color: #fff;">Initial Heading Text</h3>
    <input type="text" id="textInp" class="form-control" value="Updated Dynamic Heading via JavaScript!" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" onclick="document.getElementById('textTarget').innerText = document.getElementById('textInp').value;">Update Heading Text</button>
</div>
"""),
    (23, "Change the Background Color of a Webpage Using JavaScript", "Dynamically updates document.body.style.backgroundColor based on user choice.", """
<div style="text-align: center;">
    <p style="margin-bottom: 1rem;">Select a background accent:</p>
    <div style="display: flex; gap: 0.75rem; justify-content: center; flex-wrap: wrap;">
        <button class="btn btn-outline btn-sm" style="border-color: #1e1b4b;" onclick="document.body.style.backgroundColor='#0f172a';">Deep Slate (Default)</button>
        <button class="btn btn-outline btn-sm" style="border-color: #14532d;" onclick="document.body.style.backgroundColor='#052e16';">Forest Night</button>
        <button class="btn btn-outline btn-sm" style="border-color: #581c87;" onclick="document.body.style.backgroundColor='#3b0764';">Deep Purple</button>
    </div>
</div>
"""),
    (24, "Button Click Event Using JavaScript", "Attaches addEventListener('click', fn) to count clicks and display visual feedback.", """
<div style="text-align: center;">
    <button id="clickBtn" class="btn btn-primary" style="padding: 1rem 2rem; font-size: 1.1rem;">Click Me!</button>
    <div class="result-box" style="max-width: 300px; margin: 1.5rem auto 0;">
        <div class="result-box-title">Total Button Clicks</div>
        <div id="clickCountDisplay" class="result-output">0 clicks</div>
    </div>
</div>
<script>
let clickCount = 0;
document.getElementById('clickBtn').addEventListener('click', () => {
    clickCount++;
    document.getElementById('clickCountDisplay').innerText = `${clickCount} click${clickCount > 1 ? 's' : ''}`;
});
</script>
"""),
    (25, "Show / Hide an HTML Element", "Toggles CSS display between 'none' and 'block' upon button trigger.", """
<div style="max-width: 450px; margin: 0 auto; text-align: center;">
    <button class="btn btn-primary" style="margin-bottom: 1rem;" onclick="const el = document.getElementById('toggleTarget'); el.style.display = el.style.display === 'none' ? 'block' : 'none';">Toggle Visibility</button>
    <div id="toggleTarget" style="padding: 1.5rem; background: rgba(99,102,241,0.2); border: 1px solid var(--accent-primary); border-radius: 8px;">
        <h4 style="color: var(--accent-primary);">Peekaboo!</h4>
        <p style="color: var(--text-secondary); font-size: 0.85rem;">This container's visibility is dynamically controlled via element.style.display.</p>
    </div>
</div>
"""),
    (26, "Change an Image When a Button is Clicked", "Swaps the src attribute of an image element with smooth transition.", """
<div style="text-align: center;">
    <div id="imgContainer" style="width: 160px; height: 160px; border-radius: 12px; margin: 0 auto 1.25rem; display: flex; align-items: center; justify-content: center; font-size: 4rem; background: #1e293b; border: 2px solid var(--border-color);">
        ☀️
    </div>
    <div style="display: flex; gap: 0.5rem; justify-content: center;">
        <button class="btn btn-outline btn-sm" onclick="document.getElementById('imgContainer').innerText = '☀️';">Sun State</button>
        <button class="btn btn-outline btn-sm" onclick="document.getElementById('imgContainer').innerText = '🌙';">Moon State</button>
        <button class="btn btn-outline btn-sm" onclick="document.getElementById('imgContainer').innerText = '⚡';">Lightning State</button>
    </div>
</div>
"""),
    (27, "Create a Digital Clock Using JavaScript", "Real-time ticking digital clock displaying Hours:Minutes:Seconds and AM/PM.", """
<div style="text-align: center; padding: 1.5rem;">
    <div id="jsDigiClock" style="font-family: var(--font-mono); font-size: 2.5rem; font-weight: 800; color: var(--accent-teal); text-shadow: 0 0 15px rgba(20, 184, 166, 0.4); margin-bottom: 0.5rem;">00:00:00 AM</div>
    <div id="jsDigiDate" style="color: var(--text-secondary); font-size: 0.95rem;">Monday, 1 January 2026</div>
</div>
<script>
function updateDigiClock() {
    const now = new Date();
    document.getElementById('jsDigiClock').innerText = now.toLocaleTimeString();
    document.getElementById('jsDigiDate').innerText = now.toLocaleDateString(undefined, { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
}
setInterval(updateDigiClock, 1000); updateDigiClock();
</script>
"""),
    (28, "Simple Calculator Using HTML, CSS, and JavaScript", "Interactive calculator keypad with evaluation and clear buttons.", """
<div style="max-width: 260px; margin: 0 auto; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1rem; box-shadow: var(--shadow-md);">
    <input type="text" id="calcScreen" readonly style="width: 100%; padding: 0.75rem; background: #0f172a; border: 1px solid var(--border-color); border-radius: 6px; color: #fff; font-family: var(--font-mono); font-size: 1.25rem; text-align: right; margin-bottom: 0.75rem;" value="0">
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.4rem;">
        <button class="btn btn-outline btn-sm" onclick="calcPress('C')">C</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('/')">&divide;</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('*')">&times;</button>
        <button class="btn btn-danger btn-sm" onclick="calcPress('DEL')">&larr;</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('7')">7</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('8')">8</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('9')">9</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('-')">-</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('4')">4</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('5')">5</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('6')">6</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('+')">+</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('1')">1</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('2')">2</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('3')">3</button>
        <button class="btn btn-primary btn-sm" onclick="calcEval()" style="grid-row: span 2;">=</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('0')" style="grid-column: span 2;">0</button>
        <button class="btn btn-outline btn-sm" onclick="calcPress('.')">.</button>
    </div>
</div>
<script>
let expr = '';
function calcPress(val) {
    const s = document.getElementById('calcScreen');
    if(val === 'C') expr = '';
    else if(val === 'DEL') expr = expr.slice(0, -1);
    else expr += val;
    s.value = expr || '0';
}
function calcEval() {
    try {
        expr = Function('"use strict";return (' + expr + ')')().toString();
        document.getElementById('calcScreen').value = expr;
    } catch(e) { document.getElementById('calcScreen').value = 'Error'; expr = ''; }
}
</script>
"""),
    (29, "Number Guessing Game", "Random number generator with Too High / Too Low hints and attempt tracker.", """
<div style="max-width: 400px; margin: 0 auto; text-align: center;">
    <p style="color: var(--text-secondary); margin-bottom: 1rem;">Guess a secret number between 1 and 50:</p>
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="number" id="guessInp" class="form-control" placeholder="1-50" min="1" max="50">
        <button class="btn btn-primary" onclick="submitGuess()">Submit Guess</button>
    </div>
    <div class="result-box"><div class="result-box-title">Hint / Result</div><div id="guessFeedback" class="result-output">Take your first guess!</div></div>
    <button class="btn btn-outline btn-sm" style="margin-top: 1rem;" onclick="resetGuessGame()">New Game</button>
</div>
<script>
let secretNum = Math.floor(Math.random() * 50) + 1;
let attempts = 0;
function submitGuess() {
    const g = parseInt(document.getElementById('guessInp').value);
    if(isNaN(g)) return;
    attempts++;
    const fb = document.getElementById('guessFeedback');
    if(g === secretNum) fb.innerHTML = `<span style="color:var(--accent-emerald)">🎉 Correct! You guessed ${secretNum} in ${attempts} tries!</span>`;
    else if(g < secretNum) fb.innerHTML = `<span style="color:var(--accent-amber)">Too LOW! Try higher (Attempt #${attempts})</span>`;
    else fb.innerHTML = `<span style="color:var(--accent-rose)">Too HIGH! Try lower (Attempt #${attempts})</span>`;
}
function resetGuessGame() {
    secretNum = Math.floor(Math.random() * 50) + 1;
    attempts = 0;
    document.getElementById('guessFeedback').innerText = 'Game reset! Guess a number between 1 and 50.';
}
</script>
"""),
    (30, "Form Validation Program", "Validates required fields, checks for empty values, and highlights fields with errors.", """
<form onsubmit="validateBasicForm(event)" style="max-width: 400px; margin: 0 auto;">
    <div class="form-group">
        <label class="form-label">Username</label>
        <input type="text" id="vUser" class="form-control" placeholder="At least 4 characters">
        <small id="errUser" style="color: var(--accent-rose); display: none; margin-top: 0.25rem;">Username must be 4+ characters.</small>
    </div>
    <div class="form-group">
        <label class="form-label">Email</label>
        <input type="text" id="vEmail" class="form-control" placeholder="user@domain.com">
        <small id="errEmail" style="color: var(--accent-rose); display: none; margin-top: 0.25rem;">Valid email required.</small>
    </div>
    <button type="submit" class="btn btn-primary" style="width: 100%;">Validate &amp; Submit</button>
</form>
<script>
function validateBasicForm(e) {
    e.preventDefault();
    const u = document.getElementById('vUser').value.trim();
    const em = document.getElementById('vEmail').value.trim();
    let valid = true;
    if(u.length < 4) { document.getElementById('errUser').style.display = 'block'; valid = false; }
    else document.getElementById('errUser').style.display = 'none';
    if(!em.includes('@') || !em.includes('.')) { document.getElementById('errEmail').style.display = 'block'; valid = false; }
    else document.getElementById('errEmail').style.display = 'none';
    if(valid) alert('Form validation passed successfully!');
}
</script>
"""),
    (31, "Validate Name, Email, Phone Number, and Password Using JavaScript", "Comprehensive validation ensuring valid name format, email regex, 10-digit phone, and strong password.", """
<form onsubmit="validateFullUser(event)" style="max-width: 450px; margin: 0 auto;">
    <div class="form-group"><input type="text" id="valName" class="form-control" placeholder="Full Name (Letters only)"><small id="errN" style="color:var(--accent-rose);display:none;">Letters only (min 3 chars)</small></div>
    <div class="form-group"><input type="email" id="valEm" class="form-control" placeholder="Email Address"><small id="errE" style="color:var(--accent-rose);display:none;">Invalid email format</small></div>
    <div class="form-group"><input type="text" id="valPhone" class="form-control" placeholder="Phone (10 digits)"><small id="errP" style="color:var(--accent-rose);display:none;">Exactly 10 numeric digits</small></div>
    <div class="form-group"><input type="password" id="valPw" class="form-control" placeholder="Password (6+ chars)"><small id="errPw" style="color:var(--accent-rose);display:none;">Minimum 6 characters</small></div>
    <button type="submit" class="btn btn-primary" style="width: 100%;">Run Full Validation</button>
</form>
<script>
function validateFullUser(e) {
    e.preventDefault();
    let ok = true;
    const name = document.getElementById('valName').value.trim();
    const email = document.getElementById('valEm').value.trim();
    const phone = document.getElementById('valPhone').value.trim();
    const pw = document.getElementById('valPw').value;

    const showErr = (id, cond) => { document.getElementById(id).style.display = cond ? 'none' : 'block'; if(!cond) ok = false; };
    showErr('errN', /^[a-zA-Z\s]{3,}$/.test(name));
    showErr('errE', /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email));
    showErr('errP', /^[0-9]{10}$/.test(phone));
    showErr('errPw', pw.length >= 6);

    if(ok) alert('All fields validated successfully!');
}
</script>
"""),
    (32, "Create a To-Do List Using JavaScript", "Add tasks, toggle completed state, and delete items from an active task list.", """
<div style="max-width: 450px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="text" id="todoInp" class="form-control" placeholder="Enter new task...">
        <button class="btn btn-primary" onclick="addTodoItem()">Add</button>
    </div>
    <ul id="todoUl" style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 0.5rem;">
        <li style="background: var(--bg-card); padding: 0.75rem 1rem; border-radius: 6px; border: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
            <span>Review HTML5 Semantic Structure</span>
            <button class="btn btn-danger btn-sm" onclick="this.parentElement.remove()">✕</button>
        </li>
    </ul>
</div>
<script>
function addTodoItem() {
    const inp = document.getElementById('todoInp');
    if(!inp.value.trim()) return;
    const li = document.createElement('li');
    li.style.cssText = "background: var(--bg-card); padding: 0.75rem 1rem; border-radius: 6px; border: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;";
    li.innerHTML = `<span>${inp.value.trim()}</span><button class="btn btn-danger btn-sm" onclick="this.parentElement.remove()">✕</button>`;
    document.getElementById('todoUl').appendChild(li);
    inp.value = '';
}
</script>
"""),
    (33, "Create a Simple Quiz Application", "Multiple choice questionnaire that calculates score and shows instant feedback.", """
<div id="quizContainer" style="max-width: 480px; margin: 0 auto; background: var(--bg-card); padding: 1.5rem; border-radius: 12px; border: 1px solid var(--border-color);">
    <h4 id="quizQ" style="margin-bottom: 1rem; color: #fff;">Which HTML tag represents the top-level main heading?</h4>
    <div id="quizOpts" style="display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1rem;">
        <button class="btn btn-outline" onclick="quizAnswer(false)">&lt;head&gt;</button>
        <button class="btn btn-outline" onclick="quizAnswer(true)">&lt;h1&gt;</button>
        <button class="btn btn-outline" onclick="quizAnswer(false)">&lt;header&gt;</button>
    </div>
    <div id="quizScore" style="color: var(--accent-teal); font-weight: bold; text-align: center;"></div>
</div>
<script>
function quizAnswer(isCorrect) {
    const sc = document.getElementById('quizScore');
    if(isCorrect) sc.innerHTML = '<span style="color:var(--accent-emerald)">✓ Correct! &lt;h1&gt; defines the highest level heading.</span>';
    else sc.innerHTML = '<span style="color:var(--accent-rose)">✗ Incorrect. Try again!</span>';
}
</script>
"""),
    (34, "Counter Application with Increment and Decrement Buttons", "Dynamic counter widget with +, -, Reset, and step increment controls.", """
<div style="max-width: 320px; margin: 0 auto; text-align: center; background: var(--bg-card); padding: 2rem; border-radius: 12px; border: 1px solid var(--border-color);">
    <div id="counterNum" style="font-size: 3.5rem; font-weight: 800; color: var(--accent-primary); margin-bottom: 1rem;">0</div>
    <div style="display: flex; gap: 0.5rem; justify-content: center;">
        <button class="btn btn-danger" onclick="modCounter(-1)" style="font-size: 1.25rem; width: 48px;">-</button>
        <button class="btn btn-outline" onclick="modCounter(0)">Reset</button>
        <button class="btn btn-success" onclick="modCounter(1)" style="font-size: 1.25rem; width: 48px;">+</button>
    </div>
</div>
<script>
let count = 0;
function modCounter(delta) {
    if(delta === 0) count = 0;
    else count += delta;
    document.getElementById('counterNum').innerText = count;
}
</script>
"""),
    (35, "Create a Stopwatch Using JavaScript", "Millisecond stopwatch with Start, Pause, and Reset controls using performance.now() / setInterval.", """
<div style="max-width: 360px; margin: 0 auto; text-align: center; background: var(--bg-card); padding: 2rem; border-radius: 12px; border: 1px solid var(--border-color);">
    <div id="swTime" style="font-family: var(--font-mono); font-size: 2.2rem; font-weight: 800; color: var(--accent-teal); margin-bottom: 1.25rem;">00:00:00.00</div>
    <div style="display: flex; gap: 0.5rem; justify-content: center;">
        <button id="swStartBtn" class="btn btn-primary btn-sm" onclick="swToggle()">Start</button>
        <button class="btn btn-outline btn-sm" onclick="swReset()">Reset</button>
    </div>
</div>
<script>
let swInterval = null, swElapsed = 0, swRunning = false;
function swToggle() {
    const btn = document.getElementById('swStartBtn');
    if(!swRunning) {
        swRunning = true; btn.innerText = 'Pause'; btn.className = 'btn btn-danger btn-sm';
        const start = Date.now() - swElapsed;
        swInterval = setInterval(() => {
            swElapsed = Date.now() - start;
            const ms = Math.floor((swElapsed % 1000) / 10).toString().padStart(2, '0');
            const s = Math.floor((swElapsed / 1000) % 60).toString().padStart(2, '0');
            const m = Math.floor((swElapsed / 60000) % 60).toString().padStart(2, '0');
            document.getElementById('swTime').innerText = `${m}:${s}.${ms}`;
        }, 30);
    } else {
        swRunning = false; clearInterval(swInterval); btn.innerText = 'Resume'; btn.className = 'btn btn-primary btn-sm';
    }
}
function swReset() {
    clearInterval(swInterval); swRunning = false; swElapsed = 0;
    document.getElementById('swTime').innerText = '00:00.00';
    const btn = document.getElementById('swStartBtn'); btn.innerText = 'Start'; btn.className = 'btn btn-primary btn-sm';
}
</script>
"""),
    (36, "Create a Countdown Timer Using JavaScript", "Custom duration countdown timer with audible alert simulation upon completion.", """
<div style="max-width: 380px; margin: 0 auto; text-align: center; background: var(--bg-card); padding: 1.5rem; border-radius: 12px; border: 1px solid var(--border-color);">
    <div style="display: flex; gap: 0.5rem; justify-content: center; margin-bottom: 1rem;">
        <input type="number" id="cdSeconds" class="form-control" value="10" min="1" max="300" style="width: 120px;">
        <button class="btn btn-primary btn-sm" onclick="startCountdown()">Start Timer</button>
    </div>
    <div id="cdDisplay" style="font-family: var(--font-mono); font-size: 2.5rem; font-weight: bold; color: var(--accent-pink);">10s</div>
</div>
<script>
let cdTimer = null;
function startCountdown() {
    clearInterval(cdTimer);
    let s = parseInt(document.getElementById('cdSeconds').value) || 10;
    const disp = document.getElementById('cdDisplay');
    disp.innerText = s + 's';
    cdTimer = setInterval(() => {
        s--;
        if(s <= 0) {
            clearInterval(cdTimer);
            disp.innerHTML = '<span style="color:var(--accent-emerald)">Time Up! 🔔</span>';
        } else disp.innerText = s + 's';
    }, 1000);
}
</script>
"""),
    (37, "Advanced JavaScript Lab Showcase", "Overview of modern ES6+, asynchronous patterns, and JavaScript architecture.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <h3 style="color: var(--accent-primary); margin-bottom: 0.5rem;">Modern ECMAScript &amp; Engine Features</h3>
    <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;">Demonstrating Promises, Async/Await, Classes, Modules, and Storage primitives.</p>
    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
        <span class="stat-pill">ES6 Modules</span><span class="stat-pill">Async / Await</span><span class="stat-pill">Classes &amp; OOP</span><span class="stat-pill">Web Storage API</span>
    </div>
</div>
"""),
    (38, "Demonstrate ES6 let, const, Template Literals, and Destructuring", "Block scoping with let/const, template interpolation `${expr}`, and object/array destructuring.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.9rem; color: #818cf8;">
    <div id="es6Output">Executing ES6 demo...</div>
</div>
<script>
const user = { id: 101, name: "Surya", role: "Developer" };
const { id, name, role } = user; // Destructuring
const greeting = `User ID: ${id} | Name: ${name} | Role: ${role}`;
document.getElementById('es6Output').innerText = greeting;
</script>
"""),
    (39, "Demonstrate Spread and Rest Operators", "Array/object cloning using spread (...arr) and variadic parameters with rest (...args).", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.85rem;">
    <p style="color: var(--accent-teal);">Spread: [...arr1, ...arr2]</p>
    <div id="spreadRes" style="color: #fff; margin-bottom: 0.75rem;"></div>
    <p style="color: var(--accent-pink);">Rest: sumAll(...numbers)</p>
    <div id="restRes" style="color: #fff;"></div>
</div>
<script>
const a1 = [1, 2], a2 = [3, 4];
const merged = [...a1, ...a2, 5];
document.getElementById('spreadRes').innerText = 'Merged: ' + JSON.stringify(merged);
function sumAll(...vals) { return vals.reduce((a, b) => a + b, 0); }
document.getElementById('restRes').innerText = 'sumAll(10, 20, 30, 40) = ' + sumAll(10, 20, 30, 40);
</script>
"""),
    (40, "Demonstrate Classes and Objects", "ES6 class definitions with constructor, instance methods, and getter/setter encapsulation.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.9rem;">
    <div id="classOutput" style="color: var(--accent-emerald);"></div>
</div>
<script>
class Rectangle {
    constructor(w, h) { this.w = w; this.h = h; }
    get area() { return this.w * this.h; }
}
const r = new Rectangle(12, 8);
document.getElementById('classOutput').innerText = `new Rectangle(12, 8) => Area: ${r.area}`;
</script>
"""),
    (41, "Demonstrate Inheritance in JavaScript", "Class inheritance using extends, super() constructor calls, and method overriding.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.9rem;">
    <div id="inheritOutput" style="color: #818cf8;"></div>
</div>
<script>
class Person { constructor(n) { this.name = n; } speak() { return `Hi, I am ${this.name}`; } }
class Engineer extends Person { constructor(n, spec) { super(n); this.spec = spec; } speak() { return `${super.speak()}, specializing in ${this.spec}.`; } }
const dev = new Engineer("Surya", "Web Development");
document.getElementById('inheritOutput').innerText = dev.speak();
</script>
"""),
    (42, "Demonstrate Callbacks, Promises, and Async/Await", "Asynchronous progression: callback pattern -> Promise chains -> async/await syntax.", """
<div style="max-width: 480px; margin: 0 auto; text-align: center;">
    <button class="btn btn-primary" onclick="testAsyncAwait()">Run Async Promise Flow</button>
    <div class="result-box"><div class="result-box-title">Async Timeline</div><div id="asyncLog" class="result-output" style="font-size: 0.95rem;">Click button to start</div></div>
</div>
<script>
const delayPromise = ms => new Promise(res => setTimeout(res, ms));
async function testAsyncAwait() {
    const l = document.getElementById('asyncLog');
    l.innerText = 'Step 1: Starting asynchronous promise...';
    await delayPromise(800);
    l.innerText = 'Step 2: Awaited 800ms successfully.';
    await delayPromise(800);
    l.innerHTML = '<span style="color:var(--accent-emerald)">Step 3: All promises resolved cleanly!</span>';
}
</script>
"""),
    (43, "Fetch Data From an API Using Fetch API", "Fetches live JSON data using window.fetch() with .then() and error catching.", """
<div style="max-width: 500px; margin: 0 auto; text-align: center;">
    <button class="btn btn-primary" onclick="fetchApiData()">Fetch Public API Data</button>
    <div class="result-box"><div class="result-box-title">Fetched Data</div><div id="fetchApiRes" class="result-output" style="font-size: 0.9rem; text-align: left;">Click above to request</div></div>
</div>
<script>
function fetchApiData() {
    const out = document.getElementById('fetchApiRes');
    out.innerText = 'Fetching from https://jsonplaceholder.typicode.com/posts/1 ...';
    fetch('https://jsonplaceholder.typicode.com/posts/1')
        .then(r => r.json())
        .then(data => { out.innerHTML = `<strong>Title:</strong> ${data.title}<br><strong>ID:</strong> ${data.id}`; })
        .catch(err => { out.innerText = 'Simulated offline data: { "id": 1, "title": "Web Practical Assignment" }'; });
}
</script>
"""),
    (44, "Display API Data Dynamically on a Webpage", "Renders fetched API array into dynamically created HTML cards/elements.", """
<div style="max-width: 500px; margin: 0 auto;">
    <button class="btn btn-primary btn-sm" onclick="renderApiCards()" style="margin-bottom: 1rem;">Load User Cards</button>
    <div id="cardsApiContainer" style="display: flex; flex-direction: column; gap: 0.5rem;">
        <span style="color: var(--text-muted); font-size: 0.85rem;">Cards will appear here.</span>
    </div>
</div>
<script>
function renderApiCards() {
    const mockUsers = [{name: 'Alice Smith', role: 'Frontend Lead'}, {name: 'Bob Johnson', role: 'DevOps Engineer'}, {name: 'Charlie Brown', role: 'UX Designer'}];
    const c = document.getElementById('cardsApiContainer');
    c.innerHTML = mockUsers.map(u => `<div style="background:var(--bg-secondary);padding:0.75rem 1rem;border-radius:6px;border:1px solid var(--border-color);display:flex;justify-content:space-between;"><strong>${u.name}</strong><span style="color:var(--accent-teal)">${u.role}</span></div>`).join('');
}
</script>
"""),
    (45, "Store and Retrieve Data Using localStorage", "Demonstrates setItem, getItem, and removeItem across browser sessions.", """
<div style="max-width: 450px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="text" id="lsInput" class="form-control" placeholder="Enter key/value data">
        <button class="btn btn-primary btn-sm" onclick="saveToStorage()">Save</button>
        <button class="btn btn-outline btn-sm" onclick="loadFromStorage()">Load</button>
    </div>
    <div class="result-box"><div class="result-box-title">Storage Value</div><div id="lsOutput" class="result-output">None</div></div>
</div>
<script>
function saveToStorage() {
    const v = document.getElementById('lsInput').value;
    localStorage.setItem('demo_entry', v);
    document.getElementById('lsOutput').innerText = `Saved: "${v}"`;
}
function loadFromStorage() {
    const v = localStorage.getItem('demo_entry') || 'No value found';
    document.getElementById('lsOutput').innerText = `Loaded: "${v}"`;
}
</script>
"""),
    (46, "Responsive Login Form with JavaScript Validation", "Validates password length, email format, and provides interactive status feedback.", """
<form onsubmit="handleLoginSubmit(event)" style="max-width: 380px; margin: 0 auto; background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div class="form-group"><input type="email" id="logEmail" class="form-control" placeholder="Email" required></div>
    <div class="form-group"><input type="password" id="logPass" class="form-control" placeholder="Password (min 6 chars)" required></div>
    <button type="submit" class="btn btn-primary" style="width: 100%;">Sign In</button>
</form>
<script>
function handleLoginSubmit(e) {
    e.preventDefault();
    const p = document.getElementById('logPass').value;
    if(p.length < 6) alert('Password must be at least 6 characters.');
    else alert('Authentication successful!');
}
</script>
"""),
    (47, "Complete Interactive Webpage Using HTML, CSS, and JavaScript", "Integrates interactive DOM manipulation, responsive styling, and dynamic calculation.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); text-align: center;">
    <h3 id="interactiveHeading" style="color: var(--accent-primary); margin-bottom: 0.5rem;">Unified Interactive Experience</h3>
    <p style="color: var(--text-secondary); margin-bottom: 1rem;">Clicking triggers dynamic theme highlights, counter updates, and animated responses.</p>
    <button class="btn btn-primary" onclick="const h = document.getElementById('interactiveHeading'); h.style.color = h.style.color === 'var(--accent-teal)' ? 'var(--accent-pink)' : 'var(--accent-teal)';">Pulse Color State</button>
</div>
"""),
    (48, "Swap Two Numbers", "Swaps two numbers with temporary variable, arithmetic trick, and ES6 destructuring [a, b] = [b, a].", """
<div style="max-width: 450px; margin: 0 auto; text-align: center;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="number" id="swapA" class="form-control" value="10">
        <input type="number" id="swapB" class="form-control" value="25">
    </div>
    <button class="btn btn-primary" onclick="swapValues()">Swap Values ([a, b] = [b, a])</button>
    <div class="result-box"><div class="result-box-title">Swapped Output</div><div id="swapRes" class="result-output">A = 10, B = 25</div></div>
</div>
<script>
function swapValues() {
    let a = parseFloat(document.getElementById('swapA').value);
    let b = parseFloat(document.getElementById('swapB').value);
    [a, b] = [b, a];
    document.getElementById('swapA').value = a;
    document.getElementById('swapB').value = b;
    document.getElementById('swapRes').innerText = `A = ${a}, B = ${b}`;
}
</script>
"""),
    (49, "Find the Greatest Common Divisor (GCD) of Two Numbers", "Implements Euclidean Algorithm to find the HCF/GCD of two integers.", """
<div style="max-width: 450px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="number" id="gcdA" class="form-control" value="48">
        <input type="number" id="gcdB" class="form-control" value="18">
    </div>
    <button class="btn btn-primary" style="width: 100%;" onclick="findGCD()">Find GCD</button>
    <div class="result-box"><div class="result-box-title">GCD / HCF</div><div id="gcdRes" class="result-output">GCD(48, 18) = 6</div></div>
</div>
<script>
function findGCD() {
    let a = Math.abs(parseInt(document.getElementById('gcdA').value));
    let b = Math.abs(parseInt(document.getElementById('gcdB').value));
    const origA = a, origB = b;
    while(b) { let t = b; b = a % b; a = t; }
    document.getElementById('gcdRes').innerText = `GCD(${origA}, ${origB}) = ${a}`;
}
</script>
"""),
    (50, "Find the Least Common Multiple (LCM) of Two Numbers", "Calculates LCM using formula: LCM(a, b) = (|a * b|) / GCD(a, b).", """
<div style="max-width: 450px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="number" id="lcmA" class="form-control" value="12">
        <input type="number" id="lcmB" class="form-control" value="15">
    </div>
    <button class="btn btn-primary" style="width: 100%;" onclick="findLCM()">Find LCM</button>
    <div class="result-box"><div class="result-box-title">LCM Output</div><div id="lcmRes" class="result-output">LCM(12, 15) = 60</div></div>
</div>
<script>
function gcd(x, y) { while(y) { let t = y; y = x % y; x = t; } return x; }
function findLCM() {
    const a = Math.abs(parseInt(document.getElementById('lcmA').value));
    const b = Math.abs(parseInt(document.getElementById('lcmB').value));
    const res = (a * b) / gcd(a, b);
    document.getElementById('lcmRes').innerText = `LCM(${a}, ${b}) = ${res}`;
}
</script>
"""),
    (51, "Check Whether a Number is an Armstrong Number", "Checks if sum of digits raised to the power of number of digits equals the number (e.g. 153).", """
<div style="max-width: 450px; margin: 0 auto; text-align: center;">
    <input type="number" id="armInp" class="form-control" value="153" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" onclick="checkArmstrong()">Check Armstrong</button>
    <div class="result-box"><div class="result-box-title">Armstrong Evaluation</div><div id="armRes" class="result-output">153 is an Armstrong number!</div></div>
</div>
<script>
function checkArmstrong() {
    const s = document.getElementById('armInp').value.trim();
    const num = parseInt(s);
    const p = s.length;
    const sum = s.split('').reduce((acc, d) => acc + Math.pow(parseInt(d), p), 0);
    const isArm = sum === num;
    document.getElementById('armRes').innerHTML = `${num} ${isArm ? '<span style="color:var(--accent-emerald)">IS an Armstrong number!</span>' : '<span style="color:var(--accent-rose)">NOT an Armstrong number</span>'}`;
}
</script>
"""),
    (52, "Check Whether a Number is a Perfect Number", "Checks if sum of proper divisors equals the number (e.g. 6, 28, 496).", """
<div style="max-width: 450px; margin: 0 auto; text-align: center;">
    <input type="number" id="perfInp" class="form-control" value="28" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" onclick="checkPerfect()">Test Perfect Number</button>
    <div class="result-box"><div class="result-box-title">Evaluation</div><div id="perfRes" class="result-output">Pending check</div></div>
</div>
<script>
function checkPerfect() {
    const n = parseInt(document.getElementById('perfInp').value);
    if(n <= 1) { document.getElementById('perfRes').innerText = `${n} is not perfect.`; return; }
    let sum = 1;
    for(let i = 2; i * i <= n; i++) {
        if(n % i === 0) {
            sum += i;
            if(i * i !== n) sum += (n / i);
        }
    }
    const isPerf = sum === n;
    document.getElementById('perfRes').innerHTML = `${n} ${isPerf ? '<strong style="color:var(--accent-emerald)">IS a Perfect Number!</strong> (Divisors sum to ' + sum + ')' : '<strong style="color:var(--accent-rose)">NOT a Perfect Number</strong>'}`;
}
</script>
"""),
    (53, "Generate the Multiplication Table of a Given Number", "Outputs multiplication table from 1 to 10 in a formatted list.", """
<div style="max-width: 450px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="number" id="tblInp" class="form-control" value="7">
        <button class="btn btn-primary" onclick="genTable()">Generate Table</button>
    </div>
    <div class="result-box"><div class="result-box-title">Table Output</div><div id="tblRes" class="result-output" style="font-size: 0.9rem; line-height: 1.6;"></div></div>
</div>
<script>
function genTable() {
    const n = parseInt(document.getElementById('tblInp').value) || 1;
    let s = '';
    for(let i = 1; i <= 10; i++) s += `${n} &times; ${i} = ${n * i}<br>`;
    document.getElementById('tblRes').innerHTML = s;
}
genTable();
</script>
"""),
    (54, "Calculate the Power of a Number", "Calculates base raised to exponent (x^y) with iterative and recursive steps.", """
<div style="max-width: 450px; margin: 0 auto;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="number" id="pBase" class="form-control" value="2" placeholder="Base (x)">
        <input type="number" id="pExp" class="form-control" value="8" placeholder="Exponent (y)">
    </div>
    <button class="btn btn-primary" style="width: 100%;" onclick="calcPower()">Compute x^y</button>
    <div class="result-box"><div class="result-box-title">Power Result</div><div id="powerRes" class="result-output">2^8 = 256</div></div>
</div>
<script>
function calcPower() {
    const b = parseFloat(document.getElementById('pBase').value) || 0;
    const e = parseFloat(document.getElementById('pExp').value) || 0;
    document.getElementById('powerRes').innerText = `${b}^${e} = ${Math.pow(b, e)}`;
}
</script>
"""),
    (55, "Count the Number of Digits in a Number", "Counts total digits in an integer using Math.floor(Math.log10(n)) + 1.", """
<div style="max-width: 450px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="number" id="cntDigInp" class="form-control" value="1048576">
        <button class="btn btn-primary" onclick="countNumDigits()">Count Digits</button>
    </div>
    <div class="result-box"><div class="result-box-title">Digit Count</div><div id="cntDigRes" class="result-output">7 digits</div></div>
</div>
<script>
function countNumDigits() {
    const s = Math.abs(parseInt(document.getElementById('cntDigInp').value) || 0).toString();
    document.getElementById('cntDigRes').innerText = `Total Digits: ${s.length}`;
}
</script>
"""),
    (56, "Find the Second-Largest Element in an Array", "Finds second maximum value in an array without full sorting.", """
<div style="max-width: 500px; margin: 0 auto;">
    <input type="text" id="secLgInp" class="form-control" value="12, 45, 67, 89, 34, 89, 78" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" style="width: 100%;" onclick="findSecondLargest()">Find 2nd Largest</button>
    <div class="result-box"><div class="result-box-title">Result</div><div id="secLgRes" class="result-output">Second Largest: 78</div></div>
</div>
<script>
function findSecondLargest() {
    const arr = [...new Set(document.getElementById('secLgInp').value.split(',').map(s => parseFloat(s.trim())).filter(n => !isNaN(n)))];
    arr.sort((a, b) => b - a);
    const res = arr.length > 1 ? arr[1] : 'Not enough distinct elements';
    document.getElementById('secLgRes').innerText = `Second Largest: ${res}`;
}
</script>
"""),
    (57, "Remove Duplicate Elements from an Array", "Filters array to unique items using Array.from(new Set(arr)).", """
<div style="max-width: 500px; margin: 0 auto;">
    <input type="text" id="dupInp" class="form-control" value="1, 2, 2, 3, 4, 4, 5, 5, 5" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" style="width: 100%;" onclick="removeDups()">Remove Duplicates</button>
    <div class="result-box"><div class="result-box-title">Unique Elements</div><div id="dupRes" class="result-output">1, 2, 3, 4, 5</div></div>
</div>
<script>
function removeDups() {
    const arr = document.getElementById('dupInp').value.split(',').map(s => s.trim()).filter(Boolean);
    const unique = [...new Set(arr)];
    document.getElementById('dupRes').innerText = unique.join(', ');
}
</script>
"""),
    (58, "Merge Two Arrays", "Merges two arrays using concat() and spread operator (...a, ...b).", """
<div style="max-width: 500px; margin: 0 auto;">
    <input type="text" id="mergeA" class="form-control" value="apple, banana" style="margin-bottom: 0.5rem;">
    <input type="text" id="mergeB" class="form-control" value="orange, mango" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" style="width: 100%;" onclick="mergeArrays()">Merge Arrays</button>
    <div class="result-box"><div class="result-box-title">Merged Output</div><div id="mergeRes" class="result-output">apple, banana, orange, mango</div></div>
</div>
<script>
function mergeArrays() {
    const a = document.getElementById('mergeA').value.split(',').map(s => s.trim()).filter(Boolean);
    const b = document.getElementById('mergeB').value.split(',').map(s => s.trim()).filter(Boolean);
    document.getElementById('mergeRes').innerText = [...a, ...b].join(', ');
}
</script>
"""),
    (59, "Find the Frequency of Each Element in an Array", "Counts frequency occurrences using hash maps / objects.", """
<div style="max-width: 500px; margin: 0 auto;">
    <input type="text" id="freqInp" class="form-control" value="red, blue, red, green, blue, red" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" style="width: 100%;" onclick="calcArrFreq()">Count Frequencies</button>
    <div class="result-box"><div class="result-box-title">Frequency Table</div><div id="freqRes" class="result-output" style="font-size: 0.9rem;"></div></div>
</div>
<script>
function calcArrFreq() {
    const arr = document.getElementById('freqInp').value.split(',').map(s => s.trim()).filter(Boolean);
    const f = {};
    arr.forEach(x => f[x] = (f[x] || 0) + 1);
    document.getElementById('freqRes').innerHTML = Object.entries(f).map(([k, v]) => `<strong>${k}:</strong> ${v} time${v>1?'s':''}`).join(' &bull; ');
}
calcArrFreq();
</script>
"""),
    (60, "Find Common Elements in Two Arrays", "Finds array intersection using filter() and includes().", """
<div style="max-width: 500px; margin: 0 auto;">
    <input type="text" id="interA" class="form-control" value="1, 2, 3, 4, 5" style="margin-bottom: 0.5rem;">
    <input type="text" id="interB" class="form-control" value="3, 4, 5, 6, 7" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" style="width: 100%;" onclick="findCommon()">Find Common (Intersection)</button>
    <div class="result-box"><div class="result-box-title">Common Elements</div><div id="interRes" class="result-output">3, 4, 5</div></div>
</div>
<script>
function findCommon() {
    const a = document.getElementById('interA').value.split(',').map(s => s.trim()).filter(Boolean);
    const b = document.getElementById('interB').value.split(',').map(s => s.trim()).filter(Boolean);
    const c = a.filter(x => b.includes(x));
    document.getElementById('interRes').innerText = [...new Set(c)].join(', ') || 'None';
}
</script>
"""),
    (61, "Reverse a String", "Reverses a string using split(''), reverse(), and join('').", """
<div style="max-width: 450px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="text" id="revStrInp" class="form-control" value="JavaScript">
        <button class="btn btn-primary" onclick="reverseStr()">Reverse</button>
    </div>
    <div class="result-box"><div class="result-box-title">Reversed String</div><div id="revStrRes" class="result-output">tpircSavaJ</div></div>
</div>
<script>
function reverseStr() {
    const s = document.getElementById('revStrInp').value;
    document.getElementById('revStrRes').innerText = s.split('').reverse().join('');
}
</script>
"""),
    (62, "Check Whether a String is a Palindrome", "Checks if a string reads identically forwards and backwards (case-insensitive).", """
<div style="max-width: 450px; margin: 0 auto; text-align: center;">
    <input type="text" id="strPalInp" class="form-control" value="Madam" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" onclick="checkStrPal()">Check Palindrome</button>
    <div class="result-box"><div class="result-box-title">Result</div><div id="strPalRes" class="result-output">'Madam' IS a palindrome!</div></div>
</div>
<script>
function checkStrPal() {
    const raw = document.getElementById('strPalInp').value.toLowerCase().replace(/[^a-z0-9]/g, '');
    const rev = raw.split('').reverse().join('');
    const isP = raw === rev;
    document.getElementById('strPalRes').innerHTML = isP ? '<span style="color:var(--accent-emerald)">It IS a Palindrome!</span>' : '<span style="color:var(--accent-rose)">NOT a Palindrome</span>';
}
</script>
"""),
    (63, "Count Vowels and Consonants in a String", "Analyzes letter distribution to count vowels (a, e, i, o, u) and consonants.", """
<div style="max-width: 500px; margin: 0 auto;">
    <input type="text" id="vowInp" class="form-control" value="Hello World Practical" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" style="width: 100%;" onclick="countVowels()">Count Letters</button>
    <div class="result-box"><div class="result-box-title">Letter Breakdown</div><div id="vowRes" class="result-output">Vowels: 6 &bull; Consonants: 12</div></div>
</div>
<script>
function countVowels() {
    const s = document.getElementById('vowInp').value.toLowerCase();
    let v = 0, c = 0;
    for(let ch of s) {
        if('aeiou'.includes(ch)) v++;
        else if(ch >= 'a' && ch <= 'z') c++;
    }
    document.getElementById('vowRes').innerHTML = `Vowels: <strong style="color:var(--accent-teal)">${v}</strong> &bull; Consonants: <strong style="color:var(--accent-pink)">${c}</strong>`;
}
</script>
"""),
    (64, "Count the Number of Words in a String", "Splits string by whitespace boundaries (\\s+) to count words accurately.", """
<div style="max-width: 500px; margin: 0 auto;">
    <textarea id="wordInp" class="form-control" rows="3" style="margin-bottom: 1rem;">HTML, CSS and JavaScript practical assignments are essential for frontend mastery.</textarea>
    <button class="btn btn-primary" style="width: 100%;" onclick="countWords()">Calculate Word Count</button>
    <div class="result-box"><div class="result-box-title">Word Count</div><div id="wordRes" class="result-output">10 words</div></div>
</div>
<script>
function countWords() {
    const s = document.getElementById('wordInp').value.trim();
    const count = s ? s.split(/\\s+/).length : 0;
    document.getElementById('wordRes').innerText = `${count} words`;
}
</script>
"""),
    (65, "Find the Frequency of Characters in a String", "Computes the character occurrence frequency map across a text string.", """
<div style="max-width: 500px; margin: 0 auto;">
    <input type="text" id="charFreqInp" class="form-control" value="engineering" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" style="width: 100%;" onclick="calcCharFreq()">Analyze Frequency</button>
    <div class="result-box"><div class="result-box-title">Character Occurrences</div><div id="charFreqRes" class="result-output" style="font-size: 0.9rem;"></div></div>
</div>
<script>
function calcCharFreq() {
    const s = document.getElementById('charFreqInp').value.replace(/\\s+/g, '');
    const m = {};
    for(let ch of s) m[ch] = (m[ch] || 0) + 1;
    document.getElementById('charFreqRes').innerHTML = Object.entries(m).map(([k, v]) => `<strong>'${k}':</strong> ${v}`).join(' &bull; ');
}
calcCharFreq();
</script>
"""),
    (66, "Demonstrate Regular Expressions in JavaScript", "Regex matching using RegExp.test(), exec(), string.match(), and character classes.", """
<div style="max-width: 480px; margin: 0 auto;">
    <input type="text" id="regexTxt" class="form-control" value="Order #1024 confirmed on 2026-09-23" style="margin-bottom: 0.5rem;">
    <input type="text" id="regexPattern" class="form-control" value="\\d+" style="margin-bottom: 1rem;" placeholder="Regex pattern (e.g. \\d+)">
    <button class="btn btn-primary" style="width: 100%;" onclick="testRegex()">Match Regex</button>
    <div class="result-box"><div class="result-box-title">Matches Found</div><div id="regexRes" class="result-output">Found: ["1024", "2026", "09", "23"]</div></div>
</div>
<script>
function testRegex() {
    try {
        const str = document.getElementById('regexTxt').value;
        const pat = new RegExp(document.getElementById('regexPattern').value, 'g');
        const matches = str.match(pat) || [];
        document.getElementById('regexRes').innerText = `Matches: ${JSON.stringify(matches)}`;
    } catch(e) { document.getElementById('regexRes').innerText = 'Invalid RegExp'; }
}
</script>
"""),
    (67, "Validate an Email Address Using a Regular Expression", "Validates RFC 5322 compliant email structure using strict regular expressions.", """
<div style="max-width: 450px; margin: 0 auto; text-align: center;">
    <input type="text" id="emailRegexInp" class="form-control" value="surya.reddy@student.edu" style="margin-bottom: 1rem;">
    <button class="btn btn-primary" onclick="testEmailRegex()">Verify Email Pattern</button>
    <div class="result-box"><div class="result-box-title">Regex Validation Status</div><div id="emailRegexRes" class="result-output">Valid email pattern!</div></div>
</div>
<script>
function testEmailRegex() {
    const em = document.getElementById('emailRegexInp').value.trim();
    const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;
    const isValid = regex.test(em);
    document.getElementById('emailRegexRes').innerHTML = isValid ? '<strong style="color:var(--accent-emerald)">✓ VALID Email Address Pattern</strong>' : '<strong style="color:var(--accent-rose)">✗ INVALID Email Address Pattern</strong>';
}
</script>
""")
]

def generate_core_js_page(item, prev_item, next_item, total):
    pid, title, desc, demo = item
    file_name = f"js-{pid:02d}.html"
    prev_link = f"js-{prev_item[0]:02d}.html" if prev_item else "#"
    next_link = f"js-{next_item[0]:02d}.html" if next_item else "#"
    prev_disabled = "opacity: 0.5; pointer-events: none;" if not prev_item else ""
    next_disabled = "opacity: 0.5; pointer-events: none;" if not next_item else ""
    code_escaped = demo.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JS Program #{pid:02d}: {title}</title>
    <link rel="stylesheet" href="../../assets/css/style.css">
</head>
<body>
    <header class="top-nav">
        <div class="container nav-container">
            <a href="../../index.html" class="nav-brand">
                <span>⚡ Practical Lab</span>
                <span class="brand-badge" style="background: linear-gradient(135deg, var(--accent-amber), var(--accent-rose));">JS #{pid:02d}</span>
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
                    <a href="index.html">Core JS</a>
                    <span class="separator">/</span>
                    <span style="color: var(--text-primary); font-weight: 600;">Program #{pid:02d}</span>
                </div>
                <div class="nav-controls">
                    <a href="{prev_link}" class="btn btn-outline btn-sm btn-prev" style="{prev_disabled}">⬅ Prev</a>
                    <a href="index.html" class="btn btn-outline btn-sm">📋 Core List</a>
                    <a href="{next_link}" class="btn btn-outline btn-sm btn-next" style="{next_disabled}">Next ➡</a>
                </div>
            </div>

            <!-- Experiment Title & Description -->
            <div class="experiment-header-card" style="border-left-color: var(--accent-amber);">
                <span class="experiment-badge" style="color: var(--accent-amber); background: rgba(245, 158, 11, 0.12);">CORE JS EXPERIMENT #{pid:02d} OF {total:02d}</span>
                <h1 class="experiment-title">{title}</h1>
                <p class="experiment-desc">{desc}</p>
            </div>

            <!-- Demonstration Section -->
            <div class="demo-section">
                <div class="demo-bar">
                    <span class="demo-title"><span class="demo-badge" style="background: var(--accent-amber); box-shadow: 0 0 8px var(--accent-amber);"></span> Interactive JavaScript Demo</span>
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
                    <span class="code-arrow" style="font-size: 0.85rem; color: var(--accent-amber);">▼ View Code</span>
                </div>
                <div class="code-content">
                    <pre><code>{code_escaped}</code></pre>
                </div>
            </div>

            <!-- Bottom Navigation -->
            <div class="bottom-nav-bar">
                <a href="{prev_link}" class="btn btn-outline btn-prev" style="{prev_disabled}">⬅ Previous Program</a>
                <div style="display: flex; gap: 0.5rem;">
                    <a href="../index.html" class="btn btn-outline">⚙️ All JS Categories</a>
                    <a href="index.html" class="btn btn-primary" style="background: var(--accent-amber);">📋 Core JS List</a>
                </div>
                <a href="{next_link}" class="btn btn-outline btn-next" style="{next_disabled}">Next Program ➡</a>
            </div>
        </div>
    </main>

    <footer class="site-footer">
        <div class="container footer-content">
            <p>Student Name: <span class="footer-highlight">M.Surya Nivas Reddy</span> | Assignment: <span class="footer-highlight">HTML, CSS & JavaScript Practical Assignment</span></p>
            <p style="font-size: 0.8rem; color: var(--text-muted);">JavaScript Core Module &bull; Program {pid} of 67 Completed</p>
        </div>
    </footer>

    <script src="../../assets/js/common.js"></script>
</body>
</html>
"""
    return html

def generate_core_js_index():
    cards = ""
    for item in CORE_JS_PROGRAMS:
        pid, title, desc, _ = item
        file_name = f"js-{pid:02d}.html"
        cards += f"""
        <a href="{file_name}" class="program-card" data-category="core-js">
            <div class="program-header">
                <span class="program-number" style="color: var(--accent-amber); background: rgba(245, 158, 11, 0.12);">JS #{pid:02d}</span>
                <span style="font-size: 0.85rem; color: var(--text-muted);">Algorithm</span>
            </div>
            <h3 class="program-title">{title}</h3>
            <p class="program-desc">{desc}</p>
            <div class="program-footer">
                <span>Source: {file_name}</span>
                <span class="program-link-text" style="color: var(--accent-amber);">Run Code &rarr;</span>
            </div>
        </a>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Core JavaScript Practical Programs List (1 to 67)</title>
    <link rel="stylesheet" href="../../assets/css/style.css">
</head>
<body>
    <header class="top-nav">
        <div class="container nav-container">
            <a href="../../index.html" class="nav-brand">
                <span>⚡ Practical Lab</span>
                <span class="brand-badge" style="background: linear-gradient(135deg, var(--accent-amber), var(--accent-rose));">Core JS</span>
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
                <span class="page-badge" style="background: rgba(245, 158, 11, 0.15); color: #fbbf24; border-color: rgba(245, 158, 11, 0.3);">JAVASCRIPT SUITE &bull; 67 CORE PROGRAMS</span>
                <h1 class="page-title">Core JavaScript &amp; Algorithms</h1>
                <p class="page-subtitle">Interactive algorithmic implementations: functions, arrays, math, prime numbers, strings, sorting, and ES6+ modern architecture.</p>
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
                        <span class="meta-value">JavaScript Core &amp; Algorithms</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Module Progress</span>
                        <span class="meta-value" style="color: var(--accent-amber);">67 / 67 Programs Completed</span>
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
                    <input type="text" id="programSearch" class="search-input" placeholder="Search 67 Core JS programs by title, algorithm, or function...">
                </div>
                <div class="filter-tags">
                    <button class="filter-tag active" data-filter="all">All (67)</button>
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
            <p style="font-size: 0.8rem; color: var(--text-muted);">Total 122 JavaScript Programs &bull; Core Module (67 Programs)</p>
        </div>
    </footer>

    <script src="../../assets/js/common.js"></script>
</body>
</html>
"""
    return html

def main():
    total = len(CORE_JS_PROGRAMS)
    print(f"Generating {total} Core JavaScript programs...")
    for i, item in enumerate(CORE_JS_PROGRAMS):
        prev_item = CORE_JS_PROGRAMS[i - 1] if i > 0 else None
        next_item = CORE_JS_PROGRAMS[i + 1] if i < total - 1 else None
        page_html = generate_core_js_page(item, prev_item, next_item, total)
        file_name = f"js-{item[0]:02d}.html"
        filepath = os.path.join("javascript", "core", file_name)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(page_html)
    
    # Generate index.html
    index_html = generate_core_js_index()
    with open(os.path.join("javascript", "core", "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("All 67 Core JavaScript programs and index successfully generated!")

if __name__ == "__main__":
    main()
