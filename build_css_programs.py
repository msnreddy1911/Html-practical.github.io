"""
Generator for CSS Practical Programs (1 to 75) and css/index.html
"""
import os

# Define the 75 CSS programs with metadata and rich demonstrations
CSS_DATA = [
    (1, "Inline, Internal, and External CSS", "Demonstrates the three cascading methods of styling: inline style attributes, internal <style> blocks, and external stylesheet links.", """
<div style="display: flex; flex-direction: column; gap: 1rem;">
    <div style="background-color: #6366f1; color: #ffffff; padding: 1.25rem; border-radius: 8px; font-weight: 600;">
        Inline Styled Element: &lt;div style="background-color: #6366f1; color: #ffffff;"&gt; (Highest specificity among author styles)
    </div>
    <div class="internal-styled-box" style="background: rgba(20, 184, 166, 0.15); border: 2px solid #14b8a6; color: #14b8a6; padding: 1.25rem; border-radius: 8px; font-weight: 600;">
        Internal Styled Element: Controlled via page-scoped &lt;style&gt; declaration
    </div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); color: var(--text-primary); padding: 1.25rem; border-radius: 8px;">
        External Styled Element: Utilizing global CSS variables and classes from assets/css/style.css
    </div>
</div>
"""),
    (2, "Different CSS Selectors", "Demonstrating Universal (*), Type (p, h1), Class (.highlight), ID (#special), and Attribute ([data-role]) selectors.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="color: var(--text-muted);">Element selector: Targets all &lt;p&gt; tags directly.</p>
    <div style="background: rgba(99, 102, 241, 0.15); color: #818cf8; padding: 0.75rem; border-radius: 6px; margin: 0.5rem 0;">.class-selector: Reusable across multiple elements on a webpage.</div>
    <div style="background: rgba(236, 72, 153, 0.15); color: #f472b6; padding: 0.75rem; border-radius: 6px; margin: 0.5rem 0;">#id-selector: Unique identifier with higher specificity.</div>
    <div style="background: rgba(245, 158, 11, 0.15); color: #fbbf24; padding: 0.75rem; border-radius: 6px; margin: 0.5rem 0;">[data-type="demo"]: Attribute selector matching custom metadata attributes.</div>
</div>
"""),
    (3, "CSS Colors, Backgrounds, and Borders", "Showcases RGB, RGBA, HSL, HEX colors, border styles (solid, dashed, dotted, double), and background properties.", """
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
    <div style="background: #4f46e5; border: 3px solid #818cf8; color: white; padding: 1rem; border-radius: 8px; text-align: center;">HEX Color & Solid Border</div>
    <div style="background: rgba(16, 185, 129, 0.25); border: 3px dashed #10b981; color: #10b981; padding: 1rem; border-radius: 8px; text-align: center;">RGBA Alpha & Dashed Border</div>
    <div style="background: hsl(330, 80%, 40%); border: 3px double #f472b6; color: white; padding: 1rem; border-radius: 8px; text-align: center;">HSL Color & Double Border</div>
    <div style="background: linear-gradient(135deg, #f59e0b, #ec4899); border: 3px dotted #ffffff; color: white; padding: 1rem; border-radius: 8px; text-align: center;">Gradient & Dotted Border</div>
</div>
"""),
    (4, "Font Properties and Text Formatting", "Demonstrates font-family, font-size, font-weight, line-height, letter-spacing, text-transform, text-align, and text-decoration.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); display: flex; flex-direction: column; gap: 0.75rem;">
    <p style="font-family: Georgia, serif; font-size: 1.3rem; font-style: italic;">Serif Typography: Georgia, font-style: italic, font-size: 1.3rem</p>
    <p style="font-family: monospace; letter-spacing: 3px; color: var(--accent-teal);">Monospace with letter-spacing: 3px and custom color</p>
    <p style="text-transform: uppercase; font-weight: 800; color: var(--accent-pink);">text-transform: uppercase with font-weight: 800</p>
    <p style="text-decoration: underline wavy var(--accent-amber); font-size: 1.1rem;">text-decoration: underline wavy with colored accent</p>
</div>
"""),
    (5, "CSS Box Model (Margin, Border, Padding, Content)", "Interactive visualization of the CSS Box Model with colored concentric boundaries for Content, Padding, Border, and Margin.", """
<div style="background: rgba(245, 158, 11, 0.15); border: 2px dashed #f59e0b; padding: 25px; border-radius: 12px; text-align: center;">
    <span style="color: #f59e0b; font-weight: bold; font-size: 0.8rem; text-transform: uppercase;">Margin Box (Outer Space: 25px)</span>
    <div style="background: rgba(99, 102, 241, 0.2); border: 4px solid #6366f1; padding: 20px; border-radius: 8px; margin: 15px auto; max-width: 500px;">
        <span style="color: #818cf8; font-weight: bold; font-size: 0.8rem; text-transform: uppercase;">Border (4px Solid) & Padding (20px)</span>
        <div style="background: #0f172a; border: 1px solid var(--border-color); padding: 15px; border-radius: 6px;">
            <strong style="color: var(--accent-teal);">Content Area (Width &times; Height)</strong>
            <p style="font-size: 0.85rem; color: var(--text-secondary); margin-top: 0.3rem;">Total Width = Content + Left/Right Padding + Left/Right Border + Left/Right Margin</p>
        </div>
    </div>
</div>
"""),
    (6, "Different Width, Height, and Sizing Properties", "Demonstrates fixed px, percentage %, viewport units (vw, vh), and min/max width/height properties.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); display: flex; flex-direction: column; gap: 1rem;">
    <div style="width: 100%; background: rgba(99, 102, 241, 0.2); border: 1px solid var(--accent-primary); padding: 0.75rem; border-radius: 6px;">width: 100% (Responsive full parent container width)</div>
    <div style="width: 50%; min-width: 260px; background: rgba(20, 184, 166, 0.2); border: 1px solid var(--accent-teal); padding: 0.75rem; border-radius: 6px;">width: 50%; min-width: 260px</div>
    <div style="max-width: 400px; height: 70px; background: rgba(236, 72, 153, 0.2); border: 1px solid var(--accent-pink); padding: 0.75rem; border-radius: 6px;">max-width: 400px; height: 70px fixed container</div>
</div>
"""),
    (7, "CSS Positioning (Static, Relative, Absolute, Fixed, Sticky)", "Demonstrates how elements flow with static, relative offset, absolute anchor within relative parent, and sticky headers.", """
<div style="position: relative; height: 260px; background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 8px; padding: 1rem; overflow: hidden;">
    <div style="position: static; background: rgba(255,255,255,0.05); padding: 0.5rem; margin-bottom: 0.5rem; border-radius: 4px;">1. position: static (Normal document flow)</div>
    <div style="position: relative; left: 30px; top: 5px; background: rgba(99, 102, 241, 0.3); border: 1px solid var(--accent-primary); padding: 0.5rem; width: 60%; border-radius: 4px;">2. position: relative (Offset from original spot)</div>
    <div style="position: absolute; right: 20px; bottom: 20px; background: rgba(16, 185, 129, 0.3); border: 1px solid var(--accent-emerald); padding: 0.75rem; border-radius: 6px;">3. position: absolute (Anchored bottom-right of parent)</div>
    <div style="position: sticky; top: 0; background: rgba(245, 158, 11, 0.2); border: 1px solid var(--accent-amber); padding: 0.5rem; border-radius: 4px; margin-top: 1.5rem;">4. position: sticky (Sticks while scrolling parent)</div>
</div>
"""),
    (8, "Float and Clear Properties", "Illustrates floating elements left and right with clearfix to prevent container collapse.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div style="float: left; width: 140px; height: 100px; background: var(--accent-primary); color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; border-radius: 6px; margin-right: 1.25rem; margin-bottom: 0.5rem;">
        float: left
    </div>
    <div style="float: right; width: 140px; height: 100px; background: var(--accent-teal); color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; border-radius: 6px; margin-left: 1.25rem; margin-bottom: 0.5rem;">
        float: right
    </div>
    <p style="color: var(--text-secondary); line-height: 1.6;">Float removes an element from normal flow, placing it along the left or right of its container. Text and inline elements wrap smoothly around it until a clear or clearfix rule resets the boundary.</p>
    <div style="clear: both; margin-top: 1rem; padding-top: 0.75rem; border-top: 1px solid var(--border-color); color: var(--accent-amber); font-weight: bold;">
        &bull; clear: both ensures subsequent content begins beneath the floated boxes.
    </div>
</div>
"""),
    (9, "Styled Navigation Bar Using CSS", "A modern responsive navigation bar with logo, hover indicators, active state, and CTA button.", """
<nav style="background: #1e293b; padding: 1rem 1.5rem; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; border: 1px solid var(--border-color);">
    <div style="font-weight: bold; color: #fff; font-size: 1.2rem; display: flex; align-items: center; gap: 0.5rem;">
        <span style="color: var(--accent-primary);">&lt;/&gt;</span> TechPortal
    </div>
    <ul style="display: flex; list-style: none; gap: 1.5rem; margin: 0; padding: 0;">
        <li><a href="#" style="color: #6366f1; text-decoration: none; font-weight: 600; border-bottom: 2px solid #6366f1; padding-bottom: 4px;">Dashboard</a></li>
        <li><a href="#" style="color: #94a3b8; text-decoration: none; transition: 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Services</a></li>
        <li><a href="#" style="color: #94a3b8; text-decoration: none; transition: 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Projects</a></li>
        <li><a href="#" style="color: #94a3b8; text-decoration: none; transition: 0.2s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#94a3b8'">Contact</a></li>
    </ul>
    <button class="btn btn-primary btn-sm">Get Started</button>
</nav>
"""),
    (10, "CSS Pseudo-Classes (:hover, :active, :focus, :visited)", "Interactive demonstration of state-driven pseudo-classes responding to pointer interaction and form focus.", """
<div style="display: flex; flex-wrap: wrap; gap: 1.5rem; background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); align-items: center;">
    <button style="background: #4f46e5; color: white; border: none; padding: 0.75rem 1.25rem; border-radius: 6px; cursor: pointer; transition: 0.2s;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        Hover over me (:hover)
    </button>
    <button style="background: #10b981; color: white; border: none; padding: 0.75rem 1.25rem; border-radius: 6px; cursor: pointer; transition: 0.1s;" onmousedown="this.style.transform='scale(0.95)'" onmouseup="this.style.transform='scale(1)'">
        Press down (:active)
    </button>
    <input type="text" placeholder="Click to focus me (:focus)" style="padding: 0.75rem; background: #0f172a; color: white; border: 1px solid #475569; border-radius: 6px; outline: none;" onfocus="this.style.borderColor='#6366f1'; this.style.boxShadow='0 0 10px rgba(99,102,241,0.5)'" onblur="this.style.borderColor='#475569'; this.style.boxShadow='none'">
</div>
"""),
    (11, "CSS Pseudo-Elements (::before, ::after, ::first-letter, ::first-line)", "Using pseudo-elements to insert decorative icons, badges, drop caps, and first-line styling.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <p style="font-size: 1.05rem; line-height: 1.8; color: var(--text-secondary);">
        <span style="float: left; font-size: 3rem; line-height: 0.8; font-weight: bold; color: var(--accent-primary); margin-right: 8px; font-family: serif;">C</span>
        ascading Style Sheets provide pseudo-elements to style specific parts of selected elements. The ::first-letter pseudo-element formats decorative editorial drop caps.
    </p>
    <div style="margin-top: 1rem; padding: 0.75rem 1rem; background: rgba(99, 102, 241, 0.1); border-radius: 6px; display: inline-flex; align-items: center; gap: 0.5rem; color: #818cf8;">
        <span>🔔</span> <strong>Notice:</strong> Decorated with generated content markers.
    </div>
</div>
"""),
    (12, "CSS Lists and Tables", "Zebra striping tables, hover highlights, custom styled counters, and bullet customization.", """
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
    <div>
        <h4 style="margin-bottom: 0.75rem; color: var(--accent-teal);">Custom Counter List</h4>
        <ol style="list-style: none; counter-reset: custom-counter; padding-left: 0;">
            <li style="counter-increment: custom-counter; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
                <span style="background: var(--accent-teal); color: white; width: 24px; height: 24px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: bold;">1</span> Semantic Markup
            </li>
            <li style="counter-increment: custom-counter; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
                <span style="background: var(--accent-teal); color: white; width: 24px; height: 24px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: bold;">2</span> Cascading Styling
            </li>
            <li style="counter-increment: custom-counter; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
                <span style="background: var(--accent-teal); color: white; width: 24px; height: 24px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: bold;">3</span> Dynamic DOM Scripts
            </li>
        </ol>
    </div>
    <div>
        <h4 style="margin-bottom: 0.75rem; color: var(--accent-primary);">Zebra-Striped Styled Table</h4>
        <table style="width: 100%; border-collapse: collapse; font-size: 0.9rem;">
            <tr style="background: rgba(99,102,241,0.2);"><th style="padding: 0.5rem; text-align: left;">Item</th><th style="padding: 0.5rem;">Price</th></tr>
            <tr style="background: rgba(255,255,255,0.02);"><td style="padding: 0.5rem;">Domain Name</td><td style="padding: 0.5rem; text-align: center;">$12</td></tr>
            <tr style="background: rgba(255,255,255,0.06);"><td style="padding: 0.5rem;">Web Hosting</td><td style="padding: 0.5rem; text-align: center;">$45</td></tr>
            <tr style="background: rgba(255,255,255,0.02);"><td style="padding: 0.5rem;">SSL Certificate</td><td style="padding: 0.5rem; text-align: center;">Free</td></tr>
        </table>
    </div>
</div>
"""),
    (13, "Styled Registration Form Using CSS", "A modern card form with custom focused input glow, rounded controls, and clean gradients.", """
<div style="max-width: 450px; margin: 0 auto; background: var(--bg-card); padding: 2rem; border-radius: 12px; border: 1px solid var(--border-color); box-shadow: var(--shadow-md);">
    <h3 style="color: var(--text-primary); margin-bottom: 1.25rem; text-align: center;">Create Account</h3>
    <div class="form-group">
        <label class="form-label">Full Name</label>
        <input type="text" class="form-control" placeholder="John Doe">
    </div>
    <div class="form-group">
        <label class="form-label">Email Address</label>
        <input type="email" class="form-control" placeholder="john@example.com">
    </div>
    <div class="form-group">
        <label class="form-label">Password</label>
        <input type="password" class="form-control" placeholder="••••••••">
    </div>
    <button class="btn btn-primary" style="width: 100%; margin-top: 0.5rem;">Register Now</button>
</div>
"""),
    (14, "CSS Flexbox Layout", "Comprehensive demonstration of flex container properties: flex-direction, justify-content, align-items, and gap.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div style="display: flex; justify-content: space-between; align-items: center; gap: 1rem; flex-wrap: wrap;">
        <div style="background: #4f46e5; color: white; padding: 1.5rem; border-radius: 8px; flex: 1 1 150px; text-align: center; font-weight: bold;">Flex Item 1</div>
        <div style="background: #06b6d4; color: white; padding: 1.5rem; border-radius: 8px; flex: 2 1 200px; text-align: center; font-weight: bold;">Flex Item 2 (flex: 2)</div>
        <div style="background: #ec4899; color: white; padding: 1.5rem; border-radius: 8px; flex: 1 1 150px; text-align: center; font-weight: bold;">Flex Item 3</div>
    </div>
</div>
"""),
    (15, "CSS Grid Layout", "Two-dimensional grid system showcasing grid-template-columns, gap, and grid-column span.", """
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div style="grid-column: 1 / -1; background: #6366f1; color: white; padding: 1rem; border-radius: 6px; text-align: center; font-weight: bold;">Header (grid-column: 1 / -1)</div>
    <div style="background: #0ea5e9; color: white; padding: 2rem 1rem; border-radius: 6px; text-align: center;">Sidebar (Col 1)</div>
    <div style="grid-column: span 2; background: #10b981; color: white; padding: 2rem 1rem; border-radius: 6px; text-align: center;">Main Content (Col 2 &amp; 3 Span)</div>
    <div style="grid-column: 1 / -1; background: #64748b; color: white; padding: 0.75rem; border-radius: 6px; text-align: center;">Footer (grid-column: 1 / -1)</div>
</div>
"""),
    (16, "Responsive Webpage Using CSS Media Queries", "Viewport-dependent layouts with dynamic column stacking and color alterations via @media breakpoints.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); text-align: center;">
    <p style="color: var(--accent-teal); font-weight: 600; margin-bottom: 1rem;">Resize the window to observe breakpoint transitions:</p>
    <div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center;">
        <div style="flex: 1 1 220px; background: rgba(99, 102, 241, 0.2); border: 1px solid var(--accent-primary); padding: 1rem; border-radius: 6px;">Breakpoint 1 (&lt; 640px)</div>
        <div style="flex: 1 1 220px; background: rgba(20, 184, 166, 0.2); border: 1px solid var(--accent-teal); padding: 1rem; border-radius: 6px;">Breakpoint 2 (640px - 1024px)</div>
        <div style="flex: 1 1 220px; background: rgba(236, 72, 153, 0.2); border: 1px solid var(--accent-pink); padding: 1rem; border-radius: 6px;">Breakpoint 3 (&gt; 1024px)</div>
    </div>
</div>
"""),
    (17, "Transitions and Transformations", "Interactive CSS properties for translate, rotate, scale, and skew with smooth easing curves.", """
<div style="display: flex; flex-wrap: wrap; gap: 2rem; justify-content: center; background: var(--bg-card); padding: 2.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div style="width: 100px; height: 100px; background: #6366f1; color: white; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: bold; transition: transform 0.4s ease;" onmouseover="this.style.transform='scale(1.2)'" onmouseout="this.style.transform='scale(1)'">Scale</div>
    <div style="width: 100px; height: 100px; background: #14b8a6; color: white; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: bold; transition: transform 0.4s ease;" onmouseover="this.style.transform='rotate(45deg)'" onmouseout="this.style.transform='rotate(0deg)'">Rotate</div>
    <div style="width: 100px; height: 100px; background: #ec4899; color: white; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: bold; transition: transform 0.4s ease;" onmouseover="this.style.transform='translateY(-15px)'" onmouseout="this.style.transform='translateY(0)'">Translate</div>
    <div style="width: 100px; height: 100px; background: #f59e0b; color: white; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: bold; transition: transform 0.4s ease;" onmouseover="this.style.transform='skewX(15deg)'" onmouseout="this.style.transform='skewX(0)'">Skew</div>
</div>
"""),
    (18, "CSS Keyframe Animations", "Demonstrating @keyframes animation rules including pulse, bounce, rotate, and color shifts.", """
<style>
@keyframes pulseGlow { 0% { transform: scale(1); opacity: 0.8; } 50% { transform: scale(1.1); opacity: 1; } 100% { transform: scale(1); opacity: 0.8; } }
@keyframes bounceBox { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-20px); } }
</style>
<div style="display: flex; gap: 3rem; justify-content: center; align-items: center; background: var(--bg-card); padding: 3rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div style="width: 80px; height: 80px; background: #8b5cf6; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; animation: pulseGlow 1.5s infinite ease-in-out;">Pulse</div>
    <div style="width: 80px; height: 80px; background: #06b6d4; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; animation: bounceBox 1.2s infinite ease-in-out;">Bounce</div>
</div>
"""),
    (19, "Responsive Navigation Menu Using HTML and CSS", "A hamburger-style responsive menu pattern with pure CSS toggle.", """
<div style="background: #1e293b; border-radius: 8px; padding: 1rem 1.5rem; border: 1px solid var(--border-color);">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span style="font-weight: bold; color: #fff;">ResponsiveNav</span>
        <button onclick="const m = document.getElementById('mobileMenu'); m.style.display = m.style.display === 'flex' ? 'none' : 'flex';" style="background: transparent; border: 1px solid #475569; color: #fff; padding: 0.4rem 0.75rem; border-radius: 4px; cursor: pointer;">☰ Menu</button>
    </div>
    <div id="mobileMenu" style="display: none; flex-direction: column; gap: 0.75rem; margin-top: 1rem; border-top: 1px solid #334155; padding-top: 0.75rem;">
        <a href="#" style="color: #6366f1;">Home</a>
        <a href="#" style="color: #94a3b8;">About Company</a>
        <a href="#" style="color: #94a3b8;">Products &amp; Solutions</a>
        <a href="#" style="color: #94a3b8;">Contact Support</a>
    </div>
</div>
"""),
    (20, "Personal Portfolio Webpage Using HTML and CSS", "A structured portfolio hero card with badge tags, call-to-action buttons, and social handles.", """
<div style="background: var(--bg-card); border-radius: 12px; border: 1px solid var(--border-color); overflow: hidden; max-width: 600px; margin: 0 auto;">
    <div style="height: 120px; background: linear-gradient(135deg, #6366f1, #ec4899);"></div>
    <div style="padding: 1.5rem; text-align: center; margin-top: -50px;">
        <div style="width: 80px; height: 80px; border-radius: 50%; background: #0f172a; border: 3px solid #fff; margin: 0 auto 0.75rem; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; color: #818cf8;">SN</div>
        <h3 style="color: var(--text-primary); margin-bottom: 0.25rem;">M. Surya Nivas Reddy</h3>
        <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;">Frontend Developer &amp; UI/UX Enthusiast</p>
        <div style="display: flex; justify-content: center; gap: 0.5rem; margin-bottom: 1.25rem;">
            <span class="stat-pill">HTML5</span><span class="stat-pill">CSS3</span><span class="stat-pill">JavaScript</span>
        </div>
        <button class="btn btn-primary btn-sm">Download CV</button>
    </div>
</div>
"""),
    (21, "College/Student Profile Page Using HTML and CSS", "A student identity card layout detailing department, registration number, and enrolled subjects.", """
<div style="background: var(--bg-card); max-width: 480px; margin: 0 auto; border-radius: 10px; border: 1px solid var(--border-color); padding: 1.75rem;">
    <div style="display: flex; gap: 1rem; align-items: center; margin-bottom: 1.25rem; border-bottom: 1px solid var(--border-color); padding-bottom: 1rem;">
        <div style="width: 60px; height: 60px; border-radius: 8px; background: var(--accent-primary); color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.25rem;">ENG</div>
        <div>
            <h4 style="color: var(--text-primary); margin-bottom: 0.2rem;">M. Surya Nivas Reddy</h4>
            <p style="color: var(--accent-teal); font-size: 0.85rem;">Reg: 21BCE1024 &bull; Dept: CSE</p>
        </div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 0.5rem; font-size: 0.9rem;">
        <div style="display: flex; justify-content: space-between;"><span style="color: var(--text-muted);">Current Semester:</span> <span>IV Semester</span></div>
        <div style="display: flex; justify-content: space-between;"><span style="color: var(--text-muted);">Cumulative GPA:</span> <span style="color: var(--accent-emerald); font-weight: bold;">9.2 / 10.0</span></div>
        <div style="display: flex; justify-content: space-between;"><span style="color: var(--text-muted);">Lab Group:</span> <span>Section A - Batch 2</span></div>
    </div>
</div>
"""),
    (22, "Login Page Using HTML and CSS", "A glassmorphism-inspired secure user login interface with social buttons and remember-me checkbox.", """
<div style="max-width: 400px; margin: 0 auto; background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(12px); padding: 2rem; border-radius: 12px; border: 1px solid var(--border-color);">
    <h3 style="text-align: center; margin-bottom: 1.5rem; color: #fff;">Portal Sign In</h3>
    <div class="form-group">
        <label class="form-label">Username / Student ID</label>
        <input type="text" class="form-control" placeholder="surya@student.edu">
    </div>
    <div class="form-group">
        <label class="form-label">Password</label>
        <input type="password" class="form-control" placeholder="••••••••">
    </div>
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; font-size: 0.85rem;">
        <label style="color: var(--text-secondary);"><input type="checkbox"> Remember me</label>
        <a href="#">Forgot password?</a>
    </div>
    <button class="btn btn-primary" style="width: 100%;">Sign In</button>
</div>
"""),
    (23, "Product Card Layout Using CSS", "An e-commerce product card with discount badge, price tag, rating stars, and Add to Cart button.", """
<div style="max-width: 320px; margin: 0 auto; background: var(--bg-card); border-radius: 12px; border: 1px solid var(--border-color); overflow: hidden; box-shadow: var(--shadow-md);">
    <div style="height: 180px; background: linear-gradient(135deg, #0ea5e9, #6366f1); position: relative; display: flex; align-items: center; justify-content: center; font-size: 3rem;">
        🎧
        <span style="position: absolute; top: 12px; left: 12px; background: #ec4899; color: white; padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.75rem; font-weight: bold;">30% OFF</span>
    </div>
    <div style="padding: 1.25rem;">
        <span style="color: var(--text-muted); font-size: 0.8rem; text-transform: uppercase;">Audio Electronics</span>
        <h4 style="margin: 0.25rem 0 0.5rem; color: var(--text-primary);">Wireless Pro Noise Cancelling</h4>
        <div style="color: #f59e0b; margin-bottom: 0.75rem;">★★★★★ <span style="color: var(--text-muted); font-size: 0.8rem;">(128 reviews)</span></div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div><span style="font-size: 1.25rem; font-weight: bold; color: var(--text-primary);">$149.00</span> <span style="text-decoration: line-through; color: var(--text-muted); font-size: 0.85rem;">$199.00</span></div>
            <button class="btn btn-primary btn-sm">Add to Cart</button>
        </div>
    </div>
</div>
"""),
    (24, "Responsive Photo Gallery Using CSS Grid/Flexbox", "A fluid photo gallery with aspect-ratio management and hover zoom styling.", """
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem;">
    <div style="height: 140px; background: linear-gradient(45deg, #f43f5e, #fb923c); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">Sunrise 🌄</div>
    <div style="height: 140px; background: linear-gradient(45deg, #3b82f6, #2dd4bf); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">Ocean 🌊</div>
    <div style="height: 140px; background: linear-gradient(45deg, #8b5cf6, #ec4899); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">Galaxy 🌌</div>
    <div style="height: 140px; background: linear-gradient(45deg, #10b981, #059669); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">Forest 🌲</div>
</div>
"""),
    (25, "Complete Website Homepage Using HTML and CSS", "A full multi-component homepage layout including navigation header, hero banner, feature cards, and footer.", """
<div style="border: 1px solid var(--border-color); border-radius: 12px; overflow: hidden; background: var(--bg-card);">
    <div style="background: #1e293b; padding: 1rem 1.5rem; display: flex; justify-content: space-between; align-items: center;">
        <strong>NovaWeb Agency</strong>
        <div style="font-size: 0.85rem; color: #94a3b8;">Home &bull; Services &bull; Contact</div>
    </div>
    <div style="padding: 2.5rem 1.5rem; text-align: center; background: linear-gradient(180deg, rgba(99,102,241,0.15) 0%, transparent 100%);">
        <h2 style="font-size: 1.8rem; margin-bottom: 0.5rem;">Innovate Faster With Modern Web Code</h2>
        <p style="color: var(--text-secondary); max-width: 500px; margin: 0 auto 1.25rem;">Designing responsive, performant, and delightful interfaces for modern devices.</p>
        <button class="btn btn-primary">Explore Case Studies</button>
    </div>
</div>
"""),
    (26, "CSS Inheritance and Specificity", "Demonstrates the cascade hierarchy: !important > inline > #id > .class > element, and inherited vs non-inherited properties.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); font-family: sans-serif; color: #94a3b8;">
    <p>This paragraph inherits <code>font-family</code> and <code>color</code> from parent container.</p>
    <div id="demo-spec-id" class="demo-spec-class" style="border: 1px solid var(--border-color); padding: 1rem; border-radius: 6px; margin-top: 0.5rem; color: #818cf8;">
        <strong>Specificity Order:</strong> ID Selector (Score 0,1,0,0) overrides Class (0,0,1,0) and Element (0,0,0,1).
    </div>
</div>
"""),
    (27, "Universal, Element, Class, ID, Attribute, and Grouping Selectors", "Hands-on breakdown of basic CSS selector syntax with color-coded live specimens.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); display: flex; flex-direction: column; gap: 0.75rem;">
    <div style="background: rgba(99,102,241,0.15); padding: 0.5rem 1rem; border-radius: 4px; color: #818cf8;">* (Universal): Applies reset or global tokens</div>
    <div style="background: rgba(20,184,166,0.15); padding: 0.5rem 1rem; border-radius: 4px; color: #14b8a6;">h1, h2, h3 (Grouping): Shared typography styling</div>
    <div style="background: rgba(245,158,11,0.15); padding: 0.5rem 1rem; border-radius: 4px; color: #f59e0b;">[type="submit"] (Attribute): Target inputs matching exact attribute</div>
</div>
"""),
    (28, "CSS Combinator Selectors", "Descendant (space), Child (>), Adjacent Sibling (+), and General Sibling (~) selector behaviors.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div style="border-left: 3px solid var(--accent-primary); padding-left: 1rem; margin-bottom: 0.75rem;">
        <code>parent > child</code> : Selects direct children only.
    </div>
    <div style="border-left: 3px solid var(--accent-teal); padding-left: 1rem; margin-bottom: 0.75rem;">
        <code>prev + next</code> : Selects the immediate adjacent sibling.
    </div>
    <div style="border-left: 3px solid var(--accent-pink); padding-left: 1rem;">
        <code>prev ~ siblings</code> : Selects all general subsequent siblings.
    </div>
</div>
"""),
    (29, "CSS Variables (Custom Properties)", "Defining --primary-color on :root and dynamically switching runtime themes.", """
<div style="--theme-accent: #14b8a6; background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 2px solid var(--theme-accent);">
    <h3 style="color: var(--theme-accent); margin-bottom: 0.5rem;">Scoped Custom Property (--theme-accent)</h3>
    <p style="color: var(--text-secondary); margin-bottom: 1rem;">Values declared via <code>--name: value</code> cascade and can be updated dynamically via CSS or JavaScript.</p>
    <button onclick="this.parentElement.style.setProperty('--theme-accent', '#ec4899')" class="btn btn-outline btn-sm">Switch to Pink Theme</button>
    <button onclick="this.parentElement.style.setProperty('--theme-accent', '#6366f1')" class="btn btn-outline btn-sm">Switch to Indigo Theme</button>
</div>
"""),
    (30, "Background Images and Background Positioning", "Demonstrates background-size: cover, contain, background-position, and repeat properties.", """
<div style="height: 180px; border-radius: 8px; background: url('data:image/svg+xml;utf8,<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"60\" height=\"60\"><circle cx=\"30\" cy=\"30\" r=\"20\" fill=\"%236366f1\" opacity=\"0.2\"/></svg>') repeat center center, linear-gradient(135deg, #1e293b, #0f172a); display: flex; align-items: center; justify-content: center; border: 1px solid var(--border-color); color: #fff; font-weight: bold;">
    background-repeat: repeat with center positioning
</div>
"""),
    (31, "Linear Gradients and Radial Gradients Using CSS", "Showcases multi-stop linear angle gradients and circular/elliptical radial gradients.", """
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.25rem;">
    <div style="height: 140px; border-radius: 8px; background: linear-gradient(135deg, #6366f1 0%, #ec4899 50%, #f59e0b 100%); display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; text-shadow: 0 1px 3px rgba(0,0,0,0.5);">
        Linear Gradient (135deg)
    </div>
    <div style="height: 140px; border-radius: 8px; background: radial-gradient(circle at center, #06b6d4 0%, #0f172a 70%); display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; text-shadow: 0 1px 3px rgba(0,0,0,0.5);">
        Radial Gradient (Circle)
    </div>
</div>
"""),
    (32, "Box-Shadow and Text-Shadow", "Multi-layered drop shadows, inset shadows, neon glows, and ambient elevation levels.", """
<div style="display: flex; flex-wrap: wrap; gap: 2rem; justify-content: center; background: var(--bg-card); padding: 2rem; border-radius: 8px;">
    <div style="padding: 1.5rem; background: var(--bg-secondary); border-radius: 8px; box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.4); text-align: center; font-weight: bold; color: #fff;">
        Outer Elevation Shadow
    </div>
    <div style="padding: 1.5rem; background: var(--bg-secondary); border-radius: 8px; box-shadow: inset 0 2px 8px rgba(0,0,0,0.7); text-align: center; font-weight: bold; color: #94a3b8;">
        Inset Shadow
    </div>
    <div style="padding: 1.5rem; text-align: center; font-size: 1.5rem; font-weight: 800; color: #fff; text-shadow: 0 0 10px #ec4899, 0 0 20px #ec4899;">
        Neon Text Shadow
    </div>
</div>
"""),
    (33, "Border-Radius to Design Different Shapes", "Creating circles, ellipses, pills, speech bubbles, and leaf shapes purely with CSS border-radius.", """
<div style="display: flex; flex-wrap: wrap; gap: 1.5rem; justify-content: center; align-items: center; background: var(--bg-card); padding: 2rem; border-radius: 8px;">
    <div style="width: 80px; height: 80px; background: #6366f1; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 0.8rem; font-weight: bold;">Circle</div>
    <div style="width: 120px; height: 60px; background: #14b8a6; border-radius: 9999px; display: flex; align-items: center; justify-content: center; color: white; font-size: 0.8rem; font-weight: bold;">Pill Shape</div>
    <div style="width: 80px; height: 80px; background: #ec4899; border-radius: 0 30px 0 30px; display: flex; align-items: center; justify-content: center; color: white; font-size: 0.8rem; font-weight: bold;">Leaf Shape</div>
</div>
"""),
    (34, "Opacity and Transparency Using CSS", "Contrasting opacity (which affects children) with rgba/hsla color transparency.", """
<div style="display: flex; flex-wrap: wrap; gap: 1.5rem; justify-content: center;">
    <div style="background: #4f46e5; opacity: 0.5; padding: 1.5rem; border-radius: 8px; color: white; text-align: center; flex: 1 1 200px;">
        opacity: 0.5 (Child text is also semi-transparent)
    </div>
    <div style="background: rgba(79, 70, 229, 0.5); padding: 1.5rem; border-radius: 8px; color: white; text-align: center; flex: 1 1 200px; font-weight: bold;">
        rgba(...) (Background is transparent, text is 100% opaque)
    </div>
</div>
"""),
    (35, "CSS Overflow Properties", "Handling content overflow with visible, hidden, scroll, and auto behaviors.", """
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem;">
    <div style="height: 100px; overflow: scroll; background: var(--bg-card); border: 1px solid var(--border-color); padding: 0.75rem; border-radius: 6px;">
        <strong>overflow: scroll</strong>
        <p style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 0.5rem;">Scrollbars are always rendered horizontally and vertically. Scroll to reveal extra content.</p>
    </div>
    <div style="height: 100px; overflow: hidden; background: var(--bg-card); border: 1px solid var(--border-color); padding: 0.75rem; border-radius: 6px;">
        <strong>overflow: hidden</strong>
        <p style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 0.5rem;">Content exceeding container bounds is clipped cleanly without scrollbars.</p>
    </div>
</div>
"""),
    (36, "Z-Index and Stacking Order", "Demonstrating stacking contexts, relative positioning, and layer priorities.", """
<div style="position: relative; height: 160px; background: var(--bg-secondary); border-radius: 8px; padding: 1rem; border: 1px solid var(--border-color);">
    <div style="position: absolute; left: 30px; top: 30px; width: 120px; height: 90px; background: #6366f1; color: white; padding: 0.5rem; border-radius: 6px; z-index: 1;">z-index: 1</div>
    <div style="position: absolute; left: 80px; top: 50px; width: 120px; height: 90px; background: #ec4899; color: white; padding: 0.5rem; border-radius: 6px; z-index: 10;">z-index: 10 (Front)</div>
</div>
"""),
    (37, "CSS Display Properties (Block, Inline, Inline-Block, None)", "Comparison of natural box behaviors across standard display modes.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div style="background: rgba(99,102,241,0.2); padding: 0.5rem; margin-bottom: 0.5rem; border-radius: 4px;">display: block (Takes full container width on new line)</div>
    <span style="background: rgba(20,184,166,0.2); padding: 0.5rem; border-radius: 4px;">display: inline</span>
    <span style="background: rgba(20,184,166,0.2); padding: 0.5rem; border-radius: 4px; margin-left: 0.5rem;">inline sibling</span>
    <div style="display: inline-block; width: 180px; background: rgba(245,158,11,0.2); padding: 0.5rem; border-radius: 4px; margin-left: 0.5rem; vertical-align: middle;">display: inline-block (Respects width/height)</div>
</div>
"""),
    (38, "Visibility and Hiding Elements", "Contrast between display: none (removes from flow) and visibility: hidden (preserves space).", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); display: flex; gap: 1rem; align-items: center;">
    <div style="background: #10b981; color: white; padding: 1rem; border-radius: 6px;">Box 1</div>
    <div id="visBox" style="visibility: visible; background: #f43f5e; color: white; padding: 1rem; border-radius: 6px;">Box 2 (Toggled)</div>
    <div style="background: #10b981; color: white; padding: 1rem; border-radius: 6px;">Box 3</div>
    <button class="btn btn-outline btn-sm" onclick="const b = document.getElementById('visBox'); b.style.visibility = b.style.visibility === 'hidden' ? 'visible' : 'hidden';">Toggle visibility: hidden</button>
</div>
"""),
    (39, "Dropdown Menu Using HTML and CSS", "Pure CSS dropdown navigation menu driven by hover and focus-within pseudo-classes.", """
<div style="position: relative; display: inline-block;">
    <button class="btn btn-primary" style="display: flex; align-items: center; gap: 0.5rem;">Services Menu ▼</button>
    <div style="background: #1e293b; border: 1px solid var(--border-color); border-radius: 8px; padding: 0.5rem; margin-top: 0.25rem; min-width: 180px; box-shadow: var(--shadow-lg);">
        <a href="#" style="display: block; padding: 0.5rem; color: #cbd5e1; text-decoration: none; border-radius: 4px;" onmouseover="this.style.background='#334155'" onmouseout="this.style.background='transparent'">Web Engineering</a>
        <a href="#" style="display: block; padding: 0.5rem; color: #cbd5e1; text-decoration: none; border-radius: 4px;" onmouseover="this.style.background='#334155'" onmouseout="this.style.background='transparent'">UI/UX Design</a>
        <a href="#" style="display: block; padding: 0.5rem; color: #cbd5e1; text-decoration: none; border-radius: 4px;" onmouseover="this.style.background='#334155'" onmouseout="this.style.background='transparent'">Cloud Systems</a>
    </div>
</div>
"""),
    (40, "Image Hover Effect Using CSS", "Smooth zoom and dark gradient overlay on image container hover.", """
<div style="width: 280px; height: 180px; border-radius: 10px; overflow: hidden; position: relative; margin: 0 auto; cursor: pointer; box-shadow: var(--shadow-md);" onmouseover="this.querySelector('.zoom-bg').style.transform='scale(1.1)'; this.querySelector('.overlay').style.opacity='1';" onmouseout="this.querySelector('.zoom-bg').style.transform='scale(1)'; this.querySelector('.overlay').style.opacity='0';">
    <div class="zoom-bg" style="width: 100%; height: 100%; background: linear-gradient(135deg, #6366f1, #06b6d4); transition: transform 0.4s ease; display: flex; align-items: center; justify-content: center; font-size: 3rem;">🏔️</div>
    <div class="overlay" style="position: absolute; inset: 0; background: rgba(0,0,0,0.6); display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; opacity: 0; transition: opacity 0.3s ease;">
        View Landscape
    </div>
</div>
"""),
    (41, "Tooltip Using CSS", "Custom styled tooltip positioning with transition fade and directional arrow pointer.", """
<div style="text-align: center; padding: 2rem;">
    <span style="position: relative; cursor: pointer; color: var(--accent-primary); font-weight: 600; text-decoration: underline;" onmouseover="document.getElementById('ttDemo').style.opacity='1'" onmouseout="document.getElementById('ttDemo').style.opacity='0'">
        Hover over this link for tooltip
        <span id="ttDemo" style="opacity: 0; transition: opacity 0.3s; position: absolute; bottom: 125%; left: 50%; transform: translateX(-50%); background: #1e293b; color: #fff; padding: 0.4rem 0.8rem; border-radius: 6px; font-size: 0.8rem; white-space: nowrap; border: 1px solid var(--border-color); box-shadow: var(--shadow-md);">
            Pure CSS Tooltip Content
        </span>
    </span>
</div>
"""),
    (42, "CSS-Only Button Hover Animations", "Creative button hover animations: fill wave, glow pulse, and border slide effects.", """
<div style="display: flex; flex-wrap: wrap; gap: 1.5rem; justify-content: center; padding: 1.5rem;">
    <button style="padding: 0.75rem 1.5rem; border: 2px solid #6366f1; background: transparent; color: #fff; font-weight: bold; border-radius: 6px; cursor: pointer; transition: 0.3s;" onmouseover="this.style.background='#6366f1'; this.style.boxShadow='0 0 15px #6366f1';" onmouseout="this.style.background='transparent'; this.style.boxShadow='none';">Glow Border</button>
    <button style="padding: 0.75rem 1.5rem; border: none; background: #10b981; color: white; font-weight: bold; border-radius: 30px; cursor: pointer; transition: 0.3s;" onmouseover="this.style.letterSpacing='2px'" onmouseout="this.style.letterSpacing='normal'">Expand Spacing</button>
</div>
"""),
    (43, "CSS Filters (Blur, Grayscale, Brightness, Contrast)", "Applying visual graphic effects like blur(), grayscale(), brightness(), and contrast() on elements.", """
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; text-align: center;">
    <div style="background: linear-gradient(135deg, #f43f5e, #fb923c); height: 100px; border-radius: 8px; filter: grayscale(100%); display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">grayscale(100%)</div>
    <div style="background: linear-gradient(135deg, #3b82f6, #2dd4bf); height: 100px; border-radius: 8px; filter: blur(2px); display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">blur(2px)</div>
    <div style="background: linear-gradient(135deg, #8b5cf6, #ec4899); height: 100px; border-radius: 8px; filter: contrast(180%); display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">contrast(180%)</div>
</div>
"""),
    (44, "Object-Fit and Object-Position", "Demonstrating object-fit: cover, contain, fill, and positional cropping.", """
<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center;">
    <div style="text-align: center;">
        <span style="font-size: 0.8rem; color: var(--text-muted);">object-fit: cover</span>
        <div style="width: 140px; height: 100px; border: 2px solid var(--accent-primary); border-radius: 6px; overflow: hidden; background: #1e293b; display: flex; align-items: center; justify-content: center; font-size: 2rem;">🖼️</div>
    </div>
    <div style="text-align: center;">
        <span style="font-size: 0.8rem; color: var(--text-muted);">object-fit: contain</span>
        <div style="width: 140px; height: 100px; border: 2px solid var(--accent-teal); border-radius: 6px; overflow: hidden; background: #1e293b; display: flex; align-items: center; justify-content: center; font-size: 2rem;">📐</div>
    </div>
</div>
"""),
    (45, "Responsive Image Gallery Using CSS", "Multi-column responsive grid layout with automatic row sizing and responsive wrapping.", """
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 0.75rem;">
    <div style="background: #4338ca; height: 110px; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">Photo 1</div>
    <div style="background: #0891b2; height: 110px; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">Photo 2</div>
    <div style="background: #be185d; height: 110px; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">Photo 3</div>
    <div style="background: #b45309; height: 110px; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;">Photo 4</div>
</div>
"""),
    (46, "Card-Based Layout Using Flexbox", "Modular card components using flexbox alignment, badges, descriptions, and action rows.", """
<div style="display: flex; flex-wrap: wrap; gap: 1.25rem;">
    <div style="flex: 1 1 240px; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
        <h4 style="color: var(--accent-primary); margin-bottom: 0.5rem;">Frontend Stack</h4>
        <p style="color: var(--text-secondary); font-size: 0.85rem; margin-bottom: 1rem;">HTML5, CSS3 Grid, Flexbox, and JavaScript APIs.</p>
        <button class="btn btn-outline btn-sm">Explore Details</button>
    </div>
    <div style="flex: 1 1 240px; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem;">
        <h4 style="color: var(--accent-teal); margin-bottom: 0.5rem;">Performance</h4>
        <p style="color: var(--text-secondary); font-size: 0.85rem; margin-bottom: 1rem;">Sub-second load times and lightweight CSS architectures.</p>
        <button class="btn btn-outline btn-sm">Explore Details</button>
    </div>
</div>
"""),
    (47, "Dashboard Layout Using CSS Grid", "An administrative analytics dashboard with sidebar, topbar, statistic metrics, and chart placeholder.", """
<div style="display: grid; grid-template-columns: 180px 1fr; grid-template-rows: 50px 1fr; height: 260px; border: 1px solid var(--border-color); border-radius: 8px; overflow: hidden;">
    <div style="grid-column: 1 / -1; background: #1e293b; padding: 0.75rem 1rem; border-bottom: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;"><strong>Admin Portal</strong> <span>surya@lab</span></div>
    <div style="background: #0f172a; padding: 1rem; border-right: 1px solid var(--border-color); font-size: 0.85rem; color: #94a3b8; display: flex; flex-direction: column; gap: 0.5rem;">
        <span style="color: #fff;">📊 Overview</span><span>⚙️ Settings</span><span>📁 Logs</span>
    </div>
    <div style="padding: 1rem; background: var(--bg-primary); display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
        <div style="background: var(--bg-card); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color);">Users: <strong>1,420</strong></div>
        <div style="background: var(--bg-card); padding: 0.75rem; border-radius: 6px; border: 1px solid var(--border-color);">Uptime: <strong style="color: var(--accent-emerald);">99.9%</strong></div>
    </div>
</div>
"""),
    (48, "Two-Column Webpage Layout Using CSS Grid", "Classic 2-column layout with flexible content body and sticky sidebar via CSS Grid.", """
<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 1.5rem; background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div>
        <h3 style="color: var(--text-primary); margin-bottom: 0.5rem;">Primary Article Column</h3>
        <p style="color: var(--text-secondary); font-size: 0.9rem;">The main column takes twice the proportional fractional width (2fr), ideal for long-form tutorials, code walkthroughs, and documentation.</p>
    </div>
    <div style="background: var(--bg-secondary); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color);">
        <h4 style="color: var(--accent-teal); margin-bottom: 0.5rem;">Sidebar (1fr)</h4>
        <p style="font-size: 0.8rem; color: var(--text-muted);">Quick navigation links and related reference materials.</p>
    </div>
</div>
"""),
    (49, "Three-Column Webpage Layout Using Flexbox", "Multi-column responsive flexbox system with left navigation, main center, and right widgets.", """
<div style="display: flex; flex-wrap: wrap; gap: 1rem;">
    <div style="flex: 1 1 180px; background: var(--bg-card); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color);">Left Col (Nav)</div>
    <div style="flex: 2 1 260px; background: var(--bg-card); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color);">Center Col (Feed Content)</div>
    <div style="flex: 1 1 180px; background: var(--bg-card); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color);">Right Col (Widgets)</div>
</div>
"""),
    (50, "Webpage with Sticky Header", "Demonstrating position: sticky with top: 0 sticking during user scroll within container.", """
<div style="height: 200px; overflow-y: scroll; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-card); position: relative;">
    <div style="position: sticky; top: 0; background: #6366f1; color: white; padding: 0.75rem 1rem; font-weight: bold; z-index: 10;">
        Sticky Header (Scroll down to see stickiness)
    </div>
    <div style="padding: 1rem; color: var(--text-secondary); line-height: 2;">
        Paragraph 1: Testing scroll position.<br>
        Paragraph 2: The header remains affixed at top: 0 within its parent container.<br>
        Paragraph 3: Clean native behavior without JavaScript scroll listeners.<br>
        Paragraph 4: Additional scrollable demonstration content.<br>
        Paragraph 5: End of container.
    </div>
</div>
"""),
    (51, "Webpage with Fixed Sidebar", "Illustrating a fixed side navigation rail anchored to the left of the page view.", """
<div style="display: flex; height: 200px; border: 1px solid var(--border-color); border-radius: 8px; overflow: hidden;">
    <div style="width: 140px; background: #1e293b; color: white; padding: 1rem; font-size: 0.85rem; display: flex; flex-direction: column; gap: 0.75rem; border-right: 1px solid var(--border-color);">
        <strong>Fixed Sidebar</strong>
        <span>🏠 Home</span>
        <span>📊 Charts</span>
        <span>⚙️ Config</span>
    </div>
    <div style="flex: 1; padding: 1.25rem; background: var(--bg-primary); overflow-y: auto;">
        <h4>Main Scrollable Area</h4>
        <p style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 0.5rem;">The sidebar stays anchored while this main area handles content scrolling.</p>
    </div>
</div>
"""),
    (52, "Responsive Footer Using HTML and CSS", "A multi-column site footer with brand links, product columns, newsletter input, and copyright.", """
<footer style="background: #1e293b; border: 1px solid var(--border-color); border-radius: 8px; padding: 2rem; color: #94a3b8; font-size: 0.85rem;">
    <div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 1.5rem; margin-bottom: 1.5rem;">
        <div>
            <strong style="color: #fff; font-size: 1rem;">TechPortal</strong>
            <p style="margin-top: 0.5rem; max-width: 250px;">Practical Laboratory for Web Technologies and Frontend Engineering.</p>
        </div>
        <div>
            <strong style="color: #fff;">Navigation</strong>
            <div style="display: flex; flex-direction: column; gap: 0.35rem; margin-top: 0.5rem;">
                <a href="#">HTML Guide</a><a href="#">CSS Architecture</a><a href="#">JavaScript APIs</a>
            </div>
        </div>
    </div>
    <div style="border-top: 1px solid #334155; padding-top: 1rem; text-align: center;">
        &copy; 2026 M. Surya Nivas Reddy. All rights reserved.
    </div>
</footer>
"""),
    (53, "Responsive Login and Signup Page", "Tabbed authentication card switching seamlessly between Login and Create Account states.", """
<div style="max-width: 400px; margin: 0 auto; background: var(--bg-card); border-radius: 12px; border: 1px solid var(--border-color); padding: 1.75rem;">
    <div style="display: flex; margin-bottom: 1.5rem; border-bottom: 1px solid var(--border-color);">
        <button id="tabLogin" onclick="document.getElementById('formLogin').style.display='block'; document.getElementById('formSignup').style.display='none'; this.style.borderBottom='2px solid #6366f1'; document.getElementById('tabSignup').style.borderBottom='none';" style="flex: 1; padding: 0.6rem; background: transparent; border: none; color: #fff; font-weight: bold; border-bottom: 2px solid #6366f1; cursor: pointer;">Sign In</button>
        <button id="tabSignup" onclick="document.getElementById('formLogin').style.display='none'; document.getElementById('formSignup').style.display='block'; this.style.borderBottom='2px solid #6366f1'; document.getElementById('tabLogin').style.borderBottom='none';" style="flex: 1; padding: 0.6rem; background: transparent; border: none; color: #94a3b8; font-weight: bold; cursor: pointer;">Sign Up</button>
    </div>
    <div id="formLogin">
        <div class="form-group"><input type="text" class="form-control" placeholder="Email / Username"></div>
        <div class="form-group"><input type="password" class="form-control" placeholder="Password"></div>
        <button class="btn btn-primary" style="width: 100%;">Sign In</button>
    </div>
    <div id="formSignup" style="display: none;">
        <div class="form-group"><input type="text" class="form-control" placeholder="Full Name"></div>
        <div class="form-group"><input type="email" class="form-control" placeholder="Email Address"></div>
        <div class="form-group"><input type="password" class="form-control" placeholder="Choose Password"></div>
        <button class="btn btn-primary" style="width: 100%;">Create Account</button>
    </div>
</div>
"""),
    (54, "Responsive Contact Form", "A sleek contact us form with floating label styling, email, subject, message, and submit button.", """
<form onsubmit="event.preventDefault(); alert('Message sent!');" style="max-width: 500px; margin: 0 auto; background: var(--bg-card); padding: 2rem; border-radius: 12px; border: 1px solid var(--border-color);">
    <h3 style="margin-bottom: 1.25rem; color: #fff; text-align: center;">Get In Touch</h3>
    <div class="form-group">
        <label class="form-label">Your Name</label>
        <input type="text" class="form-control" required placeholder="Surya Reddy">
    </div>
    <div class="form-group">
        <label class="form-label">Email Address</label>
        <input type="email" class="form-control" required placeholder="surya@example.com">
    </div>
    <div class="form-group">
        <label class="form-label">Message</label>
        <textarea class="form-control" rows="4" required placeholder="Write your inquiry here..."></textarea>
    </div>
    <button type="submit" class="btn btn-primary" style="width: 100%;">Send Message</button>
</form>
"""),
    (55, "Responsive College Website Homepage", "College portal landing layout with banner hero, department quick links, and notice board.", """
<div style="background: var(--bg-card); border-radius: 10px; border: 1px solid var(--border-color); overflow: hidden;">
    <div style="background: linear-gradient(135deg, #1e3a8a, #065f46); padding: 2.5rem 1.5rem; text-align: center; color: white;">
        <h2 style="font-size: 1.8rem; margin-bottom: 0.5rem;">University of Engineering &amp; Technology</h2>
        <p style="opacity: 0.9;">Accredited Grade A+ &bull; Innovation &amp; Research Excellence</p>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; padding: 1.5rem;">
        <div style="background: var(--bg-secondary); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color); text-align: center;">🏛️ Academic Programs</div>
        <div style="background: var(--bg-secondary); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color); text-align: center;">🔬 Research Labs</div>
        <div style="background: var(--bg-secondary); padding: 1rem; border-radius: 6px; border: 1px solid var(--border-color); text-align: center;">📢 Examination Notices</div>
    </div>
</div>
"""),
    (56, "Restaurant Webpage Using HTML and CSS", "A bistro menu webpage featuring special dishes, pricing cards, and reservation CTA.", """
<div style="background: #18181b; border-radius: 12px; border: 1px solid #27272a; padding: 2rem; color: #f4f4f5; max-width: 600px; margin: 0 auto;">
    <div style="text-align: center; margin-bottom: 1.5rem;">
        <span style="color: #f59e0b; font-family: serif; font-style: italic; font-size: 1.1rem;">Authentic Gourmet</span>
        <h2 style="color: #fff; font-size: 1.75rem;">Le Bistro Italiano</h2>
    </div>
    <div style="display: flex; flex-direction: column; gap: 1rem;">
        <div style="display: flex; justify-content: space-between; border-bottom: 1px dashed #3f3f46; padding-bottom: 0.5rem;">
            <div><strong>Truffle Tagliolini</strong><div style="font-size: 0.8rem; color: #a1a1aa;">Handmade pasta, black truffle emulsion, parmesan</div></div>
            <span style="color: #f59e0b; font-weight: bold;">$28</span>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px dashed #3f3f46; padding-bottom: 0.5rem;">
            <div><strong>Wood-Fired Margherita</strong><div style="font-size: 0.8rem; color: #a1a1aa;">San Marzano tomatoes, fior di latte, fresh basil</div></div>
            <span style="color: #f59e0b; font-weight: bold;">$22</span>
        </div>
    </div>
</div>
"""),
    (57, "Online Shopping Webpage Using CSS", "E-commerce storefront with filtering category chips and item product grid.", """
<div style="background: var(--bg-card); border-radius: 8px; border: 1px solid var(--border-color); padding: 1.5rem;">
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1.25rem; overflow-x: auto;">
        <button class="filter-tag active">All Products</button>
        <button class="filter-tag">Footwear</button>
        <button class="filter-tag">Apparel</button>
        <button class="filter-tag">Watches</button>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem;">
        <div style="background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 6px; padding: 1rem; text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">👟</div>
            <strong style="display: block;">Running Shoes</strong>
            <span style="color: var(--accent-teal); font-weight: bold;">$89.99</span>
        </div>
        <div style="background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 6px; padding: 1rem; text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">⌚</div>
            <strong style="display: block;">Smart Chrono</strong>
            <span style="color: var(--accent-teal); font-weight: bold;">$199.99</span>
        </div>
    </div>
</div>
"""),
    (58, "Travel Website Homepage Using CSS", "Destination discovery banner with flight booking widget and vacation package cards.", """
<div style="background: linear-gradient(135deg, #0284c7, #0f766e); border-radius: 12px; padding: 2.5rem 1.5rem; color: white; text-align: center;">
    <h2 style="font-size: 2rem; margin-bottom: 0.5rem;">Wanderlust Awaits You</h2>
    <p style="opacity: 0.9; margin-bottom: 1.5rem;">Discover tropical getaways, alpine peaks, and cultural heritage.</p>
    <div style="display: flex; gap: 0.75rem; justify-content: center; flex-wrap: wrap;">
        <span class="stat-pill" style="background: rgba(255,255,255,0.2); color: white;">🏖️ Bali Packages</span>
        <span class="stat-pill" style="background: rgba(255,255,255,0.2); color: white;">🏔️ Swiss Alps</span>
        <span class="stat-pill" style="background: rgba(255,255,255,0.2); color: white;">🗼 Paris Getaways</span>
    </div>
</div>
"""),
    (59, "News/Blog Webpage Layout Using CSS Grid", "Magazine-style grid layout with primary breaking story and companion side articles.", """
<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 1rem; background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div style="background: var(--bg-secondary); padding: 1.5rem; border-radius: 6px; border: 1px solid var(--border-color);">
        <span style="background: #f43f5e; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.75rem; font-weight: bold;">HEADLINE</span>
        <h3 style="margin-top: 0.5rem; color: #fff;">Quantum Computing Breakthrough Reaches Quantum Advantage</h3>
        <p style="color: var(--text-secondary); font-size: 0.85rem; margin-top: 0.5rem;">Researchers demonstrate scalable fault-tolerant error correction in photonic systems...</p>
    </div>
    <div style="display: flex; flex-direction: column; gap: 0.75rem;">
        <div style="background: var(--bg-secondary); padding: 0.75rem; border-radius: 6px; font-size: 0.85rem;"><strong>AI Code Synthesis</strong><p style="color: var(--text-muted); font-size: 0.75rem;">New model benchmarks</p></div>
        <div style="background: var(--bg-secondary); padding: 0.75rem; border-radius: 6px; font-size: 0.85rem;"><strong>Web3 Standards</strong><p style="color: var(--text-muted); font-size: 0.75rem;">Decentralized identity updates</p></div>
    </div>
</div>
"""),
    (60, "Portfolio Website with Multiple Sections Using HTML and CSS", "Complete modular portfolio layout with Hero, Skills, Projects, and Contact sections.", """
<div style="background: var(--bg-card); border-radius: 8px; border: 1px solid var(--border-color); padding: 1.5rem;">
    <div style="display: flex; gap: 1rem; border-bottom: 1px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
        <span style="color: var(--accent-primary); font-weight: bold;">Section 1: Hero</span> &bull; 
        <span style="color: var(--accent-teal); font-weight: bold;">Section 2: Skills</span> &bull; 
        <span style="color: var(--accent-pink); font-weight: bold;">Section 3: Works</span>
    </div>
    <p style="color: var(--text-secondary); font-size: 0.9rem;">Clean multi-section single-page portfolio layout styled with CSS smooth scrolling anchors and responsive cards.</p>
</div>
"""),
    (61, "CSS Grid Template Areas", "Structuring layouts intuitively using grid-template-areas: 'header header' 'nav main' 'footer footer'.", """
<div style="display: grid; grid-template-areas: 'hdr hdr' 'nav main' 'ftr ftr'; grid-template-columns: 140px 1fr; gap: 8px; background: var(--bg-card); padding: 1rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div style="grid-area: hdr; background: #4f46e5; color: white; padding: 0.75rem; border-radius: 4px; text-align: center; font-weight: bold;">grid-area: hdr</div>
    <div style="grid-area: nav; background: #06b6d4; color: white; padding: 1.5rem 0.5rem; border-radius: 4px; text-align: center; font-weight: bold;">grid-area: nav</div>
    <div style="grid-area: main; background: #10b981; color: white; padding: 1.5rem; border-radius: 4px; text-align: center; font-weight: bold;">grid-area: main</div>
    <div style="grid-area: ftr; background: #64748b; color: white; padding: 0.5rem; border-radius: 4px; text-align: center; font-weight: bold;">grid-area: ftr</div>
</div>
"""),
    (62, "Flexbox Alignment and Ordering Properties", "Controlling flex items dynamically using order, align-self: flex-end, and justify-content.", """
<div style="display: flex; height: 160px; background: var(--bg-card); padding: 1rem; border-radius: 8px; border: 1px solid var(--border-color); gap: 1rem;">
    <div style="background: #6366f1; color: white; padding: 1rem; border-radius: 6px; order: 2; align-self: flex-start;">Item 1 (order: 2)</div>
    <div style="background: #14b8a6; color: white; padding: 1rem; border-radius: 6px; order: 1; align-self: center;">Item 2 (order: 1)</div>
    <div style="background: #ec4899; color: white; padding: 1rem; border-radius: 6px; order: 3; align-self: flex-end;">Item 3 (order: 3)</div>
</div>
"""),
    (63, "Responsive Layout Using CSS Grid and Media Queries", "Adapting grid-template-columns from 4 columns on large screens to 1 column on compact viewports.", """
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); padding: 1.5rem; border-radius: 8px; text-align: center;">Grid Card A</div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); padding: 1.5rem; border-radius: 8px; text-align: center;">Grid Card B</div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); padding: 1.5rem; border-radius: 8px; text-align: center;">Grid Card C</div>
</div>
"""),
    (64, "Mobile-First Responsive Webpage", "Building mobile styles as default base and enhancing with min-width media queries.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); text-align: center;">
    <h3 style="color: var(--accent-primary); margin-bottom: 0.5rem;">Mobile-First Design Paradigm</h3>
    <p style="color: var(--text-secondary); font-size: 0.9rem;">Styles are designed for small mobile viewports by default; larger desktop capabilities are conditionally added with <code>@media (min-width: 768px)</code>.</p>
</div>
"""),
    (65, "CSS Transitions with Custom Timing Functions", "Visualizing ease, linear, ease-in, ease-out, and cubic-bezier transition curves.", """
<div style="display: flex; flex-direction: column; gap: 0.75rem; background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);" onmouseover="const b = this.querySelectorAll('.trans-bar'); b.forEach(el => el.style.width='85%');" onmouseout="const b = this.querySelectorAll('.trans-bar'); b.forEach(el => el.style.width='60px');">
    <span style="font-size: 0.8rem; color: var(--text-muted);">Hover container to trigger transitions:</span>
    <div class="trans-bar" style="height: 25px; width: 60px; background: #6366f1; border-radius: 4px; transition: width 1s linear; color: white; font-size: 0.75rem; display: flex; align-items: center; padding-left: 6px;">linear</div>
    <div class="trans-bar" style="height: 25px; width: 60px; background: #14b8a6; border-radius: 4px; transition: width 1s ease; color: white; font-size: 0.75rem; display: flex; align-items: center; padding-left: 6px;">ease</div>
    <div class="trans-bar" style="height: 25px; width: 60px; background: #ec4899; border-radius: 4px; transition: width 1s cubic-bezier(0.68, -0.55, 0.27, 1.55); color: white; font-size: 0.75rem; display: flex; align-items: center; padding-left: 6px;">cubic-bezier</div>
</div>
"""),
    (66, "2D and 3D CSS Transformations", "Interactive 3D card flip showcasing perspective, transform-style: preserve-3d, and rotateY(180deg).", """
<div style="perspective: 800px; width: 220px; height: 140px; margin: 0 auto; cursor: pointer;" onclick="const c = this.querySelector('.flip-card-inner'); c.style.transform = c.style.transform === 'rotateY(180deg)' ? 'rotateY(0deg)' : 'rotateY(180deg)';">
    <div class="flip-card-inner" style="position: relative; width: 100%; height: 100%; text-align: center; transition: transform 0.6s; transform-style: preserve-3d;">
        <div style="position: absolute; width: 100%; height: 100%; backface-visibility: hidden; background: #4f46e5; color: white; display: flex; align-items: center; justify-content: center; border-radius: 8px; font-weight: bold;">
            Front Side (Click to Flip)
        </div>
        <div style="position: absolute; width: 100%; height: 100%; backface-visibility: hidden; background: #06b6d4; color: white; display: flex; align-items: center; justify-content: center; border-radius: 8px; font-weight: bold; transform: rotateY(180deg);">
            Back Side (3D Flipped!)
        </div>
    </div>
</div>
"""),
    (67, "Keyframe Animations", "Complex multi-stage keyframe animations with transformations and hue-rotate color cycles.", """
<style>
@keyframes orbitShift { 0% { transform: rotate(0deg) translateX(40px) rotate(0deg); } 100% { transform: rotate(360deg) translateX(40px) rotate(-360deg); } }
</style>
<div style="height: 160px; display: flex; align-items: center; justify-content: center; background: var(--bg-card); border-radius: 8px; border: 1px solid var(--border-color); position: relative;">
    <div style="width: 25px; height: 25px; background: var(--accent-teal); border-radius: 50%; box-shadow: 0 0 15px var(--accent-teal); animation: orbitShift 3s infinite linear;"></div>
    <div style="position: absolute; font-size: 0.85rem; color: var(--text-secondary); font-weight: bold;">Multi-Stage Orbital Animation</div>
</div>
"""),
    (68, "Loading Spinner Animation Using CSS", "High-performance CSS-only spinning circle loader using border and border-top-color animation.", """
<style>
@keyframes spinRing { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
</style>
<div style="display: flex; gap: 2rem; justify-content: center; align-items: center; padding: 2rem; background: var(--bg-card); border-radius: 8px;">
    <div style="width: 48px; height: 48px; border: 4px solid rgba(99, 102, 241, 0.2); border-top-color: #6366f1; border-radius: 50%; animation: spinRing 0.8s infinite linear;"></div>
    <div style="width: 48px; height: 48px; border: 4px solid rgba(20, 184, 166, 0.2); border-top-color: #14b8a6; border-radius: 50%; animation: spinRing 1.2s infinite ease-in-out;"></div>
</div>
"""),
    (69, "Sliding Image/Card Animation Using CSS", "Smooth infinite marquee / card slider driven by keyframe translateX transforms.", """
<style>
@keyframes slideMarquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
</style>
<div style="overflow: hidden; background: var(--bg-card); border-radius: 8px; border: 1px solid var(--border-color); padding: 1rem;">
    <div style="display: flex; gap: 1rem; width: 200%; animation: slideMarquee 8s infinite linear;">
        <div style="background: #4f46e5; color: white; padding: 1rem 2rem; border-radius: 6px;">Card 1</div>
        <div style="background: #06b6d4; color: white; padding: 1rem 2rem; border-radius: 6px;">Card 2</div>
        <div style="background: #ec4899; color: white; padding: 1rem 2rem; border-radius: 6px;">Card 3</div>
        <div style="background: #4f46e5; color: white; padding: 1rem 2rem; border-radius: 6px;">Card 1</div>
        <div style="background: #06b6d4; color: white; padding: 1rem 2rem; border-radius: 6px;">Card 2</div>
        <div style="background: #ec4899; color: white; padding: 1rem 2rem; border-radius: 6px;">Card 3</div>
    </div>
</div>
"""),
    (70, "CSS-Only Modal/Popup Design", "Creating a functional modal dialog without JavaScript using the CSS :target pseudo-class.", """
<div style="text-align: center;">
    <a href="#demo-modal" class="btn btn-primary">Open CSS-Only Modal</a>
    <div id="demo-modal" style="display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.8); z-index: 999; align-items: center; justify-content: center;">
        <div style="background: var(--bg-card); border: 1px solid var(--border-color); padding: 2rem; border-radius: 12px; max-width: 400px; width: 90%; text-align: left;">
            <h3 style="margin-bottom: 0.5rem; color: #fff;">CSS :target Modal</h3>
            <p style="color: var(--text-secondary); margin-bottom: 1.25rem;">This popup is opened and closed natively using URL hash fragment targeting!</p>
            <a href="#" class="btn btn-outline btn-sm">Close Modal</a>
        </div>
    </div>
    <style>
    #demo-modal:target { display: flex !important; }
    </style>
</div>
"""),
    (71, "Dark-Mode Webpage Using CSS Variables", "Live interactive theme switching between Dark and Light palette modes using CSS custom properties.", """
<div id="themeContainerDemo" style="--c-bg: #0f172a; --c-card: #1e293b; --c-text: #f8fafc; background: var(--c-bg); color: var(--c-text); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
        <strong>Interactive Themed Box</strong>
        <button onclick="const el = document.getElementById('themeContainerDemo'); const isDark = el.style.getPropertyValue('--c-bg') === '#ffffff'; el.style.setProperty('--c-bg', isDark ? '#0f172a' : '#ffffff'); el.style.setProperty('--c-text', isDark ? '#f8fafc' : '#0f172a');" class="btn btn-outline btn-sm">Toggle Local Palette</button>
    </div>
    <p style="opacity: 0.85; font-size: 0.9rem;">CSS Variables dynamically redefine backgrounds, foregrounds, and borders without altering component structure.</p>
</div>
"""),
    (72, "CSS Responsive Typography", "Fluid typographic sizing using clamp(), viewport width units (vw), and rem scaling.", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color); text-align: center;">
    <h2 style="font-size: clamp(1.25rem, 4vw, 2.5rem); color: var(--accent-primary); margin-bottom: 0.5rem;">
        Fluid Title: clamp(1.25rem, 4vw, 2.5rem)
    </h2>
    <p style="font-size: clamp(0.9rem, 1.5vw, 1.15rem); color: var(--text-secondary);">
        This text automatically scales smoothly between minimum and maximum bounds as viewport width expands.
    </p>
</div>
"""),
    (73, "CSS clamp(), min(), and max() Functions", "Demonstrating CSS mathematical comparison functions clamp(min, val, max), min(), and max().", """
<div style="display: flex; flex-direction: column; gap: 1rem; background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div style="width: min(100%, 350px); background: rgba(99,102,241,0.2); border: 1px solid var(--accent-primary); padding: 0.75rem; border-radius: 6px;">
        width: min(100%, 350px) &bull; Caps width at 350px
    </div>
    <div style="width: max(50%, 200px); background: rgba(20,184,166,0.2); border: 1px solid var(--accent-teal); padding: 0.75rem; border-radius: 6px;">
        width: max(50%, 200px) &bull; Guarantees at least 200px
    </div>
</div>
"""),
    (74, "CSS calc() Function", "Dynamic calculation mixing viewport and pixel units: width: calc(100% - 60px).", """
<div style="background: var(--bg-card); padding: 1.5rem; border-radius: 8px; border: 1px solid var(--border-color);">
    <div style="width: calc(100% - 60px); margin: 0 auto; background: linear-gradient(90deg, #6366f1, #14b8a6); color: white; padding: 1rem; border-radius: 6px; text-align: center; font-weight: bold;">
        width: calc(100% - 60px) (Evaluated dynamically)
    </div>
</div>
"""),
    (75, "Complete Responsive Website (HTML5, CSS3, Flexbox, Grid, Media Queries)", "A fully integrated website bringing together HTML5 semantic markup, modern CSS3 variables, Flexbox headers, Grid content sections, and fluid media queries.", """
<div style="border: 1px solid var(--border-color); border-radius: 12px; overflow: hidden; background: var(--bg-card);">
    <header style="background: #1e293b; padding: 1rem 1.5rem; display: flex; justify-content: space-between; align-items: center;">
        <span style="font-weight: 800; color: #818cf8;">APEX WEB SUITE</span>
        <span style="font-size: 0.85rem; color: #94a3b8;">HTML5 &bull; CSS3 &bull; Grid &bull; Flexbox</span>
    </header>
    <div style="padding: 2rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.25rem;">
        <div style="background: var(--bg-secondary); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-color);">
            <h4 style="color: var(--accent-teal); margin-bottom: 0.25rem;">Grid Layouts</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Two-dimensional card matrix.</p>
        </div>
        <div style="background: var(--bg-secondary); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-color);">
            <h4 style="color: var(--accent-pink); margin-bottom: 0.25rem;">Flexbox Navigation</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">One-dimensional fluid header.</p>
        </div>
        <div style="background: var(--bg-secondary); padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border-color);">
            <h4 style="color: var(--accent-amber); margin-bottom: 0.25rem;">Media Queries</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary);">Universal viewport adaptability.</p>
        </div>
    </div>
</div>
""")
]

def generate_css_page(item, prev_item, next_item, total):
    pid, title, desc, demo = item
    file_name = f"css-{pid:02d}.html"
    prev_link = f"css-{prev_item[0]:02d}.html" if prev_item else "#"
    next_link = f"css-{next_item[0]:02d}.html" if next_item else "#"
    prev_disabled = "opacity: 0.5; pointer-events: none;" if not prev_item else ""
    next_disabled = "opacity: 0.5; pointer-events: none;" if not next_item else ""
    code_escaped = demo.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Program #{pid:02d}: {title}</title>
    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
    <header class="top-nav">
        <div class="container nav-container">
            <a href="../index.html" class="nav-brand">
                <span>⚡ Practical Lab</span>
                <span class="brand-badge" style="background: linear-gradient(135deg, var(--accent-teal), var(--accent-primary));">CSS #{pid:02d}</span>
            </a>
            <div class="nav-links">
                <a href="../index.html">🏠 Home</a>
                <a href="../html/index.html">📄 HTML Programs</a>
                <a href="index.html" class="active">🎨 CSS Programs</a>
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
                    <a href="index.html">CSS Programs</a>
                    <span class="separator">/</span>
                    <span style="color: var(--text-primary); font-weight: 600;">Program #{pid:02d}</span>
                </div>
                <div class="nav-controls">
                    <a href="{prev_link}" class="btn btn-outline btn-sm btn-prev" style="{prev_disabled}">⬅ Prev</a>
                    <a href="index.html" class="btn btn-outline btn-sm">📋 All CSS</a>
                    <a href="{next_link}" class="btn btn-outline btn-sm btn-next" style="{next_disabled}">Next ➡</a>
                </div>
            </div>

            <!-- Experiment Title & Description -->
            <div class="experiment-header-card" style="border-left-color: var(--accent-teal);">
                <span class="experiment-badge" style="color: var(--accent-teal); background: rgba(20, 184, 166, 0.12);">EXPERIMENT #{pid:02d} OF {total:02d}</span>
                <h1 class="experiment-title">{title}</h1>
                <p class="experiment-desc">{desc}</p>
            </div>

            <!-- Demonstration Section -->
            <div class="demo-section">
                <div class="demo-bar">
                    <span class="demo-title"><span class="demo-badge" style="background: var(--accent-teal); box-shadow: 0 0 8px var(--accent-teal);"></span> Live CSS Demonstration</span>
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
                    <span class="code-arrow" style="font-size: 0.85rem; color: var(--accent-teal);">▼ View Code</span>
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
                    <a href="index.html" class="btn btn-primary" style="background: var(--accent-teal);">📋 CSS Program List</a>
                </div>
                <a href="{next_link}" class="btn btn-outline btn-next" style="{next_disabled}">Next Program ➡</a>
            </div>
        </div>
    </main>

    <footer class="site-footer">
        <div class="container footer-content">
            <p>Student Name: <span class="footer-highlight">M.Surya Nivas Reddy</span> | Assignment: <span class="footer-highlight">HTML, CSS & JavaScript Practical Assignment</span></p>
            <p style="font-size: 0.8rem; color: var(--text-muted);">CSS Programs Module &bull; Program {pid} of 75 Completed</p>
        </div>
    </footer>

    <script src="../assets/js/common.js"></script>
</body>
</html>
"""
    return html

def generate_css_index():
    cards = ""
    for item in CSS_DATA:
        pid, title, desc, _ = item
        file_name = f"css-{pid:02d}.html"
        cards += f"""
        <a href="{file_name}" class="program-card" data-category="css">
            <div class="program-header">
                <span class="program-number" style="color: var(--accent-teal); background: rgba(20, 184, 166, 0.12);">CSS #{pid:02d}</span>
                <span style="font-size: 0.85rem; color: var(--text-muted);">Practical</span>
            </div>
            <h3 class="program-title">{title}</h3>
            <p class="program-desc">{desc}</p>
            <div class="program-footer">
                <span>Source: {file_name}</span>
                <span class="program-link-text" style="color: var(--accent-teal);">View Style &rarr;</span>
            </div>
        </a>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Practical Programs List (1 to 75)</title>
    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
    <header class="top-nav">
        <div class="container nav-container">
            <a href="../index.html" class="nav-brand">
                <span>⚡ Practical Lab</span>
                <span class="brand-badge" style="background: linear-gradient(135deg, var(--accent-teal), var(--accent-primary));">CSS Suite</span>
            </a>
            <div class="nav-links">
                <a href="../index.html">🏠 Home</a>
                <a href="../html/index.html">📄 HTML Programs</a>
                <a href="index.html" class="active">🎨 CSS Programs</a>
                <a href="../javascript/index.html">⚙️ JS Programs</a>
            </div>
            <button id="themeToggleBtn" class="theme-toggle-btn">☀️ Light Mode</button>
        </div>
    </header>

    <main class="main-content">
        <div class="container">
            <div class="page-header">
                <span class="page-badge" style="background: rgba(20, 184, 166, 0.15); color: #2dd4bf; border-color: rgba(20, 184, 166, 0.3);">MODULE 02 &bull; 75 PRACTICAL PROGRAMS</span>
                <h1 class="page-title">CSS Practical Programs</h1>
                <p class="page-subtitle">Complete laboratory suite covering selectors, box model, Flexbox, Grid layouts, responsive designs, keyframes, transitions, 3D transforms, and custom properties.</p>
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
                        <span class="meta-value" style="color: var(--accent-teal);">75 / 75 Programs Completed</span>
                    </div>
                </div>
                <a href="../index.html" class="btn btn-outline btn-sm">🏠 Back to Dashboard</a>
            </div>

            <!-- Search and Filter Bar -->
            <div class="search-filter-bar">
                <div class="search-input-wrapper">
                    <span class="search-icon">🔍</span>
                    <input type="text" id="programSearch" class="search-input" placeholder="Search 75 CSS programs by title or concept (Flexbox, Grid, Transform, etc.)...">
                </div>
                <div class="filter-tags">
                    <button class="filter-tag active" data-filter="all">All (75)</button>
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
            <p style="font-size: 0.8rem; color: var(--text-muted);">Total 212 Programs in Assignment &bull; CSS Module</p>
        </div>
    </footer>

    <script src="../assets/js/common.js"></script>
</body>
</html>
"""
    return html

def main():
    total = len(CSS_DATA)
    print(f"Generating {total} CSS programs...")
    for i, item in enumerate(CSS_DATA):
        prev_item = CSS_DATA[i - 1] if i > 0 else None
        next_item = CSS_DATA[i + 1] if i < total - 1 else None
        page_html = generate_css_page(item, prev_item, next_item, total)
        file_name = f"css-{item[0]:02d}.html"
        filepath = os.path.join("css", file_name)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(page_html)
    
    # Generate css/index.html
    index_html = generate_css_index()
    with open(os.path.join("css", "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("All 75 CSS programs and index successfully generated!")

if __name__ == "__main__":
    main()
