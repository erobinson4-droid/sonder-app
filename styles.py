from __future__ import annotations

from config import (
    ACCENT,
    BG,
    BG_ELEVATED,
    BORDER,
    BODY_STACK,
    CARD_BG,
    FONT_STACK,
    PRIMARY,
    PRIMARY_SOFT,
    TEXT,
    TEXT_MUTED,
)


def global_styles() -> str:
    return f"""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@400;500;600;700;800&family=Orbitron:wght@500;700;800;900&family=Rajdhani:wght@500;600;700&display=swap');

      :root {{
        --bg: {BG};
        --bg-elevated: {BG_ELEVATED};
        --card-bg: {CARD_BG};
        --border: {BORDER};
        --primary: {PRIMARY};
        --primary-soft: {PRIMARY_SOFT};
        --accent: {ACCENT};
        --text: {TEXT};
        --muted: {TEXT_MUTED};
        --shadow: 0 28px 90px rgba(88, 33, 255, 0.28);
      }}

      html, body, [class*="css"] {{
        font-family: {BODY_STACK};
      }}

      .stApp {{
        background:
          radial-gradient(circle at top left, rgba(157, 77, 255, 0.26), transparent 28%),
          radial-gradient(circle at 82% 8%, rgba(111, 255, 233, 0.10), transparent 26%),
          linear-gradient(180deg, #050508 0%, #090912 46%, #06060b 100%);
        color: var(--text);
      }}

      .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background-image:
          linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
          linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
        background-size: 42px 42px;
        mask-image: radial-gradient(circle at center, black 38%, transparent 92%);
        pointer-events: none;
        z-index: 0;
      }}

      .block-container {{
        max-width: 1240px;
        padding-top: 1.2rem;
        padding-bottom: 4rem;
        position: relative;
        z-index: 2;
      }}

      section[data-testid="stSidebar"] {{
        display: none;
      }}

      .stTabs [data-baseweb="tab-list"] {{
        gap: 0.8rem;
        background: rgba(9, 9, 14, 0.58);
        border: 1px solid var(--border);
        padding: 0.55rem;
        border-radius: 999px;
        backdrop-filter: blur(18px);
      }}

      .stTabs [data-baseweb="tab"] {{
        height: auto;
        padding: 0.8rem 1.1rem;
        border-radius: 999px;
        color: var(--text);
        font-weight: 700;
        background: rgba(255,255,255,0.03);
      }}

      .stTabs [aria-selected="true"] {{
        background: linear-gradient(135deg, rgba(157,77,255,0.92), rgba(111,255,233,0.22));
      }}

      .sonder-nav {{
        position: sticky;
        top: 0.75rem;
        z-index: 30;
        backdrop-filter: blur(18px);
        background: rgba(9, 9, 14, 0.58);
        border: 1px solid var(--border);
        border-radius: 999px;
        padding: 0.8rem 1.1rem;
        box-shadow: 0 16px 50px rgba(0, 0, 0, 0.28);
        margin-bottom: 1.25rem;
      }}

      .sonder-nav-inner {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        flex-wrap: wrap;
      }}

      .sonder-brand {{
        display: flex;
        align-items: center;
        gap: 0.9rem;
      }}

      .sonder-brand-mark {{
        width: 48px;
        height: 48px;
        border-radius: 16px;
        background:
          linear-gradient(145deg, rgba(157,77,255,0.95), rgba(111,255,233,0.24)),
          radial-gradient(circle at 30% 30%, rgba(255,255,255,0.3), transparent 48%);
        box-shadow: 0 0 34px rgba(157,77,255,0.5);
        display: grid;
        place-items: center;
        font-family: {FONT_STACK};
        font-weight: 900;
        color: white;
        position: relative;
        overflow: hidden;
      }}

      .sonder-brand-mark::after {{
        content: "";
        position: absolute;
        inset: 7px;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.14);
      }}

      .sonder-brand-copy h1 {{
        margin: 0;
        font-family: {FONT_STACK};
        font-size: 1.05rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
      }}

      .sonder-brand-copy p {{
        margin: 0.12rem 0 0;
        color: var(--muted);
        font-size: 0.85rem;
      }}

      .sonder-nav-links {{
        display: flex;
        gap: 0.7rem;
        flex-wrap: wrap;
      }}

      .sonder-nav-links a,
      .sonder-pill-link {{
        text-decoration: none;
        color: var(--text);
        padding: 0.75rem 1rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.06);
        transition: 180ms ease;
        font-weight: 700;
      }}

      .sonder-nav-links a:hover,
      .sonder-pill-link:hover {{
        transform: translateY(-1px);
        border-color: rgba(157,77,255,0.5);
        box-shadow: 0 0 24px rgba(157,77,255,0.18);
      }}

      .hero-shell {{
        display: grid;
        grid-template-columns: 1.15fr 0.85fr;
        gap: 1.25rem;
        align-items: stretch;
        margin: 1.8rem 0 1rem;
      }}

      .hero-card, .glass-card {{
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 30px;
        overflow: hidden;
        box-shadow: var(--shadow);
      }}

      .hero-card {{
        padding: 2.4rem;
        position: relative;
        min-height: 460px;
      }}

      .hero-card::before {{
        content: "";
        position: absolute;
        inset: auto -10% -24% auto;
        width: 290px;
        height: 290px;
        background: radial-gradient(circle, rgba(111,255,233,0.18), transparent 70%);
        filter: blur(12px);
      }}

      .eyebrow {{
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.52rem 0.94rem;
        border-radius: 999px;
        background: rgba(157,77,255,0.12);
        border: 1px solid rgba(157,77,255,0.28);
        color: var(--primary-soft);
        text-transform: uppercase;
        letter-spacing: 0.16em;
        font-size: 0.72rem;
        font-weight: 700;
      }}

      .hero-title {{
        font-family: {FONT_STACK};
        font-size: clamp(2.7rem, 4vw, 5rem);
        line-height: 0.96;
        letter-spacing: 0.04em;
        margin: 1rem 0;
        text-transform: uppercase;
      }}

      .hero-title span {{
        color: var(--primary-soft);
        text-shadow: 0 0 18px rgba(199,156,255,0.4);
      }}

      .hero-copy {{
        color: var(--muted);
        font-size: 1.02rem;
        max-width: 42rem;
        line-height: 1.75;
      }}

      .hero-actions {{
        display: flex;
        gap: 0.8rem;
        flex-wrap: wrap;
        margin-top: 1.5rem;
      }}

      .hero-button {{
        text-decoration: none;
        color: white;
        padding: 0.95rem 1.2rem;
        border-radius: 999px;
        border: 1px solid rgba(255,255,255,0.08);
        font-weight: 700;
        transition: 180ms ease;
      }}

      .hero-button.primary {{
        background: linear-gradient(135deg, rgba(157,77,255,1), rgba(111,255,233,0.38));
      }}

      .hero-button.secondary {{
        background: rgba(255,255,255,0.04);
      }}

      .hero-button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(157,77,255,0.28);
      }}

      .hero-stat-grid {{
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 0.9rem;
        padding: 1.15rem;
      }}

      .hero-stat {{
        padding: 1rem;
        border-radius: 22px;
        background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.01));
        border: 1px solid rgba(255,255,255,0.06);
      }}

      .hero-stat h3 {{
        margin: 0;
        font-family: {FONT_STACK};
        font-size: 1.8rem;
      }}

      .hero-stat p {{
        margin: 0.4rem 0 0;
        color: var(--muted);
        line-height: 1.4;
      }}

      .banner-frame {{
        padding: 1rem;
        min-height: 460px;
        display: flex;
        align-items: center;
      }}

      .banner-frame img {{
        width: 100%;
        border-radius: 26px;
        display: block;
        border: 1px solid rgba(255,255,255,0.08);
      }}

      .section-shell {{
        margin-top: 1.35rem;
      }}

      .section-kicker {{
        color: var(--primary-soft);
        letter-spacing: 0.16em;
        text-transform: uppercase;
        font-weight: 800;
        font-size: 0.74rem;
        margin-bottom: 0.4rem;
      }}

      .section-title {{
        font-family: {FONT_STACK};
        font-size: clamp(1.6rem, 2.8vw, 2.6rem);
        margin: 0;
        text-transform: uppercase;
      }}

      .section-copy {{
        color: var(--muted);
        max-width: 54rem;
        line-height: 1.8;
        margin: 0.7rem 0 1.2rem;
      }}

      .card-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 1rem;
      }}

      .product-card {{
        position: relative;
        overflow: hidden;
        border-radius: 28px;
        background: linear-gradient(180deg, rgba(18,18,28,0.94), rgba(11,11,18,0.94));
        border: 1px solid rgba(255,255,255,0.08);
        padding: 1rem;
        box-shadow: 0 24px 70px rgba(0,0,0,0.28);
      }}

      .product-card::before {{
        content: "";
        position: absolute;
        inset: -20% 35% auto -10%;
        height: 180px;
        background: radial-gradient(circle, rgba(157,77,255,0.18), transparent 68%);
        filter: blur(8px);
      }}

      .product-badge {{
        display: inline-flex;
        align-items: center;
        padding: 0.45rem 0.72rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
        color: var(--primary-soft);
        font-size: 0.74rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        font-weight: 800;
      }}

      .box-stage {{
        perspective: 1400px;
        margin: 1rem 0 1.1rem;
        min-height: 320px;
        display: flex;
        align-items: center;
        justify-content: center;
      }}

      .box-3d {{
        width: min(100%, 290px);
        height: 320px;
        position: relative;
        transform-style: preserve-3d;
        transform: rotateY(-22deg) rotateX(10deg);
        transition: transform 220ms ease;
      }}

      .product-card:hover .box-3d {{
        transform: rotateY(-16deg) rotateX(6deg) translateY(-4px);
      }}

      .box-face, .box-spine, .box-top {{
        position: absolute;
        border-radius: 24px;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.09);
        background: linear-gradient(180deg, rgba(157,77,255,0.16), rgba(8,8,14,0.98));
      }}

      .box-face {{
        inset: 0;
        transform: translateZ(34px);
        box-shadow: 0 20px 50px rgba(0,0,0,0.35);
      }}

      .box-face img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
      }}

      .box-top {{
        height: 68px;
        left: 16px;
        right: 22px;
        top: 2px;
        transform: rotateX(90deg) translateZ(34px) translateY(-34px);
        transform-origin: top;
        background: linear-gradient(90deg, rgba(157,77,255,0.34), rgba(111,255,233,0.16));
      }}

      .box-spine {{
        width: 68px;
        left: -2px;
        top: 14px;
        bottom: 20px;
        transform: rotateY(-90deg) translateZ(34px) translateX(-34px);
        transform-origin: left;
        background: linear-gradient(180deg, rgba(157,77,255,0.42), rgba(17,17,26,0.98));
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 0.8rem 0.3rem;
      }}

      .box-spine span {{
        writing-mode: vertical-rl;
        transform: rotate(180deg);
        font-family: {FONT_STACK};
        font-size: 0.8rem;
        letter-spacing: 0.24em;
        color: white;
      }}

      .product-title {{
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        gap: 0.8rem;
        margin-bottom: 0.25rem;
      }}

      .product-title h3 {{
        margin: 0;
        font-family: {FONT_STACK};
        font-size: 1.3rem;
        text-transform: uppercase;
      }}

      .product-category {{
        color: var(--primary-soft);
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 0.14em;
        font-weight: 700;
      }}

      .product-desc {{
        color: var(--muted);
        line-height: 1.7;
        min-height: 88px;
      }}

      .price-row {{
        display: grid;
        gap: 0.65rem;
        margin: 1rem 0 1.1rem;
      }}

      .price-pill {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 0.8rem;
        padding: 0.82rem 0.95rem;
        border-radius: 18px;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.06);
      }}

      .price-pill span:first-child {{
        color: var(--muted);
      }}

      .price-pill strong {{
        font-family: {FONT_STACK};
        font-size: 0.92rem;
      }}

      .product-cta {{
        display: inline-flex;
        width: 100%;
        justify-content: center;
        padding: 0.95rem 1rem;
        border-radius: 18px;
        text-decoration: none;
        color: white;
        font-weight: 800;
        background: linear-gradient(135deg, rgba(157,77,255,1), rgba(111,255,233,0.18));
        border: 1px solid rgba(255,255,255,0.08);
      }}

      .feature-panel {{
        margin-top: 1rem;
        padding: 1.2rem;
      }}

      .feature-columns {{
        columns: 2 280px;
        column-gap: 1.4rem;
      }}

      .feature-bullet {{
        break-inside: avoid;
        margin-bottom: 0.68rem;
        color: var(--muted);
        line-height: 1.6;
      }}

      .reseller-highlight {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
        margin-top: 1rem;
      }}

      .info-card {{
        padding: 1.2rem;
        border-radius: 24px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.06);
      }}

      .info-card h4 {{
        margin: 0 0 0.5rem;
        font-family: {FONT_STACK};
        text-transform: uppercase;
      }}

      .info-card p {{
        color: var(--muted);
        line-height: 1.75;
        margin: 0;
      }}

      .status-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
        gap: 0.9rem;
      }}

      .status-card {{
        position: relative;
        padding: 1rem 1rem 1.1rem;
        border-radius: 22px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.06);
      }}

      .status-dot {{
        width: 12px;
        height: 12px;
        border-radius: 999px;
        display: inline-block;
        margin-right: 0.55rem;
        box-shadow: 0 0 18px currentColor;
        animation: sonderPulse 1.8s infinite ease-in-out;
      }}

      .status-name {{
        font-weight: 700;
        margin-bottom: 0.45rem;
      }}

      .status-label {{
        color: var(--muted);
      }}

      .footer-note {{
        color: var(--muted);
        font-size: 0.92rem;
        text-align: center;
        margin-top: 2rem;
      }}

      @keyframes sonderPulse {{
        0%, 100% {{ transform: scale(1); opacity: 0.65; }}
        50% {{ transform: scale(1.24); opacity: 1; }}
      }}

      @media (max-width: 960px) {{
        .hero-shell,
        .reseller-highlight {{
          grid-template-columns: 1fr;
        }}

        .hero-card {{
          min-height: auto;
        }}

        .box-stage {{
          min-height: 290px;
        }}

        .box-3d {{
          transform: rotateY(-18deg) rotateX(8deg);
        }}
      }}

      @media (max-width: 640px) {{
        .hero-card {{
          padding: 1.5rem;
        }}

        .hero-stat-grid {{
          grid-template-columns: 1fr;
        }}

        .feature-columns {{
          columns: 1;
        }}
      }}
    </style>
    """
