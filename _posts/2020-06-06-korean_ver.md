---
layout: post
title: "[한글 기능 구현] 한글 기능 구현 과정"
tags: [Documentation]
---
> 한글 기능 구현에 대한 설명 내용을 포함한 문서입니다.
<hr>

Word Cloud 프로젝트는 긴 글(문장)을 tokenize 수행하여, 단어 등장 횟수에 따라 글자 크기를 조정하여 word cloud를 생성하도록 하는 프로젝트이기에,
각 언어의 특성과 문장 형태에 따라 word cloud가 제대로 수행되지 않을 확률이 높다.
해당 [issue][issue1]에 의하면 영어 기반의 프로젝트이기에,
다양한 언어의 특성을 적절하게 반영하지 못하고 있으며 이에 따라 상당 부분 word cloud의 기본 수행능력이 발휘되지 않은 경우가 간혹 발생된다.
다음 그림에서 한글 글꼴로 한글 text를 실행할 시 생기는 문제점을 발견할 수 있다.<br>
![example2][example2]

위의 예시는 황순원의 소설 소나기의 내용을 wordcloud로 구현한 그림이다.<br>
위의 그림에서 눈에 띄는 것은 '소녀', '소년'이라는 단어가 많이 들어가 있는데 '소녀가', '소녀는' 등의 단어가 구분되어 나와있다.
여기서 원 프로젝트에서 한글로 구현할 때 나타나는 문제점이 생긴다.

한글의 문장 특성 중에 '조사'라는 품사는 항상 명사, 형용사, 부사뒤에 붙여서 사용된다는 특성이 있다.
그래서 한글 자연어처리 과정에서, 조사는 필히 앞에 붙여진 단어와 분리하여 처리되어야 한다.
하지만 단어 등장 빈도를 측정할 때, 조사를 포함한 하나의 어절로 구분하여 빈도를 측정하게 된다.
그렇게 되면 예를 들어, '소녀는', '소녀가'라는 두 어절은 사실상 같은 '소프트웨어' 단어를 표현한 것인데
따로 구분하여 처리된다.

이는 확실히, 본 코드에 한글NLP 기능이 없기 때문에 나타난 현상이라 볼 수 있다.
영어 NLP의 경우, 띄어쓰기를 기준으로, 단어가 구분되기 때문에 단어 구분에 있어서 어렵지 않게 처리할 수 있다.
그러나 한글의 단어구분은 띄어쓰기가 아니기 때문에, 한글 NLP 기능을 추가 구현하는 것이 불가피하다.

한글 NLP 패키지 중 [konlpy][konlpy]라는 패키지가 있다.
해당 패키지도 역시나 오픈소스프로젝트로 활발히 진행 중인 패키지나, 상당 부분 한글 NLP 기능을 구현할 만큼 유용한 패키지다.
konlpy 패키지에서 해당 text를 명사와 나머지를 구분하여 명사만을 추출하도록 할 수 있는 Hannanum 모듈을 사용하였다.

```
    h = Hannanum()
    list_nouns = h.nouns(sample)
```

Hannanum 모듈을 통해 명사들만을 추출하는 list형태로 나오게 되는데,
원프로젝트의 wordcloud를 실행하기 위해서는 list형태의 현재 결과물을 다시 string형태로 변환하여 wordcloud함수에 인수로 활용해야 한다.

```
def listToString(list1):
    str=" "
    return (str.join(list1))
```
이후, 글꼴 형태를 한글 출력이 가능한 글꼴로 설정한 후, wordcloud를 실행하면 된다.

다음의 예시는 황순원의 소나기 text 파일을 한글 버전 기능 구현 코드에 인수로 받아서 실행하였을 때 나오는 결과물이다.
![rain][rain] <br>
![leaves2][leaves2] <br>
![leaves3][leaves3] <br>

첫번째 그림은 소나기 text 파일을 인수로 받아 직접 실행한 결과로, 특정 그림없이 일반적이고 단순한 결과물이다. 두번째 그림은 소나기 text 파일을 인수로 받아 직접 실행한 결과로, 나뭇잎.jpg를 background image로 하였고, 색깔변화를 주지 않았다. 세번째 그림은 소나기 text 파일을 인수로 받아 직접 실행한 결과로, 나뭇잎.jpg를 background image로 하였고, 글자 색깔을 기존 나뭇잎 색깔과 동일하게 하도록 색깔변화를 주었다.

위의 NLP기능을 활용하지 않고 그대로 wordcloud를 실행하여 출력된 예시와 비교할 때,
한글 NLP기능을 활용하여 출력된 예시는 조사 등 불필요한 품사들은 사전에 삭제되고, 명사, 부사 위주의 단어로 재구성하였음을 알 수 있다.
또한 조사 등을 삭제하게 되면서 겹치는 단어들이 추가되어 더 확실한 wordcloud를 구성하게 됨을 알 수 있다.

[example2]: https://github.com/20-1-SKKU-OSS/2020-1-OSS-5/blob/gh-pages/images/prev_example.png?raw=true
[issue1]: https://github.com/amueller/word_cloud/issues/238
[konlpy]: https://github.com/konlpy/konlpy
[rain]: https://github.com/20-1-SKKU-OSS/2020-1-OSS-5/blob/gh-pages/images/kor_example.png?raw=true
[leaves2]: https://github.com/20-1-SKKU-OSS/2020-1-OSS-5/blob/gh-pages/images/kor_example_leaves.png?raw=true
[leaves3]: https://github.com/20-1-SKKU-OSS/2020-1-OSS-5/blob/gh-pages/images/kor_example_leaves_green.png?raw=true
