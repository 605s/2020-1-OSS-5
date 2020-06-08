---
layout: post
title: "[한글 문서화] API Reference"
tags: [Documentation]
---

>word_cloud GitHub Page의 [API Reference][API] 항목을 한국어로 번역 및 보완한 문서입니다.
<hr>

## API Reference
모든 기능은 WordCloud 클래스에 캡슐화되어 있습니다.

|||
|:---|:---|
|[**`WordCloud`**](#wordcloudwordcloud)([font_path, width, height, …])|생성 및 그리기를 위한 Word Cloud 객체|
|[**`ImageColorGenerator`**](#wordcloudimagecolorgenerator)(image[, default_color])|컬러 이미지를 기반으로 한 컬러 생성기|
|[**`random_color_func`**](#wordcloudrandom_color_func)([word, font_size, …])|임의의 색조 색상 생성|
|`colormap_color_func`||
|[**`get_single_color_func`**](#wordcloudget_single_color_func)(color)|단일 색조와 채도를 반환하는 color function을 생성|
<hr>

### wordcloud.WordCloud
```
class wordcloud.WordCloud(font_path=None, width=400, height=200, 
margin=2, ranks_only=None, prefer_horizontal=0.9, mask=None, scale=1, 
color_func=None, max_words=200, min_font_size=4, stopwords=None, 
random_state=None, background_color='black', max_font_size=None, font_step=1, 
mode='RGB', relative_scaling='auto', regexp=None, collocations=True, 
colormap=None, normalize_plurals=True, contour_width=0, contour_color='black', 
repeat=False, include_numbers=False, min_word_length=0, 
collocation_threshold=30)
```

생성 및 그리기를 위한 Word Cloud 객체
<br>

#### 매개변수

  `font_path : string`

  사용될 폰트의 폰트 경로(OTF 또는 TTF). Linux 시스템에서 기본값은 DroidSansMono 경로입니다. 다른 OS에 있거나 이 글꼴이 없는 경우 경로를 조정해야합니다.

  `width : int (default=400)`

  캔버스의 너비입니다.

  `height : int (default=200)`

  캔버스의 높이입니다.

  `prefer_horizontal : float (default=0.90)`

  수직이 아닌 수평 피팅을 시도하는 시간의 비율입니다. prefer_horizontal < 1 이면 알고리즘이 맞지 않을때 단어 회전을 시도합니다. (현재 세로 단어만 얻는 기본 제공 방법은 없습니다.)

  `mask : nd-array or None (default=None)`

  None이 아닌 경우 단어를 그릴 위치에 이진 마스크를 제공합니다. 마스크가 None이 아닌 경우 너비와 높이가 무시되고 대신 마스크 모양이 사용됩니다. 모든 흰색 (#FF 또는 #FFFFFF) 항목은 “마스크에 포함되지 않는” 것으로 간주되며 다른 항목은 자유롭게 그릴 수 있습니다. [이것은 최신 버전으로 변경되었습니다!]

  `contour_width : float (default=0)`

  mask가 None이 아니고 contour_width > 0 인 경우, 마스크 윤곽을 그립니다.

  `contour_color : color value(default=”black”)`

  마스크 컨투어 색상입니다.

  `scale : float (default=1)`

  계산과 그리기 사이의 스케일링입니다. 큰 word cloud 이미지의 경우 큰 캔버스 크기 대신 스케일을 사용하는 것이 훨씬 빠르지만, 단어에 더 적합할 수 있습니다.

  `min_font_size : int (default=4)`

  사용할 가장 작은 글꼴 크기입니다. 이 크기의 공간이 더 이상 없으면 중지됩니다.

  `font_step : int (default=1)`

  글꼴의 크기 단계입니다. font_step > 1은 계산 속도를 높이지만 적합하지 않습니다.

  `max_words : number (default=200)`

  최대 단어 수입니다.

  `stopwords : set of strings or None`

  제거될 단어입니다. None인 경우 내장된 STOPWORDS 목록이 사용됩니다. generate_from_frequencies를 사용하는 경우 무시됩니다.

  `background_color : color value (default=”black”)`

  word cloud 이미지의 배경색입니다.

  `max_font_size : int or None (default=None)`

  가장 큰 단어의 최대 글꼴 크기입니다. None인 경우 이미지의 높이가 사용됩니다.

  `mode : string (default=”RGB”)`

  모드가 "RGBA"이고 background_color가 None이면 투명한 배경이 생성됩니다.

  `relative_scaling : float (default=’auto’)`

  글꼴 크기에 대한 상대 단어 빈도의 중요성. relative_scaling = 0 이면 단어 순위만 고려됩니다. relative_scaling = 1을 사용하면 빈도가 두 배인 단어의 크기가 두 배가됩니다. 단어의 순위뿐만 아니라 빈도를 고려하려면 0.5의 relative_scaling이 좋아 보입니다. 'auto'인 경우 repeat이 true가 아닌 한 0.5로 설정되며, true인 경우 0으로 설정됩니다.

  `color_funcc : allable (default=None)`

  각 단어의 PIL 색상을 반환하는 매개변수 word, font_size, position, orientation, font_path, random_state를 사용하여 호출할 수 있습니다. "colormap"을 덮어 씁니다. matplotlib의 컬러 맵을 지정하려면 "colormap"을 참조하십시오. 단색으로 word cloud를 만들고자 한다면 `color_func=lambda *args, **kwargs: "white"`를 사용하십시오 . RGB 코드를 사용하여 단색을 지정할 수도 있습니다. 예를 들어 `color_func=lambda *args, **kwargs: (255,0,0)`는 색상을 빨간색으로 설정합니다.

  `regexp : string or None (optional)`

  process_text에서 입력 텍스트를 토큰으로 나누는 정규식입니다. None을 지정하면 `r"\w[\w']+"`이 사용됩니다. generate_from_frequencies를 사용하는 경우 무시됩니다.

  `collocations : bool (default=True)`

  두 단어의 배열(bigrams)을 포함할지 여부입니다. generate_from_frequencies를 사용하는 경우 무시됩니다.

  `colormap : string or matplotlib colormap (default=”viridis”)`

  Matplotlib 컬러 맵은 각 단어에 대해 무작위로 색상을 그립니다. "color_func"가 지정되면 무시됩니다.

  `normalize_plurals : bool (default=True)`

  단어에서 후행 's'를 제거할지 여부입니다. True인 경우 후행 's'가 있거나 없는 단어가 표시되면 단어가 'ss'로 끝나지 않는 한, 후미에 's'가 있는 단어가 제거되고 이 단어의 counts가 's'가 없는 버전에 추가됩니다. generate_from_frequencies를 사용하는 경우 무시됩니다.

  `repeat : bool (default=False)`

  max_words 또는 min_font_size에 도달할 때까지 단어와 구를 반복할지 여부입니다.

  `include_numbers : bool (default=False)`

  숫자를 문구로 포함할지 여부입니다.

  `min_word_length : int (default=0)`

  단어를 포함해야하는 최소 글자 수입니다.

  `collocation_threshold : int (default=30)`

  Bigram이 Bigram으로 계산되려면 이 매개변수보다 큰 Dunning likelihood collocation 점수가 있어야합니다. 기본값은 30입니다.

  Manning, C.D., Manning, C.D. 및 Schütze, H., 1999를 참조하십시오. 자연 언어 처리 통계의 기초. MIT press, p. 162

  <https://nlp.stanford.edu/fsnlp/promo/colloc.pdf#page=22>
<br>

#### Notes

캔버스가 클수록 코드 속도가 크게 느려집니다. 큰 word cloud가 필요한 경우 캔버스 크기를 낮추고 scale 매개 변수를 설정하십시오.

알고리즘은 `max_font_size`스케일링 휴리스틱에 따라 실제 빈도보다 단어 순위에 더 많은 가중치를 부여 할 수 있습니다 .

`Attributes:`

` ``words_`` : dict of string to float `

빈도와 관련된 단어 토큰.<br>

` ``layout_`` : list of tuples (string, int, (int, int), int, color)) `

적합한 word cloud를 인코딩합니다. 각 단어마다 문자열, 글꼴 크기, 위치, 방향 및 색상을 인코딩합니다.
<br>

#### 메소드

|||
|:---|:---|
|`fit_words`(self, frequencies)|단어와 빈도로 word_cloud를 만듭니다.|
|`generate`(self, text)|텍스트에서 word_cloud를 생성합니다.|
|`generate_from_frequencies`(self, frequencies)|단어와 빈도로 word_cloud를 만듭니다.|
|`generate_from_text`(self, text)|텍스트에서 word_cloud를 생성합니다.|
|`process_text`(self, text)|긴 텍스트를 단어로 나누고 stopword를 제거합니다.|
|`recolor`(self[, random_state, color_func, …])|기존 레이아웃을 다시 칠합니다.|
|`to_array`(self)|numpy 배열로 변환합니다.|
|`to_file`(self, filename)|이미지 파일로 내보냅니다.|
|`to_svg`(self[, embed_font, …])|SVG로 내보냅니다.|
<br>

```
__init__(self, font_path=None, width=400, height=200, margin=2, ranks_only=None, 
prefer_horizontal=0.9, mask=None, scale=1, color_func=None, max_words=200, min_font_size=4, 
stopwords=None, random_state=None, background_color='black', max_font_size=None, font_step=1, 
mode='RGB', relative_scaling='auto', regexp=None, collocations=True, colormap=None, 
normalize_plurals=True, contour_width=0, contour_color='black', repeat=False, include_numbers=False, 
min_word_length=0, collocation_threshold=30)
```
자기를 초기화합니다. 정확한 서명은 help(type(self))를 참조하십시오.
<hr>

### wordcloud.ImageColorGenerator


```
class wordcloud.ImageColorGenerator(image, default_color=None)
```

컬러 이미지를 기반으로 한 컬러 생성기

RGB 이미지를 기반으로 색상을 생성합니다. 색상 이미지에서 둘러싸는 사각형의 평균 색상을 사용하여 단어의 색상이 지정됩니다.

생성 후, 객체는 color_func로 word cloud생성자 또는 색상변경method에 전달할 수 있는 호출 가능 기능을 합니다.

`Parameters` 

`imagend-array, shape (height, width, 3)`

단어 색상을 생성하는 데 사용되는 이미지입니다. 알파 채널은 무시됩니다. 이는 배경 크기와 같아야 합니다.

`default_colortuple or None, default=None`

배경이 이미지보다 큰 경우 사용할 대체 색상 (r, g, b)입니다. 만약 None이면, 대신 ValueError를 발생시킵니다. 

#### 메소드
|||
|:---|:---|
|`Methods call`(self, word, font_size, font_path, …) | 고정 된 이미지를 사용하여 주어진 단어의 색상을 생성하십시오.|

`init(self, image, default_color=None)`

자기를 초기화합니다. 정확한 특징은 help(type(self))를 참조하십시오.
<hr>

### wordcloud.random_color_func


```
random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None)
```
임의의 색조 색상 생성.

기본 채색 방법. 값이 80 %이고 lumination이 50 % 인 임의의 색조를 선택합니다.

`Parameters` 

`word, font_size, position, orientation : ignored.`

`random_staterandom.Random object or None, (default=None)`

임의의 개체가 제공되면 임의의 숫자를 생성하는 데 사용됩니다.
<hr>

### wordcloud.get_single_color_func

```
wordcloud.get_single_color_func(color)
```
다른 값 (HSV)으로 단일 색조와 채도를 반환하는 색상 함수를 만듭니다. 

허용되는 값은 PIL / Pillow에서 사용할 수있는 색상 문자열입니다.

```
>>> color_func1 = get_single_color_func('deepskyblue') 
>>> color_func2 = get_single_color_func('#00b4d2')
```

[API]: http://amueller.github.io/word_cloud/references.html
