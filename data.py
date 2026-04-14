from __future__ import annotations

from textwrap import dedent

from config import APPLY_TESTER_URL, DISCORD_URL


R6_FEATURES = [
    "Smooth aiming",
    "Adjustable distance",
    "Custom hotkey",
    "Target marker",
    "Configurable FOV (Field of View)",
    "Team targeting options",
    "Sticky target system",
    "Hitbox options: Force head, Closest to crosshair, Most damage, Prefer head, Ignore head",
    "Target priority: Distance to crosshair, World distance, Smart targeting",
    "Adjustable FOV thickness",
    "Skeleton ESP",
    "Name ESP and name tags",
    "Health bar display",
    "Box ESP: 2D, 3D, and bounding box",
    "Snaplines with top, middle, and bottom origin",
    "Target line and bullet tracers",
    "Head dot / head circle",
    "Root / foot circle",
    "Offscreen enemy pointer",
    "Radar ESP for enemies and teammates",
    "Box styles: Corners, Rounded, Filled, Gradient, Cyber",
    "Skeleton styles: Dotted, Glow, Gradient, Rainbow per bone",
    "Nametag styles: Minimal, Badge, Pill, Military, Floating",
    "Head marker styles: Circle, Crosshair, Diamond, Star",
    "Snapline styles: Dashed, Dotted, Arrow, Pulse, Zigzag",
    "Outline ESP: Glow, Shadow, Tech, Threat",
    "Silhouette ESP: Soft fill, Gradient, Pulse, Neon",
    "Chams ESP: Flat, Glass, Neon, Heat, Ice, Wireframe",
    "Extra effects: root rings, ground discs, head halos, edge pointers, radar sweep, pings, orbit animations",
    "Rainbow effects per element",
    "Thickness control for all ESP elements",
    "Size scaling for markers, pointers, and radar",
    "Opacity and transparency control",
    "Bullet tracer lifetime and spacing",
    "Offscreen pointer margin and radius",
    "Radar settings: custom size, zoom, range, camera rotation, point clamping",
    "Radar shapes: Circle, Square, Hex, Diamond",
    "Radar styles: Classic, Tactical, Neon, Military, Scanner",
    "Performance modes: FPS update mode with Performance and Quality",
]

PRICE_R6 = {"1 Day": "Ask in ticket", "7 Days": "Ask in ticket", "30 Days": "Ask in ticket"}
PRICE_FORTNITE = {"1 Day": "Ask in ticket", "7 Days": "Ask in ticket", "30 Days": "Ask in ticket"}
PRICE_COD = {"1 Day": "Ask in ticket", "7 Days": "Ask in ticket", "30 Days": "Ask in ticket"}
PRICE_VALORANT = {"1 Day": "TBA", "7 Days": "TBA", "30 Days": "TBA"}
PRICE_RECOIL = {"Lifetime": "$5"}

STATUS_DATA = {
    "Rainbow Six": "updating",
    "Valorant": "updating",
    "Fortnite": "offline",
    "Call of Duty": "offline",
    "Recoil Scripts": "offline",
}


def character_svg(title: str, subtitle: str, colors: tuple[str, str, str]) -> str:
    primary, soft, accent = colors
    return dedent(
        f"""
        <svg viewBox="0 0 420 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{title}">
          <defs>
            <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="{primary}" stop-opacity="0.95"/>
              <stop offset="100%" stop-color="#09090f" stop-opacity="1"/>
            </linearGradient>
            <linearGradient id="glow" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="{soft}" stop-opacity="0"/>
              <stop offset="50%" stop-color="{soft}" stop-opacity="0.95"/>
              <stop offset="100%" stop-color="{accent}" stop-opacity="0"/>
            </linearGradient>
          </defs>
          <rect width="420" height="260" rx="28" fill="url(#bg)"/>
          <circle cx="320" cy="62" r="44" fill="{accent}" opacity="0.22"/>
          <circle cx="78" cy="206" r="54" fill="{soft}" opacity="0.14"/>
          <path d="M110 208c14-52 41-83 83-98 20-7 44-11 60-31 9-11 18-29 32-29 13 0 22 10 22 24 0 16-8 26-15 39 29 8 52 30 62 66-26 20-61 35-105 43-66 12-117 8-139-14Z" fill="#0f1020" opacity="0.96"/>
          <path d="M185 82c17-19 44-29 69-23 22 5 39 22 44 45-19 8-38 14-58 20-16 4-34 8-53 7-5-18-4-34-2-49Z" fill="{soft}" opacity="0.72"/>
          <path d="M70 219h286" stroke="url(#glow)" stroke-width="8" stroke-linecap="round"/>
          <path d="M76 217c27-18 61-34 107-45 54-14 117-15 170-6" stroke="{accent}" stroke-opacity="0.65" stroke-width="2" fill="none" stroke-dasharray="7 8"/>
          <text x="38" y="42" fill="white" font-size="30" font-family="Orbitron, sans-serif" font-weight="700">{title}</text>
          <text x="38" y="68" fill="{soft}" font-size="14" font-family="Inter, sans-serif">{subtitle}</text>
        </svg>
        """
    ).strip()


HERO_BANNER_SVG = character_svg(
    "SONDER // FUTURE DIVISION",
    "Cursor-reactive storefront built for multi-title releases",
    ("#9D4DFF", "#F0B6FF", "#6FFFE9"),
)


PRODUCTS = [
    {
        "name": "Sonder R6",
        "slug": "r6",
        "category": "Rainbow Six Utility",
        "description": "Flagship build with a stacked R6 feature list, premium overlays, and the strongest Sonder presentation.",
        "prices": PRICE_R6,
        "badge": "Main Product",
        "cta": "Join Discord",
        "url": DISCORD_URL,
        "svg": character_svg("R6 // SHADOW", "Precision stack + tactical overlays", ("#9D4DFF", "#F0B6FF", "#6FFFE9")),
        "box_label": "R6 CHEAT",
        "features": R6_FEATURES,
    },
    {
        "name": "Sonder Fortnite",
        "slug": "fortnite",
        "category": "Fortnite Utility",
        "description": "Bright arcade energy, clean tiered access, and a matching Sonder storefront treatment for Fortnite.",
        "prices": PRICE_FORTNITE,
        "badge": "Storefront",
        "cta": "See Pricing",
        "url": DISCORD_URL,
        "svg": character_svg("FN // VELOCITY", "Arcade energy + neon pressure", ("#864BFF", "#FF8AF1", "#79FFE1")),
        "box_label": "FN CHEAT",
        "features": ["1 day access", "7 day access", "30 day access"],
    },
    {
        "name": "Sonder COD",
        "slug": "cod",
        "category": "Call of Duty Utility",
        "description": "Military-leaning presentation with dark chrome styling and short-term or monthly COD access tiers.",
        "prices": PRICE_COD,
        "badge": "Storefront",
        "cta": "Open Discord",
        "url": DISCORD_URL,
        "svg": character_svg("COD // PHANTOM", "Stealth ops + aggressive styling", ("#6D3CFF", "#C8AEFF", "#6FFFE9")),
        "box_label": "COD CHEAT",
        "features": ["1 day access", "7 day access", "30 day access"],
    },
    {
        "name": "Sonder Recoil Scripts",
        "slug": "recoil",
        "category": "Universal Script",
        "description": "Simple universal recoil-script offer with one lifetime purchase and a stripped-back premium layout.",
        "prices": PRICE_RECOIL,
        "badge": "Lifetime",
        "cta": "Buy Lifetime",
        "url": DISCORD_URL,
        "svg": character_svg("SCRIPT // ZERO", "Minimal utility + fast setup", ("#5B21FF", "#BC9AFF", "#84FFF1")),
        "box_label": "SCRIPT PACK",
        "features": ["Lifetime access", "Simple flat price", "Quick setup flow"],
    },
]

RESELLER_PRODUCTS = [
    {
        "name": "Kitty Turtle Valorant",
        "slug": "valorant",
        "category": "Reseller Listing",
        "description": "Reseller slot for Valorant. It is not developed yet, but Kitty Turtle is actively looking for testers.",
        "prices": PRICE_VALORANT,
        "badge": "Reseller",
        "cta": "Apply as Tester",
        "url": APPLY_TESTER_URL,
        "svg": character_svg("VAL // TEST BUILD", "Reseller spotlight + tester call", ("#8C45FF", "#FF96E8", "#65F9D8")),
        "box_label": "VAL CHEAT",
        "features": ["Tester spots open", "1 day, 7 day, and 30 day placeholders", "Sold by Kitty Turtle"],
    }
]
