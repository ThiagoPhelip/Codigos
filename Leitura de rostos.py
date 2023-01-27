import cv2
import dlib

# Inicializar detector de faces (HOG-based)
face_detector = dlib.get_frontal_face_detector()

# Carregar modelo de reconhecimento facial (usando o modelo ResNet)
face_recognition_model = dlib.face_recognition_model_v1("resnet_model.dat")

# Carregar imagem
image = cv2.imread("image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar faces na imagem
faces = face_detector(gray, 1)

# Iterar sobre as faces detectadas
for face in faces:
    # Calcular descritor facial (vetor de 128 dimensões)
    face_descriptor = face_recognition_model.compute_face_descriptor(image, face)

    # Comparar com outros rostos previamente registrados
    # (por exemplo, usando distância Euclideana)
    # e reconhecer a pessoa se a distância for suficientemente pequena
    distance = compare_with_known_faces(face_descriptor)
    if distance < threshold:
        print("Reconhecido como: " + name)
    else:
        print("Não reconhecido")
