"""Dependency and numerical checks; requires the installed research environment."""
import importlib
import json
import os
import tempfile
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")
modules = ["numpy", "scipy", "matplotlib", "pandas", "sympy", "control",
           "pymupdf", "pypdf", "docx", "openpyxl", "pytest", "ipykernel", "nbformat"]
for name in modules:
    importlib.import_module(name)

import numpy as np
from scipy.integrate import solve_ivp
import control
import matplotlib.pyplot as plt
from pypdf import PdfReader, PdfWriter

# Synthetic first-order yaw-rate step response, not a calibrated vessel model.
# T dr/dt + r = K delta, r(0)=0; compare integration with its analytic solution.
T, K, delta = 5.0, 0.2, 0.1
t = np.linspace(0.0, 30.0, 301)
sol = solve_ivp(lambda time, y: [(K * delta - y[0]) / T],
                (t[0], t[-1]), [0.0], t_eval=t, rtol=1e-9, atol=1e-11)
assert sol.success, sol.message
expected = K * delta * (1.0 - np.exp(-t / T))
np.testing.assert_allclose(sol.y[0], expected, rtol=1e-6, atol=1e-9)
assert np.all(np.real(control.poles(control.tf([K], [T, 1]))) < 0)

with tempfile.TemporaryDirectory() as scratch:
    path = Path(scratch)
    plt.plot(t, sol.y[0])
    plt.savefig(path / "yaw_response.png")
    plt.close()
    assert (path / "yaw_response.png").stat().st_size > 0
    writer = PdfWriter()
    writer.add_blank_page(width=595, height=842)
    with (path / "check.pdf").open("wb") as stream:
        writer.write(stream)
    assert len(PdfReader(path / "check.pdf").pages) == 1

print(json.dumps({"result": "PASS", "imports": modules,
                  "checks": ["analytic yaw response", "stable transfer function",
                             "headless plot export", "PDF round trip"]}, indent=2))
