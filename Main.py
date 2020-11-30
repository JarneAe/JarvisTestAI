from SpeechRecognition import recordAudio
from CommandListener import CommandListener
import warnings

warnings.filterwarnings('ignore')

while True:
    userInput = recordAudio()

    commandListener = CommandListener(userInput)
    commandExecutor = commandListener.commandListener()

    commandListener = CommandListener(userInput)
    commandExecutor = commandListener.commandListener()
