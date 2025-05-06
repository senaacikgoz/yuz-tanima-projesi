import cv2
from fer import FER
from emotion_utils import detect_emotion
from suggestion_utils import get_study_suggestion

cap = cv2.VideoCapture(0)
detector = FER(mtcnn=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = detector.detect_emotions(frame)
    for result in results:
        (x, y, w, h) = result["box"]
        emotion, score = max(result["emotions"].items(), key=lambda item: item[1])
        suggestion = get_study_suggestion(emotion)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f"{emotion} ({score:.2f})", (x, y - 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(frame, suggestion, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    cv2.imshow("Duygu Tespiti ve Öneri", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
