"""
Python Fundamentals Lab - Project 9: AI in Transportation
---------------------------------------------------------
Author: [STUDENT NAME]
Description:
    This script demonstrates fundamental Python concepts by processing transportation
    route data, calculating travel times using a custom function, identifying the
    fastest route using Python's built-in min() with a key, and dynamically generating
    a polished, responsive HTML5 webpage (index.html).

Demonstrated Python Fundamentals:
    1. Functions (def travel_time)
    2. Arithmetic operations (division, multiplication)
    3. For loops (processing routes and benefits dynamically)
    4. String formatting & f-strings (with escaped CSS braces)
    5. Lists and dictionaries (storing structured route and benefit data)
    6. Conditional logic (identifying and styling the fastest route)
    7. File handling using open() with UTF-8 encoding
    8. Python-generated HTML
"""

import sys

# Ensure UTF-8 output encoding for console on Windows systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


# ==============================================================================
# 1. CORE FUNCTION (Functions & Arithmetic)
# ==============================================================================
def travel_time(distance, speed):
    """
    Calculate and return the estimated travel time in minutes.

    Formula:
        time in hours = distance / speed
        time in minutes = (distance / speed) * 60

    Parameters:
        distance (float/int): Distance of the route in kilometres (km).
        speed (float/int): Average travel speed in kilometres per hour (km/h).

    Returns:
        float: Travel time in minutes.
    """
    return (distance / speed) * 60


# ==============================================================================
# 2. DATA STORAGE (Lists & Dictionaries)
# ==============================================================================
# List of 5 sample routes with realistic distance (km) and speed (km/h) values
routes = [
    {
        "name": "City Center → Airport",
        "distance": 18.0,
        "speed": 45.0,
    },
    {
        "name": "City Center → University",
        "distance": 15.0,
        "speed": 32.0,
    },
    {
        "name": "North District → Business Park",
        "distance": 22.0,
        "speed": 40.0,
    },
    {
        "name": "Railway Station → Tech Park",
        "distance": 16.0,
        "speed": 30.0,
    },
    {
        "name": "Residential Area → Shopping Mall",
        "distance": 14.0,
        "speed": 28.0,
    },
]

# List of key benefits of AI in transportation for dynamic card rendering
benefits = [
    {
        "title": "Reduced Travel Time",
        "icon": "⏱️",
        "desc": "Smart algorithms analyze live road data and dynamic rerouting to eliminate bottlenecks, cutting commuter delays by up to 25%.",
    },
    {
        "title": "Better Traffic Management",
        "icon": "🚦",
        "desc": "Intelligent traffic lights synchronize dynamically according to real-time queue lengths, preventing gridlock at major intersections.",
    },
    {
        "title": "Improved Route Planning",
        "icon": "🗺️",
        "desc": "Predictive AI models calculate multi-factor optimal paths factoring in elevation, real-time speed, weather, and battery/fuel economy.",
    },
    {
        "title": "Safer Transportation",
        "icon": "🛡️",
        "desc": "Computer vision models and collision-avoidance sensors identify road hazards in milliseconds, drastically curbing driver error.",
    },
    {
        "title": "Lower Congestion",
        "icon": "🌱",
        "desc": "Evenly distributed traffic across urban road grids lowers vehicle idle times, curbing greenhouse emissions and fuel waste.",
    },
]


# ==============================================================================
# 3. IDENTIFY FASTEST ROUTE (min() with key)
# ==============================================================================
# Use Python's built-in min() function with a lambda key to find the fastest route
fastest_route = min(
    routes,
    key=lambda route: travel_time(route["distance"], route["speed"])
)

# Calculate the fastest travel time for display
fastest_time = travel_time(fastest_route["distance"], fastest_route["speed"])


# ==============================================================================
# 4. DYNAMIC HTML GENERATION USING FOR LOOPS & CONDITIONALS
# ==============================================================================
# Build table rows dynamically using a for loop and conditional statements
table_rows = ""
for route in routes:
    # Call our travel_time function
    time_minutes = travel_time(route["distance"], route["speed"])

    # Conditional logic: check if current route is the fastest route
    if route == fastest_route:
        row_class = "fastest-row"
        badge_html = '<span class="badge badge-fastest">⚡ FASTEST ROUTE</span>'
    else:
        row_class = "standard-row"
        badge_html = ""

    # Append formatted HTML row (formatted to 2 decimal places)
    table_rows += f"""
                    <tr class="{row_class}">
                        <td class="route-name-cell">
                            <span class="route-name">{route["name"]}</span>
                            {badge_html}
                        </td>
                        <td class="text-right">{route["distance"]:.1f} km</td>
                        <td class="text-right">{route["speed"]:.1f} km/h</td>
                        <td class="text-right time-cell"><strong>{time_minutes:.2f} min</strong></td>
                    </tr>"""

# Build benefits cards dynamically using a for loop
benefit_cards = ""
for benefit in benefits:
    benefit_cards += f"""
            <div class="benefit-card">
                <div class="benefit-icon">{benefit["icon"]}</div>
                <h3 class="benefit-title">{benefit["title"]}</h3>
                <p class="benefit-desc">{benefit["desc"]}</p>
            </div>"""


# ==============================================================================
# 5. ASSEMBLE FULL HTML5 WEBPAGE (Python f-string with Escaped CSS Braces)
# ==============================================================================
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI in Transportation</title>
    <style>
        /* Modern CSS Design System */
        :root {{
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --primary-light: #60a5fa;
            --secondary: #0f172a;
            --accent: #10b981;
            --accent-glow: rgba(16, 185, 129, 0.18);
            --bg-light: #f8fafc;
            --card-bg: #ffffff;
            --text-dark: #0f172a;
            --text-muted: #64748b;
            --border-color: #e2e8f0;
            --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.08);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.06);
            --shadow-lg: 0 10px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
            --radius-md: 12px;
            --radius-lg: 16px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-light);
            color: var(--text-dark);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
        }}

        /* Container */
        .container {{
            max-width: 1140px;
            margin: 0 auto;
            padding: 0 24px;
        }}

        /* Header / Hero Section */
        .hero {{
            background: linear-gradient(135deg, #091e3a 0%, #102a4e 50%, #0a3a40 100%);
            color: #ffffff;
            padding: 64px 0 56px 0;
            text-align: center;
            border-bottom: 3px solid var(--accent);
            position: relative;
        }}

        .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #38bdf8;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            padding: 6px 16px;
            border-radius: 9999px;
            margin-bottom: 20px;
        }}

        .hero h1 {{
            font-size: 2.75rem;
            font-weight: 800;
            letter-spacing: -0.5px;
            margin-bottom: 14px;
            background: linear-gradient(to right, #ffffff, #93c5fd);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .hero-subtitle {{
            font-size: 1.25rem;
            font-weight: 400;
            color: #94a3b8;
            max-width: 780px;
            margin: 0 auto 20px auto;
        }}

        .hero-intro {{
            font-size: 1.02rem;
            color: #cbd5e1;
            max-width: 820px;
            margin: 0 auto;
            line-height: 1.7;
        }}

        /* Main Content Layout */
        .main-content {{
            padding: 48px 0 64px 0;
        }}

        .section-header {{
            margin-bottom: 28px;
        }}

        .section-title {{
            font-size: 1.85rem;
            font-weight: 700;
            color: var(--secondary);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .section-subtitle {{
            font-size: 1rem;
            color: var(--text-muted);
        }}

        /* Fastest Route Heroic Card */
        .fastest-card {{
            background: linear-gradient(135deg, #ffffff 0%, #ecfdf5 100%);
            border: 2px solid var(--accent);
            border-radius: var(--radius-lg);
            padding: 28px 32px;
            margin-bottom: 36px;
            box-shadow: var(--shadow-lg), 0 0 20px var(--accent-glow);
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}

        .fastest-card-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }}

        .fastest-label {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.75px;
            color: #047857;
            background: #d1fae5;
            padding: 6px 14px;
            border-radius: 9999px;
            border: 1px solid #a7f3d0;
        }}

        .python-tag {{
            font-size: 0.82rem;
            font-weight: 600;
            color: #0369a1;
            background: #e0f2fe;
            padding: 4px 12px;
            border-radius: 6px;
            border: 1px solid #bae6fd;
            font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
        }}

        .fastest-route-name {{
            font-size: 1.75rem;
            font-weight: 800;
            color: #065f46;
        }}

        .fastest-metrics {{
            display: flex;
            align-items: baseline;
            gap: 24px;
            flex-wrap: wrap;
            padding-top: 4px;
        }}

        .metric-item {{
            display: flex;
            flex-direction: column;
        }}

        .metric-title {{
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #047857;
            font-weight: 600;
        }}

        .metric-value {{
            font-size: 1.4rem;
            font-weight: 700;
            color: #064e3b;
        }}

        .metric-highlight {{
            font-size: 2rem;
            font-weight: 800;
            color: #047857;
        }}

        /* Table Design */
        .table-card {{
            background: var(--card-bg);
            border-radius: var(--radius-lg);
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow-md);
            overflow: hidden;
            margin-bottom: 48px;
        }}

        .table-responsive {{
            width: 100%;
            overflow-x: auto;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }}

        th {{
            background-color: #f1f5f9;
            color: #334155;
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            padding: 16px 20px;
            border-bottom: 1px solid var(--border-color);
        }}

        td {{
            padding: 16px 20px;
            font-size: 0.95rem;
            border-bottom: 1px solid var(--border-color);
            color: #334155;
        }}

        .text-right {{
            text-align: right;
        }}

        .route-name-cell {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }}

        .route-name {{
            font-weight: 600;
            color: var(--secondary);
        }}

        .badge {{
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            padding: 3px 10px;
            border-radius: 9999px;
            text-transform: uppercase;
        }}

        .badge-fastest {{
            background-color: #10b981;
            color: #ffffff;
            box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);
        }}

        /* Highlighted row */
        .fastest-row {{
            background-color: #f0fdf4 !important;
            font-weight: 600;
        }}

        .fastest-row td {{
            color: #065f46;
            border-top: 1.5px solid #86efac;
            border-bottom: 1.5px solid #86efac;
        }}

        .fastest-row .time-cell {{
            color: #047857;
            font-size: 1.05rem;
        }}

        tr:last-child td {{
            border-bottom: none;
        }}

        tr.standard-row:hover {{
            background-color: #f8fafc;
        }}

        /* How AI Helps Section */
        .ai-helps-section {{
            margin-bottom: 48px;
        }}

        .three-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
        }}

        .feature-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 28px 24px;
            box-shadow: var(--shadow-sm);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}

        .feature-card:hover {{
            transform: translateY(-4px);
            box-shadow: var(--shadow-md);
        }}

        .feature-num {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 36px;
            height: 36px;
            background: #eff6ff;
            color: var(--primary);
            font-weight: 800;
            border-radius: 8px;
            margin-bottom: 16px;
            border: 1px solid #dbeafe;
        }}

        .feature-card h3 {{
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--secondary);
            margin-bottom: 12px;
        }}

        .feature-card p {{
            font-size: 0.95rem;
            color: #475569;
            line-height: 1.65;
        }}

        /* Autonomous Vehicles Section */
        .autonomous-section {{
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            color: #ffffff;
            border-radius: var(--radius-lg);
            padding: 36px 32px;
            margin-bottom: 48px;
            box-shadow: var(--shadow-lg);
        }}

        .autonomous-header {{
            margin-bottom: 20px;
        }}

        .autonomous-header h2 {{
            font-size: 1.75rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 8px;
        }}

        .autonomous-header p {{
            font-size: 1rem;
            color: #94a3b8;
        }}

        .autonomous-intro {{
            font-size: 1.02rem;
            color: #cbd5e1;
            line-height: 1.7;
            margin-bottom: 24px;
        }}

        .steps-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }}

        .step-box {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: var(--radius-md);
            padding: 20px;
        }}

        .step-box h4 {{
            font-size: 1.05rem;
            font-weight: 700;
            color: #38bdf8;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .step-box p {{
            font-size: 0.9rem;
            color: #94a3b8;
            line-height: 1.55;
        }}

        /* Benefits Grid Section */
        .benefits-section {{
            margin-bottom: 48px;
        }}

        .benefits-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }}

        .benefit-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 22px 20px;
            box-shadow: var(--shadow-sm);
            transition: transform 0.2s ease;
        }}

        .benefit-card:hover {{
            transform: translateY(-3px);
            box-shadow: var(--shadow-md);
        }}

        .benefit-icon {{
            font-size: 1.8rem;
            margin-bottom: 12px;
        }}

        .benefit-title {{
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--secondary);
            margin-bottom: 8px;
        }}

        .benefit-desc {{
            font-size: 0.88rem;
            color: var(--text-muted);
            line-height: 1.55;
        }}

        /* Footer */
        footer {{
            background-color: #0f172a;
            color: #94a3b8;
            padding: 32px 0;
            border-top: 1px solid #1e293b;
            text-align: center;
            font-size: 0.9rem;
        }}

        footer p {{
            margin-bottom: 6px;
        }}

        .footer-highlight {{
            color: #38bdf8;
            font-weight: 600;
        }}

        /* Sticky Top Navigation Bar with Quick Action Buttons */
        .top-nav {{
            position: sticky;
            top: 0;
            z-index: 1000;
            background: rgba(9, 30, 58, 0.94);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.12);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }}

        .nav-container {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 24px;
            gap: 16px;
        }}

        .nav-brand {{
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
            color: #ffffff;
            font-weight: 700;
            font-size: 1.05rem;
            letter-spacing: -0.2px;
            transition: opacity 0.2s ease;
        }}

        .nav-brand:hover {{
            opacity: 0.9;
        }}

        .brand-icon {{
            font-size: 1.35rem;
            filter: drop-shadow(0 2px 6px rgba(56, 189, 248, 0.4));
        }}

        .brand-badge {{
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #38bdf8;
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid rgba(56, 189, 248, 0.3);
            padding: 2px 8px;
            border-radius: 9999px;
            margin-left: 2px;
        }}

        .nav-buttons {{
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .nav-btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.18);
            color: #e2e8f0;
            font-family: inherit;
            font-size: 0.88rem;
            font-weight: 600;
            padding: 8px 16px;
            border-radius: 9999px;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            outline: none;
            user-select: none;
        }}

        .nav-btn .btn-icon {{
            font-size: 1rem;
            line-height: 1;
            transition: transform 0.25s ease;
        }}

        .nav-btn:hover {{
            background: rgba(255, 255, 255, 0.18);
            color: #ffffff;
            border-color: rgba(56, 189, 248, 0.6);
            transform: translateY(-2px);
            box-shadow: 0 4px 14px rgba(56, 189, 248, 0.25);
        }}

        .nav-btn:hover .btn-icon {{
            transform: scale(1.18);
        }}

        .nav-btn:active {{
            transform: translateY(0) scale(0.97);
        }}

        .nav-btn.active {{
            background: linear-gradient(135deg, rgba(37, 99, 235, 0.9) 0%, rgba(16, 185, 129, 0.9) 100%);
            border-color: rgba(16, 185, 129, 0.8);
            color: #ffffff;
            box-shadow: 0 4px 16px rgba(16, 185, 129, 0.35);
        }}

        .nav-btn:focus-visible {{
            outline: 2px solid #38bdf8;
            outline-offset: 2px;
        }}

        /* Section spotlight glow animation when button is clicked */
        @keyframes sectionSpotlight {{
            0% {{
                box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
                transform: scale(1);
            }}
            30% {{
                box-shadow: 0 0 0 10px rgba(16, 185, 129, 0.35), 0 12px 30px rgba(16, 185, 129, 0.25);
                transform: scale(1.012);
            }}
            100% {{
                box-shadow: 0 0 0 0 rgba(16, 185, 129, 0);
                transform: scale(1);
            }}
        }}

        .section-spotlight {{
            animation: sectionSpotlight 1.8s ease-out;
            border-color: #10b981 !important;
        }}

        /* Responsive Breakpoints */
        @media (max-width: 900px) {{
            .three-grid, .steps-grid {{
                grid-template-columns: 1fr;
            }}
            .hero h1 {{
                font-size: 2.2rem;
            }}
            .nav-container {{
                flex-direction: column;
                gap: 12px;
                padding: 12px 16px;
            }}
            .nav-buttons {{
                width: 100%;
                justify-content: center;
                gap: 8px;
            }}
            .nav-btn {{
                font-size: 0.82rem;
                padding: 7px 12px;
            }}
        }}

        @media (max-width: 640px) {{
            .nav-buttons {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                width: 100%;
                gap: 8px;
            }}
            .nav-btn {{
                justify-content: center;
                padding: 8px 10px;
                font-size: 0.8rem;
            }}
            .fastest-card {{
                padding: 20px;
            }}
            .fastest-route-name {{
                font-size: 1.35rem;
            }}
            .fastest-metrics {{
                gap: 16px;
            }}
            .hero {{
                padding: 44px 0 36px 0;
            }}
            .hero h1 {{
                font-size: 1.85rem;
            }}
            th, td {{
                padding: 12px 14px;
            }}
        }}
    </style>
</head>
<body>

    <!-- Top Navigation Bar with Quick Action Buttons (At Most 4 Buttons) -->
    <nav class="top-nav" id="top-nav" aria-label="Main Navigation">
        <div class="container nav-container">
            <a href="#" class="nav-brand" aria-label="AI Transportation Home">
                <span class="brand-icon">🚗</span>
                <span class="brand-text">AI Transportation</span>
                <span class="brand-badge">Python Lab</span>
            </a>
            <div class="nav-buttons" role="group" aria-label="Quick Action Buttons">
                <button type="button" class="nav-btn active" id="btn-fastest" onclick="navigateToSection('fastest-route-card', this)" aria-label="Fastest Route">
                    <span class="btn-icon">⚡</span>
                    <span class="btn-text">Fastest Route</span>
                </button>
                <button type="button" class="nav-btn" id="btn-planner" onclick="navigateToSection('planner-section', this)" aria-label="Route Planner">
                    <span class="btn-icon">🗺️</span>
                    <span class="btn-text">Route Planner</span>
                </button>
                <button type="button" class="nav-btn" id="btn-autonomous" onclick="navigateToSection('autonomous-section', this)" aria-label="Autonomous Tech">
                    <span class="btn-icon">🤖</span>
                    <span class="btn-text">Autonomous Tech</span>
                </button>
                <button type="button" class="nav-btn" id="btn-benefits" onclick="navigateToSection('benefits-section', this)" aria-label="Key Benefits">
                    <span class="btn-icon">✨</span>
                    <span class="btn-text">Key Benefits</span>
                </button>
            </div>
        </div>
    </nav>

    <!-- Header / Hero Section -->
    <header class="hero">
        <div class="container">
            <h1>AI in Transportation</h1>
            <p class="hero-subtitle">How Artificial Intelligence is making travel smarter, safer and more efficient.</p>
            <p class="hero-intro">
                Artificial Intelligence is transforming global mobility. By analyzing real-time traffic data,
                predicting road congestion, dynamically optimizing routes, and powering autonomous vehicle systems,
                AI helps cities minimize transit delays, cut emissions, and enhance passenger safety.
            </p>
        </div>
    </header>

    <!-- Main Content Container -->
    <main class="container main-content">

        <!-- Fastest Route Summary Card (Generated dynamically by Python) -->
        <section class="fastest-card" id="fastest-route-card">
            <div class="fastest-card-top">
                <span class="fastest-label">⚡ Calculated Fastest Route</span>
                <span class="python-tag">Python min() &amp; travel_time()</span>
            </div>
            <div class="fastest-route-name">{fastest_route["name"]}</div>
            <div class="fastest-metrics">
                <div class="metric-item">
                    <span class="metric-title">Distance &amp; Speed</span>
                    <span class="metric-value">{fastest_route["distance"]:.0f} km • {fastest_route["speed"]:.0f} km/h</span>
                </div>
                <div class="metric-item">
                    <span class="metric-title">Estimated Travel Time</span>
                    <span class="metric-highlight">{fastest_time:.2f} minutes</span>
                </div>
            </div>
        </section>

        <!-- Route Planner Section -->
        <section class="planner-section" id="planner-section">
            <div class="section-header">
                <h2 class="section-title">🗺️ Smart Route Planner</h2>
                <p class="section-subtitle">
                    Dynamic travel times calculated using Python arithmetic: 
                    <code>time = (distance / speed) * 60</code>.
                </p>
            </div>

            <div class="table-card">
                <div class="table-responsive">
                    <table>
                        <thead>
                            <tr>
                                <th>Route</th>
                                <th class="text-right">Distance</th>
                                <th class="text-right">Average Speed</th>
                                <th class="text-right">Estimated Travel Time</th>
                            </tr>
                        </thead>
                        <tbody>{table_rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- How AI Helps Section -->
        <section class="ai-helps-section">
            <div class="section-header">
                <h2 class="section-title">💡 How AI helps</h2>
                <p class="section-subtitle">Three key pillars where artificial intelligence reshapes daily travel.</p>
            </div>

            <div class="three-grid">
                <div class="feature-card">
                    <div class="feature-num">1</div>
                    <h3>Traffic prediction</h3>
                    <p>
                        AI models continuously process incoming data streams from highway sensors, traffic cameras, 
                        and connected GPS devices. By spotting recurring bottlenecks and correlating them with weather 
                        or public events, intelligent systems accurately forecast traffic jams before they build up, 
                        enabling cities to balance road capacity proactively.
                    </p>
                </div>

                <div class="feature-card">
                    <div class="feature-num">2</div>
                    <h3>Route optimisation</h3>
                    <p>
                        Rather than only measuring the static distance on a road map, AI-powered routing engines 
                        continually evaluate live traffic speeds, intersection delays, and temporary roadworks. 
                        Drivers and transit fleets receive instant, adaptive rerouting recommendations that minimize 
                        idle time and conserve fuel or battery charge.
                    </p>
                </div>

                <div class="feature-card">
                    <div class="feature-num">3</div>
                    <h3>Autonomous vehicles</h3>
                    <p>
                        Self-driving vehicles utilize deep neural networks to synthesize live sensor feeds, recognizing 
                        lane markings, pedestrians, road signs, and adjacent cars in fractions of a second. This allows 
                        autonomous platforms to navigate complex urban intersections safely with rapid, dependable 
                        reaction times.
                    </p>
                </div>
            </div>
        </section>

        <!-- Autonomous Vehicles Section -->
        <section class="autonomous-section" id="autonomous-section">
            <div class="autonomous-header">
                <h2>🤖 Autonomous Vehicles &amp; AI Decision-Making</h2>
                <p>How self-driving systems perceive, process, and act on the road.</p>
            </div>
            <p class="autonomous-intro">
                Autonomous vehicles rely on artificial intelligence to process high-frequency streams of information 
                from onboard sensors, LiDAR, and high-resolution cameras. By constantly evaluating road conditions and 
                anticipating the behavior of surrounding motorists and pedestrians, the AI driving agent makes 
                split-second control decisions such as throttle modulation, steering adjustments, and safe emergency braking.
            </p>

            <div class="steps-grid">
                <div class="step-box">
                    <h4>📡 1. Perception &amp; Sensors</h4>
                    <p>Cameras, radar, and LiDAR capture a full 360-degree digital representation of the car's surroundings in real time.</p>
                </div>
                <div class="step-box">
                    <h4>🧠 2. Object Detection</h4>
                    <p>Computer vision models classify surrounding entities—including pedestrians, cyclists, road signs, and lanes.</p>
                </div>
                <div class="step-box">
                    <h4>🎯 3. Action Planning</h4>
                    <p>Trajectory planners decide safe speeds, steering angles, and gap distances to ensure accident-free transit.</p>
                </div>
            </div>
        </section>

        <!-- AI Transportation Benefits (Generated dynamically via Python loop) -->
        <section class="benefits-section" id="benefits-section">
            <div class="section-header">
                <h2 class="section-title">✨ AI Transportation Benefits</h2>
                <p class="section-subtitle">Measurable advantages delivered by intelligent transit solutions.</p>
            </div>

            <div class="benefits-grid">{benefit_cards}
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer>
        <div class="container">
            <p><span class="footer-highlight">Project 9: AI in Transportation</span> • Python Fundamentals Lab</p>
            <p>Generated dynamically using standard Python • Built-in <code>open()</code>, <code>f-strings</code>, and <code>min()</code></p>
        </div>
    </footer>

    <!-- Interactive Navigation & Section Spotlight Script -->
    <script>
        // Smooth scroll to section with sticky header offset & spotlight animation
        function navigateToSection(sectionId, btnElement) {{
            const target = document.getElementById(sectionId);
            if (!target) return;

            const nav = document.getElementById('top-nav');
            const navHeight = nav ? nav.offsetHeight : 0;
            const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navHeight - 16;

            window.scrollTo({{
                top: targetPosition,
                behavior: 'smooth'
            }});

            // Update active button state
            document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
            if (btnElement) {{
                btnElement.classList.add('active');
            }}

            // Trigger visual spotlight pulse on the target section
            target.classList.remove('section-spotlight');
            void target.offsetWidth; // Force reflow
            target.classList.add('section-spotlight');

            setTimeout(() => {{
                target.classList.remove('section-spotlight');
            }}, 2000);
        }}

        // Scrollspy: Automatically highlight the button matching the section in view
        window.addEventListener('DOMContentLoaded', () => {{
            const sectionMap = [
                {{ id: 'fastest-route-card', btnId: 'btn-fastest' }},
                {{ id: 'planner-section', btnId: 'btn-planner' }},
                {{ id: 'autonomous-section', btnId: 'btn-autonomous' }},
                {{ id: 'benefits-section', btnId: 'btn-benefits' }}
            ];

            const navButtons = document.querySelectorAll('.nav-btn');

            function updateScrollSpy() {{
                const nav = document.getElementById('top-nav');
                const navHeight = nav ? nav.offsetHeight : 0;
                const scrollPos = window.scrollY + navHeight + 120;

                let currentBtnId = null;
                for (let i = sectionMap.length - 1; i >= 0; i--) {{
                    const el = document.getElementById(sectionMap[i].id);
                    if (el && el.offsetTop <= scrollPos) {{
                        currentBtnId = sectionMap[i].btnId;
                        break;
                    }}
                }}

                if (!currentBtnId && window.scrollY < 200) {{
                    currentBtnId = 'btn-fastest';
                }}

                if (currentBtnId) {{
                    navButtons.forEach(btn => {{
                        btn.classList.toggle('active', btn.id === currentBtnId);
                    }});
                }}
            }}

            window.addEventListener('scroll', updateScrollSpy, {{ passive: true }});
            updateScrollSpy();
        }});
    </script>
</body>
</html>
"""


# ==============================================================================
# 6. WRITE HTML TO FILE USING open()
# ==============================================================================
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)


# ==============================================================================
# 7. CONSOLE VERIFICATION & COMPLETION MESSAGE
# ==============================================================================
print("=" * 65)
print("Webpage created successfully: index.html")
print("=" * 65)
print(f"Total routes evaluated : {len(routes)}")
print(f"Fastest route detected  : {fastest_route['name']}")
print(f"Distance & Speed        : {fastest_route['distance']} km at {fastest_route['speed']} km/h")
print(f"Calculated travel time  : {fastest_time:.2f} minutes")
print("=" * 65)
