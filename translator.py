"""Import the translator service"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

URL_TRANS = ""

API_KEY_TRANS = ""

VERSION_TRANS = '2018-05-01'

authenticator = IAMAuthenticator(API_KEY_TRANS)
translator = LanguageTranslatorV3(version=VERSION_TRANS, authenticator=authenticator)
translator.set_service_url(URL_TRANS)


def english_to_french(texttobetranslated):
    """translate eng to french"""
    try:
        translation_response = translator.translate(text=texttobetranslated, model_id='en-fr')
        translation = translation_response.get_result()
        translated_text = translation['translations'][0]['translation']
    except ValueError:
        translated_text = "No text provided!"
    return translated_text


def english_to_german(texttobetranslated):
    """translate eng to german"""
    try:
        translation_response = translator.translate(text=texttobetranslated, model_id='en-de')
        translation = translation_response.get_result()
        translated_text = translation['translations'][0]['translation']
    except ValueError:
        translated_text = "No text provided!"
    return translated_text
