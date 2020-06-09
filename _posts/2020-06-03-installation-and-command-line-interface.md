---
layout: post
title: "[한글 문서화] Installation & Command Line Interface"
tags: [WordCloud Docs]
---

>word_cloud README.md의 [Installation][Install] 항목과 word_cloud GitHub Page의 [Command Line Interface][CLI] 항목을 한국어로 번역 및 보완한 문서입니다.
<hr>

## word_cloud 설치
word_cloud는 Python 기반 프로젝트이며 아래와 같이 두가지 방법으로 설치를 진행할 수 있습니다.

1. pip을 사용하는 경우
```
pip install wordcloud
```
2. conda를 사용하는 경우 `conda-forge` 에서 설치해야 합니다.
```
conda install -c conda-forge wordcloud
```
<br>

## 명령어 인터페이스 (Command Line Interface)
word_cloud에서 사용하는 명령어 인터페이스는 아래와 같습니다.
```
wordcloud_cli [-h] [--text file] [--regexp regexp][--stopwords file]
　 　 　 　 　 [--imagefile file] [--fontfile path] [--mask file]
　 　 　 　 　 [--colormask file] [--contour_width width]
　 　 　 　 　 [--contour_color color] [--relative_scaling rs]
　 　 　 　 　 [--margin width] [--width width] [--height height]
　 　 　 　 　 [--color color] [--background color] [--no_collocations]
　 　 　 　 　 [--include_numbers] [--min_word_length min_word_length]
　 　 　 　 　 [--prefer_horizontal ratio] [--scale scale]
　 　 　 　 　 [--colormap map] [--mode mode] [--max_words N]
　 　 　 　 　 [--min_font_size size] [--max_font_size size]
　 　 　 　 　 [--font_step step] [--random_state seed]
　 　 　 　 　 [--no_normalize_plurals] [--repeat] [--version]
```
<br>

## Arguments 설명
`--text`

wordcloud로 만들 텍스트 파일을 지정합니다.

예시) `--text text.txt`
<hr>

`--regexp`

단어를 구성하는 것을 정의하는 정규식을 override 합니다.
<hr>

`--stopwords`

wordcloud에서 제외할 단어들이 포함된 텍스트 파일을 지정합니다. 제외할 단어는 한 줄에 한 단어씩 입력해야 합니다.

예시) `--stopwords stopwords.txt`
<hr>

`--imagefile`

완성된 PNG 이미지를 작성할 파일을 지정합니다. wordcloud의 결과가 파일에 저장됩니다.

예시) `--imagefile imagefile.png`
<hr>

`--fontfile`

사용할 글꼴 파일을 지정합니다. (default: DroidSansMono)

예시) `--fontfile fontfile.ttf`
<hr>

`--mask`

word_cloud의 형태를 만드는데 사용할 mask 파일을 지정합니다.

예시) `--mask file.jpg`
<hr>

`--colormask`

word_cloud를 채색하는데 사용할 color mask 파일을 지정합니다.

예시) `--colormask file.jpg`
<hr>

`--contour_width`

입력값이 0보다 크면, 그 두께로 mask의 윤곽선을 그립니다.

Default: 0
<hr>

`--contour_color`

mask의 윤곽선을 그릴 때 지정한 색을 사용합니다. PIL.ImageColor.getcolor의 모든 값이 허용됩니다.

Default: "black"
<hr>

`--relative_scaling`

빈도(0-1)에 따라서 단어들을 scaling합니다.

Default: 0
<hr>

`--margin`

wordcloud에서 단어 사이의 간격을 지정합니다.

Default: 2
<hr>

`--width`

출력 이미지의 가로길이를 정합니다.

Default: 400
<hr>

`--height`

출력 이미지의 세로길이를 정합니다.

Default: 200
<hr>

`--color`

이미지를 채색할 때 지정한 색을 사용합니다. PIL.ImageColor.getcolor의 모든 값이 허용됩니다.

예시) `--color red`
<hr>

`--background`

이미지의 배경으로 지정한 색을 사용합니다. PIL.ImageColor.getcolor의 모든 값이 허용됩니다.

Default: "black"
<hr>

`--no_collocations`

wordcloud에 bigram을 추가하지 않습니다.

Default: True
<hr>

`--include_numbers`

wordcloud에 숫자를 포함합니다.

Default: False
<hr>

`--min_word_length`

X자 이상으로 이루어진 단어만 wordcloud에 포함합니다.

Default: 0
<hr>

`--prefer_horizontal`

단어를 수평으로 배치하는 시간의 비율을 설정합니다.

Default: 0.9
<hr>

`--scale`

계산과 그리기를 scaling 합니다.

Default: 1
<hr>

`--colormap`

matplotlib colormap을 지정합니다.

Default: "viridis"
<hr>

`--mode`

투명한 배경에 RGB와 RGBA 중 무엇을 사용할 지 선택합니다

Default: "RGB"
<hr>

`--max_words`

최대 단어 수를 설정합니다.

Default: 200
<hr>

`--min_font_size`

글꼴 크기의 최솟값을 설정합니다.

Default: 4
<hr>

`--max_font_size`

글꼴 크기의 최댓값을 설정합니다.

예시) `--max-font_size 10`
<hr>

`--font_step`

글꼴 크기의 간격을 설정합니다.

Default: 1
<hr>

`--random_state`

int형 random seed를 설정합니다.

예시) `--random-state 11`
<hr>

`--no_normalize_plurals`

단어 마지막의 's'를 제거하지 않습니다.

Default: True
<hr>

`--repeat`

wordcloud에 같은 단어나 구절이 여러번 나타나는 것을 허용합니다.

Default: False
<hr>

`--version`

wordcloud의 버전을 보여주고 종료합니다.

[Install]: https://github.com/amueller/word_cloud/blob/master/README.md
[CLI]: http://amueller.github.io/word_cloud/cli.html#
