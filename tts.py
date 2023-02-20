from TTS.api import TTS

print("Hello World")

tts = TTS(model_name="tts_models/en/ek1/tacotron2")
tts.tts_to_file(text = "This is a test.")