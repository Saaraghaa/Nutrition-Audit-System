!pip install pandas numpy
import pandas as pd
import numpy as np
#Define Data Structures
# Sample data for users
users = pd.DataFrame({
    'user_id': [1, 2],
    'name': ['Alice', 'Bob'],
    'age': [30, 25],
    'height_cm': [165, 175],
    'weight_kg': [68, 75]
})

# Sample data for nutrition records
nutrition_records = pd.DataFrame({
    'user_id': [1, 1, 2],
    'date': ['2023-01-01', '2023-01-02', '2023-01-01'],
    'meal': ['breakfast', 'lunch', 'breakfast'],
    'calories': [300, 500, 350],
    'protein_g': [15, 25, 20],
    'carbs_g': [50, 75, 55],
    'fats_g': [10, 20, 15]
})

# Sample data for goals
goals = pd.DataFrame({
    'user_id': [1, 2],
    'goal': ['Lose 5 kg', 'Gain 3 kg'],
    'start_date': ['2023-01-01', '2023-01-01'],
    'end_date': ['2023-06-01', '2023-04-01'],
    'status': ['in_progress', 'in_progress']
})

#Define Functions for User Operations
#Add New User
def add_user(users, name, age, height_cm, weight_kg):
    new_user_id = users['user_id'].max() + 1
    new_user = pd.DataFrame({
        'user_id': [new_user_id],
        'name': [name],
        'age': [age],
        'height_cm': [height_cm],
        'weight_kg': [weight_kg]
    })
    users = pd.concat([users, new_user], ignore_index=True)
    return users
#Add Nutrition Record
def add_nutrition_record(nutrition_records, user_id, date, meal, calories, protein_g, carbs_g, fats_g):
    new_record = pd.DataFrame({
        'user_id': [user_id],
        'date': [date],
        'meal': [meal],
        'calories': [calories],
        'protein_g': [protein_g],
        'carbs_g': [carbs_g],
        'fats_g': [fats_g]
    })
    nutrition_records = pd.concat([nutrition_records, new_record], ignore_index=True)
    return nutrition_records
#Set Nutrition Goal
def set_goal(goals, user_id, goal, start_date, end_date):
    new_goal = pd.DataFrame({
        'user_id': [user_id],
        'goal': [goal],
        'start_date': [start_date],
        'end_date': [end_date],
        'status': ['in_progress']
    })
    goals = pd.concat([goals, new_goal], ignore_index=True)
    return goals
#Get User Summary
def get_user_summary(users, nutrition_records, goals, user_id):
    user = users[users['user_id'] == user_id].iloc[0]
    user_nutrition = nutrition_records[nutrition_records['user_id'] == user_id]
    user_goals = goals[goals['user_id'] == user_id]
    
    summary = {
        'user_info': user.to_dict(),
        'nutrition_records': user_nutrition.to_dict(orient='records'),
        'goals': user_goals.to_dict(orient='records')
    }
    return summary
#Example
# Add a new user
users = add_user(users, 'Charlie', 28, 180, 80)

# Add a new nutrition record
nutrition_records = add_nutrition_record(nutrition_records, 1, '2023-01-03', 'dinner', 600, 30, 80, 20)

# Set a new goal
goals = set_goal(goals, 1, 'Run a marathon', '2023-02-01', '2023-08-01')

# Get user summary
user_summary = get_user_summary(users, nutrition_records, goals, 1)
print(user_summary)
