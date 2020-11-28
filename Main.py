from SpeechRecognition import SpeechRecognition
from CommandListener import CommandListener
from GetDate import GetDate
import Narrator
import warnings
import wikipedia


warnings.filterwarnings('ignore')

#speechRecognition = SpeechRecognition()
#userInput = speechRecognition.recordAudio()

commandListener = CommandListener("say ik ben heet")
commandExecutor = commandListener.commandListener()

print(commandExecutor)