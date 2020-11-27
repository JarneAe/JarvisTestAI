from SpeechRecognition import SpeechRecognition
from GetDate import GetDate
import Narrator
import warnings
import wikipedia


warnings.filterwarnings('ignore')

speechRecognition = SpeechRecognition()
speechRecognition.recordAudio()