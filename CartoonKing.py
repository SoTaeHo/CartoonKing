import cv2

def cartoonize_image(image):
    # 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이미지에 가우시안 블러 적용하여 잡음 제거
    gray = cv2.medianBlur(gray, 5)

    # 엣지 감지를 위해 이미지를 줄임
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # 엣지에 색상을 부여하여 카툰 스타일로 변환
    color = cv2.bilateralFilter(image, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

# 입력 이미지 로드
input_image = cv2.imread('input_image.jpg')

# 이미지를 카툰 스타일로 변환
cartoon_image = cartoonize_image(input_image)

# 이미지를 그레이 스케일로 변환
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# 카툰 이미지를 jpg 파일로 저장
output_filename = 'cartoon_image.jpg'
cv2.imwrite(output_filename, cartoon_image)

# 그레이 이미지를 jpg 파일로 저장
output_filename = 'gray_image.jpg'
cv2.imwrite(output_filename, gray_image)

# 윈도우 생성 및 이미지 표시
cv2.imshow('Cartoonized Image', cartoon_image)
cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
