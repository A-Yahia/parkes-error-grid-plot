# Parkes Error Grid

This repository contains a Python script (`parke_error_grid.py`) that generates a Parkes Error Grid for comparing reference (true) blood glucose concentrations against predicted values. The Parkes Error Grid provides a visual representation of the accuracy of blood glucose monitoring and prediction systems in terms of clinically acceptable zones.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Example](#example)
6. [Visualization](#visualization)
7. [License](#license)

---

## Overview

The **Parkes Error Grid** (also known as the **Consensus Error Grid** for Type 1 diabetes) is used to categorize the clinical significance of the difference between reference glucose measurements and those obtained from a device or prediction model. The grid is divided into different zones (A, B, C, D, and E), each indicating a range of clinical accuracy and the potential for erroneous treatment decisions.

This script:
- Plots reference (true) blood glucose values on the x-axis.
- Plots predicted blood glucose values on the y-axis.
- Draws the Parkes Error Grid zones (A-E) using dashed lines.
- Highlights zone areas by labeling them (A, B, C, D, E).

---

## Features

- **Straightforward API**: A single function `parke_error_grid` takes two NumPy arrays (reference and predicted values) and a title string.
- **Customizable Plot**: You can easily adjust titles, labels, axis limits, and styles as needed.
- **Zone Demarcation**: Pre-drawn boundaries for Parkes Error Grid (Type 1) zones A, B, C, D, and E.

---

## Installation

1. **Clone this repository** (if using Git):
   ```bash
   git clone https://github.com/your-username/parkes-error-grid.git
   cd parkes-error-grid
   ```

2. **Install dependencies**:
   - [NumPy](https://numpy.org/) for handling arrays.
   - [Matplotlib](https://matplotlib.org/) for plotting.
   
   You can install them using `pip`:
   ```bash
   pip install numpy matplotlib
   ```

---

## Usage

1. **Import the function** in your Python script:
   ```python
   from parke_error_grid import parke_error_grid
   ```

2. **Prepare your data** as NumPy arrays:
   ```python
   import numpy as np

   ref_values = np.array([ ... ])  # Replace with actual reference data
   pred_values = np.array([ ... ]) # Replace with your predictions
   ```

3. **Generate the Parkes Error Grid plot**:
   ```python
   parke_error_grid(ref_values, pred_values, "My Model Predictions")
   ```

4. **Show or save the plot**:
   ```python
   import matplotlib.pyplot as plt

   plt.show()  # To display the plot
   ```
   Or
   ```python
   plt.savefig("my_parkes_error_grid.png", dpi=300)
   ```

---

## Example

Below is a simple example included at the bottom of the script:

```python
if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt

    # Example reference and predicted values
    ref_values = np.array([50, 100, 150, 200, 250, 300, 350, 400])
    pred_values = np.array([60, 110, 140, 190, 260, 290, 340, 410])

    # Generate and display the Parkes Error Grid
    parke_error_grid(ref_values, pred_values, "Test")
    plt.show()
```

Running:
```bash
python parke_error_grid.py
```
will generate and display a window with the Parkes Error Grid labeled zones.

---

## Visualization

When you run the script or call the `parke_error_grid` function, you will see a plot that:
- Shows a scatter plot of your (reference, predicted) data points.
- Outlines zones A, B, C, D, and E using dashed lines.
- Labels these zones clearly on the plot.

**Zone Meanings (High-Level)**:
- **Zone A**: Clinically accurate measurements; no effect on clinical action.
- **Zone B**: Data that deviate slightly from Zone A but would not lead to significant clinical error.
- **Zone C**: Data could lead to clinical action that is not optimal but likely not harmful in an immediate sense.
- **Zone D**: Data could lead to dangerous treatment errors.
- **Zone E**: Data could lead to erroneous treatment with significant risk to the patient.

---

## License

This project is provided under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and integrate it into your own projects as needed.
