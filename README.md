# SeisPlotPy Desktop

SeisPlotPy Desktop is a fast, lightweight seismic viewer and analysis tool designed for 2D SEG-Y data.  
It enables interpreters, researchers, and students to load seismic profiles, visualize traces using efficient Qt/pyqtgraph rendering, perform attribute analysis, interactively pick horizons, and export publication-ready images.

---

## Key Features

- Load SEG-Y seismic lines (supports 2D single-line SEG-Y)
- Fast rendering using PyQt6 + PyQtGraph (no lag with thousands of traces)
- Geometry extraction & cumulative distance calculation
- Processing tools:
  - AGC
  - Bandpass Filtering
  - Envelope
  - Phase / Cosine Phase
  - RMS Amplitude
  - Instantaneous Frequency
- Interactive tools:
  - Zoom / Pan
  - Trace interval control
- Horizon Picking & Management:
  - Add multiple horizons
  - Lock to trace index or cumulative distance
  - Export horizons to CSV
- Export high-quality images (PNG, JPG, PDF)

---

## Installation

### Option 1 — Using Python (Developer Install)

```sh
git clone https://github.com/arjun-vh/SeisPlotPy-Desktop.git
cd SeisPlotPy-Desktop
pip install -r requirements.txt
python main.py
```

### Option 2 — Standalone Executable (Windows)

A portable .exe version (no Python required) is available under

Releases:
https://github.com/arjun-vh/SeisPlotPy-Desktop/releases/latest

Simply download, extract, and run:

## SEG-Y Support Notes

- Supported formats: .segy, .sgy
- Uses segyio backend for data access
- Assumes 2D single-line SEG-Y
- Multi-line or 3D cubes currently not supported

## Reporting Issues / Feature Requests

- Found something strange? Want a feature?
➡️ https://github.com/arjun-vh/SeisPlotPy-Desktop/issues

## Author & Contact

### Developed and maintained by:
- Arjun V H
- arjunvelliyidathu@gmail.com

## License

- This project is licensed under the GPL License
- See the LICENSE file for details

## Citation

If you use SeisPlotPy in your work, please acknowledge the software. Citation format will be added in a future release