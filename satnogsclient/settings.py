from os import environ

DEMODULATION_COMMAND = environ.get('SATNOGS_DEMODULATION_COMMAND', None)
ENCODING_COMMAND = environ.get('SATNOGS_ENCODING_COMMAND', None)
DECODING_COMMAND = environ.get('SATNOGS_DECODING_COMMAND', None)
OUTPUT_PATH = environ.get('SATNOGS_OUTPUT_PATH', None)
