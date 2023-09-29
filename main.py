from flask import Flask, request, render_template
import requests

app = Flask(__name__)
#1. Make the Project work without internet - Deployed to github if it helps
#2. Make the face change images when the robot is talking and make the face show up!!!
#3. Make the eyes blink


# Global AI variable
first = False
ai = None
get_data = None
# Function to classify text
def classify(text):
    key = "56ca0990-491b-11ee-8185-efa4bf132feb9f5030c9-d45f-40c4-b086-b103949476f4"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={"data": text})

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

# Function to update AI response
def response(label):
    global get_data
    if label == "Good":
        get_data = "Your Good"
    elif label == "Bad":
        get_data = "I am sorry, when i am sad, i like to draw a picture"
    else:
        get_data = "I don't understand."
@app.route('/')


@app.route('/', methods=['GET', 'POST'])
def home():
	global ai, get_data
	
	if request.method == 'POST':
			get_data = request.form.get('get')
			if get_data:
				recognize = classify(get_data)
				response(recognize["class_name"])
				print(get_data)
	return render_template("index.html", aichat = get_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

