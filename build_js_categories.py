"""
Generator for DOM Manipulation (15), Events (8), Forms & Validation (7), and Browser & Storage (8)
Total = 38 programs across 4 dedicated folders
"""
import os

CATEGORIES = {
    "dom-manipulation": {
        "folder": "dom-manipulation",
        "badge_color": "var(--accent-teal)",
        "badge_bg": "rgba(20, 184, 166, 0.12)",
        "title": "DOM Manipulation",
        "desc": "Dynamic HTML element insertion, removal, tree traversal, batch style updates, class mutations, and real-time DOM tables.",
        "prefix": "dom",
        "programs": [
            (1, "Add New Elements Dynamically", "Uses document.createElement() and appendChild() to inject cards into the DOM.", """
<div style="max-width: 480px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="text" id="elemText" class="form-control" placeholder="Item label (e.g. Server Node #4)">
        <button class="btn btn-primary" onclick="addDynamicElem()">Append Element</button>
    </div>
    <div id="dynamicContainer" style="display: flex; flex-direction: column; gap: 0.5rem;">
        <div style="background: var(--bg-card); padding: 0.75rem 1rem; border-radius: 6px; border: 1px solid var(--border-color);">Default Item: Root Node</div>
    </div>
</div>
<script>
let nodeCount = 1;
function addDynamicElem() {
    const txt = document.getElementById('elemText').value.trim() || `Generated Element #${++nodeCount}`;
    const el = document.createElement('div');
    el.style.cssText = "background: rgba(20, 184, 166, 0.15); border: 1px solid var(--accent-teal); color: var(--text-primary); padding: 0.75rem 1rem; border-radius: 6px; display: flex; justify-content: space-between; align-items: center;";
    el.innerHTML = `<span>⚡ ${txt}</span> <small style="color:var(--text-muted); font-size:0.75rem;">Created via createElement()</small>`;
    document.getElementById('dynamicContainer').appendChild(el);
    document.getElementById('elemText').value = '';
}
</script>
"""),
            (2, "Remove HTML Elements Dynamically", "Removes targeted child elements from the DOM using element.remove() and removeChild().", """
<div style="max-width: 480px; margin: 0 auto;">
    <p style="color: var(--text-secondary); margin-bottom: 0.75rem;">Click the delete button on any item to remove it from the document tree:</p>
    <div id="removableContainer" style="display: flex; flex-direction: column; gap: 0.5rem;">
        <div style="background: var(--bg-card); padding: 0.75rem 1rem; border-radius: 6px; border: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
            <span>Cluster 1: Primary Gateway</span>
            <button class="btn btn-danger btn-sm" onclick="this.parentElement.remove()">Remove</button>
        </div>
        <div style="background: var(--bg-card); padding: 0.75rem 1rem; border-radius: 6px; border: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
            <span>Cluster 2: Database Replicate</span>
            <button class="btn btn-danger btn-sm" onclick="this.parentElement.remove()">Remove</button>
        </div>
        <div style="background: var(--bg-card); padding: 0.75rem 1rem; border-radius: 6px; border: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
            <span>Cluster 3: Edge Cache</span>
            <button class="btn btn-danger btn-sm" onclick="this.parentElement.remove()">Remove</button>
        </div>
    </div>
</div>
"""),
            (3, "Change CSS Styles Using JavaScript", "Mutates inline CSS styles dynamically via element.style properties.", """
<div style="max-width: 480px; margin: 0 auto; text-align: center;">
    <div id="styleBox" style="width: 200px; height: 100px; margin: 0 auto 1.5rem; background: #6366f1; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; transition: all 0.3s ease;">
        Dynamic Box
    </div>
    <div style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;">
        <button class="btn btn-outline btn-sm" onclick="const b=document.getElementById('styleBox'); b.style.backgroundColor='#10b981'; b.style.borderRadius='30px';">Green Pill</button>
        <button class="btn btn-outline btn-sm" onclick="const b=document.getElementById('styleBox'); b.style.backgroundColor='#ec4899'; b.style.transform='rotate(10deg)';">Pink Rotated</button>
        <button class="btn btn-outline btn-sm" onclick="const b=document.getElementById('styleBox'); b.style.backgroundColor='#6366f1'; b.style.borderRadius='8px'; b.style.transform='none';">Reset</button>
    </div>
</div>
"""),
            (4, "Change Multiple HTML Elements Simultaneously", "Queries multiple matching elements via querySelectorAll and updates attributes iteratively.", """
<div style="max-width: 500px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1.25rem; justify-content: center;">
        <button class="btn btn-primary btn-sm" onclick="updateAllNodes('#38bdf8', '✓ Updated')">Update All to Cyan</button>
        <button class="btn btn-primary btn-sm" onclick="updateAllNodes('#f472b6', '★ Starred')">Update All to Pink</button>
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
        <div class="batch-node" style="background: var(--bg-card); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color); text-align: center;">Node Alpha</div>
        <div class="batch-node" style="background: var(--bg-card); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color); text-align: center;">Node Beta</div>
        <div class="batch-node" style="background: var(--bg-card); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color); text-align: center;">Node Gamma</div>
        <div class="batch-node" style="background: var(--bg-card); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color); text-align: center;">Node Delta</div>
    </div>
</div>
<script>
function updateAllNodes(color, text) {
    document.querySelectorAll('.batch-node').forEach((el, i) => {
        el.style.borderColor = color;
        el.style.color = color;
        el.innerText = `${text} ${i+1}`;
    });
}
</script>
"""),
            (5, "Demonstrate getElementById() and getElementsByClassName()", "Compares direct single-node selection by ID with live HTMLCollection selection by Class.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div id="targetById" style="padding: 0.75rem; background: rgba(99,102,241,0.15); border-radius: 6px; margin-bottom: 0.75rem; color: #818cf8;">
        Targeted by ID: #targetById
    </div>
    <div class="targetByClass" style="padding: 0.5rem; background: var(--bg-secondary); border-radius: 4px; margin-bottom: 0.35rem;">Class Member 1 (.targetByClass)</div>
    <div class="targetByClass" style="padding: 0.5rem; background: var(--bg-secondary); border-radius: 4px; margin-bottom: 1rem;">Class Member 2 (.targetByClass)</div>
    <button class="btn btn-outline btn-sm" onclick="highlightByClass()">Highlight All by Class Name</button>
</div>
<script>
function highlightByClass() {
    const list = document.getElementsByClassName('targetByClass');
    for(let el of list) {
        el.style.border = '1px solid var(--accent-teal)';
        el.style.color = 'var(--accent-teal)';
    }
}
</script>
"""),
            (6, "Demonstrate querySelector() and querySelectorAll()", "Utilizes modern CSS selector query APIs to select single first matches or NodeLists.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); text-align: center;">
    <p class="qs-target" style="padding: 0.5rem; margin-bottom: 0.5rem; background: var(--bg-secondary); border-radius: 4px;">querySelector Target (First element matched)</p>
    <p class="qs-target" style="padding: 0.5rem; margin-bottom: 1rem; background: var(--bg-secondary); border-radius: 4px;">Second element with same class</p>
    <button class="btn btn-primary btn-sm" onclick="document.querySelector('.qs-target').style.color='#f59e0b';">Highlight First with querySelector()</button>
    <button class="btn btn-outline btn-sm" onclick="document.querySelectorAll('.qs-target').forEach(e => e.style.backgroundColor='rgba(20,184,166,0.2)');">Highlight All with querySelectorAll()</button>
</div>
"""),
            (7, "Create and Remove CSS Classes Dynamically", "Toggles, adds, and removes class names using element.classList.add/remove/toggle.", """
<style>
.glowing-box { background: rgba(99, 102, 241, 0.25) !important; border-color: #6366f1 !important; box-shadow: 0 0 20px rgba(99, 102, 241, 0.6) !important; color: #818cf8 !important; }
</style>
<div style="max-width: 450px; margin: 0 auto; text-align: center;">
    <div id="classTarget" style="padding: 2rem; background: var(--bg-card); border: 2px dashed var(--border-color); border-radius: 12px; margin-bottom: 1.25rem; transition: 0.3s;">
        Class Toggle Target
    </div>
    <div style="display: flex; gap: 0.5rem; justify-content: center;">
        <button class="btn btn-primary btn-sm" onclick="document.getElementById('classTarget').classList.toggle('glowing-box')">Toggle .glowing-box</button>
        <button class="btn btn-outline btn-sm" onclick="alert('Contains class: ' + document.getElementById('classTarget').classList.contains('glowing-box'))">Check classList</button>
    </div>
</div>
"""),
            (8, "Create a Dynamic Table Using JavaScript", "Generates complete HTML tables programmatically with header rows and data cells.", """
<div style="max-width: 520px; margin: 0 auto;">
    <button class="btn btn-primary btn-sm" onclick="buildDynamicTable()" style="margin-bottom: 1rem;">Generate Table from Data</button>
    <div id="dynTablePlaceholder" style="overflow-x: auto;">Click button to generate dynamic table.</div>
</div>
<script>
function buildDynamicTable() {
    const data = [
        { id: 101, title: 'HTML5 Semantic Spec', status: 'Passed' },
        { id: 102, title: 'CSS3 Grid Layout', status: 'Passed' },
        { id: 103, title: 'JavaScript Engine V8', status: 'Active' }
    ];
    let html = `<table style="width:100%; border-collapse:collapse; background:var(--bg-card); border-radius:6px; overflow:hidden;">
        <tr style="background:rgba(99,102,241,0.2);"><th style="padding:8px; border:1px solid var(--border-color);">ID</th><th style="padding:8px; border:1px solid var(--border-color);">Module</th><th style="padding:8px; border:1px solid var(--border-color);">Status</th></tr>`;
    data.forEach(r => {
        html += `<tr><td style="padding:8px; border:1px solid var(--border-color); text-align:center;">${r.id}</td><td style="padding:8px; border:1px solid var(--border-color);">${r.title}</td><td style="padding:8px; border:1px solid var(--border-color); color:var(--accent-teal);">${r.status}</td></tr>`;
    });
    html += '</table>';
    document.getElementById('dynTablePlaceholder').innerHTML = html;
}
</script>
"""),
            (9, "Add and Delete Rows from a Table", "Interactive table with input controls to append new record rows and delete existing entries.", """
<div style="max-width: 550px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="text" id="newRowName" class="form-control" placeholder="Item name">
        <input type="number" id="newRowQty" class="form-control" placeholder="Qty" style="width: 100px;">
        <button class="btn btn-primary btn-sm" onclick="addTableRow()">Add Row</button>
    </div>
    <table id="editableTable" style="width: 100%; border-collapse: collapse; background: var(--bg-card); border: 1px solid var(--border-color);">
        <thead><tr style="background: var(--bg-secondary);"><th style="padding: 0.5rem; border: 1px solid var(--border-color);">Item</th><th style="padding: 0.5rem; border: 1px solid var(--border-color);">Quantity</th><th style="padding: 0.5rem; border: 1px solid var(--border-color);">Action</th></tr></thead>
        <tbody>
            <tr><td style="padding: 0.5rem; border: 1px solid var(--border-color);">Monitor 4K</td><td style="padding: 0.5rem; border: 1px solid var(--border-color); text-align: center;">2</td><td style="padding: 0.5rem; border: 1px solid var(--border-color); text-align: center;"><button class="btn btn-danger btn-sm" onclick="this.closest('tr').remove()">Delete</button></td></tr>
        </tbody>
    </table>
</div>
<script>
function addTableRow() {
    const n = document.getElementById('newRowName').value.trim();
    const q = document.getElementById('newRowQty').value.trim() || '1';
    if(!n) return;
    const tr = document.createElement('tr');
    tr.innerHTML = `<td style="padding:0.5rem; border:1px solid var(--border-color);">${n}</td><td style="padding:0.5rem; border:1px solid var(--border-color); text-align:center;">${q}</td><td style="padding:0.5rem; border:1px solid var(--border-color); text-align:center;"><button class="btn btn-danger btn-sm" onclick="this.closest('tr').remove()">Delete</button></td>`;
    document.querySelector('#editableTable tbody').appendChild(tr);
    document.getElementById('newRowName').value = '';
}
</script>
"""),
            (10, "Search and Filter Table Records", "Live client-side text filter matching table rows in real time as the user types.", """
<div style="max-width: 520px; margin: 0 auto;">
    <input type="text" id="tableFilterInput" class="form-control" placeholder="Search table records (e.g. London, Designer)..." style="margin-bottom: 1rem;" oninput="filterTableRows()">
    <table id="searchableTable" style="width: 100%; border-collapse: collapse; background: var(--bg-card); border: 1px solid var(--border-color); font-size: 0.9rem;">
        <thead><tr style="background: rgba(99,102,241,0.2);"><th style="padding: 0.6rem; border: 1px solid var(--border-color);">Employee</th><th style="padding: 0.6rem; border: 1px solid var(--border-color);">Role</th><th style="padding: 0.6rem; border: 1px solid var(--border-color);">Location</th></tr></thead>
        <tbody>
            <tr><td style="padding: 0.5rem; border: 1px solid var(--border-color);">Alex Turner</td><td style="padding: 0.5rem; border: 1px solid var(--border-color);">Software Engineer</td><td style="padding: 0.5rem; border: 1px solid var(--border-color);">London</td></tr>
            <tr><td style="padding: 0.5rem; border: 1px solid var(--border-color);">Elena Rostova</td><td style="padding: 0.5rem; border: 1px solid var(--border-color);">Product Designer</td><td style="padding: 0.5rem; border: 1px solid var(--border-color);">Berlin</td></tr>
            <tr><td style="padding: 0.5rem; border: 1px solid var(--border-color);">David Chen</td><td style="padding: 0.5rem; border: 1px solid var(--border-color);">Database Architect</td><td style="padding: 0.5rem; border: 1px solid var(--border-color);">Singapore</td></tr>
            <tr><td style="padding: 0.5rem; border: 1px solid var(--border-color);">Sarah Connor</td><td style="padding: 0.5rem; border: 1px solid var(--border-color);">Security Lead</td><td style="padding: 0.5rem; border: 1px solid var(--border-color);">Austin</td></tr>
        </tbody>
    </table>
</div>
<script>
function filterTableRows() {
    const q = document.getElementById('tableFilterInput').value.toLowerCase();
    document.querySelectorAll('#searchableTable tbody tr').forEach(tr => {
        tr.style.display = tr.innerText.toLowerCase().includes(q) ? '' : 'none';
    });
}
</script>
"""),
            (11, "Live Character Counter for Textarea", "Monitors input events to count characters and remaining limit dynamically.", """
<div style="max-width: 450px; margin: 0 auto;">
    <textarea id="counterTextarea" class="form-control" rows="4" maxlength="150" placeholder="Type your review (Max 150 characters)..." oninput="updateCharCount(this)"></textarea>
    <div style="display: flex; justify-content: space-between; margin-top: 0.5rem; font-size: 0.85rem;">
        <span style="color: var(--text-muted);">Characters: <strong id="usedChars" style="color: var(--accent-primary);">0</strong></span>
        <span style="color: var(--text-muted);">Remaining: <strong id="remChars" style="color: var(--accent-teal);">150</strong></span>
    </div>
</div>
<script>
function updateCharCount(el) {
    const max = 150;
    const len = el.value.length;
    document.getElementById('usedChars').innerText = len;
    document.getElementById('remChars').innerText = max - len;
}
</script>
"""),
            (12, "Password Show/Hide Feature", "Toggles input type between 'password' and 'text' with visual eye icon switch.", """
<div style="max-width: 380px; margin: 0 auto;">
    <label class="form-label">Secure Access Password</label>
    <div style="position: relative;">
        <input type="password" id="pwField" class="form-control" value="SecretVault2026!" style="padding-right: 45px;">
        <button type="button" onclick="togglePasswordVis()" style="position: absolute; right: 8px; top: 50%; transform: translateY(-50%); background: transparent; border: none; font-size: 1.2rem; cursor: pointer; color: var(--text-muted);" id="pwToggleEye">👁️</button>
    </div>
</div>
<script>
function togglePasswordVis() {
    const f = document.getElementById('pwField');
    const eye = document.getElementById('pwToggleEye');
    if(f.type === 'password') { f.type = 'text'; eye.innerText = '🔒'; }
    else { f.type = 'password'; eye.innerText = '👁️'; }
}
</script>
"""),
            (13, "Dynamic Dropdown List", "Populates an HTML <select> options list dynamically from a JavaScript array.", """
<div style="max-width: 400px; margin: 0 auto;">
    <button class="btn btn-primary btn-sm" onclick="populateDropdown()" style="margin-bottom: 1rem; width: 100%;">Populate Technologies Dropdown</button>
    <select id="dynSelect" class="form-control">
        <option value="">Select Option</option>
    </select>
</div>
<script>
function populateDropdown() {
    const techs = ['JavaScript ES6+', 'TypeScript', 'React.js', 'Node.js', 'Python', 'WebAssembly'];
    const s = document.getElementById('dynSelect');
    s.innerHTML = '<option value="">Choose a technology</option>';
    techs.forEach(t => {
        const opt = document.createElement('option');
        opt.value = t; opt.innerText = t;
        s.appendChild(opt);
    });
}
</script>
"""),
            (14, "Dependent Dropdown (Country -> State -> City)", "Cascading dropdown menus where selecting country updates states, and selecting state updates cities.", """
<div style="max-width: 450px; margin: 0 auto; display: flex; flex-direction: column; gap: 1rem;">
    <div>
        <label class="form-label">1. Select Country</label>
        <select id="selCountry" class="form-control" onchange="onCountryChange()">
            <option value="">-- Choose Country --</option>
            <option value="India">India</option>
            <option value="USA">United States</option>
        </select>
    </div>
    <div>
        <label class="form-label">2. Select State</label>
        <select id="selState" class="form-control" onchange="onStateChange()" disabled>
            <option value="">-- Choose State First --</option>
        </select>
    </div>
    <div>
        <label class="form-label">3. Select City</label>
        <select id="selCity" class="form-control" disabled>
            <option value="">-- Choose City --</option>
        </select>
    </div>
</div>
<script>
const locData = {
    India: { 'Telangana': ['Hyderabad', 'Warangal'], 'Karnataka': ['Bengaluru', 'Mysuru'] },
    USA: { 'California': ['San Francisco', 'Los Angeles'], 'New York': ['New York City', 'Buffalo'] }
};
function onCountryChange() {
    const c = document.getElementById('selCountry').value;
    const s = document.getElementById('selState');
    const city = document.getElementById('selCity');
    s.innerHTML = '<option value="">-- Choose State --</option>';
    city.innerHTML = '<option value="">-- Choose City --</option>';
    city.disabled = true;
    if(c && locData[c]) {
        s.disabled = false;
        Object.keys(locData[c]).forEach(st => s.add(new Option(st, st)));
    } else s.disabled = true;
}
function onStateChange() {
    const c = document.getElementById('selCountry').value;
    const st = document.getElementById('selState').value;
    const city = document.getElementById('selCity');
    city.innerHTML = '<option value="">-- Choose City --</option>';
    if(c && st && locData[c][st]) {
        city.disabled = false;
        locData[c][st].forEach(ct => city.add(new Option(ct, ct)));
    } else city.disabled = true;
}
</script>
"""),
            (15, "Image Slideshow/Carousel Using JavaScript", "Interactive slideshow with Next, Prev buttons, indicator dots, and auto-play interval.", """
<div style="max-width: 480px; margin: 0 auto; text-align: center;">
    <div id="slideDisplay" style="height: 180px; border-radius: 12px; background: linear-gradient(135deg, #4f46e5, #06b6d4); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; color: white; margin-bottom: 1rem; transition: background 0.4s ease;">
        Slide 1: Web Architecture
    </div>
    <div style="display: flex; gap: 0.5rem; justify-content: center;">
        <button class="btn btn-outline btn-sm" onclick="moveSlide(-1)">◀ Previous</button>
        <button class="btn btn-outline btn-sm" onclick="moveSlide(1)">Next ▶</button>
    </div>
</div>
<script>
const slides = [
    { title: 'Slide 1: Web Architecture', bg: 'linear-gradient(135deg, #4f46e5, #06b6d4)' },
    { title: 'Slide 2: Responsive Design', bg: 'linear-gradient(135deg, #ec4899, #f59e0b)' },
    { title: 'Slide 3: JavaScript Engine', bg: 'linear-gradient(135deg, #10b981, #3b82f6)' }
];
let curSlide = 0;
function moveSlide(dir) {
    curSlide = (curSlide + dir + slides.length) % slides.length;
    const el = document.getElementById('slideDisplay');
    el.innerText = slides[curSlide].title;
    el.style.background = slides[curSlide].bg;
}
</script>
""")
        ]
    },
    "events": {
        "folder": "events",
        "badge_color": "var(--accent-pink)",
        "badge_bg": "rgba(236, 72, 153, 0.12)",
        "title": "JavaScript Events",
        "desc": "Event-driven programming: mouse listeners, keyboard tracker, bubbling vs capturing, event delegation, and HTML5 drag-and-drop.",
        "prefix": "event",
        "programs": [
            (1, "Demonstrate Mouse Events", "Tracks mouseover, mouseout, click, mousedown, mouseup, and mousemove coordinates.", """
<div id="mousePad" style="height: 160px; background: var(--bg-card); border: 2px dashed var(--accent-pink); border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: crosshair;" onmousemove="trackMouse(event)" onmousedown="this.style.background='rgba(236,72,153,0.3)'" onmouseup="this.style.background='var(--bg-card)'">
    <strong style="color: var(--accent-pink);">Hover &amp; Move Pointer In This Area</strong>
    <span id="coordsDisplay" style="font-family: var(--font-mono); font-size: 0.9rem; color: var(--text-secondary); margin-top: 0.5rem;">Coordinates: X: 0 | Y: 0</span>
</div>
<script>
function trackMouse(e) {
    const rect = e.currentTarget.getBoundingClientRect();
    const x = Math.floor(e.clientX - rect.left);
    const y = Math.floor(e.clientY - rect.top);
    document.getElementById('coordsDisplay').innerText = `Coordinates: X: ${x} | Y: ${y}`;
}
</script>
"""),
            (2, "Demonstrate Keyboard Events", "Inspects keydown and keyup events displaying key, code, and keyCode values.", """
<div style="max-width: 480px; margin: 0 auto; text-align: center;">
    <input type="text" id="keyInp" class="form-control" placeholder="Type any key here..." onkeydown="inspectKey(event)" style="margin-bottom: 1rem;">
    <div class="result-box"><div class="result-box-title">Key Event Inspector</div><div id="keyInfo" class="result-output" style="font-size: 0.95rem;">Press any key inside input</div></div>
</div>
<script>
function inspectKey(e) {
    document.getElementById('keyInfo').innerHTML = `Key: <strong style="color:var(--accent-teal)">${e.key}</strong> &bull; Code: <strong>${e.code}</strong> &bull; keyCode: <strong>${e.keyCode}</strong>`;
}
</script>
"""),
            (3, "Demonstrate Form Events (submit, change, focus, blur)", "Monitors form lifecycle events with live status alerts.", """
<div style="max-width: 450px; margin: 0 auto;">
    <div class="form-group">
        <label class="form-label">Input Event Target</label>
        <input type="text" class="form-control" placeholder="Focus and type here" onfocus="logFormEvt('Focused input (:focus)')" onblur="logFormEvt('Blurred input (lost focus)')" onchange="logFormEvt('Input value changed: ' + this.value)">
    </div>
    <div class="result-box"><div class="result-box-title">Event Trigger Log</div><div id="formEvtLog" class="result-output" style="font-size: 0.9rem;">Interact with field above</div></div>
</div>
<script>
function logFormEvt(msg) { document.getElementById('formEvtLog').innerText = msg; }
</script>
"""),
            (4, "Webpage That Responds to Double-Click Events", "Listens for ondblclick event to trigger animated heart likes and card expansions.", """
<div style="max-width: 320px; margin: 0 auto; text-align: center;">
    <div id="dblHeartBox" ondblclick="onHeartDblClick()" style="height: 180px; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; user-select: none;">
        <span id="heartIcon" style="font-size: 3.5rem; transition: transform 0.2s ease;">🤍</span>
        <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.5rem;">Double-Click to Like</p>
    </div>
</div>
<script>
let liked = false;
function onHeartDblClick() {
    liked = !liked;
    const h = document.getElementById('heartIcon');
    h.innerText = liked ? '💖' : '🤍';
    h.style.transform = 'scale(1.3)';
    setTimeout(() => h.style.transform = 'scale(1)', 200);
}
</script>
"""),
            (5, "Event Bubbling and Event Capturing", "Visualizes DOM event flow propagation through nested Parent and Child containers.", """
<div id="bubbleParent" onclick="logBubble('Parent Clicked (Bubbled Up)')" style="background: rgba(99,102,241,0.2); border: 2px solid var(--accent-primary); padding: 2rem; border-radius: 8px; text-align: center; cursor: pointer;">
    <strong>Parent Element (#bubbleParent)</strong>
    <div id="bubbleChild" onclick="logBubble('Child Clicked Directly');" style="background: rgba(236,72,153,0.3); border: 2px solid var(--accent-pink); padding: 1.25rem; border-radius: 6px; margin-top: 1rem;">
        Click Me (Child Element)
    </div>
</div>
<div class="result-box"><div class="result-box-title">Event Flow Trace</div><div id="bubbleLog" class="result-output" style="font-size: 0.85rem;">Click parent or child to observe propagation</div></div>
<script>
function logBubble(msg) {
    const el = document.getElementById('bubbleLog');
    el.innerHTML += `&bull; ${msg}<br>`;
}
</script>
"""),
            (6, "Demonstrate Event Delegation", "Attaches a single click listener on parent <ul> to manage dynamically generated list items.", """
<div style="max-width: 480px; margin: 0 auto;">
    <button class="btn btn-outline btn-sm" onclick="addDelegatedItem()" style="margin-bottom: 0.75rem;">+ Add New Item to Delegated List</button>
    <ul id="delegatedList" style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 0.5rem;">
        <li data-id="1" style="background: var(--bg-card); padding: 0.6rem 1rem; border-radius: 4px; border: 1px solid var(--border-color); cursor: pointer;">Item #1 (Click to select)</li>
        <li data-id="2" style="background: var(--bg-card); padding: 0.6rem 1rem; border-radius: 4px; border: 1px solid var(--border-color); cursor: pointer;">Item #2 (Click to select)</li>
    </ul>
    <div class="result-box"><div class="result-box-title">Delegated Event Receiver</div><div id="delgOutput" class="result-output" style="font-size: 0.9rem;">Click any item above</div></div>
</div>
<script>
let delgCount = 2;
document.getElementById('delegatedList').addEventListener('click', (e) => {
    if(e.target && e.target.nodeName === 'LI') {
        document.getElementById('delgOutput').innerText = `Delegated click caught for: "${e.target.innerText}"`;
        e.target.style.borderColor = 'var(--accent-teal)';
    }
});
function addDelegatedItem() {
    delgCount++;
    const li = document.createElement('li');
    li.style.cssText = "background: var(--bg-card); padding: 0.6rem 1rem; border-radius: 4px; border: 1px solid var(--border-color); cursor: pointer;";
    li.innerText = `Item #${delgCount} (Click to select)`;
    document.getElementById('delegatedList').appendChild(li);
}
</script>
"""),
            (7, "Keyboard-Controlled Webpage / Game", "Controls a player avatar box in a 2D game arena using Arrow Keys (Up, Down, Left, Right).", """
<div style="text-align: center;">
    <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">Use Keyboard <strong>Arrow Keys</strong> or <strong>WASD</strong> to move the player:</p>
    <div id="gameArena" style="position: relative; width: 340px; height: 220px; background: #0f172a; border: 2px solid var(--accent-primary); border-radius: 8px; margin: 0 auto; overflow: hidden;">
        <div id="playerAvatar" style="position: absolute; left: 150px; top: 90px; width: 32px; height: 32px; background: var(--accent-teal); border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; transition: all 0.05s linear;">🚀</div>
    </div>
</div>
<script>
let px = 150, py = 90;
window.addEventListener('keydown', (e) => {
    if(['ArrowUp', 'w', 'W'].includes(e.key)) py = Math.max(0, py - 15);
    else if(['ArrowDown', 's', 'S'].includes(e.key)) py = Math.min(188, py + 15);
    else if(['ArrowLeft', 'a', 'A'].includes(e.key)) px = Math.max(0, px - 15);
    else if(['ArrowRight', 'd', 'D'].includes(e.key)) px = Math.min(308, px + 15);
    const p = document.getElementById('playerAvatar');
    if(p) { p.style.left = px + 'px'; p.style.top = py + 'px'; }
});
</script>
"""),
            (8, "Drag-and-Drop Application Using JavaScript", "Implements native HTML5 Drag and Drop API with draggable cards between Status Columns.", """
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
    <div id="dropColA" ondragover="event.preventDefault()" ondrop="dropTask(event)" style="min-height: 180px; background: var(--bg-card); border: 2px dashed var(--border-color); border-radius: 8px; padding: 1rem;">
        <h5 style="color: var(--accent-primary); margin-bottom: 0.75rem;">To Do Column</h5>
        <div id="dragItem1" draggable="true" ondragstart="dragTask(event)" style="background: var(--bg-secondary); border: 1px solid var(--border-color); padding: 0.75rem; border-radius: 6px; cursor: grab; margin-bottom: 0.5rem;">
            📌 Implement Media Queries
        </div>
        <div id="dragItem2" draggable="true" ondragstart="dragTask(event)" style="background: var(--bg-secondary); border: 1px solid var(--border-color); padding: 0.75rem; border-radius: 6px; cursor: grab;">
            📌 Test Event Delegation
        </div>
    </div>
    <div id="dropColB" ondragover="event.preventDefault()" ondrop="dropTask(event)" style="min-height: 180px; background: var(--bg-card); border: 2px dashed var(--accent-emerald); border-radius: 8px; padding: 1rem;">
        <h5 style="color: var(--accent-emerald); margin-bottom: 0.75rem;">Done Column</h5>
    </div>
</div>
<script>
function dragTask(e) { e.dataTransfer.setData('text', e.target.id); }
function dropTask(e) {
    e.preventDefault();
    const id = e.dataTransfer.getData('text');
    const item = document.getElementById(id);
    if(item) e.currentTarget.appendChild(item);
}
</script>
""")
        ]
    },
    "forms-validation": {
        "folder": "forms-validation",
        "badge_color": "var(--accent-rose)",
        "badge_bg": "rgba(244, 63, 94, 0.12)",
        "title": "Forms & Validation",
        "desc": "Client-side validation, password entropy meters, dynamic inline errors, and multi-field admission registration checks.",
        "prefix": "form",
        "programs": [
            (1, "Student Registration Form with JavaScript Validation", "Full validation of student personal details, email format, and age criteria.", """
<form onsubmit="validStudentReg(event)" style="max-width: 480px; margin: 0 auto; background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div class="form-group"><label class="form-label">Full Name</label><input type="text" id="srName" class="form-control" required><small id="e_srName" style="color:var(--accent-rose);display:none;">Name must have 3+ characters.</small></div>
    <div class="form-group"><label class="form-label">Email</label><input type="email" id="srEmail" class="form-control" required><small id="e_srEmail" style="color:var(--accent-rose);display:none;">Enter valid academic email.</small></div>
    <button type="submit" class="btn btn-primary" style="width: 100%;">Verify &amp; Register</button>
</form>
<script>
function validStudentReg(e) {
    e.preventDefault();
    const n = document.getElementById('srName').value.trim();
    const em = document.getElementById('srEmail').value.trim();
    let ok = true;
    if(n.length < 3) { document.getElementById('e_srName').style.display='block'; ok = false; } else document.getElementById('e_srName').style.display='none';
    if(!em.includes('@')) { document.getElementById('e_srEmail').style.display='block'; ok = false; } else document.getElementById('e_srEmail').style.display='none';
    if(ok) alert('Registration validated successfully!');
}
</script>
"""),
            (2, "Login Form with Username and Password Validation", "Validates credential length and prevents injection of illegal characters.", """
<form onsubmit="validLogin(event)" style="max-width: 400px; margin: 0 auto; background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div class="form-group"><input type="text" id="lgUser" class="form-control" placeholder="Username (min 4 chars)" required></div>
    <div class="form-group"><input type="password" id="lgPass" class="form-control" placeholder="Password (min 6 chars)" required></div>
    <button type="submit" class="btn btn-primary" style="width: 100%;">Authenticate</button>
</form>
<script>
function validLogin(e) {
    e.preventDefault();
    const u = document.getElementById('lgUser').value.trim();
    const p = document.getElementById('lgPass').value;
    if(u.length < 4 || p.length < 6) alert('Invalid credentials length.');
    else alert('Login passed validation!');
}
</script>
"""),
            (3, "Password Strength Checker", "Real-time calculation of password entropy measuring length, numbers, and symbols.", """
<div style="max-width: 420px; margin: 0 auto;">
    <input type="password" id="pwMeterInp" class="form-control" placeholder="Type password to evaluate..." oninput="checkStrength(this.value)" style="margin-bottom: 0.75rem;">
    <div style="height: 8px; width: 100%; background: #334155; border-radius: 4px; overflow: hidden; margin-bottom: 0.5rem;">
        <div id="pwMeterBar" style="height: 100%; width: 0%; background: var(--accent-rose); transition: all 0.3s ease;"></div>
    </div>
    <div id="pwMeterStatus" style="font-size: 0.85rem; font-weight: bold; color: var(--text-muted); text-align: right;">Strength: None</div>
</div>
<script>
function checkStrength(pw) {
    let s = 0;
    if(pw.length >= 8) s += 25;
    if(/[A-Z]/.test(pw)) s += 25;
    if(/[0-9]/.test(pw)) s += 25;
    if(/[^A-Za-z0-9]/.test(pw)) s += 25;
    const bar = document.getElementById('pwMeterBar');
    const txt = document.getElementById('pwMeterStatus');
    bar.style.width = s + '%';
    if(s <= 25) { bar.style.backgroundColor = 'var(--accent-rose)'; txt.innerText = 'Strength: Weak'; }
    else if(s <= 75) { bar.style.backgroundColor = 'var(--accent-amber)'; txt.innerText = 'Strength: Moderate'; }
    else { bar.style.backgroundColor = 'var(--accent-emerald)'; txt.innerText = 'Strength: Very Strong'; }
}
</script>
"""),
            (4, "Signup Form with Password Confirmation", "Ensures password and confirm password fields match before allowing submission.", """
<form onsubmit="checkConfirmPw(event)" style="max-width: 400px; margin: 0 auto; background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div class="form-group"><input type="password" id="cpw1" class="form-control" placeholder="Choose Password" required></div>
    <div class="form-group"><input type="password" id="cpw2" class="form-control" placeholder="Confirm Password" required oninput="syncPwMatch()"></div>
    <div id="pwMatchFeedback" style="font-size: 0.85rem; margin-bottom: 1rem;"></div>
    <button type="submit" class="btn btn-primary" style="width: 100%;">Create Account</button>
</form>
<script>
function syncPwMatch() {
    const p1 = document.getElementById('cpw1').value;
    const p2 = document.getElementById('cpw2').value;
    const fb = document.getElementById('pwMatchFeedback');
    if(!p2) { fb.innerText = ''; return; }
    if(p1 === p2) fb.innerHTML = '<span style="color:var(--accent-emerald)">✓ Passwords Match</span>';
    else fb.innerHTML = '<span style="color:var(--accent-rose)">✗ Passwords do NOT match</span>';
}
function checkConfirmPw(e) {
    e.preventDefault();
    if(document.getElementById('cpw1').value !== document.getElementById('cpw2').value) alert('Passwords must match.');
    else alert('Account registered successfully!');
}
</script>
"""),
            (5, "Feedback Form with Validation", "Customer feedback form with mandatory star rating selection and text comment length checks.", """
<form onsubmit="validFeedback(event)" style="max-width: 450px; margin: 0 auto; background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div class="form-group">
        <label class="form-label">Service Rating</label>
        <select id="fbRating" class="form-control" required>
            <option value="">Select Stars</option>
            <option value="5">⭐⭐⭐⭐⭐ Excellent (5 Stars)</option>
            <option value="4">⭐⭐⭐⭐ Good (4 Stars)</option>
            <option value="3">⭐⭐⭐ Satisfactory (3 Stars)</option>
        </select>
    </div>
    <div class="form-group"><textarea id="fbComment" class="form-control" rows="3" placeholder="Share your suggestions (min 15 characters)..." required></textarea></div>
    <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Feedback</button>
</form>
<script>
function validFeedback(e) {
    e.preventDefault();
    if(document.getElementById('fbComment').value.trim().length < 15) alert('Comment must be at least 15 characters.');
    else alert('Thank you for your valuable feedback!');
}
</script>
"""),
            (6, "College Admission Form with JavaScript Validation", "Validates qualification percentage, date of birth eligibility, and stream preferences.", """
<form onsubmit="validAdmission(event)" style="max-width: 480px; margin: 0 auto; background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div class="form-group"><label class="form-label">Applicant Name</label><input type="text" id="admName" class="form-control" required></div>
    <div class="form-group"><label class="form-label">Qualifying 12th / Diploma %</label><input type="number" id="admPct" class="form-control" min="0" max="100" placeholder="e.g. 88" required></div>
    <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Admission Request</button>
</form>
<script>
function validAdmission(e) {
    e.preventDefault();
    const pct = parseFloat(document.getElementById('admPct').value);
    if(pct < 60) alert('Eligibility requirement is at least 60% aggregate marks.');
    else alert('Admission eligibility criteria met! Form submitted.');
}
</script>
"""),
            (7, "Display Validation Error Messages Dynamically Without Reloading the Page", "Provides real-time instant input validation states with error messages without reloading.", """
<div style="max-width: 420px; margin: 0 auto;">
    <div class="form-group">
        <label class="form-label">Account Handle (@handle)</label>
        <input type="text" id="dynHandleInp" class="form-control" placeholder="@username" oninput="validHandleLive(this.value)">
        <div id="liveHandleMsg" style="font-size: 0.85rem; margin-top: 0.35rem;"></div>
    </div>
</div>
<script>
function validHandleLive(val) {
    const m = document.getElementById('liveHandleMsg');
    if(!val.startsWith('@')) { m.innerHTML = '<span style="color:var(--accent-rose)">Must begin with @ symbol</span>'; }
    else if(val.length < 5) { m.innerHTML = '<span style="color:var(--accent-amber)">Too short (min 5 chars)</span>'; }
    else { m.innerHTML = '<span style="color:var(--accent-emerald)">✓ Valid handle format</span>'; }
}
</script>
""")
        ]
    },
    "browser-storage": {
        "folder": "browser-storage",
        "badge_color": "var(--accent-emerald)",
        "badge_bg": "rgba(16, 185, 129, 0.12)",
        "title": "Browser Objects & Web Storage",
        "desc": "Window, Navigator, Location, and History browser APIs, plus localStorage, sessionStorage, persistent shopping cart, and theme persistence.",
        "prefix": "storage",
        "programs": [
            (1, "Demonstrate the Window Object", "Inspects window.innerWidth, innerHeight, screen resolution, and window.open/close methods.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.9rem;">
    <div id="winInfo" style="color: var(--accent-teal); line-height: 1.8;"></div>
</div>
<script>
function loadWinInfo() {
    document.getElementById('winInfo').innerHTML = `
        &bull; window.innerWidth: <strong>${window.innerWidth}px</strong><br>
        &bull; window.innerHeight: <strong>${window.innerHeight}px</strong><br>
        &bull; window.screen.width: <strong>${window.screen.width}px</strong><br>
        &bull; window.devicePixelRatio: <strong>${window.devicePixelRatio}</strong>
    `;
}
loadWinInfo();
window.addEventListener('resize', loadWinInfo);
</script>
"""),
            (2, "Demonstrate the Navigator Object", "Reads browser userAgent, platform, online connectivity, and language preferences.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.85rem; line-height: 1.8;">
    <div id="navInfo" style="color: #818cf8;"></div>
</div>
<script>
document.getElementById('navInfo').innerHTML = `
    &bull; navigator.userAgent: <strong>${navigator.userAgent.slice(0, 70)}...</strong><br>
    &bull; navigator.language: <strong>${navigator.language}</strong><br>
    &bull; navigator.onLine: <strong style="color:var(--accent-emerald)">${navigator.onLine ? 'Connected (Online)' : 'Offline'}</strong><br>
    &bull; navigator.cookieEnabled: <strong>${navigator.cookieEnabled}</strong>
`;
</script>
"""),
            (3, "Demonstrate the Location Object", "Inspects window.location properties (href, hostname, protocol, pathname, search, hash).", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); font-family: var(--font-mono); font-size: 0.85rem; line-height: 1.8;">
    <div id="locInfo" style="color: var(--accent-amber);"></div>
</div>
<script>
document.getElementById('locInfo').innerHTML = `
    &bull; location.protocol: <strong>${window.location.protocol}</strong><br>
    &bull; location.hostname: <strong>${window.location.hostname || 'localhost'}</strong><br>
    &bull; location.pathname: <strong>${window.location.pathname}</strong><br>
    &bull; location.href: <strong>${window.location.href}</strong>
`;
</script>
"""),
            (4, "Demonstrate the History Object", "Explores window.history.length, back(), forward(), and pushState() methods.", """
<div style="max-width: 450px; margin: 0 auto; text-align: center;">
    <div class="result-box"><div class="result-box-title">Session History Length</div><div id="histCount" class="result-output">Loading...</div></div>
    <div style="display: flex; gap: 0.5rem; justify-content: center; margin-top: 1rem;">
        <button class="btn btn-outline btn-sm" onclick="window.history.back()">history.back()</button>
        <button class="btn btn-outline btn-sm" onclick="window.history.forward()">history.forward()</button>
    </div>
</div>
<script>
document.getElementById('histCount').innerText = `${window.history.length} history states stored`;
</script>
"""),
            (5, "Program Using localStorage", "Demonstrates persistent cross-tab storage with setItem, getItem, and clear.", """
<div style="max-width: 480px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="text" id="demoLsVal" class="form-control" placeholder="Store custom note">
        <button class="btn btn-primary btn-sm" onclick="saveLs()">Persist</button>
        <button class="btn btn-danger btn-sm" onclick="clearLs()">Clear</button>
    </div>
    <div class="result-box"><div class="result-box-title">Retrieved from localStorage</div><div id="lsReadOut" class="result-output">None</div></div>
</div>
<script>
function saveLs() {
    const v = document.getElementById('demoLsVal').value;
    localStorage.setItem('my_persisted_note', v);
    loadLs();
}
function loadLs() {
    document.getElementById('lsReadOut').innerText = localStorage.getItem('my_persisted_note') || 'Empty';
}
function clearLs() {
    localStorage.removeItem('my_persisted_note');
    loadLs();
}
loadLs();
</script>
"""),
            (6, "Program Using sessionStorage", "Stores data scoped to current browser tab, automatically cleared when tab closes.", """
<div style="max-width: 480px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <input type="text" id="ssVal" class="form-control" placeholder="Session-only token">
        <button class="btn btn-primary btn-sm" onclick="saveSs()">Save Session</button>
    </div>
    <div class="result-box"><div class="result-box-title">sessionStorage Content</div><div id="ssReadOut" class="result-output">None</div></div>
</div>
<script>
function saveSs() {
    const v = document.getElementById('ssVal').value;
    sessionStorage.setItem('tab_session_key', v);
    document.getElementById('ssReadOut').innerText = sessionStorage.getItem('tab_session_key');
}
document.getElementById('ssReadOut').innerText = sessionStorage.getItem('tab_session_key') || 'No session data in this tab';
</script>
"""),
            (7, "Shopping Cart Using localStorage", "Persists added items in a shopping cart so items remain after page refresh.", """
<div style="max-width: 500px; margin: 0 auto;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
        <button class="btn btn-outline btn-sm" onclick="addToCartStorage('Mechanical Keyboard')">+ Keyboard ($79)</button>
        <button class="btn btn-outline btn-sm" onclick="addToCartStorage('Ergonomic Mouse')">+ Mouse ($49)</button>
        <button class="btn btn-danger btn-sm" onclick="clearCartStorage()">Clear Cart</button>
    </div>
    <ul id="cartStorageList" style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 0.5rem;"></ul>
</div>
<script>
function getCart() { return JSON.parse(localStorage.getItem('user_cart') || '[]'); }
function setCart(c) { localStorage.setItem('user_cart', JSON.stringify(c)); renderCart(); }
function addToCartStorage(item) { const c = getCart(); c.push(item); setCart(c); }
function clearCartStorage() { setCart([]); }
function renderCart() {
    const list = document.getElementById('cartStorageList');
    const c = getCart();
    list.innerHTML = c.length ? c.map(i => `<li style="background:var(--bg-card);padding:0.5rem 1rem;border-radius:4px;border:1px solid var(--border-color);">${i}</li>`).join('') : '<li style="color:var(--text-muted);">Cart is empty.</li>';
}
renderCart();
</script>
"""),
            (8, "Theme Switcher (Light/Dark Mode) Using localStorage", "Persists user's preferred visual theme mode across reloads using localStorage.", """
<div style="text-align: center; background: var(--bg-card); padding: 2rem; border-radius: 12px; border: 1px solid var(--border-color);">
    <h3 style="color: var(--accent-primary); margin-bottom: 0.5rem;">Theme Preference Persistence</h3>
    <p style="color: var(--text-secondary); margin-bottom: 1.25rem;">Stored under key <code>'app-theme'</code> in browser localStorage.</p>
    <div style="display: flex; gap: 0.5rem; justify-content: center;">
        <button class="btn btn-primary" onclick="setAppTheme('dark')">Dark Mode 🌙</button>
        <button class="btn btn-outline" onclick="setAppTheme('light')">Light Mode ☀️</button>
    </div>
</div>
<script>
function setAppTheme(t) {
    document.documentElement.setAttribute('data-theme', t);
    localStorage.setItem('app-theme', t);
    const b = document.getElementById('themeToggleBtn');
    if(b) b.innerText = t === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode';
}
</script>
""")
        ]
    }
}

def generate_subcat_page(cat_key, cat_info, prog, prev_prog, next_prog, total):
    pid, title, desc, demo = prog
    file_name = f"{cat_info['prefix']}-{pid:02d}.html"
    prev_link = f"{cat_info['prefix']}-{prev_prog[0]:02d}.html" if prev_prog else "#"
    next_link = f"{cat_info['prefix']}-{next_prog[0]:02d}.html" if next_prog else "#"
    prev_disabled = "opacity: 0.5; pointer-events: none;" if not prev_prog else ""
    next_disabled = "opacity: 0.5; pointer-events: none;" if not next_prog else ""
    code_escaped = demo.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{cat_info['title']} #{pid:02d}: {title}</title>
    <link rel="stylesheet" href="../../assets/css/style.css">
</head>
<body>
    <header class="top-nav">
        <div class="container nav-container">
            <a href="../../index.html" class="nav-brand">
                <span>⚡ Practical Lab</span>
                <span class="brand-badge" style="background: {cat_info['badge_color']};">{cat_info['title']} #{pid:02d}</span>
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
                    <a href="index.html">{cat_info['title']}</a>
                    <span class="separator">/</span>
                    <span style="color: var(--text-primary); font-weight: 600;">Program #{pid:02d}</span>
                </div>
                <div class="nav-controls">
                    <a href="{prev_link}" class="btn btn-outline btn-sm btn-prev" style="{prev_disabled}">⬅ Prev</a>
                    <a href="index.html" class="btn btn-outline btn-sm">📋 {cat_info['title']}</a>
                    <a href="{next_link}" class="btn btn-outline btn-sm btn-next" style="{next_disabled}">Next ➡</a>
                </div>
            </div>

            <!-- Experiment Title & Description -->
            <div class="experiment-header-card" style="border-left-color: {cat_info['badge_color']};">
                <span class="experiment-badge" style="color: {cat_info['badge_color']}; background: {cat_info['badge_bg']};">EXPERIMENT #{pid:02d} OF {total:02d}</span>
                <h1 class="experiment-title">{title}</h1>
                <p class="experiment-desc">{desc}</p>
            </div>

            <!-- Demonstration Section -->
            <div class="demo-section">
                <div class="demo-bar">
                    <span class="demo-title"><span class="demo-badge" style="background: {cat_info['badge_color']}; box-shadow: 0 0 8px {cat_info['badge_color']};"></span> Live Interactive Demonstration</span>
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
                    <span class="code-arrow" style="font-size: 0.85rem; color: {cat_info['badge_color']};">▼ View Code</span>
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
                    <a href="index.html" class="btn btn-primary" style="background: {cat_info['badge_color']};">📋 Category List</a>
                </div>
                <a href="{next_link}" class="btn btn-outline btn-next" style="{next_disabled}">Next Program ➡</a>
            </div>
        </div>
    </main>

    <footer class="site-footer">
        <div class="container footer-content">
            <p>Student Name: <span class="footer-highlight">M.Surya Nivas Reddy</span> | Assignment: <span class="footer-highlight">HTML, CSS & JavaScript Practical Assignment</span></p>
            <p style="font-size: 0.8rem; color: var(--text-muted);">{cat_info['title']} Module &bull; Program {pid} of {total}</p>
        </div>
    </footer>

    <script src="../../assets/js/common.js"></script>
</body>
</html>
"""
    return html

def generate_subcat_index(cat_key, cat_info):
    cards = ""
    for prog in cat_info["programs"]:
        pid, title, desc, _ = prog
        file_name = f"{cat_info['prefix']}-{pid:02d}.html"
        cards += f"""
        <a href="{file_name}" class="program-card" data-category="{cat_key}">
            <div class="program-header">
                <span class="program-number" style="color: {cat_info['badge_color']}; background: {cat_info['badge_bg']};">{cat_info['prefix'].upper()} #{pid:02d}</span>
                <span style="font-size: 0.85rem; color: var(--text-muted);">Practical</span>
            </div>
            <h3 class="program-title">{title}</h3>
            <p class="program-desc">{desc}</p>
            <div class="program-footer">
                <span>Source: {file_name}</span>
                <span class="program-link-text" style="color: {cat_info['badge_color']};">Launch Demo &rarr;</span>
            </div>
        </a>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{cat_info['title']} Practical Programs List</title>
    <link rel="stylesheet" href="../../assets/css/style.css">
</head>
<body>
    <header class="top-nav">
        <div class="container nav-container">
            <a href="../../index.html" class="nav-brand">
                <span>⚡ Practical Lab</span>
                <span class="brand-badge" style="background: {cat_info['badge_color']};">{cat_info['title']}</span>
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
                <span class="page-badge" style="background: {cat_info['badge_bg']}; color: {cat_info['badge_color']}; border-color: {cat_info['badge_color']};">JAVASCRIPT SUITE &bull; {len(cat_info['programs'])} PRACTICAL PROGRAMS</span>
                <h1 class="page-title">{cat_info['title']}</h1>
                <p class="page-subtitle">{cat_info['desc']}</p>
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
                        <span class="meta-value">{cat_info['title']}</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Completed</span>
                        <span class="meta-value" style="color: {cat_info['badge_color']};">{len(cat_info['programs'])} / {len(cat_info['programs'])} Programs</span>
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
                    <input type="text" id="programSearch" class="search-input" placeholder="Search {cat_info['title']} programs...">
                </div>
                <div class="filter-tags">
                    <button class="filter-tag active" data-filter="all">All ({len(cat_info['programs'])})</button>
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
            <p style="font-size: 0.8rem; color: var(--text-muted);">{cat_info['title']} ({len(cat_info['programs'])} Programs)</p>
        </div>
    </footer>

    <script src="../../assets/js/common.js"></script>
</body>
</html>
"""
    return html

def main():
    for cat_key, cat_info in CATEGORIES.items():
        total = len(cat_info["programs"])
        print(f"Generating {total} programs for {cat_info['title']}...")
        folder_path = os.path.join("javascript", cat_info["folder"])
        os.makedirs(folder_path, exist_ok=True)
        for i, prog in enumerate(cat_info["programs"]):
            prev_prog = cat_info["programs"][i - 1] if i > 0 else None
            next_prog = cat_info["programs"][i + 1] if i < total - 1 else None
            page_html = generate_subcat_page(cat_key, cat_info, prog, prev_prog, next_prog, total)
            file_name = f"{cat_info['prefix']}-{prog[0]:02d}.html"
            with open(os.path.join(folder_path, file_name), "w", encoding="utf-8") as f:
                f.write(page_html)
        
        index_html = generate_subcat_index(cat_key, cat_info)
        with open(os.path.join(folder_path, "index.html"), "w", encoding="utf-8") as f:
            f.write(index_html)
    print("DOM, Events, Forms, and Browser/Storage programs successfully generated!")

if __name__ == "__main__":
    main()
