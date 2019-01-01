from flask import Flask, jsonify, render_template

app = Flask(__name__, static_url_path="/flag-status/static")

############################################################
# Homepage for flagstatus api
############################################################
@app.route("/flag-status", strict_slashes=False)
def home():
    """
    This function responds to the URL
    lab.seekup.nl/flag-status/

    :return:    the rendered template 'home.html'
    """
    return render_template('home.html')

############################################################
# List of available flags
############################################################
@app.route("/flag-status/flags.json")
@app.route("/flag-status/flags", strict_slashes=False)
def listFlags():
    """
    This function responds to the URL
    lab.seekup.nl/flag-status/flags

    :return:    json response with array of available flags
    """
    flagList = ["ms", "us"]
    
    return jsonify(
        flags   = flagList,
        message = "success"
    )

############################################################
# United States flag
############################################################
@app.route("/flag-status/flags/us.json")
@app.route("/flag-status/flags/us", strict_slashes=False)
def usFlag():
    """
    This function responds to the URL
    lab.seekup.nl/flag-status/flags/us/

    :return:    json response with status of US flag
    """
    return jsonify(
        half_staff = False,
        until      = "indefinitely",
        reason     = "normal operations",
        message    = "success"
    )

############################################################
# Mississippi flag
############################################################
@app.route("/flag-status/flags/ms.json")
@app.route("/flag-status/flags/ms", strict_slashes=False)
def msFlag():
    """
    This function responds to the URL
    lab.seekup.nl/flag-status/flags/ms/

    :return:    json response with status of MS flag
    """
    return usFlag(); # mirror US flag
#   return jsonify(
#       half_staff = False,
#       until      = "",
#       reason     = "",
#       message    = ""
#   )
