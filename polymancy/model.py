from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import mean_squared_error


class PolyFilmModel:
    """
    A class used to represent a model for predicting polystyrene film thickness
    and molecular weight.
    """

    def __init__(self):
        """
        Initialize the PolyFilmModel.
        """
        self.model = None
        self.inverse_model = None
        self.poly = PolynomialFeatures(degree=2)

    def train(self, x_data, y_data):
        """
        Train the model using polynomial regression and ridge regularization.

        Parameters:
        x_data (array-like): Input features (molecular weight and concentration).
        y_data (array-like): Target values (thickness in nm).
        """
        # Create polynomial features
        x_poly = self.poly.fit_transform(x_data)

        # Train-test split
        x_train, x_test, y_train, y_test = train_test_split(
            x_poly, y_data, test_size=0.2, random_state=42
        )

        # Hyperparameter tuning for Ridge Regression
        ridge = Ridge()
        params = {"alpha": [0.1, 1.0, 10.0, 100.0]}
        grid_search = GridSearchCV(
            ridge, param_grid=params, scoring="neg_mean_squared_error", cv=5
        )
        grid_search.fit(x_train, y_train)

        # Store the best model
        self.model = grid_search.best_estimator_
        print(f"Best parameters for Ridge: {grid_search.best_params_}")
        print(f"Best cross-validation MSE: {-grid_search.best_score_}")

        # Evaluate on test set
        test_mse = mean_squared_error(y_test, self.model.predict(x_test))
        print(f"Test MSE: {test_mse}")

    def predict_thickness(self, molecular_weight, concentration):
        """
        Predict the film thickness given molecular weight and concentration.

        Parameters:
        molecular_weight (float): Molecular weight of the polymer.
        concentration (float): Concentration of the polymer solution.

        Returns:
        float: Predicted thickness in nm.
        """
        x_input = self.poly.transform([[molecular_weight, concentration]])
        return self.model.predict(x_input)[0]

    def evaluate(self, x_data, y_data):
        """
        Evaluate the model using cross-validation.

        Parameters:
        x_data (array-like): Input features (molecular weight and concentration).
        y_data (array-like): Target values (thickness in nm).

        Returns:
        tuple: Mean and standard deviation of the cross-validation MSE.
        """
        x_poly = self.poly.transform(x_data)
        scores = cross_val_score(
            self.model, x_poly, y_data, cv=5, scoring="neg_mean_squared_error"
        )
        return -scores.mean(), -scores.std()
