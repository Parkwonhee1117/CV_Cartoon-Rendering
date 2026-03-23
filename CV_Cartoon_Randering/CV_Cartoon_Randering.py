import cv2
import numpy as np
import os

def apply_cartoon_filter(image_path):
    # 1. 이미지 로드
    img = cv2.imread(image_path)
    if img is None:
        print(f"오류: {image_path} 파일을 찾을 수 없습니다.")
        return

    # 2. 전처리: 그레이스케일 변환 및 노이즈 제거
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    # 3. 외곽선(Edge) 검출: Adaptive Thresholding
    edges = cv2.adaptiveThreshold(gray, 255, 
                                  cv2.ADAPTIVE_THRESH_MEAN_C, 
                                  cv2.THRESH_BINARY, 9, 5)

    # 4. 색상 단순화: Bilateral Filter (수채화 효과)
    color = cv2.bilateralFilter(img, 9, 75, 75)

    # 5. 마스크를 이용해 색상 이미지와 외곽선 결합
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # 결과 시각화 (원본과 결과물 비교)
    result = np.hstack((img, cartoon)) # 가로로 이어 붙이기
    cv2.imshow("Original vs Cartoon Rendering", result)
    
    print(f"이미지 처리 완료: {image_path}")
    print("아무 키나 누르면 창이 닫힙니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 실행 부분
if __name__ == "__main__":
    apply_cartoon_filter('Character_Image.png')
    apply_cartoon_filter('Character_Image_2.png')
    apply_cartoon_filter('Character_Image_3.png')
    apply_cartoon_filter('Character_Image_4.png')