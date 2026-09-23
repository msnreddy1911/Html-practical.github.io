"""
Generator for HTML Practical Programs (1 to 15) and html/index.html
"""
import os

HTML_PROGRAMS = [
    {
        "id": 1,
        "file": "html-01.html",
        "title": "Basic HTML Webpage with Headings, Paragraphs, and Line Breaks",
        "desc": "Demonstrates standard HTML document structure, hierarchy of headings (h1-h6), paragraph tags (<p>), line breaks (<br>), and horizontal rules (<hr>).",
        "demo": """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
    <h1>Main Heading (h1) - Web Technologies Overview</h1>
    <p>HTML (HyperText Markup Language) is the standard markup language used to structure web pages and their content.<br>It consists of a series of elements that instruct the browser on how to display content.</p>
    <hr style="margin: 1.5rem 0; border: 0; border-top: 1px solid var(--border-color);">
    <h2>Secondary Heading (h2) - Structural Typography</h2>
    <p>Headings allow screen readers and search engines to understand the document outline. Line breaks (<br>) allow wrapping text without starting a new paragraph.</p>
    <h3>Section Heading (h3) - Paragraph Variations</h3>
    <p><strong>Bold text:</strong> HTML is essential for web development.<br>
       <em>Italic text:</em> Used for emphasis and nuances.<br>
       <u>Underlined text:</u> Highlights specific keywords.<br>
       <mark style="background: rgba(245, 158, 11, 0.3); color: #f59e0b; padding: 0.1rem 0.3rem; border-radius: 3px;">Marked text:</mark> Visual attention highlight.</p>
    <h4>Sub-heading Level 4 (h4)</h4>
    <h5>Sub-heading Level 5 (h5)</h5>
    <h6>Sub-heading Level 6 (h6) - Smallest Structural Heading</h6>
</div>
        """
    },
    {
        "id": 2,
        "file": "html-02.html",
        "title": "Ordered, Unordered, and Description Lists",
        "desc": "Showcases ordered lists (<ol>), unordered bulleted lists (<ul>), nested lists, and description lists (<dl>, <dt>, <dd>).",
        "demo": """
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
    <div style="background: var(--bg-card); padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
        <h3 style="color: var(--accent-teal); margin-bottom: 0.75rem;">Unordered List (&lt;ul&gt;)</h3>
        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.5rem;">Web Development Pillars:</p>
        <ul style="padding-left: 1.5rem; color: var(--text-primary); line-height: 1.8;">
            <li>HTML5 - Content & Structure</li>
            <li>CSS3 - Styling & Layouts
                <ul style="padding-left: 1.5rem; margin-top: 0.25rem;">
                    <li>Flexbox & Grid</li>
                    <li>Animations & Transitions</li>
                </ul>
            </li>
            <li>JavaScript - Interactivity & Logic</li>
        </ul>
    </div>
    <div style="background: var(--bg-card); padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
        <h3 style="color: var(--accent-primary); margin-bottom: 0.75rem;">Ordered List (&lt;ol&gt;)</h3>
        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.5rem;">Execution Steps:</p>
        <ol style="padding-left: 1.5rem; color: var(--text-primary); line-height: 1.8;">
            <li>Plan page hierarchy and wireframe</li>
            <li>Write semantic HTML tags</li>
            <li>Apply responsive CSS rules</li>
            <li>Add interactive JavaScript events</li>
        </ol>
    </div>
    <div style="background: var(--bg-card); padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
        <h3 style="color: var(--accent-pink); margin-bottom: 0.75rem;">Description List (&lt;dl&gt;)</h3>
        <dl style="line-height: 1.6;">
            <dt style="font-weight: 700; color: var(--text-primary);">HTML</dt>
            <dd style="color: var(--text-secondary); margin-left: 1rem; margin-bottom: 0.5rem;">HyperText Markup Language for document structures.</dd>
            <dt style="font-weight: 700; color: var(--text-primary);">CSS</dt>
            <dd style="color: var(--text-secondary); margin-left: 1rem; margin-bottom: 0.5rem;">Cascading Style Sheets for visual styling.</dd>
            <dt style="font-weight: 700; color: var(--text-primary);">DOM</dt>
            <dd style="color: var(--text-secondary); margin-left: 1rem;">Document Object Model representing page elements as an object tree.</dd>
        </dl>
    </div>
</div>
        """
    },
    {
        "id": 3,
        "file": "html-03.html",
        "title": "Tables with Rows, Columns, Borders, and Merged Cells",
        "desc": "Demonstrates HTML tables using <table>, <thead>, <tbody>, <tr>, <th>, <td> with cell merging via colspan and rowspan attributes.",
        "demo": """
<div style="overflow-x: auto;">
    <table style="width: 100%; border-collapse: collapse; text-align: left; background: var(--bg-card); border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-color);">
        <thead>
            <tr style="background: rgba(99, 102, 241, 0.15); border-bottom: 2px solid var(--border-color);">
                <th style="padding: 1rem; border: 1px solid var(--border-color);">Department</th>
                <th style="padding: 1rem; border: 1px solid var(--border-color);">Semester</th>
                <th style="padding: 1rem; border: 1px solid var(--border-color);">Subject Name</th>
                <th style="padding: 1rem; border: 1px solid var(--border-color);">Credits</th>
                <th style="padding: 1rem; border: 1px solid var(--border-color);">Exam Type</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td rowspan="3" style="padding: 0.85rem; border: 1px solid var(--border-color); font-weight: 600; vertical-align: middle;">Computer Science & Engineering</td>
                <td rowspan="2" style="padding: 0.85rem; border: 1px solid var(--border-color); vertical-align: middle;">Semester IV</td>
                <td style="padding: 0.85rem; border: 1px solid var(--border-color);">Web Technologies (HTML, CSS, JS)</td>
                <td style="padding: 0.85rem; border: 1px solid var(--border-color);">4</td>
                <td style="padding: 0.85rem; border: 1px solid var(--border-color);">Theory + Lab</td>
            </tr>
            <tr>
                <td style="padding: 0.85rem; border: 1px solid var(--border-color);">Database Management Systems</td>
                <td style="padding: 0.85rem; border: 1px solid var(--border-color);">4</td>
                <td style="padding: 0.85rem; border: 1px solid var(--border-color);">Theory + Lab</td>
            </tr>
            <tr>
                <td style="padding: 0.85rem; border: 1px solid var(--border-color);">Semester V</td>
                <td style="padding: 0.85rem; border: 1px solid var(--border-color);">Operating Systems & Virtualization</td>
                <td style="padding: 0.85rem; border: 1px solid var(--border-color);">3</td>
                <td style="padding: 0.85rem; border: 1px solid var(--border-color);">Theory</td>
            </tr>
            <tr style="background: rgba(255, 255, 255, 0.03);">
                <td colspan="3" style="padding: 0.85rem; border: 1px solid var(--border-color); font-weight: 700; text-align: right;">Total Program Cumulative Credits:</td>
                <td colspan="2" style="padding: 0.85rem; border: 1px solid var(--border-color); font-weight: 700; color: var(--accent-teal);">11 Credits (Verified)</td>
            </tr>
        </tbody>
    </table>
</div>
        """
    },
    {
        "id": 4,
        "file": "html-04.html",
        "title": "HTML Page Containing Images and Hyperlinks",
        "desc": "Illustrates relative and absolute image paths, alt attributes, figure/figcaption, external links (_blank), internal anchor bookmarks, and mailto links.",
        "demo": """
<div style="display: flex; flex-direction: column; gap: 1.5rem;">
    <div style="display: flex; flex-wrap: wrap; gap: 1.5rem; align-items: center; background: var(--bg-card); padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
        <figure style="margin: 0; text-align: center;">
            <svg width="220" height="140" style="border-radius: var(--radius-md); background: linear-gradient(135deg, #4f46e5, #06b6d4);">
                <text x="50%" y="45%" text-anchor="middle" fill="#ffffff" font-size="16" font-family="sans-serif" font-weight="bold">Responsive Web</text>
                <text x="50%" y="65%" text-anchor="middle" fill="#e0e7ff" font-size="12" font-family="sans-serif">Vector Image Demo (SVG)</text>
            </svg>
            <figcaption style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.5rem;">Figure: High-Resolution Scalable Vector Artwork</figcaption>
        </figure>
        <div style="flex: 1; min-width: 250px;">
            <h3 style="margin-bottom: 0.75rem; color: var(--text-primary);">Navigation Hyperlinks</h3>
            <p style="color: var(--text-secondary); margin-bottom: 1rem;">HTML provides standard attributes for linking documents, pages, and section bookmarks.</p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.75rem;">
                <a href="#target-section" class="btn btn-primary btn-sm">Go to Bookmark Target ↓</a>
                <a href="https://developer.mozilla.org" target="_blank" rel="noopener" class="btn btn-outline btn-sm">MDN Web Docs ↗</a>
                <a href="mailto:student@example.edu" class="btn btn-outline btn-sm">✉ Send Email</a>
            </div>
        </div>
    </div>
    <div id="target-section" style="padding: 1.25rem; background: rgba(99, 102, 241, 0.1); border: 1px dashed var(--accent-primary); border-radius: var(--radius-md);">
        <h4 style="color: var(--accent-primary); margin-bottom: 0.25rem;">Bookmark Target Section Reached (#target-section)</h4>
        <p style="color: var(--text-secondary); font-size: 0.9rem;">You navigated directly to this internal bookmark using anchor fragment navigation.</p>
    </div>
</div>
        """
    },
    {
        "id": 5,
        "file": "html-05.html",
        "title": "Student Registration Form Using HTML Form Elements",
        "desc": "Demonstrates comprehensive HTML form components including fieldsets, legends, labels, inputs, radios, checkboxes, dropdown selects, and textareas.",
        "demo": """
<form onsubmit="event.preventDefault(); alert('Form submitted successfully!');" style="background: var(--bg-card); padding: 1.75rem; border-radius: var(--radius-lg); border: 1px solid var(--border-color);">
    <fieldset style="border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.25rem;">
        <legend style="padding: 0 0.5rem; color: var(--accent-teal); font-weight: 600;">Personal Information</legend>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem;">
            <div>
                <label class="form-label" for="stdName">Full Name *</label>
                <input class="form-control" type="text" id="stdName" required placeholder="Enter student full name">
            </div>
            <div>
                <label class="form-label" for="stdReg">Registration Number *</label>
                <input class="form-control" type="text" id="stdReg" required placeholder="e.g. 21BCE1024">
            </div>
            <div>
                <label class="form-label">Gender</label>
                <div style="display: flex; gap: 1rem; align-items: center; margin-top: 0.5rem;">
                    <label style="color: var(--text-secondary); display: flex; align-items: center; gap: 0.3rem;"><input type="radio" name="gender" value="male" checked> Male</label>
                    <label style="color: var(--text-secondary); display: flex; align-items: center; gap: 0.3rem;"><input type="radio" name="gender" value="female"> Female</label>
                    <label style="color: var(--text-secondary); display: flex; align-items: center; gap: 0.3rem;"><input type="radio" name="gender" value="other"> Other</label>
                </div>
            </div>
        </div>
    </fieldset>
    <fieldset style="border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.25rem;">
        <legend style="padding: 0 0.5rem; color: var(--accent-primary); font-weight: 600;">Academic Enrollment</legend>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem;">
            <div>
                <label class="form-label" for="courseSelect">Degree Program</label>
                <select class="form-control" id="courseSelect">
                    <option>B.Tech Computer Science & Engineering</option>
                    <option>B.Tech Information Technology</option>
                    <option>B.Tech Artificial Intelligence & Data Science</option>
                    <option>MCA Master of Computer Applications</option>
                </select>
            </div>
            <div>
                <label class="form-label">Specializations / Electives</label>
                <div style="display: flex; flex-direction: column; gap: 0.35rem; margin-top: 0.25rem;">
                    <label style="color: var(--text-secondary);"><input type="checkbox" checked> Cloud Architecture</label>
                    <label style="color: var(--text-secondary);"><input type="checkbox" checked> Web Development Frameworks</label>
                    <label style="color: var(--text-secondary);"><input type="checkbox"> Cybersecurity Principles</label>
                </div>
            </div>
        </div>
    </fieldset>
    <div style="margin-bottom: 1.25rem;">
        <label class="form-label" for="stdAddress">Residential Address</label>
        <textarea class="form-control" id="stdAddress" rows="3" placeholder="Enter permanent residential address"></textarea>
    </div>
    <div style="display: flex; gap: 1rem;">
        <button type="submit" class="btn btn-primary">Submit Registration</button>
        <button type="reset" class="btn btn-outline">Reset Form</button>
    </div>
</form>
        """
    },
    {
        "id": 6,
        "file": "html-06.html",
        "title": "Audio and Video Elements",
        "desc": "Demonstrates native HTML5 multimedia tags (<audio> and <video>) with built-in controls, loop, muted, and format fallbacks.",
        "demo": """
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem;">
    <div style="background: var(--bg-card); padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
        <h3 style="color: var(--accent-primary); margin-bottom: 0.75rem;">HTML5 Video Player</h3>
        <p style="color: var(--text-secondary); font-size: 0.85rem; margin-bottom: 1rem;">Native video element embedding animated canvas demonstration:</p>
        <div style="border-radius: var(--radius-md); overflow: hidden; background: #000; text-align: center;">
            <video controls width="100%" style="display: block; max-height: 240px; background: #111;" poster="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='200' viewBox='0 0 400 200'><rect width='400' height='200' fill='%231e293b'/><text x='50%25' y='50%25' fill='%23818cf8' font-size='16' text-anchor='middle'>HTML5 Video Preview</text></svg>">
                <source src="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
    </div>
    <div style="background: var(--bg-card); padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
        <h3 style="color: var(--accent-teal); margin-bottom: 0.75rem;">HTML5 Audio Player</h3>
        <p style="color: var(--text-secondary); font-size: 0.85rem; margin-bottom: 1rem;">Native audio playback with standard media controls:</p>
        <div style="padding: 1.5rem; background: var(--bg-secondary); border-radius: var(--radius-md); text-align: center;">
            <audio controls style="width: 100%;">
                <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
            <p style="color: var(--text-muted); font-size: 0.8rem; margin-top: 1rem;">Supports standard MP3, OGG, and WAV streams.</p>
        </div>
    </div>
</div>
        """
    },
    {
        "id": 7,
        "file": "html-07.html",
        "title": "Webpage Using Frames and Iframes",
        "desc": "Demonstrates inline frames (<iframe>) with sandbox attributes, loading lazy, custom borders, responsive wrapping, and embedded sandbox content.",
        "demo": """
<div style="display: flex; flex-direction: column; gap: 1.25rem;">
    <div style="background: var(--bg-card); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
        <h4 style="color: var(--accent-primary); margin-bottom: 0.5rem;">Embedded Inline Frame (&lt;iframe&gt;)</h4>
        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;">Iframes embed independent HTML documents inside the parent page:</p>
        <iframe srcdoc="<body style='font-family:sans-serif;background:%230f172a;color:%23f8fafc;padding:20px;text-align:center;'><h3>Embedded Document Inside IFrame</h3><p style='color:%2394a3b8;'>This content is rendered inside an isolated document frame.</p><button onclick='alert(&quot;Triggered from inside iframe!&quot;)' style='padding:8px 16px;background:%236366f1;color:%23fff;border:none;border-radius:6px;cursor:pointer;'>Click Me Inside Frame</button></body>" 
                style="width: 100%; height: 200px; border: 1px solid var(--border-color); border-radius: var(--radius-md);" 
                title="Interactive Iframe Demo" 
                loading="lazy">
        </iframe>
    </div>
</div>
        """
    },
    {
        "id": 8,
        "file": "html-08.html",
        "title": "Semantic HTML5 Elements (<header>, <nav>, <section>, <article>, <footer>)",
        "desc": "Demonstrates semantic structural elements providing search engine optimization (SEO), accessibility (a11y), and clean document semantics.",
        "demo": """
<div style="border: 2px dashed var(--accent-primary); border-radius: var(--radius-lg); padding: 1rem; background: var(--bg-secondary);">
    <header style="background: rgba(99, 102, 241, 0.2); padding: 1rem; border-radius: var(--radius-md); text-align: center; margin-bottom: 1rem;">
        <h3 style="color: var(--accent-primary);">&lt;header&gt; Header Component</h3>
        <p style="font-size: 0.85rem; color: var(--text-secondary);">Contains introductory information, logos, or primary navigation</p>
    </header>
    <nav style="background: rgba(20, 184, 166, 0.2); padding: 0.75rem; border-radius: var(--radius-md); text-align: center; margin-bottom: 1rem;">
        <strong style="color: var(--accent-teal);">&lt;nav&gt; Navigation Bar:</strong> [Home] | [Articles] | [About] | [Contact]
    </nav>
    <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 1rem; margin-bottom: 1rem;">
        <main style="background: rgba(236, 72, 153, 0.15); padding: 1rem; border-radius: var(--radius-md);">
            <strong style="color: var(--accent-pink);">&lt;main&gt; Primary Document Content</strong>
            <article style="background: var(--bg-card); padding: 0.75rem; margin-top: 0.5rem; border-radius: var(--radius-sm); border: 1px solid var(--border-color);">
                <h4>&lt;article&gt; Self-Contained Article 1</h4>
                <p style="font-size: 0.85rem; color: var(--text-secondary);">A standalone syndicatable entry such as a blog post or news item.</p>
            </article>
        </main>
        <aside style="background: rgba(245, 158, 11, 0.15); padding: 1rem; border-radius: var(--radius-md);">
            <strong style="color: var(--accent-amber);">&lt;aside&gt; Sidebar</strong>
            <p style="font-size: 0.85rem; color: var(--text-secondary); margin-top: 0.5rem;">Tangentially related items, advertisements, or quick links.</p>
        </aside>
    </div>
    <footer style="background: rgba(100, 116, 139, 0.2); padding: 0.85rem; border-radius: var(--radius-md); text-align: center;">
        <small style="color: var(--text-muted);">&lt;footer&gt; Copyright &copy; 2026 Practical Web Technologies</small>
    </footer>
</div>
        """
    },
    {
        "id": 9,
        "file": "html-09.html",
        "title": "HTML5 Input Types (email, date, number, password, color, range)",
        "desc": "Demonstrates modern HTML5 form input types with built-in browser validation, pickers, and interactive values.",
        "demo": """
<form onsubmit="event.preventDefault(); alert('All input values are valid!');" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.25rem; background: var(--bg-card); padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
    <div>
        <label class="form-label" for="inpEmail">Email Input (type="email")</label>
        <input class="form-control" type="email" id="inpEmail" required placeholder="user@example.com">
    </div>
    <div>
        <label class="form-label" for="inpPass">Password (type="password")</label>
        <input class="form-control" type="password" id="inpPass" required placeholder="••••••••">
    </div>
    <div>
        <label class="form-label" for="inpNum">Numeric Stepper (type="number")</label>
        <input class="form-control" type="number" id="inpNum" min="1" max="100" value="25">
    </div>
    <div>
        <label class="form-label" for="inpDate">Date Picker (type="date")</label>
        <input class="form-control" type="date" id="inpDate" value="2026-09-23">
    </div>
    <div>
        <label class="form-label" for="inpColor">Color Picker (type="color")</label>
        <input class="form-control" type="color" id="inpColor" value="#6366f1" style="height: 42px; padding: 4px; cursor: pointer;">
    </div>
    <div>
        <label class="form-label" for="inpRange">Range Slider (type="range")</label>
        <input type="range" id="inpRange" min="0" max="100" value="75" style="width: 100%; margin-top: 0.75rem;" oninput="document.getElementById('rangeVal').innerText = this.value">
        <span style="font-size: 0.85rem; color: var(--accent-teal);">Value: <strong id="rangeVal">75</strong>%</span>
    </div>
    <div style="grid-column: 1 / -1; margin-top: 0.5rem;">
        <button type="submit" class="btn btn-primary">Test HTML5 Built-In Validation</button>
    </div>
</form>
        """
    },
    {
        "id": 10,
        "file": "html-10.html",
        "title": "College Timetable Using an HTML Table",
        "desc": "A college class timetable created with complex HTML table headers, rowspan for lab sessions, lunch breaks, and formatted time slots.",
        "demo": """
<div style="overflow-x: auto;">
    <table style="width: 100%; border-collapse: collapse; text-align: center; background: var(--bg-card); border-radius: var(--radius-md); border: 1px solid var(--border-color); font-size: 0.9rem;">
        <thead>
            <tr style="background: rgba(99, 102, 241, 0.2);">
                <th style="padding: 0.75rem; border: 1px solid var(--border-color);">Day / Time</th>
                <th style="padding: 0.75rem; border: 1px solid var(--border-color);">09:00 - 10:00</th>
                <th style="padding: 0.75rem; border: 1px solid var(--border-color);">10:00 - 11:00</th>
                <th style="padding: 0.75rem; border: 1px solid var(--border-color);">11:00 - 11:15</th>
                <th style="padding: 0.75rem; border: 1px solid var(--border-color);">11:15 - 12:15</th>
                <th style="padding: 0.75rem; border: 1px solid var(--border-color);">12:15 - 01:00</th>
                <th style="padding: 0.75rem; border: 1px solid var(--border-color);">01:00 - 03:00</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="font-weight: 700; border: 1px solid var(--border-color); background: rgba(255,255,255,0.02);">Monday</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">HTML5 & Web Tech</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">Data Structures</td>
                <td rowspan="5" style="border: 1px solid var(--border-color); background: rgba(245, 158, 11, 0.15); color: var(--accent-amber); font-weight: 600; writing-mode: vertical-rl; transform: rotate(180deg); padding: 0.5rem;">TEA BREAK</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">Operating Systems</td>
                <td rowspan="5" style="border: 1px solid var(--border-color); background: rgba(16, 185, 129, 0.15); color: var(--accent-emerald); font-weight: 600; writing-mode: vertical-rl; transform: rotate(180deg); padding: 0.5rem;">LUNCH INTERVAL</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem; background: rgba(99, 102, 241, 0.08);">Web Tech Laboratory</td>
            </tr>
            <tr>
                <td style="font-weight: 700; border: 1px solid var(--border-color); background: rgba(255,255,255,0.02);">Tuesday</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">DBMS</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">Discrete Math</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">Computer Networks</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem; background: rgba(20, 184, 166, 0.08);">DBMS Laboratory</td>
            </tr>
            <tr>
                <td style="font-weight: 700; border: 1px solid var(--border-color); background: rgba(255,255,255,0.02);">Wednesday</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">Operating Systems</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">Web Tech</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">Data Structures</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">Project Seminar</td>
            </tr>
            <tr>
                <td style="font-weight: 700; border: 1px solid var(--border-color); background: rgba(255,255,255,0.02);">Thursday</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">Discrete Math</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">Computer Networks</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">DBMS</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem; background: rgba(236, 72, 153, 0.08);">Networks Lab</td>
            </tr>
            <tr>
                <td style="font-weight: 700; border: 1px solid var(--border-color); background: rgba(255,255,255,0.02);">Friday</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">Computer Networks</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">Operating Systems</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">Elective - Cloud</td>
                <td style="border: 1px solid var(--border-color); padding: 0.6rem;">Library & Sports</td>
            </tr>
        </tbody>
    </table>
</div>
        """
    },
    {
        "id": 11,
        "file": "html-11.html",
        "title": "Internal and External CSS Styling",
        "desc": "Demonstrates the cascade and usage of internal stylesheets (<style>) versus external link stylesheets (<link rel='stylesheet'>).",
        "demo": """
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
    <div style="background: var(--bg-card); padding: 1.5rem; border-radius: var(--radius-md); border: 2px solid var(--accent-primary);">
        <span style="font-size: 0.75rem; background: var(--accent-primary); color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: bold;">EXTERNAL CSS</span>
        <h3 style="margin-top: 0.75rem;">Global Consistency</h3>
        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 0.5rem;">External stylesheets link via <code>&lt;link rel="stylesheet" href="../assets/css/style.css"&gt;</code>. Ideal for keeping visual styling uniform across hundreds of HTML pages.</p>
    </div>
    <div style="background: var(--bg-card); padding: 1.5rem; border-radius: var(--radius-md); border: 2px dashed var(--accent-teal);">
        <span style="font-size: 0.75rem; background: var(--accent-teal); color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-weight: bold;">INTERNAL CSS</span>
        <h3 style="margin-top: 0.75rem;">Page-Scoped Rules</h3>
        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 0.5rem;">Internal styles are declared inside <code>&lt;style&gt;</code> tags in the <code>&lt;head&gt;</code>. Used for document-specific styling without altering global styles.</p>
    </div>
</div>
        """
    },
    {
        "id": 12,
        "file": "html-12.html",
        "title": "CSS Selectors, Colors, Fonts, Margins, Padding, and Borders",
        "desc": "Demonstrates core CSS foundational styling: tag/class/id selectors, color models (HEX, RGB, HSL), typography, and spacing models.",
        "demo": """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
    <div style="border: 2px solid #8b5cf6; margin: 10px 0; padding: 15px; border-radius: 8px; background: rgba(139, 92, 246, 0.1);">
        <h4 style="color: #a78bfa; font-family: Georgia, serif;">Class Selector (.styled-box)</h4>
        <p style="color: var(--text-secondary); font-size: 0.9rem;">Demonstrating Margin (10px outer spacing), Padding (15px inner space), and Solid Purple Border (2px).</p>
    </div>
    <div style="border: 2px dashed #06b6d4; margin: 10px 0; padding: 15px; border-radius: 8px; background: rgba(6, 182, 212, 0.1);">
        <h4 style="color: #22d3ee; font-family: 'Courier New', monospace;">ID Selector (#unique-highlight)</h4>
        <p style="color: var(--text-secondary); font-size: 0.9rem;">Demonstrates monospaced font, cyan accent color, and dashed border styling.</p>
    </div>
</div>
        """
    },
    {
        "id": 13,
        "file": "html-13.html",
        "title": "Responsive Webpage Using CSS Media Queries",
        "desc": "Showcases fluid responsive design utilizing @media rules for Mobile (<600px), Tablet (600px-992px), and Desktop (>992px) viewports.",
        "demo": """
<div class="responsive-query-demo" style="background: var(--bg-card); padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border-color); text-align: center;">
    <div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center;">
        <div style="flex: 1 1 200px; padding: 1.25rem; background: var(--bg-secondary); border-radius: var(--radius-md); border: 1px solid var(--border-color);">
            <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">📱</div>
            <h4>Mobile View</h4>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Max-width: 600px (1 Column)</p>
        </div>
        <div style="flex: 1 1 200px; padding: 1.25rem; background: var(--bg-secondary); border-radius: var(--radius-md); border: 1px solid var(--border-color);">
            <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">💻</div>
            <h4>Tablet View</h4>
            <p style="font-size: 0.8rem; color: var(--text-muted);">601px - 992px (2 Columns)</p>
        </div>
        <div style="flex: 1 1 200px; padding: 1.25rem; background: var(--bg-secondary); border-radius: var(--radius-md); border: 1px solid var(--border-color);">
            <div style="font-size: 1.8rem; margin-bottom: 0.5rem;">🖥️</div>
            <h4>Desktop View</h4>
            <p style="font-size: 0.8rem; color: var(--text-muted);">Min-width: 993px (3+ Columns)</p>
        </div>
    </div>
    <p style="margin-top: 1rem; color: var(--accent-teal); font-size: 0.9rem;">Resize your browser window to observe dynamic flex and media query adaptations!</p>
</div>
        """
    },
    {
        "id": 14,
        "file": "html-14.html",
        "title": "Webpage Using Bootstrap Components",
        "desc": "Demonstrates integration of Bootstrap CSS framework components: responsive Navbar, cards, buttons, badges, and alerts.",
        "demo": """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
    <div style="background: #212529; color: #fff; padding: 0.75rem 1.25rem; border-radius: 6px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
        <span style="font-weight: bold; font-size: 1.1rem;">Bootstrap 5 Brand</span>
        <div style="display: flex; gap: 0.75rem; font-size: 0.85rem;">
            <span>Home</span>
            <span>Features</span>
            <span>Pricing</span>
        </div>
    </div>
    <div style="background: rgba(13, 110, 253, 0.15); border: 1px solid #0d6efd; color: #9ec5fe; padding: 0.75rem 1rem; border-radius: 6px; margin-bottom: 1rem; font-size: 0.9rem;">
        <strong>Bootstrap Alert:</strong> Responsive grid system and utility classes loaded successfully.
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 1rem;">
        <div style="background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 6px; padding: 1rem; flex: 1 1 200px;">
            <h5 style="color: var(--text-primary); margin-bottom: 0.5rem;">Card Title</h5>
            <p style="color: var(--text-secondary); font-size: 0.85rem; margin-bottom: 0.75rem;">Clean card structure with standardized Bootstrap margin & utility helpers.</p>
            <button class="btn btn-primary btn-sm">Action Button</button>
        </div>
        <div style="background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 6px; padding: 1rem; flex: 1 1 200px;">
            <h5 style="color: var(--text-primary); margin-bottom: 0.5rem;">Component Badges</h5>
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.5rem;">
                <span style="background: #0d6efd; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.75rem;">Primary</span>
                <span style="background: #198754; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.75rem;">Success</span>
                <span style="background: #dc3545; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.75rem;">Danger</span>
            </div>
        </div>
    </div>
</div>
        """
    },
    {
        "id": 15,
        "file": "html-15.html",
        "title": "Simple Personal Portfolio Webpage Using HTML and CSS",
        "desc": "A personal developer portfolio webpage featuring an About Me section, skills showcase, projects gallery, and interactive contact form.",
        "demo": """
<div style="background: var(--bg-card); border-radius: var(--radius-lg); border: 1px solid var(--border-color); overflow: hidden;">
    <div style="background: linear-gradient(135deg, rgba(99, 102, 241, 0.3), rgba(20, 184, 166, 0.3)); padding: 2rem; text-align: center;">
        <div style="width: 80px; height: 80px; border-radius: 50%; background: var(--accent-primary); color: white; display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: bold; margin: 0 auto 1rem;">
            SN
        </div>
        <h2 style="color: var(--text-primary); margin-bottom: 0.25rem;">M. Surya Nivas Reddy</h2>
        <p style="color: var(--accent-teal); font-weight: 500;">Front-End Engineer & Web Technologist</p>
    </div>
    <div style="padding: 1.5rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
        <div>
            <h4 style="color: var(--text-primary); border-bottom: 2px solid var(--accent-primary); padding-bottom: 0.25rem; margin-bottom: 0.75rem;">About Me</h4>
            <p style="color: var(--text-secondary); font-size: 0.9rem; line-height: 1.6;">Passionate student software engineer crafting responsive, accessible, and high-performance web applications using modern HTML5, CSS3, and JavaScript.</p>
        </div>
        <div>
            <h4 style="color: var(--text-primary); border-bottom: 2px solid var(--accent-teal); padding-bottom: 0.25rem; margin-bottom: 0.75rem;">Core Skills</h4>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                <span class="stat-pill">HTML5</span>
                <span class="stat-pill">CSS3 (Grid & Flexbox)</span>
                <span class="stat-pill">JavaScript (ES6+)</span>
                <span class="stat-pill">DOM & Events</span>
                <span class="stat-pill">Bootstrap</span>
            </div>
        </div>
    </div>
</div>
        """
    }
]

def generate_program_page(prog, prev_prog, next_prog, total):
    code_escaped = prog["demo"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    prev_link = prev_prog["file"] if prev_prog else "#"
    next_link = next_prog["file"] if next_prog else "#"
    prev_disabled = "opacity: 0.5; pointer-events: none;" if not prev_prog else ""
    next_disabled = "opacity: 0.5; pointer-events: none;" if not next_prog else ""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Program #{prog['id']:02d}: {prog['title']}</title>
    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
    <header class="top-nav">
        <div class="container nav-container">
            <a href="../index.html" class="nav-brand">
                <span>⚡ Practical Lab</span>
                <span class="brand-badge">HTML #{prog['id']:02d}</span>
            </a>
            <div class="nav-links">
                <a href="../index.html">🏠 Home</a>
                <a href="index.html" class="active">📄 HTML Programs</a>
                <a href="../css/index.html">🎨 CSS Programs</a>
                <a href="../javascript/index.html">⚙️ JS Programs</a>
            </div>
            <button id="themeToggleBtn" class="theme-toggle-btn">☀️ Light Mode</button>
        </div>
    </header>

    <main class="main-content">
        <div class="program-page-container">
            <!-- Navigation Breadcrumbs -->
            <div class="program-nav-bar">
                <div class="nav-breadcrumbs">
                    <a href="../index.html">Home</a>
                    <span class="separator">/</span>
                    <a href="index.html">HTML Programs</a>
                    <span class="separator">/</span>
                    <span style="color: var(--text-primary); font-weight: 600;">Program #{prog['id']:02d}</span>
                </div>
                <div class="nav-controls">
                    <a href="{prev_link}" class="btn btn-outline btn-sm btn-prev" style="{prev_disabled}">⬅ Prev</a>
                    <a href="index.html" class="btn btn-outline btn-sm">📋 All HTML</a>
                    <a href="{next_link}" class="btn btn-outline btn-sm btn-next" style="{next_disabled}">Next ➡</a>
                </div>
            </div>

            <!-- Experiment Title & Description -->
            <div class="experiment-header-card">
                <span class="experiment-badge">EXPERIMENT #{prog['id']:02d} OF {total:02d}</span>
                <h1 class="experiment-title">{prog['title']}</h1>
                <p class="experiment-desc">{prog['desc']}</p>
            </div>

            <!-- Demonstration Section -->
            <div class="demo-section">
                <div class="demo-bar">
                    <span class="demo-title"><span class="demo-badge"></span> Live Interactive Demonstration</span>
                    <span style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono);">{prog['file']}</span>
                </div>
                <div class="demo-content">
                    {prog['demo']}
                </div>
            </div>

            <!-- Source Code Drawer -->
            <div class="code-section">
                <div class="code-header">
                    <span class="code-header-title">💻 Source Code Inspector</span>
                    <span class="code-arrow" style="font-size: 0.85rem; color: var(--accent-primary);">▼ View Code</span>
                </div>
                <div class="code-content">
                    <pre><code>{code_escaped}</code></pre>
                </div>
            </div>

            <!-- Bottom Navigation -->
            <div class="bottom-nav-bar">
                <a href="{prev_link}" class="btn btn-outline btn-prev" style="{prev_disabled}">⬅ Previous Program</a>
                <div style="display: flex; gap: 0.5rem;">
                    <a href="../index.html" class="btn btn-outline">🏠 Dashboard</a>
                    <a href="index.html" class="btn btn-primary">📋 HTML Program List</a>
                </div>
                <a href="{next_link}" class="btn btn-outline btn-next" style="{next_disabled}">Next Program ➡</a>
            </div>
        </div>
    </main>

    <footer class="site-footer">
        <div class="container footer-content">
            <p>Student Name: <span class="footer-highlight">M.Surya Nivas Reddy</span> | Assignment: <span class="footer-highlight">HTML, CSS & JavaScript Practical Assignment</span></p>
            <p style="font-size: 0.8rem; color: var(--text-muted);">HTML Programs Module &bull; 15 of 212 Total Completed</p>
        </div>
    </footer>

    <script src="../assets/js/common.js"></script>
</body>
</html>
"""
    return html

def generate_html_index():
    cards = ""
    for prog in HTML_PROGRAMS:
        cards += f"""
        <a href="{prog['file']}" class="program-card" data-category="html">
            <div class="program-header">
                <span class="program-number">HTML #{prog['id']:02d}</span>
                <span style="font-size: 0.85rem; color: var(--text-muted);">Practical</span>
            </div>
            <h3 class="program-title">{prog['title']}</h3>
            <p class="program-desc">{prog['desc']}</p>
            <div class="program-footer">
                <span>Source: {prog['file']}</span>
                <span class="program-link-text">Launch Demo &rarr;</span>
            </div>
        </a>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Practical Programs List (1 to 15)</title>
    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
    <header class="top-nav">
        <div class="container nav-container">
            <a href="../index.html" class="nav-brand">
                <span>⚡ Practical Lab</span>
                <span class="brand-badge">HTML Suite</span>
            </a>
            <div class="nav-links">
                <a href="../index.html">🏠 Home</a>
                <a href="index.html" class="active">📄 HTML Programs</a>
                <a href="../css/index.html">🎨 CSS Programs</a>
                <a href="../javascript/index.html">⚙️ JS Programs</a>
            </div>
            <button id="themeToggleBtn" class="theme-toggle-btn">☀️ Light Mode</button>
        </div>
    </header>

    <main class="main-content">
        <div class="container">
            <div class="page-header">
                <span class="page-badge">MODULE 01 &bull; 15 PRACTICAL PROGRAMS</span>
                <h1 class="page-title">HTML Practical Programs</h1>
                <p class="page-subtitle">Complete laboratory implementations covering semantic tags, document hierarchy, forms, tables, multimedia, and responsive structures.</p>
            </div>

            <!-- Student Info Banner -->
            <div class="student-banner">
                <div class="student-meta">
                    <div class="meta-item">
                        <span class="meta-label">Student Name</span>
                        <span class="meta-value">M.Surya Nivas Reddy</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Subject</span>
                        <span class="meta-value">HTML, CSS & JavaScript</span>
                    </div>
                    <div class="meta-item">
                        <span class="meta-label">Module Progress</span>
                        <span class="meta-value" style="color: var(--accent-emerald);">15 / 15 Programs Completed</span>
                    </div>
                </div>
                <a href="../index.html" class="btn btn-outline btn-sm">🏠 Back to Dashboard</a>
            </div>

            <!-- Search and Filter Bar -->
            <div class="search-filter-bar">
                <div class="search-input-wrapper">
                    <span class="search-icon">🔍</span>
                    <input type="text" id="programSearch" class="search-input" placeholder="Search HTML programs by title, tag, or concept...">
                </div>
                <div class="filter-tags">
                    <button class="filter-tag active" data-filter="all">All (15)</button>
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
            <p style="font-size: 0.8rem; color: var(--text-muted);">Total 212 Programs in Assignment &bull; HTML Module</p>
        </div>
    </footer>

    <script src="../assets/js/common.js"></script>
</body>
</html>
"""
    return html

def main():
    total = len(HTML_PROGRAMS)
    print(f"Generating {total} HTML programs...")
    for i, prog in enumerate(HTML_PROGRAMS):
        prev_prog = HTML_PROGRAMS[i - 1] if i > 0 else None
        next_prog = HTML_PROGRAMS[i + 1] if i < total - 1 else None
        page_html = generate_program_page(prog, prev_prog, next_prog, total)
        filepath = os.path.join("html", prog["file"])
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(page_html)
    
    # Generate index.html
    index_html = generate_html_index()
    with open(os.path.join("html", "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("HTML programs and index successfully generated!")

if __name__ == "__main__":
    main()
