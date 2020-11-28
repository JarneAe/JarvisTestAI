from SpeechRecognition import SpeechRecognition
from CommandListener import CommandListener
from GetDate import GetDate
import Narrator
import warnings
import wikipedia


warnings.filterwarnings('ignore')

#speechRecognition = SpeechRecognition()
#userInput = speechRecognition.recordAudio()

commandListener = CommandListener("what is the date")
commandExecutor = commandListener.commandListener()