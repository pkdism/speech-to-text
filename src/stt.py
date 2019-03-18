import speech_recognition as sr
import pyaudio
import googlesearch
import webbrowser
import time
import string

sample_rate = 48000
chunk_size = 2048

r = sr.Recognizer()

mic_list = sr.Microphone.list_microphone_names()

mic_name = 'Built-in Microphone'

for i, microphone_name in enumerate(mic_list): 
    if microphone_name == mic_name: 
        device_id = i 

# print(microphone_name, device_id)


with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source:
	r.adjust_for_ambient_noise(source)
	print("Say something to search")

	audio = r.listen(source)

	try:
		text = r.recognize_google(audio)
		print("You said:", text)

	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")

	except sr.RequestError as e:
		print("Not")


print("Searching..")
url = list(googlesearch.search(text, stop = 10))

print("Top 10 Results from Google")

for i in range(10):
	print(i+1, ". ", url[i], sep = "")


print("Which results should I open")

idx = 0

idx_text = ""

with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source:
	r.adjust_for_ambient_noise(source)

	idx_audio = r.listen(source)
	
	try:
		idx_text = r.recognize_google(idx_audio)

		# print("You said", idx_text)

		proxy_words = {
			1: ['first', '1st', 'first one', 'first 1', '1st one', '1st 1'],
			2: ['second', '2nd', 'second one', 'second 1', '2nd one', '2nd 1'],
			3: ['third', '3rd', 'third one', 'third 1', '3rd one', '3rd 1'],
			4: ['fourth', 'fourth one', '4th', 'fourth 1', '4th one', '4th 1', '41'],
			5: ['fifth', 'fifth one', '5th', 'fifth 1', '5th one', '5th 1', '51'],
			6: ['sixth', 'sixth one', '6th', 'sixth 1', '6th one', '6th 1', '61'],
			7: ['seventh', 'seventh one', '7th', 'seventh 1', '7th one', '7th 1', '71'],
			8: ['eighth', 'eighth one', '8th', 'eighth 1', '8th one', '8th 1', '81'],
			9: ['ninth', 'ninth one', '9th', 'ninth 1', '9th one', '9th 1', '91'],
			10: ['tenth', 'tenth one', '10th', 'tenth 1', '10th one', '10th 1']
		}

		proxy_flag = False

		for index, num in enumerate(proxy_words):
			if idx_text.lower() in proxy_words[num]:
				idx = num - 1
				proxy_flag = True

		if proxy_flag == False:
			try:
				idx_int = int(idx_text)
				if idx_int >= 1 and idx_int <= 10:
					idx = (int(idx_text)-1)
					print("You said", idx_int)
				else:
					print("You said", idx_int, "which is out of range")
					idx_text = ""

			except ValueError:
				print("That's not an index")


	except sr.UnknownValueError:
		print("No input received. Opening first result on browser..")

	except sr.RequestError as e:
		print("No input received. Opening first result on browser..")


if idx_text == "No Input":
	print("No valid input received. Opening first result on browser..")
else:
	print("Opening URL ", url[idx])

time.sleep(3)

# print(idx_text)
# print(idx)

webbrowser.open(url[idx])







