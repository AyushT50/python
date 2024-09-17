import pyttsx3
# This can covert your text in Audio


engine = pyttsx3.init()

# what you want to say that write in below paralysis
engine.say("this is convert the text into audio like  this    ...")
engine.say(" hey how are you")
engine.say(" i am fine what about you")
engine.say(" iam also fine")

engine.runAndWait()