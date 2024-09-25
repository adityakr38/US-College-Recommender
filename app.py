from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)


with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


df = pd.read_csv('college_data_new.csv') 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    
    weights = {
        'Admission_Rate': float(request.form['admission_rate']),
        'In-State_Tuition': float(request.form['in_state_tuition']),
        'Out-of-State_Tuition': float(request.form['out_state_tuition']),
        'Student_Size': float(request.form['student_size']),
        'Average_SAT_Score': float(request.form['sat_score']),
        'Median_Earnings_10_Years_After': float(request.form['median_earnings']),
        'Completion_Rate': float(request.form['completion_rate']),
        'Pell_Grant_Rate': float(request.form['pell_grant_rate']),
    }

    
    df['Ranking_Score'] = (
        df['Admission_Rate'] * weights['Admission_Rate'] +
        df['In-State_Tuition'] * weights['In-State_Tuition'] +
        df['Out-of-State_Tuition'] * weights['Out-of-State_Tuition'] +
        df['Student_Size'] * weights['Student_Size'] +
        df['Average_SAT_Score'] * weights['Average_SAT_Score'] +
        df['Median_Earnings_10_Years_After'] * weights['Median_Earnings_10_Years_After'] +
        df['Completion_Rate'] * weights['Completion_Rate'] +
        df['Pell_Grant_Rate'] * weights['Pell_Grant_Rate']
    )

   
    top_colleges = df.sort_values(by='Ranking_Score', ascending=False).head(10)
    return render_template('results.html', top_colleges=top_colleges.to_dict(orient='records'))

@app.route('/college/<college_name>')
def college_details(college_name):
    # Filter the dataframe to get the specific college
    college = df[df['College_Name'] == college_name].iloc[0]

    # Pass the college details to the college_details.html template
    return render_template('college_details.html', college=college)


if __name__ == '__main__':
    app.run(debug=True)
