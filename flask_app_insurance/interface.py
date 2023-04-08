from flask import Flask,jsonify,request,render_template
import config
from utilities import MedicalInsurance

app= Flask(__name__)

@app.route("/")
def app_home():
    return "Welcome to API Home"

@app.route("/predict_charges",methods=["POST","GET"])
def get_insurance_charges():

    if request.method == "POST":
        data = request.form
        print("***************************************************************************")
        print(data)
        print("****************************************************************************")
        age = float(data["age"])
        sex = data["sex"]
        bmi = float(data["bmi"])
        children = float(data["children"])
        smoker = data["smoker"]
        region = data["region"]

        med_insurance =MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges = med_insurance.get_predicted_charges()

        return jsonify({"Result": f"Medical Insurance Charges {charges}"})








if __name__ == "__main__":
    app.run(debug=True,port=config.PORT_NUMBER,host=config.HOST)

