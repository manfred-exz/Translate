# -*- coding: utf-8 -*-
import webbrowser
from textblob import TextBlob, exceptions
from wox import Wox, WoxAPI
import enchant
import win32com.client as wincl

METHOD = 'ms'
LANGUAGE = 'zh-CN'
d = enchant.Dict('en_US')
speak = wincl.Dispatch("SAPI.SpVoice")


def is_words(text):
    words = text.split(sep=' ')
    return all(d.check(word) for word in words)


def speak_it(text):
    speak.Speak(text)


class Translate(Wox):
    def query(self, query):
        wanna_speak = query.endswith('\'')
        if wanna_speak:
            query = query[:-1]

        query_modified = query.strip().lower()
        en = set(chr(i) for i in range(ord('a'), ord('z') + 1))
        results = []
        if query_modified:
            try:
                from_lang, to_lang = ('en', LANGUAGE) if query_modified[0] in en else (LANGUAGE, 'en')
                translation = TextBlob(query_modified).translate(from_lang, to_lang)
                results.append({
                    "Title": str(translation),
                    "SubTitle": query,
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {'method': 'openUrl',
                                      'parameters': [
                                          r'http://translate.google.com/#{}/{}/{}'.format(from_lang, to_lang,
                                                                                          query)],
                                      'dontHideAfterAction': False}
                })
                if wanna_speak and is_words(query):
                    speak_it(query)

            except exceptions.NotTranslated:
                pass
        if not results:
            results.append({
                "Title": 'Not found',
                "SubTitle": '',
                "IcoPath": "Images/app.png"
            })
        return results

    def openUrl(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    Translate()
