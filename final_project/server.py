from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text=translator.englishToFrench(textToTranslate)
    app.logger.debug(f"E2F To:{textToTranslate}, Transated:{translated_text}")
    return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text=translator.frenchToEnglish(textToTranslate)
    app.logger.debug(f"F2E To:{textToTranslate}, Transated:{translated_text}")
    return translated_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
