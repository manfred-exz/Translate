# Modification of This Fork
1. Add **TTS(Text To Speech)** support for the original Translate plugin
2. Add **'** to the end of your text to trigger TTS voice
3. Change default language to Chinese

Additional dependency:
```
pip install textblob pypiwin32 enchant
```

## Why I use windows tts engine instead of google's tts engine?
Because google tts is really slow, and need to save an mp3 file to play.

# Translate
Plugin for [Wox](http://www.getwox.com/) that translates between english and any other language.

![Translate](http://i.imgur.com/In9l67U.png)

Pressing ```Enter``` will redirect to a Google Translate page with the query.

To change your main language, replace this line in ```main.py```:
``` python
LANGUAGE = 'ru'
```

## Installation
[Get Wox](http://www.getwox.com/)

Install [TextBlob](https://textblob.readthedocs.io/en/dev/contributing.html):
```
pip install textblob
```
To install the plugin, type in Wox:
```
wpm install Direct Translate
```
