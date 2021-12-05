import numpy as np
from flask import Flask, request,jsonify, render_template
import pickle



# Create flask app
flask_app =Flask(__name__, template_folder='templates')
model = pickle.load(open("model.pkl", "rb"))


@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    int_features=[0]*18

    i_features = [int(x) for x in request.form.values()]

    # int_features= i_features[:3] + int_features
    # views, i_features=i_features[:3] , i_features[3:]
    #
    for i in i_features[3:]:
        int_features[i]=1
    i_features=i_features[:3]+ int_features
    #
    #
    #
    #
    final_features=np.array(i_features).reshape(1,-1)
    # # print(i_features)
    # print(int_features)
    #
    prediction = model.predict(final_features)
    output=round(prediction[0],0)


    # print(prediction)
    return render_template("index.html", prediction_text="Predicted number of likes:  {}".format(output))

# @flask_app("/predict_api", methods=["POST"])
# def predict_api():
#
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])
#
#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    flask_app.run(debug=True)


















# import numpy as np
# from flask import Flask, app, request, render_template
# import pickle
#
# import model
#
# # Create flask app
# app = Flask(__name__)
# # model = pickle.load(open("model.pkl", "rb"))
#
# @app.route("/", method=["GET","POST"])
# def hello():
#     if request.method=="POST":
#         hrs=request.form['hrs']
#         marks=model.like_prediction(hrs)
#         print(marks)
#     return render_template("index.html")
#
# # @app.route("/sub", methods=['POST'])
# # def submit():
# #     if request.method=="POST":
# #         name=request.form["username"]
# #         # lname=request.form["lname"]
# #     return render_template("sub.html", n=name)
#
# # def Home():
# #     return render_template("index.html")
#
# # @flask_app.route("/predict", methods = ["POST"])
# # def predict():
# #     float_features = [float(x) for x in request.form.values()]
# #     features = [np.array(float_features)]
#
# #     prediction = model.predict(features)
# #     return render_template("index.html", prediction_text = "The flower species is {}".format(prediction))
#
# if __name__ == "__main__":
#     app.run(debug=True)