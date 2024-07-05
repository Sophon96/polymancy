### polymancy: Polystyrene Film Thickness and Molecular Weight Predictor for the Garcia Research Program 2024

**polymancy** is a Python package developed for the Garcia Research Program 2024, designed to predict the thickness of spin-coated polystyrene films based on the molecular weight and concentration of the polymer solution. Additionally, it can determine the molecular weight of the polymer from the measured film thickness and known concentration. This package leverages advanced regression techniques, including polynomial regression and machine learning algorithms, to establish a precise mathematical relationship between these variables, providing researchers with powerful tools for their experimental and analytical needs.

#### Key Features

- Predict the thickness of the resulting spin-coated film given the molecular weight and concentration of the polystyrene solution
- Determine the molecular weight of the polystyrene from the measured thickness of the film and the known concentration of the solution
- Utilize robust regression methods, including polynomial regression, ridge regression, and random forest regression
- Grid search and cross-validation to optimize model parameters and improve prediction accuracy
- Simple and intuitive API for integrating with existing research workflows and data analysis pipelines

#### Usage

I recommend running this locally, as it's easier to customize and test. Here's a step-by-step guide to get you started:

If you're developing or using the package locally, navigate to the directory containing `setup.py` and install it:

```bash
pip install .
```

Ensure your data is in a CSV format with the following structure:

```plaintext
Concentration,192K (Å),192K Err (Å),30K (Å),30K Err (Å),50K (Å),50K Err (Å),...
10,499.5,0.7071067812,52.183333,0.666432,54.483333,1.296583,...
15,1052.0,158.391919,80.166667,0.691423,85.300000,1.195439,...
20,1290.0,46.66904756,108.650000,1.647450,112.983333,1.173184,...
25,1691.0,103.2375901,139.950000,1.553849,150.200000,3.059526,...
30,2215.5,70.00357134,172.983333,3.240988,182.466667,2.004360,...
```

The first row should contain the column names. Currently, this package aims to predict the thickness of the resulting film, so the first column should contain the molecular weight and the second column should contain the concentration. In the future, this package will support predicting the molecular weight from the thickness and concentration too.

After loading the data, you can load, preprocess, and test the sample data `data/192k.csv` using `test/test_predict_thickness.py`:

```bash
python test/test_predict_thickness.py
```

You can also load and preprocess the data using the `load_data` and `preprocess_data` functions in the `polymancy.utils` module. However, toy with this as you see fit.
