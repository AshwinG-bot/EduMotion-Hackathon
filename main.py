import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace




emotion = "No emotion"
val = "eaudfhafvaef"

cap = cv2.VideoCapture(0)

while(True):
	try:
		success, img = cap.read()
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, 
                emotion, 
                (50, 50), 
                font, 1, 
                (244, 231, 34), 
                4, 
                cv2.LINE_4)
		cv2.imshow("Video", img)
		result = DeepFace.analyze(img, actions = ["emotion"])
		if(str(result["dominant_emotion"]) == emotion):
			val = "dwesakfjwkfwfg"
			pass
		else:


			emotion = str(result["dominant_emotion"])
			cv2.putText(img, emotion, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 5)
	except Exception as e:
			emotion = "Not Focused"

	if(cv2.waitKey(1) & 0xFF == ord("q")):
		break
