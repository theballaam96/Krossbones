
<div align="center" style="text-align:center">
  <img src="https://raw.githubusercontent.com/theballaam96/Krossbones/refs/heads/main/krossbones.png" alt="Krossbones">
</div>

# Krossbones

Krossbones is a KROSS-platform bareBONES autotracker for **DK64 Randomizer**. It focuses solely on tracking items you have obtained, providing a lightweight and reliable solution for Linux users who are waiting for cross-platform updates from [Track-o-Matic](https://github.com/Brian0255/Track-O-Matic) and [GSTHD](https://github.com/jxjacob/GSTHD).

---

## Features

- Tracks **collected items** in DK64 Randomizer in real-time.
- Works on **Linux and Windows** (Probably Mac too).
- Stores UI Scale, color pad/barrel icon preferences and background color for your tracker.

---

## Installation

### Requirements

- Python 3.10+
- `pip` package manager
- Dependencies listed in `requirements.txt`

### Steps

1. Clone the repository:

```bash
git clone https://github.com/theballaam96/Krossbones.git
cd Krossbones
```

2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Run Krossbones:

```bash
python krossbones.py
```

With linux, there is a helper `run_linux.sh` file should it be necessary.