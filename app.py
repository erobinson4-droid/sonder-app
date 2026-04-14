from __future__ import annotations

import base64
from html import escape
from textwrap import dedent

import streamlit as st

from components.background import render_particle_background
from config import (
    BRAND_NAME,
    DISCORD_URL,
    RESELLER_DISCORD_URL,
    STATUS_COLORS,
    STATUS_LABELS,
    TAGLINE,
)
from data import HERO_BANNER_SVG, PRODUCTS, RESELLER_PRODUCTS, STATUS_DATA
from styles import global_styles


def svg_to_data_uri(svg: str) -> str:
    encoded = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    return f"data:image/svg+xml;base64,{encoded}"


def render_nav() -> None:
    st.markdown(
        dedent(
            f"""
            <div class="sonder-nav">
              <div class="sonder-nav-inner">
                <div class="sonder-brand">
                  <div class="sonder-brand-mark">S</div>
                  <div class="sonder-brand-copy">
                    <h1>{BRAND_NAME}</h1>
                    <p>{TAGLINE}</p>
                  </div>
                </div>
                <div class="sonder-nav-links">
                  <a href="#store">Store</a>
                  <a href="#reseller">Reseller</a>
                  <a href="#status">Status</a>
                </div>
              </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    st.markdown(
        dedent(
            f"""
            <div class="hero-shell">
              <div class="hero-card">
                <div class="eyebrow">Future Utility Storefront</div>
                <div class="hero-title">
                  Sonder <span>Launches Loud</span><br/>
                  For Every Queue
                </div>
                <div class="hero-copy">
                  Purple-black futuristic storefront with floating reactive particles, premium 3D-style product boxes,
                  game-specific artwork, reseller access, and a built-in product status board. This first version is set
                  up around Rainbow Six, Fortnite, Call of Duty, and your lifetime recoil scripts offer.
                </div>
                <div class="hero-actions">
                  <a class="hero-button primary" href="#store">Browse Products</a>
                  <a class="hero-button secondary" href="{DISCORD_URL}">Open Discord</a>
                </div>
              </div>
              <div class="glass-card banner-frame">
                <img src="{svg_to_data_uri(HERO_BANNER_SVG)}" alt="Sonder banner" />
              </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        dedent(
            """
            <div class="glass-card">
              <div class="hero-stat-grid">
                <div class="hero-stat">
                  <h3>4</h3>
                  <p>Active storefront offers in the main Sonder lineup right now.</p>
                </div>
                <div class="hero-stat">
                  <h3>1</h3>
                  <p>Reseller spotlight featuring Kitty Turtle's Valorant testing phase.</p>
                </div>
                <div class="hero-stat">
                  <h3>2</h3>
                  <p>Products showing as updating on the live status board.</p>
                </div>
                <div class="hero-stat">
                  <h3>$5</h3>
                  <p>Lifetime recoil scripts price shown directly in the storefront.</p>
                </div>
              </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )


def render_section_header(kicker: str, title: str, copy: str, anchor: str) -> None:
    st.markdown(
        dedent(
            f"""
            <div class="section-shell" id="{anchor}">
              <div class="section-kicker">{escape(kicker)}</div>
              <h2 class="section-title">{escape(title)}</h2>
              <p class="section-copy">{escape(copy)}</p>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )


def render_product_card(product: dict) -> str:
    prices = "".join(
        f'<div class="price-pill"><span>{escape(label)}</span><strong>{escape(value)}</strong></div>'
        for label, value in product["prices"].items()
    )
    return dedent(
        f"""
        <div class="product-card">
          <div class="product-badge">{escape(product["badge"])}</div>
          <div class="box-stage">
            <div class="box-3d">
              <div class="box-top"></div>
              <div class="box-spine"><span>{escape(product["box_label"])}</span></div>
              <div class="box-face">
                <img src="{svg_to_data_uri(product["svg"])}" alt="{escape(product["name"])} art"/>
              </div>
            </div>
          </div>
          <div class="product-title">
            <h3>{escape(product["name"])}</h3>
          </div>
          <div class="product-category">{escape(product["category"])}</div>
          <p class="product-desc">{escape(product["description"])}</p>
          <div class="price-row">{prices}</div>
          <a class="product-cta" href="{escape(product["url"])}">{escape(product["cta"])}</a>
        </div>
        """
    )


def render_store_tab() -> None:
    render_section_header(
        "Main Store",
        "Sonder Products",
        "Each product is presented as a floating 3D-style box with themed art, access tiers, and a direct call to action.",
        "store",
    )

    st.markdown(
        f'<div class="card-grid">{"".join(render_product_card(product) for product in PRODUCTS)}</div>',
        unsafe_allow_html=True,
    )

    r6 = PRODUCTS[0]
    features_html = "".join(f'<div class="feature-bullet">• {escape(feature)}</div>' for feature in r6["features"])
    st.markdown(
        dedent(
            f"""
            <div class="glass-card feature-panel">
              <div class="section-kicker">Feature Deep Dive</div>
              <h3 class="section-title" style="font-size:1.45rem;">{escape(r6["name"])} Feature List</h3>
              <p class="section-copy" style="margin-top:0.45rem;">
                Full Rainbow Six feature stack, matching the list you provided, organized into one premium panel.
              </p>
              <div class="feature-columns">
                {features_html}
              </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )


def render_reseller_tab() -> None:
    render_section_header(
        "Reseller",
        "Kitty Turtle Spotlight",
        "This section mirrors the same premium box layout but is dedicated to the reseller product and its current tester call.",
        "reseller",
    )

    st.markdown(
        f'<div class="card-grid">{"".join(render_product_card(product) for product in RESELLER_PRODUCTS)}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        dedent(
            f"""
            <div class="reseller-highlight">
              <div class="info-card">
                <h4>Sold By Kitty Turtle</h4>
                <p>
                  Valorant is listed as a reseller product and is currently still in development. The page calls that out clearly
                  so visitors know it is early-stage instead of fully launched.
                </p>
              </div>
              <div class="info-card">
                <h4>Tester Call Active</h4>
                <p>
                  Anyone interested in helping test can use the button on the product card or head to the reseller contact point:
                  <a class="sonder-pill-link" href="{RESELLER_DISCORD_URL}" style="display:inline-flex; margin-top:0.8rem;">Reseller Contact</a>
                </p>
              </div>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )


def render_status_tab() -> None:
    render_section_header(
        "Live Status",
        "Product Board",
        "Yellow means updating and red means not working. Per your request, only Rainbow Six and Valorant are marked as updating.",
        "status",
    )

    cards = []
    for name, status in STATUS_DATA.items():
        color = STATUS_COLORS[status]
        label = STATUS_LABELS[status]
        cards.append(
            dedent(
                f"""
                <div class="status-card">
                  <div class="status-name">
                    <span class="status-dot" style="color:{color}; background:{color};"></span>{escape(name)}
                  </div>
                  <div class="status-label">{escape(label)}</div>
                </div>
                """
            ).strip()
        )
    st.markdown(f'<div class="status-grid">{"".join(cards)}</div>', unsafe_allow_html=True)


def main() -> None:
    st.set_page_config(page_title="Sonder", page_icon="S", layout="wide")
    st.markdown(global_styles(), unsafe_allow_html=True)
    render_particle_background()
    render_nav()
    render_hero()

    tabs = st.tabs(["Store", "Reseller", "Status"])
    with tabs[0]:
        render_store_tab()
    with tabs[1]:
        render_reseller_tab()
    with tabs[2]:
        render_status_tab()

    st.markdown(
        dedent(
            """
            <div class="footer-note">
              Built in Streamlit for Sonder. Product links and placeholder prices can be swapped for your live Discord and exact amounts anytime.
            </div>
            """
        ),
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
