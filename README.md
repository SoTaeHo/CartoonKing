## CartoonKing

![input_image](https://github.com/SoTaeHo/CartoonKing/assets/91146046/469a3085-8ae9-43cd-8d04-e77b22f7092d)
![cartoon_image](https://github.com/SoTaeHo/CartoonKing/assets/91146046/bc2c9827-2b52-4eb2-a8d9-455798c60e79)
![gray_image](https://github.com/SoTaeHo/CartoonKing/assets/91146046/7575ddd8-ae57-48d7-848d-954f87a2d19c)

### 알고리즘 설명

입력받는 사진을 cartoon style과 gray style로 편집해서 보여줍니다.

cartoon style로 바뀌는 과정은 다음의 알고리즘을 따릅니다.

1. 그레이스케일 변환: 먼저, 입력 이미지를 그레이스케일로 변환합니다. 이는 이미지의 색상을 제거하여 각 픽셀의 밝기만을 고려하는 것입니다. 그레이스케일로 변환하는 이유는 엣지 감지를 수행하기 위해 이미지의 색상 정보를 단순화하고 잡음을 줄이기 위함입니다.

2. 가우시안 블러 적용: 그레이스케일 이미지에 가우시안 블러를 적용합니다. 이는 이미지의 잡음을 제거하기 위해 사용됩니다. 가우시안 블러는 이미지를 부드럽게 만들어 주어 잡음을 감소시키고, 카툰풍 이미지를 더 부드럽게 만들어 줍니다.

3. 엣지 감지: 가우시안 블러가 적용된 이미지에서 엣지를 감지합니다. 엣지는 이미지에서 대비가 높은 부분을 나타냅니다. 엣지 감지를 통해 이미지의 주요 특징을 감지하고, 이를 통해 후속 단계에서 이미지를 더욱 카툰풍으로 만들 수 있습니다.
4. 엣지 강조: 엣지를 강조하기 위해 엣지 감지 결과를 이진화합니다. 이진화된 엣지를 사용하여 카툰풍 스타일의 이미지를 생성합니다. 엣지 강조는 이미지의 경계를 명확하게 하고, 카툰풍 이미지의 특징을 부각시킵니다.
5. 색상 부여: 엣지 강조된 이미지에 컬러 이미지를 블러 처리하여 색상을 부여합니다. 이를 통해 엣지 주변의 색상이 부드럽게 혼합되어 카툰풍 이미지가 생성됩니다.

gray style(cartoon 느낌이 나지않는 영상)은 그레이 스케일로 변환한 이미지를 바로 사용하였습니다.

### 알고리즘의 한계  

1. 정확한 표현의 부족: 카툰풍 이미지는 현실적인 이미지의 추상적인 버전으로 간주될 수 있습니다. 이 알고리즘은 실제 세계의 물체나 장면을 정확하게 재현하는 것이 아니라, 이미지의 일부 특징을 추출하고 부각시킴으로써 카툰풍 스타일을 만듭니다. 따라서 원본 이미지의 세부적인 특징이나 색상이 완벽하게 보존되지 않을 수 있습니다.
2. 일관성의 부족: 카툰풍 이미지 생성 알고리즘은 각 이미지에 따라 다르게 동작할 수 있습니다. 따라서 동일한 알고리즘과 파라미터를 사용하더라도 입력 이미지의 세부 사항에 따라 출력 결과가 다를 수 있습니다. 이는 일관된 효과를 얻기 어려울 수 있습니다.
3. 세부적인 특징 손실: 카툰풍 이미지 생성 과정에서 세부적인 특징이 일부 손실될 수 있습니다. 특히 작은 세부사항이나 이미지의 고해상도 부분은 카툰풍 이미지에서 희미해질 수 있습니다. 따라서 원본 이미지에 있는 세부사항이 중요한 경우에는 이러한 손실이 문제가 될 수 있습니다.
4. 일반화의 한계: 카툰풍 이미지 생성 알고리즘은 모든 종류의 이미지에 대해 일반화되지 않을 수 있습니다. 특히 복잡한 장면이나 세부적인 패턴을 포함하는 이미지의 경우에는 알고리즘의 효과가 덜 뚜렷할 수 있습니다.