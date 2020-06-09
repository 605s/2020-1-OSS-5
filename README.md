# 2020-1-OSS-5

 0. [홈페이지](#homepage)
 1. [팀원 소개](#members)
 2. [프로젝트 소개](#introduction)
 3. [설치 방법](#install)
 4. [프로젝트 기여 방법](#Contribution)
 5. [프로젝트 진행과정](#Status)

## <div id = "homepage">홈페이지</div>

https://20-1-skku-oss.github.io/2020-1-OSS-5/

## <div id = "members">1. 팀원 소개</div>
- 김희성 heesunkim010 (팀장)
- 신성국 davidshyn1
- 안정복 jb0307
- 이하은 HACore
- 유광호 605s

## <div id = "introduction">2. 프로젝트 소개</div>
### word_cloud (https://github.com/amueller/word_cloud)

- 텍스트 내의 단어들을 중요도(문서 내 등장횟수)를 기준으로 구분하여 특정한 이미지 영역(mask) 내부에 시각화하는 프로젝트

![example][example]

## <div id = "install">3. 설치 방법</div>

pip 사용 시, 다음 코드로 진행하시기 바랍니다.:

    pip install wordcloud

conda 사용 시, 'conda-forge'를 이용하여 설치하시기 바랍니다:

    conda install -c conda-forge wordcloud

#### 설치 시 주의사항

wordcloud은 `numpy`와 `pillow` 패키지를 사용하기 때문에, 사전에 설치해야 합니다.

wordcloud 수행 후 해당 이미지를 저장하기 위해서는, `matplotlib` 패키지 또한 설치해야 합니다.

이용자의 파이썬 버전에 'wheel'이 없는 경우, 위의 해키지를 설치하기 위해서는 C 컴파일러가 셋업되어 있어야 합니다.
컴파일러를 설치하기 전, 파이썬 환경 및 개발 환경 등에 대한 내용으로 원 프로젝트에 이슈 등록하시길 바랍니다. 

## <div id = "Contribution">4. 프로젝트 기여 방법</div>
### 한글로 구현하는 기능 추가

Word Cloud 프로젝트는 긴 글(문장)을 tokenize 수행하여, 단어 등장 횟수에 따라 글자 크기를 조정하여 word cloud를 생성하도록 하는 프로젝트이기에,
각 언어의 특성과 문장 형태에 따라 word cloud가 제대로 수행되지 않을 확률이 높다.
해당 [issue][issue1]에 의하면 영어 기반의 프로젝트이기에,
다양한 언어의 특성을 적절하게 반영하지 못하고 있으며 이에 따라 상당 부분 word cloud의 기본 수행능력이 발휘되지 않은 경우가 간혹 발생된다.<br>
한글의 경우, 글자 font를 GmarketSansTTFLight.ttf로 수행하여 진행하면 다음 그림을 출력하게 된다.

![example2][example2] 


해당 그림을 통해 본 프로젝트의 문제가 드러난다.
한글의 문장 특성 중에 '조사'라는 품사는 항상 명사, 형용사, 부사뒤에 붙여서 사용된다는 특성이 있다.
그래서 한글 자연어처리 과정에서, 조사는 필히 앞에 붙여진 단어와 분리하여 처리되어야 한다.
하지만 단어 등장 빈도를 측정할 때, 조사를 포함한 하나의 어절로 구분하여 빈도를 측정하게 된다.
그렇게 되면, 위의 그림의 결과처럼 '소프트웨어는', '소프트웨어가'라는 두 어절은 사실상 같은 '소프트웨어' 단어를 표현한 것인데
따로 구분하여 처리된다.

이는 확실히, 본 코드에 한글NLP 기능이 없기 때문에 나타난 현상이라 볼 수 있다.
영어 NLP의 경우, 띄어쓰기를 기준으로, 단어가 구분되기 때문에 단어 구분에 있어서 어렵지 않게 처리할 수 있다.
하지만 한글의 단어구분은 띄어쓰기가 아니기 때문에, 한글 NLP 기능 구현 추가가 불가피하다.

본 팀원은 한글 NLP를 전문적으로 배우지 않았기 때문에, 외부 패키지를 활용하는 것이 불가피하다.
한글 NLP 패키지 중 [konlpy][konlpy]라는 패키지가 있다.
해당 패키지도 역시나 오픈소스프로젝트로 활발히 진행 중인 패키지나, 상당 부분 한글 NLP 기능을 구현할 만큼 유용한 패키지라고 판단하여,
해당 패키지를 활용하여 wordcloud 코드를 구현하기로 결정하였다.

### wordcloud 한글 문서화

원 프로젝트는 영어를 기본 언어로 wordcloud가 작동되고, 이에 대한 구체적인 방법에 대한 설명도 영어로 소개되어있기 때문에,
한국인 사용자들에게 더욱 쉽게 해당 프로젝트를 이해하고 실행할 수 있도록 해당 프로젝트의 post와 블로그를 한글로 문서화하기로 결정하였다.
한글로 문서화 할 post는 원 프로젝트의 정적페이지에서 프로젝트 진행 사항, 설치 방법 등과 원 프로젝트의 블로그 일부가 될 것이다.


### 새로운 ISSUE 검색

한글 구현 프로젝트, 한글예제 활용하여 정적페이지 문서화 프로젝트 등 본 팀의 주요 프로젝트 뿐만 아니라, 원 프로젝트에서 고려하고 있는 이슈들을 검색하여, 해결할 수 있다고 판단되는 이슈들을 팀원들과 토론을 통해 결정하고 해결하는 활동 또한 진행하였다.

#### [plural_issue][issue2]
해당 issue는 plural issue로 해당 wordcloud 코드는 복수로 표현된 단어들을 자동으로 단수로 변환하여 tokenize하는 기능이 설정되어 있는데,
's'로 끝나는 단어와 구분하지 못하여, 단어에서 's'가 삭제되는 버그가 발생된다는 문제의 내용이다.
예를 들어, 'virus'라는 영어단어는 's'로 끝나는데, 단수 자동변환 기능을 설정하면, 'viru'로 취급한다는 문제가 발생된다는 것이다.
이를 해결 하기 위해 's'를 제거한 단어가 실제로 존재하는 단어인지 확인하여, 없으면 단수자동변환 작업을 중지할 수 있도록 수정하는 코드를 구현하고자 한다.

## <div id = "Status">5. 프로젝트 진행과정</div>
### 프로젝트 선정 과정
  * 회의를 통해 개인별로 조사한 프로젝트를 발표하고, 팀원들의 의견을 종합하여 프로젝트 선정 (~5/13)
  * 조사한 프로젝트 중 [word_cloud][word_cloud]와 [free-python-games][free-python-games]로 의견을 종합 (5/13)
  * 하나의 주제로 팀 프로젝트를 진행한다는 답변을 받아, 추가 회의를 통해 word_cloud를 팀 프로젝트로 선정 (5/22)
### #1 한글로 word_cloud 구현
  * 한글 wordcloud 구현을 위한 준비 - 저장소에 한글 기사와 소설 업로드 및 한글 글꼴 파일(NotoSansKR, GmarketSans) 추가 (5/30)
  * konlpy 라이브러리를 활용하여 주어진 텍스트 파일에서 단어를 추출하고 띄어쓰기 단위로 구분하여 하나의 텍스트 파일로 다시 구성 (~5/30)
  * kr_wordcloud2.py 일부 수정 및 추가 구현 (~5/30)
> 1. Hannaum --> Hannanum<br>
> 2. ListtoString의 str= " " (띄어쓰기 추가)<br>
> 3. font path 추가<br>
> 4. wordcloud 함수 추가<br>
  * wordcloud plotting에 대한 코드 구현 마무리 및 선택한 이미지파일에 wordcloud를 그리는 코드를 추가 구현 (~6/6)<br>
> 소설 소나기와 나뭇잎 이미지의 wordcloud 구현 예시<br>
> ![leaves][leaves]
### #2 word_cloud 한글 문서화
* Blog Post 앞 부분 한글 문서화 진행[(click)][doc1] (5/31)<br>
* word_cloud website의 Command Line Interface 항목 한글 문서화[(click)][doc2] (~6/4)<br>
* word_cloud website의 Gallery of Examples 항목 한글 문서화[(click)][doc3] (~6/6)<br>
* Blog Post 뒷 부분 한글 문서화[(click)][doc4] (~6/7)
### #3 Readme/Wiki/정적페이지 관리
* README.md에 word_cloud 설치 방법 추가 (5/28)<br>
* README.md에 프로젝트 기여 방법 구체화 (6/6)<br>
* 정적페이지 게시물 분류의 필요성으로 Jekyll Theme 변경 (6/7)
### #4 Plural Issue 해결
* 원 프로젝트 검색 후 [Issue][issue2] 등록 (5/22)<br>
* Issue 내 활발한 토론 진행 (~5/30)<br>
* Plural Issue bug 수정 코드 구현[(click)][pr1] (~6/7)<br>
* Code Review 및 업로드 [(click)][pr2](6/7)
> **virus에 관한 사전의 텍스트를 이용한 바이러스 이미지의 wordcloud 구현 예시**<br>
> <br>
> ![virus_b][virus_b]<br>
> Plural Issue 해결 전 이미지. viru 단어 하나로 인해 모든 virus 단어가 viru로 묶여버리는 현상 발생<br>
> ![virus][virus]<br>
> Plural Issue 해결 후 이미지. viru같은 잘못된 단어는 처리하지 않도록 작업하였다.

[example]: https://github.com/amueller/word_cloud/blob/master/examples/alice.png
[issue1]: https://github.com/amueller/word_cloud/issues/238
[example2]: https://github.com/davidshyn1/davidshyn1.github.io/blob/master/assets/img/word_cloud%ED%95%9C%EA%B8%80%EB%B2%84%EC%A0%84.png
[issue2]: https://github.com/20-1-SKKU-OSS/2020-1-OSS-5/issues/2
[konlpy]: https://github.com/konlpy/konlpy
[word_cloud]: https://github.com/amueller/word_cloud
[free-python-games]: https://github.com/grantjenks/free-python-games
[leaves]: https://github.com/20-1-skku-oss/2020-1-OSS-5/blob/master/word_cloud/kor_text/image/%EB%82%98%EB%AD%87%EC%9E%8E%EB%B9%84%EA%B5%90.jpg
[virus_b]: https://github.com/20-1-skku-oss/2020-1-OSS-5/blob/master/Github_Page/images/virus_before.png
[virus]: https://github.com/20-1-skku-oss/2020-1-OSS-5/blob/master/Github_Page/images/virus.png
[doc1]: https://20-1-skku-oss.github.io/2020-1-OSS-5/blog-post/
[doc2]: https://20-1-skku-oss.github.io/2020-1-OSS-5/installation-and-command-line-interface
[doc3]: https://20-1-skku-oss.github.io/2020-1-OSS-5/Gallery-of-Examples/
[doc4]: https://20-1-skku-oss.github.io/2020-1-OSS-5/blog-post-2/
[pr1]: https://github.com/20-1-SKKU-OSS/2020-1-OSS-5/pull/50
[pr2]: https://github.com/20-1-SKKU-OSS/2020-1-OSS-5/pull/52
