# KNN Rice Classifier

A small k-nearest-neighbors experiment on the Cammeo and Osmancik rice dataset.

## Code guide

`Normalize.py` loads `Rice_Cammeo_Osmancik.xlsx` and standardizes features. `Classifier.py` computes distances and predicts a class for the sample configured in that script. `Data_Show.py` prints dataset summaries, and `Plot.py` draws sample plots. Install pandas, NumPy, Matplotlib, `openpyxl`, and `texttable` as needed, then run the chosen script from the repository root. `Classifier.py` calls its `start()` function when executed.
