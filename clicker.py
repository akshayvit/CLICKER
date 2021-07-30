import speech_recognition
import pyautogui
while(1):
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as src:
        try:
            audio = recognizer.adjust_for_ambient_noise(src)
            print("Threshold Value After calibration:" + str(recognizer.energy_threshold))
            print("Please speak:")
            audio = recognizer.listen(src)
            st = recognizer.recognize_google(audio).lower()
            print(st)
            if(st=="left"):
                pyautogui.moveRel(-100, 0, duration=0.05)
            if(st=="click"):
                pyautogui.click(button='left', clicks=1, interval=0.05)
            if(st=="right"):
                pyautogui.moveRel(100, 0, duration=0.05)
            if(st=="up"):
                pyautogui.moveRel(0,-100, duration=0.05)
            if(st=="down"):
                pyautogui.moveRel(0,100, duration=0.05)
            if(st=="mute"):
                pyautogui.typewrite(['volumemute'])
        except Exception as ex:
            print(ex)
