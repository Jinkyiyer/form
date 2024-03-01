from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)



MYSQL_HOST = os.environ.get("MYSQL_HOST", "127.0.0.1")
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "Venkatesh@10")
MYSQL_DB = os.environ.get("MYSQL_DB", "vaish")

# Connect to MySQL
# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="Venkatesh@10",
#     database="vaish",
#     port="3306"


# Connect to MySQL using environment variables
mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB,
    port="3306"  # The port inside the container
)


# Create a cursor
mycursor = mydb.cursor()

# Modify the table creation SQL statement to include 'opinion_religion_atheism'

# Modify the table creation SQL statement to include 'opinion_religion_atheism'
# Modify the table creation SQL statement to include 'opinion_religion_atheism'
mycursor.execute(
    """
    CREATE TABLE IF NOT EXISTS vai (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        address VARCHAR(255),
        dob DATE,
        phone_number VARCHAR(20),
        qualification VARCHAR(255),
        college_name VARCHAR(255),
        college_address VARCHAR(255),
        percentage VARCHAR(10),
        total_marks VARCHAR(10),
        currently_studying VARCHAR(10),
        study_details TEXT,
        college_address_current VARCHAR(255),
        admission_date DATE,
        completion_date DATE,
        recent_percentage VARCHAR(10),
        recent_total_marks VARCHAR(10),
        currently_working VARCHAR(10),
        current_work_experience VARCHAR(255),
        organization_name VARCHAR(255),
        joining_date DATE,
        organization_address VARCHAR(255),
        previous_organization VARCHAR(10),
        previous_organization_name VARCHAR(255),
        previous_joining_date DATE,
        last_working_date DATE,
        previous_organization_address VARCHAR(255),
        other_previous_organization_names TEXT,
        total_work_experiences VARCHAR(10),
        favorite_color VARCHAR(255),
        favorite_food VARCHAR(255),
        favorite_movie_tv_show VARCHAR(255),
        favorite_actor_actress VARCHAR(255),
        favorite_book VARCHAR(255),
        favorite_music_artists VARCHAR(255),
        favorite_traveling_activity VARCHAR(255),
        favorite_god VARCHAR(255),
        favorite_person VARCHAR(255),
        favorite_dress VARCHAR(255),
        favorite_gifts VARCHAR(255),
        favorite_songs VARCHAR(255),
        favorite_singers VARCHAR(255),
        interests_hobbies TEXT,
        favorite_free_time VARCHAR(255),
        dream_vacation VARCHAR(255),
        goals_aspirations TEXT,
        dreams_pursuing VARCHAR(255),
        career_aspirations VARCHAR(255),
        opinions_topics TEXT,
        opinion_feminism VARCHAR(255),
        opinion_male_rights VARCHAR(255),
        opinion_politics VARCHAR(255),
        opinion_hinduism VARCHAR(255),
        opinion_religion_atheism VARCHAR(255),
        opinion_mr_venky VARCHAR(255),
        preference_dogs_or_cats VARCHAR(255),
        personal_question_male_best_friend VARCHAR(255),
        personal_question_female_best_friend VARCHAR(255),
        personal_question_brother_details TEXT,
        personal_question_father_details TEXT,
        personal_question_properties_owned TEXT,
        personal_question_annual_income VARCHAR(255),
        personal_question_vehicles_owned TEXT,
        personal_question_favorite_family_member VARCHAR(255),
        personal_question_type_of_boys_like VARCHAR(255)
    )
    """
)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = request.form

        # Convert empty strings to None
        data = {key: (None if value == '' else value) for key, value in data.items()}

        # Insert data into MySQL
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        sql = f"INSERT INTO vai ({columns}) VALUES ({placeholders})"
        val = tuple(data.values())

        try:
            mycursor.execute(sql, val)
            mydb.commit()
            return 'Form submitted successfully!'
        except mysql.connector.Error as err:
            return f"Error: {err}"


from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


