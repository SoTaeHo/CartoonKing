import cv2

def cartoonize_image(image):
    # 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이미지에 가우시안 블러 적용
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # 엣지 감지
    edges = cv2.Laplacian(gray, cv2.CV_8U, ksize=5)

    # 이진화 처리
    ret, mask = cv2.threshold(edges, 150, 255, cv2.THRESH_BINARY_INV)

    # 컬러 이미지로 변환
    color = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 엣지 강조하기 위해 마스크 적용
    cartoon = cv2.bitwise_and(color, color, mask=mask)

    return cartoon

# 입력 이미지 로드
input_image = cv2.imread('input_image.jpg')

# 이미지를 만화 스타일로 변환
cartoon_image = cartoonize_image(input_image)

# 변환된 이미지 출력
cv2.imshow('Cartoonized Image', cartoon_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
