# Luke Hudspeth CS72 Final Project
## Levi: a naive voice interactive AI
### Project Description Levi 1.0:

### API's
For this project, I used primarily Google's speech-to-text API and text-to-speech API to create most of Levi's processing of simple audio.
As far as the question answering, and functionality, that was implemented via a vector
and cosine similarity comparisons similar to our HW5.

### Implementation:
*See Levi.txt file for detailed implementation*

### Functionality:
Levi's functions are somewhat limited with Levi 1.0
*See paper for detailed functionality*. 

### Resourcces:
1. https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/
2. syntax for API from:  https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/
3. had an audio error which I ignore, code for that from: https://github.com/spatialaudio/python-sounddevice/issues/11
4. https://www.alexkras.com/transcribing-audio-file-to-text-with-google-cloud-speech-api-and-python/


### External Library Requirements: 
**This will Likely only run on a Mac OS**
***
**Using Python 3.0**
***
Check to make sure all necessary Libraries are installed. 
**download voice of "Lee" (en-aus) in Dictation settings for Mac**. 
**download voice of "Juan" (Spanish) in Dictation settings for Mac**. 
Should be able to run "pip install -r requirements.txt" from command line to download the necessary libraries. 
1. google-api-python-client==1.6.4
2. httplib2==0.10.3
3. oauth2client==4.1.2
4. pyasn1==0.4.2
5. pyasn1-modules==0.2.1
6. rsa==3.4.2
7. six==1.11.0
8. SpeechRecognition==3.8.1
9. tqdm==4.19.5
10. uritemplate==3.0.0
11. gtts
12. pyaudio13. google-cloud-api
13. tornado
14. nose
15. virtualenv
16. google-api-python-client
17. weather-api
