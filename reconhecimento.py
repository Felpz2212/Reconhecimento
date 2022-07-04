import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
solucao_reconhecimento = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento.FaceDetection()
desenho = mp.solutions.drawing_utils

while (True):
    # ler informações da webcam
    verificador, frame = webcam.read()

    if not verificador:
        break;

    # reconhecer os rostos

    listas_rostos = reconhecedor_rostos.process(frame)

    if listas_rostos.detections:
        for rosto in listas_rostos.detections:
            desenho.draw_detection(frame, rosto)

    cv2.imshow("Rostos na webcam", frame)
    # desenhar os rostos na imagem
    # qaundo apertar esc para o loop
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
