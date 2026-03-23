# 🎨 Image Cartoonizer (CV_Cartoon_Rendering)

OpenCV의 이미지 처리 기술을 활용하여 일반 사진을 만화(Cartoon) 스타일로 변환하는 프로그램입니다. `Bilateral Filter`와 `Adaptive Thresholding`을 조합하여 수채화 같은 색감과 뚜렷한 외곽선을 구현하는 것이 핵심입니다.

---

## 🚀 실행 화면 (Demo)

### 1. 만화 느낌이 잘 표현되는 예시 (Success)
<img width="1283" height="419" alt="image" src="https://github.com/user-attachments/assets/1ad085c5-8f61-48bc-801a-0e6385659c42" />
<p align="center">단순한 배경과 대비가 뚜렷한 이미지에서 깔끔한 카툰 효과가 적용된 모습입니다.</p>

### 2. 만화 느낌이 잘 표현되지 않는 예시 (Failure)
<img width="606" height="345" alt="image" src="https://github.com/user-attachments/assets/51c79886-9cab-476e-b675-9aba5c998b63" />
<p align="center">복잡한 디테일이나 노이즈가 많은 이미지에서 선이 지저분하게 표현되는 한계점입니다.</p>

---

## ✨ 주요 기능 및 기술

### 필수 기능
* **이미지 카툰화**: `cv.bilateralFilter`와 `cv.adaptiveThreshold`를 사용하여 사진을 만화처럼 변환합니다.
* **노이즈 제거**: `cv.medianBlur`를 전처리 단계에 적용하여 외곽선이 지저분하게 따지는 것을 방지했습니다.
* **색상 단순화**: 양방향 필터를 통해 사물의 경계선은 유지하면서 내부 색상만 부드럽게 뭉치는 효과를 주었습니다.
* **외곽선 합성**: 추출된 엣지 마스크를 색상 이미지 위에 `cv.bitwise_and`로 합성하여 최종 결과물을 도출합니다.

### 한계점
* **디테일의 한계**: 복잡한 패턴 있는 부분에서는 모든 미세한 선을 엣지로 인식하여 화면이 시커멓게 타버리는 현상이 발생합니다.
* **색상 단계화의 부재**: 단순히 부드럽게 뭉치는 방식이라 실제 만화처럼 색의 단계를 끊어서 표현(Posterization)하지 못하는 기술적 한계가 있습니다.

---

## 🛠️ 설치 및 실행 방법

1. **필수 라이브러리 설치**:
    ```bash
    pip install opencv-python numpy
    ```
2. **프로그램 실행**:
    ```bash
    python CV_Cartoon_Randering.py
    ```

---

### 💡 기술적 상세
* **Bilateral Filter**: 일반 가우시안 블러와 달리 픽셀의 공간적 거리와 색상 차이를 모두 고려하여 '엣지를 보존하는' 필터링을 수행했습니다.
* **Adaptive Thresholding**: 이미지 전체에 동일한 기준을 적용하는 대신, 구역별로 최적의 임계값을 계산하여 조명 변화에 유연하게 대응했습니다.
