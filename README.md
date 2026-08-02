# Hardware-Protocol-Diagnostics-PyTest


# Automated Hardware Functional Test & Protocol Diagnostics Tool

## 📌 Overview
This project is a Python-based test automation framework designed to simulate, validate, and diagnose communication across standard hardware interfaces (I2C and SPI). It utilizes **PyTest** to structure functional verification routines and automate board-level fault isolation, generating actionable diagnostic reports for hardware debugging.

## 🚀 Key Features
* **Protocol Simulation:** Mocks I2C and SPI hardware interfaces to validate test script logic without requiring physical hardware.
* **Automated Fault Isolation:** Identifies specific component-level failures (e.g., unresponsive SPI Flash Memory or faulty I2C Temperature Sensors).
* **Diagnostic Error Logging:** Automatically generates a `diagnostic_failures.log` file capturing precise timestamps, expected vs. actual hexadecimal values, and component reference designators to accelerate root-cause analysis.
* **PyTest Integration:** Uses PyTest fixtures for clean setup/teardown processes in a simulated manufacturing test environment.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Framework:** PyTest
* **Libraries:** `logging`, `pytest`

## ⚙️ How to Run
1. Clone this repository to your local machine.
2. Install PyTest if you haven't already:
   ```bash
   pip install pytest
