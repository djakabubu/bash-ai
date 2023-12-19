import googletrans
SELECTED_LANGUAGE = "it"
def AutoTranslate(text):
    translator = googletrans.Translator()
    translation = translator.translate(text, dest=SELECTED_LANGUAGE)
    return translation.text

AutoTranslate("hello guys")