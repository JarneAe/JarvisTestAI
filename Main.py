from SpeechRecognition import recordAudio
from CommandListener import CommandListener
import warnings

warnings.filterwarnings('ignore')

userInput = recordAudio()

commandListener = CommandListener(userInput)
commandExecutor = commandListener.commandListener()
