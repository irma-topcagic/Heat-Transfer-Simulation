# 🌡️ Heat Transfer Simulation between Two Bodies

## 📌 Project Overview
This project is a numerical simulation of the heat exchange process between two physical bodies. It was developed as part of a seminar paper at the **Faculty of Electrical Engineering, University of Sarajevo**. The simulation focuses on tracking temperature changes over time until thermodynamic equilibrium is reached.

---

## 🧪 Theoretical Background & Mathematical Model
The simulation is based on the fundamental laws of thermodynamics, including:
* **Thermal Conductivity:** Analysis of heat transfer through contact surfaces.
* **Law of Conservation of Energy:** The energy released by one body is absorbed by the other (assuming a closed system).
* **Time-Step Modeling:** Modeling the rate of temperature change based on the heat capacity ($c$) and mass ($m$) of the bodies.

### Key Model Assumptions:
1. **Homogeneity:** The temperature within each body is uniform at any given moment.
2. **Closed System:** Heat loss to the environment is neglected.
3. **Constant Parameters:** Specific heat capacities and heat transfer coefficients remain constant throughout the process.

---

## 🚀 Simulation Scenarios
The project includes different physical scenarios to analyze various outcomes:

* **Scenario A (Symmetric Thermal Masses):** Both bodies have the same thermal capacity ($C_1 = C_2$), resulting in an equilibrium temperature exactly at the midpoint of the initial values.
* **Scenario B1 & B2 (Significant Mass Difference):** Analysis of cases where one body is much more massive or has a significantly higher specific heat capacity ($C_1 >> C_2$). This simulates the cooling or heating of a smaller object with minimal temperature change in the larger body.

---

## 🛠 Tech Stack
* **Language:** Python
* **Libraries:** * `NumPy`: For numerical calculations and array handling.
  * `Matplotlib`: For generating temperature change graphs.
* **Tools:** Visual Studio Code / Jupyter Notebook.

---

## 📈 Results & Visualization
The simulation generates visual representations showing:
1. The exponential temperature decay of the warmer body.
2. The temperature rise of the cooler body.
3. The intersection point and asymptotic approach to the equilibrium temperature.
