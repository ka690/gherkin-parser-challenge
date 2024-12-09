import json
from flask import Flask, Response, request, jsonify
from werkzeug.utils import secure_filename
from Errors.ParsingError import ParsingError
from Gherkin.GherkinParser import GherkinParser
import argparse

# Get arguments from shell
argParser = argparse.ArgumentParser()
# Arg to run flask in debug
argParser.add_argument('--debug', action='store_true', default=False)
args = argParser.parse_args()

app = Flask(__name__)

# Setup for file upload
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB
ALLOWED_EXTENSIONS = {'feature'}

# To stop jsonify from sorting the props
app.json.sort_keys = False

def ProblemJsonResponse(title, detail, code) -> Response:
    return jsonify({
        "title" : title,
        "detail" : detail,
        "code" : code,
    }), code
    
def ParseGherkinData(featureText):
    gherkinParser = GherkinParser(debug=args.debug)
    abstractSyntaxTree = gherkinParser.parse(featureText)
    return abstractSyntaxTree

@app.route('/gherkin/parse', methods=['POST'])
def GherkinParse():
    try:
        featureText = request.get_data().decode('utf-8')
        if not featureText:
            return jsonify({
                "title" : "badRequest",
                "detail" : "No data to parse in request!",
                "code" : 400,
            }), 400

        return jsonify(ParseGherkinData(featureText)), 200

    except ParsingError as ex:
        return ProblemJsonResponse(title="parsingError", detail=str(ex), code=400)

    except Exception as ex:
        return ProblemJsonResponse(title="internalServerError", detail=str(ex), code=500)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/gherkin/parse/upload', methods=['POST'])
def GherkinParseUpload():
    if 'file' not in request.files:
        return ProblemJsonResponse(title="noFile", detail="No file provided.", code=400)

    file = request.files['file']

    if file.filename == '':
        return ProblemJsonResponse(title="noFileSelected", detail="No file selected.", code=400)
    
    if not file:
        return ProblemJsonResponse(title="noFile", detail="No file provided.", code=400)
    
    if not allowed_file(file.filename):
        return ProblemJsonResponse(title="fileNotAllowed", detail="File type not allowed.", code=400)

    try:
        featureText = file.read().decode('utf-8')
        filename = secure_filename(file.filename)
        return jsonify(ParseGherkinData(featureText)), 200
    except Exception as ex:
        return ProblemJsonResponse(title="internalServerError", detail=str(ex), code=500)

app.run(debug=args.debug)
