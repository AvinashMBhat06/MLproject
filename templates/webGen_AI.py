import openai 
import webbrowser
from IPython.display import display, HTML
def html_generator(response,file_path):
    with open(file_path,"w") as file:
        file.write(response)
    webbrowser.open(file_path)
openai.api_key ="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"
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
# prompt_1= f""" using html tags write the code for asthetic looking website containing a heading 'Predictor' and a button
# that will transfer the user to new webpage with url '/predictions' ,use css to beautify the website'''
#response=get_completion(prompt)

prompt= f"""html>
"<body>
    <div class="login">
       <h1>Student Exam Performance Indicator</h1>

       <form action="{{ url_for('predict_datapoint')}}" method="post">
        <h1>
            <legend>Student Exam Performance Prediction</legend>
        </h1>
        <div class="mb-3">
            <label class="form-label">Gender</label>
            <select class="form-control" name="gender" placeholder="Enter you Gender" required>
                <option class="placeholder" selected disabled value="">Select your Gender</option>
                <option value="male">
                    Male
                </option>
                <option value="female">
                    Female
                </option>
            </select>
        </div>
        <div class="mb-3">
            <label class="form-label">Race or Ethnicity</label>
            <select class="form-control" name="ethnicity" placeholder="Enter you ethnicity" required>
                <option class="placeholder" selected disabled value="">Select Ethnicity</option>
                <option value="group A">
                    Group A
                </option>
                <option value="group B">
                    Group B
                </option>
                <option value="group C">
                    Group C
                </option>
                <option value="group D">
                    Group D
                </option>
                <option value="group E">
                    Group E
                </option>
            </select>
        </div>
        <div class="mb-3">
            <label class="form-label">Parental Level of Education</label>
            <select class="form-control" name="parental_level_of_education"
                placeholder="Enter you Parent Education" required>
                <option class="placeholder" selected disabled value="">Select Parent Education</option>
                <option value="associate's degree">
                    associate's degree
                </option>
                <option value="bachelor's degree">
                    bachelor's degree
                </option>
                <option value="high school">
                    high school
                </option>
                <option value="master's degree">
                    master's degree
                </option>
                <option value="some college">
                    some college
                </option>
                <option value="some high school">
                    some high school
                </option>
            </select>
        </div>
        <div class="mb-3">
            <label class="form-label">Lunch Type</label>
            <select class="form-control" name="lunch" placeholder="Enter you Lunch" required>
                <option class="placeholder" selected disabled value="">Select Lunch Type</option>
                <option value="free/reduced">
                    free/reduced
                </option>
                <option value="standard">
                    standard
                </option>
            </select>
        </div>
        <div class="mb-3">
            <label class="form-label">Test preparation Course</label>
            <select class="form-control" name="test_preparation_course" placeholder="Enter you Course"
                required>
                <option class="placeholder" selected disabled value="">Select Test_course</option>
                <option value="none">
                    None
                </option>
                <option value="completed">
                    Completed
                </option>
            </select>
        </div>
        <div class="mb-3">
            <label class="form-label">Writing Score out of 100</label>
            <input class="form-control" type="number" name="reading_score"
                placeholder="Enter your Reading score" min='0' max='100' />
        </div>
        <div class="mb-3">
            <label class="form-label">Reading Score out of 100</label>
            <input class="form-control" type="number" name="writing_score"
                placeholder="Enter your Reading Score" min='0' max='100' />
        </div>
        <div class="mb-3">
            <input class="btn btn-primary" type="submit" value="Predict your Maths Score" required />
        </div>
    </form>
    <h2>
       THE  prediction is {{results}}
    </h2>
   <body>
</html>"

keeping the same place holder namer can you modify the html for me and beautify the webpage using css tags too ,add buttons where ever necessary
"""
response=get_completion(prompt)
html_generator(response,"home.html") 
print("dne")