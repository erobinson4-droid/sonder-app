from __future__ import annotations

import streamlit.components.v1 as components

from config import ACCENT, PARTICLE_COUNT, PARTICLE_LINK_DISTANCE, PARTICLE_MOUSE_RADIUS, PRIMARY


def render_particle_background() -> None:
    components.html(
        f"""
        <script>
          const parentDoc = window.parent.document;
          if (!parentDoc.getElementById("sonder-particle-canvas")) {{
            const canvas = parentDoc.createElement("canvas");
            canvas.id = "sonder-particle-canvas";
            canvas.style.position = "fixed";
            canvas.style.inset = "0";
            canvas.style.width = "100vw";
            canvas.style.height = "100vh";
            canvas.style.pointerEvents = "none";
            canvas.style.zIndex = "0";
            canvas.style.opacity = "0.95";
            parentDoc.body.appendChild(canvas);

            const ctx = canvas.getContext("2d");
            const root = window.parent;
            const mouse = {{ x: -9999, y: -9999 }};
            const dpr = root.devicePixelRatio || 1;
            const count = {PARTICLE_COUNT};
            const linkDistance = {PARTICLE_LINK_DISTANCE};
            const mouseRadius = {PARTICLE_MOUSE_RADIUS};
            const particles = Array.from({{ length: count }}, () => ({{
              x: Math.random() * root.innerWidth,
              y: Math.random() * root.innerHeight,
              vx: (Math.random() - 0.5) * 0.45,
              vy: (Math.random() - 0.5) * 0.45,
              size: Math.random() * 2.2 + 0.8,
            }}));

            const resize = () => {{
              canvas.width = root.innerWidth * dpr;
              canvas.height = root.innerHeight * dpr;
              ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
            }};

            const move = (event) => {{
              mouse.x = event.clientX;
              mouse.y = event.clientY;
            }};

            const leave = () => {{
              mouse.x = -9999;
              mouse.y = -9999;
            }};

            root.addEventListener("resize", resize);
            root.addEventListener("mousemove", move);
            root.addEventListener("mouseleave", leave);
            resize();

            const draw = () => {{
              ctx.clearRect(0, 0, root.innerWidth, root.innerHeight);

              for (let i = 0; i < particles.length; i += 1) {{
                const p = particles[i];
                const dx = mouse.x - p.x;
                const dy = mouse.y - p.y;
                const dist = Math.hypot(dx, dy);

                if (dist < mouseRadius) {{
                  const force = (mouseRadius - dist) / mouseRadius;
                  const angle = Math.atan2(dy, dx);
                  p.vx -= Math.cos(angle) * force * 0.028;
                  p.vy -= Math.sin(angle) * force * 0.028;
                }}

                p.x += p.vx;
                p.y += p.vy;
                p.vx *= 0.985;
                p.vy *= 0.985;

                if (p.x < 0 || p.x > root.innerWidth) p.vx *= -1;
                if (p.y < 0 || p.y > root.innerHeight) p.vy *= -1;
                p.x = Math.max(0, Math.min(root.innerWidth, p.x));
                p.y = Math.max(0, Math.min(root.innerHeight, p.y));

                const glow = Math.max(0, 1 - dist / mouseRadius);
                ctx.beginPath();
                ctx.fillStyle = glow > 0.08 ? "rgba(111, 255, 233, " + (0.16 + glow * 0.55) + ")" : "rgba(157, 77, 255, 0.36)";
                ctx.shadowBlur = glow > 0.08 ? 18 : 8;
                ctx.shadowColor = glow > 0.08 ? "{ACCENT}" : "{PRIMARY}";
                ctx.arc(p.x, p.y, p.size + glow * 1.8, 0, Math.PI * 2);
                ctx.fill();
              }}

              ctx.shadowBlur = 0;
              for (let i = 0; i < particles.length; i += 1) {{
                for (let j = i + 1; j < particles.length; j += 1) {{
                  const a = particles[i];
                  const b = particles[j];
                  const dx = a.x - b.x;
                  const dy = a.y - b.y;
                  const dist = Math.hypot(dx, dy);
                  if (dist < linkDistance) {{
                    const opacity = 1 - dist / linkDistance;
                    ctx.strokeStyle = "rgba(157, 77, 255, " + (opacity * 0.14) + ")";
                    ctx.lineWidth = 1;
                    ctx.beginPath();
                    ctx.moveTo(a.x, a.y);
                    ctx.lineTo(b.x, b.y);
                    ctx.stroke();
                  }}
                }}
              }}

              if (mouse.x > 0 && mouse.y > 0) {{
                const radial = ctx.createRadialGradient(mouse.x, mouse.y, 0, mouse.x, mouse.y, mouseRadius);
                radial.addColorStop(0, "rgba(111, 255, 233, 0.12)");
                radial.addColorStop(0.35, "rgba(157, 77, 255, 0.08)");
                radial.addColorStop(1, "rgba(0, 0, 0, 0)");
                ctx.fillStyle = radial;
                ctx.beginPath();
                ctx.arc(mouse.x, mouse.y, mouseRadius, 0, Math.PI * 2);
                ctx.fill();
              }}

              root.requestAnimationFrame(draw);
            }};

            draw();
          }}
        </script>
        """,
        height=0,
        width=0,
    )
