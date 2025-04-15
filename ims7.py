import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 파일 읽기
image_path = 'outstandingcloth.bmp'  # 이미지 파일 경로 (자신의 이미지 경로로 수정)
image = cv2.imread(image_path)

# 이미지가 제대로 읽혔는지 확인
if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    # 이미지를 RGB로 변환 (OpenCV는 기본적으로 BGR로 이미지를 읽음)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 이미지를 화면에 표시
    plt.figure(figsize=(8, 6))
    plt.imshow(image_rgb)
    plt.title("Captured Image")
    plt.axis('off')  # 축 없애기
    plt.show()

    # R, G, B 성분 추출
    R = image_rgb[:, :, 0]
    G = image_rgb[:, :, 1]
    B = image_rgb[:, :, 2]

    # R, G, B 성분 각각을 화면에 표시
    plt.figure(figsize=(8, 6))
    plt.subplot(1, 3, 1)
    plt.imshow(R, cmap='Reds')
    plt.title("Red Component")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(G, cmap='Greens')
    plt.title("Green Component")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(B, cmap='Blues')
    plt.title("Blue Component")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    # R 성분의 히스토그램 그리기
    plt.figure(figsize=(8, 6))
    plt.hist(R.ravel(), bins=256, color='red', alpha=0.7)
    plt.title("Histogram of Red Component")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()

    # 히스토그램 평활화 수행
    R_eq = cv2.equalizeHist(R)

    # 히스토그램 평활화 후 R 성분의 결과 히스토그램 그리기
    plt.figure(figsize=(8, 6))
    plt.hist(R_eq.ravel(), bins=256, color='red', alpha=0.7)
    plt.title("Histogram of Equalized Red Component")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()

    # 평활화된 R 성분을 사용하여 원본 이미지를 재구성
    image_eq = image_rgb.copy()
    image_eq[:, :, 0] = R_eq

    # 평활화된 이미지 표시
    plt.figure(figsize=(8, 6))
    plt.imshow(image_eq)
    plt.title("Synthetized Image with Equalized Red Component")
    plt.axis('off')
    plt.show()

    # 결과를 통해 관찰
    print("히스토그램 평활화 및 합성 이미지 처리가 완료되었습니다.")
