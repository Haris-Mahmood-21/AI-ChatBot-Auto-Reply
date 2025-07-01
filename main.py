import pyautogui
import pyperclip
import time
import threading
import keyboard
import config
from openai import OpenAI

client = OpenAI(api_key = config.OPENAI_API_KEY)

# Setting to exit the program instantly

exit_flag = False
def set_exit():
    global exit_flag
    exit_flag = True
    print("Exiting...")

keyboard.add_hotkey('q', set_exit)

# Its purpose is to prevent sending a request to OpenAI if the user hasn't replied yet.

def get_last_message(messages):
    lines = [line.strip() for line in messages.strip().split('\n') if line.strip()]
    return lines[-1] if lines else ""

#openai api

time.sleep(2)

#Click will click on chrome icon 
pyautogui.click(610, 750)
time.sleep(0.5)

last_reply = " "

while True:
    if exit_flag:
        break

    # this will drag your mouse from top to bottom to select chat
    pyautogui.moveTo(477, 154)
    pyautogui.mouseDown()
    time.sleep(0.2)

    pyautogui.moveTo(809, 701, duration=0.5)
    pyautogui.mouseUp()
    time.sleep(0.5)

    # Copy selected text to clipboard and store in variable
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(499, 174)
    time.sleep(0.5)

    copied_text = pyperclip.paste()

    last = get_last_message(copied_text)
    
    if last_reply != last:

        response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # or "gpt-4"
                messages=[
                    {"role": "system", "content": "Give some prompt to openai"},
                    {"role": "user", "content": copied_text}
                ]
            )

        reply =(response.choices[0].message.content)

        pyperclip.copy(reply)

        last_reply = reply

        # paste it where needed
        pyautogui.click(809, 701)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.press('enter')

    else:
        pass