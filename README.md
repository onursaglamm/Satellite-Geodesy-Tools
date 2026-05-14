# Satellite-Geodesy-Tools

## Orbital Plane Position Solver (Python)

This project is a computational tool developed to determine the 2D coordinates of a satellite within its orbital plane. It bridges the gap between theoretical **Satellite Geodesy** and practical software implementation by using Keplerian elements to predict satellite motion.

### Key Features
- **Orbital Parameter Calculation:** Automatically computes the semi-major axis ($a$) using Kepler’s Third Law and the gravitational parameter ($GM$).
- **Numerical Iteration:** Implements an iterative method to solve the transcendental **Kepler Equation** ($M = E - e \sin E$) for the Eccentric Anomaly ($E$).
- **Time Parsing:** Includes a custom algorithm to process human-readable time formats (`HH:MM`) into astronomical time frames.
- **Accurate Coordinates:** Provides precise $x$ and $y$ coordinates in kilometers, along with the radius vector ($r$) for verification.

### How It Works
1. **Inputs:** User provides eccentricity ($e$), orbital period ($T$), time of perigee passage ($t_0$), and target time ($t$).
2. **Calculation:** The script computes Mean Motion ($n$), Mean Anomaly ($M$), and uses iteration for Eccentric Anomaly ($E$).
3. **Output:** Results are presented in kilometers for y-plane coordinates.
