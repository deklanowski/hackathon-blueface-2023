import time
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import SpeechRecognitionEventArgs, PropertyId
from multiprocessing import Queue

from log.config_log import logger


def speech_to_text_continuous(message_queue: Queue, api_key: str, speech_region: str):
    """
    Converts speech to text non-stop
    Documentation: https://learn.microsoft.com/en-gb/azure/ai-services/speech-service/how-to-recognize-speech?pivots=programming-language-python

    This section will need some changes fo you to solve the challenges
    This logic is called by spawning a sub-process from the main game view.
    The main process and this speech recognition process communicate in a one-way manner using Queues.
    The Speech recognition process can send message to the queue which can be then retrieved by the main process.
    """
    done = False

    def stop_cb(evt):
        logger.info(f'CLOSING on {evt}')
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    def recognized_speech(event: SpeechRecognitionEventArgs):
        """Callback fired when speech is recognized. Check the event and
        place on queue"""
        if event.result.reason == speechsdk.ResultReason.RecognizedSpeech:
            message_queue.put(event.result.text.lower())
        elif event.result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(
                event.result.no_match_details))
        elif event.result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = event.result.cancellation_details
            print("Speech Recognition canceled: {}".format(
                cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(
                    cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

    # Init engine
    speech_config = speechsdk.SpeechConfig(subscription=api_key, region=speech_region)
    speech_config.speech_recognition_language = "en-GB"
    # Initial Silence Timeout: The amount of silence at the beginning of a recognition
    # before the Speech Service stops recognizing speech.

    # I think this is set to around 15 seconds by default, setting it to 5 seconds speeds up the recognition
    # process and makes the player more responsive to voice commands.
    speech_config.set_property(PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, "5000")

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Define Callbacks
    speech_recognizer.recognizing.connect(lambda evt: logger.info(f'RECOGNIZING: {evt.result.text}'))
    speech_recognizer.recognized.connect(recognized_speech)

    speech_recognizer.session_started.connect(lambda evt: logger.info(f'SESSION STARTED: {evt}'))
    speech_recognizer.session_stopped.connect(lambda evt: logger.info(f'SESSION STOPPED {evt}'))
    speech_recognizer.canceled.connect(lambda evt: logger.info(f'CANCELED {evt}'))

    speech_recognizer.session_stopped.connect(stop_cb)
    speech_recognizer.canceled.connect(stop_cb)

    speech_recognizer.start_continuous_recognition()
    
    while not done:
        time.sleep(.5)
