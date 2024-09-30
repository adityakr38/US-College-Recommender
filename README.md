# US College Recommendation System

The US College Recommendation System is a machine learning-based web application that provides personalized recommendations for US colleges based on user preferences. The system allows users to input criteria such as admission rates, tuition costs, student size, SAT scores, and more, then ranks colleges accordingly.

## Features
### 1) User Input Form
A form where users can specify preferences for college features such as:
1. Admission Rate
2. In-State and Out-of-State Tuition
3. Student Size
4. Average SAT Score
5. Median Earnings after Graduation
6. Pell Grant Rate
7. Completion Rate

### 2) Machine Learning Model
The model ranks colleges based on the weighted preferences set by the user.

### 3) College Recommendations
The top 10 colleges that match the user’s criteria are displayed on the results page.

## Dataset

The dataset includes information about US colleges and its fetch from College ScoreCard API, such as:

1. Admission_Rate: Overall admission rate for the college
2. In-State_Tuition: Tuition fees for in-state students
3. Out-of-State_Tuition: Tuition fees for out-of-state students
4. Student_Size: Total number of students enrolled
5. Average_SAT_Score: Average SAT scores of admitted students
6. Median_Earnings_10_Years_After: 7. Median earnings of students 10 years after graduation
8. Completion_Rate: Graduation rate of the college
9. Pell_Grant_Rate: Percentage of students receiving Pell Grants

## Preprocessing
### Data Cleaning and Transformation:

1. Handling Missing Values: Missing data was imputed where necessary to ensure consistent input across features.
2. Outlier Detection: Outliers were detected and treated using IQR for certain columns such as Student_Size and Median_Earnings_10_Years_After. 
Z-score treatment and capping were applied to columns such as In-State_Tuition and Completion_Rate.
3. Scaling and Normalization: Features like Student_Size were transformed using log or reciprocal transformations to reduce skewness and ensure normal distribution.
4.Encoding: Categorical data such as city and state names were text-preprocessed and encoded.

## Installation

1. Clone the repository:


```bash
git clone https://github.com/your-username/us-college-recommendation.git
```
2. Navigate to the project directory:

```bash
cd us-college-recommendation
```

3. Create a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Run the Flask app:

```bash
python app.py
```

#### The application will run locally at http://127.0.0.1:5000/.

## Model Performance

Three machine learning models were trained and evaluated using the dataset:

```bash
Model	                      MSE	      MAE	    R2_Score
XGBoost	                17.537856	4.113250  -1001.401
Gradient Boosting       0.000235	0.010672	0.986550
Random Forest	          0.000712	0.020346	0.959278
```

Among the models, Gradient Boosting performed the best.

## Cross-Validation
To check model wasn't overfitting. The Gradient Boosting model was validated using 5-fold cross-validation (5CV), yielding the following R2 scores:

1. R2 Scores: [0.9837734, 0.98045765, 0.96996104, 0.9827855, 0.97999979]
2. Average R2: 0.9794

## Usage

1. Open the application in your browser.
2. Fill in the form with your college preferences.
3. Click on "Get Recommendations."
4. View the top 10 recommended colleges on the results page.

## Future Enhancements

1. Expanding the dataset with more features like student reviews, campus photos, and program-specific details.
2. Adding international colleges to the recommendation system.
3. Allowing users to compare multiple colleges based on their preferences.
