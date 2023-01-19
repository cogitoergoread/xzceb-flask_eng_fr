"""Translation to/from english / french"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
print(apikey)
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def translate_a_b(to_translate, model):
    """Translate to_translate as model"""
    if len(to_translate) == 0:
        return ""
    translation = language_translator.translate(
        text=to_translate,
        model_id=model).get_result()
    if len(translation['translations'])>0:
        return translation['translations'][0]['translation']
    return ""


def englishToFrench(englishText):
    """Translate from english to french"""
    #write the code here
    return translate_a_b(englishText, 'en-fr')

def frenchToEnglish(frenchText):
    """Transate from french to english"""
    #write the code here
    return translate_a_b(frenchText, 'fr-en')
