---
layout: post
title: "[한글 문서화] Making a release"
tags: [WordCloud Docs]
---

>word_cloud GitHub Page의 [Making a release][MR] 항목을 한국어로 번역 및 보완한 문서입니다.
<hr>

## Making a release


이 문서는 wordcloud python 패키지의 릴리스 작성을 통해 기여자를 안내합니다.

핵심 개발자는 생성을 트리거하고 wordcloud의 X.Y.Z 릴리스를 [PyPI][PyPI]에 업로드하기 위해 이 단계들을 밟아야 합니다.
<hr>

### 설명서 규칙


아래에 보고되는 커멘드 명령은 동일한 터미널 세션에서 평가되야합니다.

평가될 명령은 달러 기호로 시작합니다. 예를 들면 다음과 같습니다.

```
$ echo "Hello"
Hello
```

`echo "Hello"`가 터미널에서 복사 및 평가되야 함을 의미합니다.
<hr>

### 환경 설정


1．[먼저 PyPI에 계정을 등록하십시오][register].
<br>

2．아직 사례가 아닌 경우, `Package Index Maintainer`으로 추가되도록 요청하십시오.
<br>

3．로그인 자격 증명으로 `~/.pypirc` 파일을 만듭니다.

```
[distutils]
index-servers =
  pypi
  pypitest

[pypi]
username=<your-username>
password=<your-password>

[pypitest]
repository=https://test.pypi.org/legacy/
username=<your-username>
password=<your-password>
```

PyPI 계정이 `<your-username>`와 `<your-password>`입니다.
<hr>

### PyPI : 단계별 설명


1．모든 CI 테스트([AppVeyor][AppVeyor], [CircleCI][CircleCI] 및 [Travis CI][Travis CI])를 통과했는지 확인하십시오.
<br>

2．버전별로 정렬된 모든 태그를 나열하십시오.

```
$ git tag -l | sort -V
```
<br>

3．다음 릴리스 버전 번호를 선택하십시오.

```
release=X.Y.Z
```
<br>

><span style="color:red">**Warning**</span><br>
>패키지가 PyPI에 업로드되도록 하려면 태그가 이 정규식과 일치해야합니다.<br>
>`^[0-9]+(\.[0-9]+)*(\.post[0-9]+)?$`
<br>

4．최신 소스 다운로드

```
cd /tmp && git clone git@github.com:amueller/word_cloud && cd word_cloud
```
<br>

5．*doc/changelog.rst*에서 `Next Release` 섹션 헤더를 `WordCloud X.Y.Z`로 변경한 후 동일한 이름을 사용하여 변경을 commit합니다.

```
$ git add doc/changelog.rst
$ git commit -m "WordCloud ${release}"
```
<br>

6．릴리스 태그

```
$ git tag --sign -m "WordCloud ${release}" ${release} master
```
<br>

><span style="color:blue">**Note**</span><br>
>태그에 서명하려면 GPG 키를 사용하는 것이 좋습니다.
<br>

7．태그 게시

```
$ git push origin ${release}
```
<br>

><span style="color:blue">**Note**</span><br>
>그러면 각 CI 서비스에서 빌드가 시작되고 PyPI에서 휠 및 소스 배포가 자동으로 업로드됩니다.
<br>

8．AppVeyor, CircleCI 및 Travis CI에서 빌드 상태를 확인하십시오.
<br>

9．빌드가 완료되면 PyPI에서 배포가 가능한지 확인하십시오.
<br>

10．깨끗한 테스트 환경을 만들어 설치를 테스트하십시오.

```
$ mkvirtualenv wordcloud-${release}-install-test && \
  pip install wordcloud && \
  python -c "import wordcloud;print(wordcloud.__version__)"
```
<br>

><span style="color:blue">**Note**</span><br>
>`mkvirtualenv`를 사용할 수 없으면 [virtualenvwrapper][virtualenvwrapper]가 설치되어 있지 않다는 의미입니다.<br>
>이 경우 이를 설치하거나 [virtualenv][virtualenv] 또는 [venv][venv]를 직접 사용할 수 있습니다.
<br>

11．정리하기

```
$ deactivate  && \
  rm -rf dist/* && \
  rmvirtualenv wordcloud-${release}-install-test
```
<br>

12．*doc/changelog.rst*에 `Next Release` 섹션을 다시 추가하고 결과를 merge하고 로컬 변경사항을 push하십시오.

```
$ git push origin master
```


[PyPI]: https://pypi.org/project/wordcloud/
[register]: https://pypi.org/
[MR]: http://amueller.github.io/word_cloud/make_a_release.html#
[AppVeyor]: https://ci.appveyor.com/project/amueller/word-cloud/history
[CircleCI]: https://circleci.com/gh/amueller/word_cloud
[Travis CI]: https://travis-ci.org/amueller/word_cloud/pull_requests
[virtualenvwrapper]: https://virtualenvwrapper.readthedocs.io/en/latest/
[virtualenv]: https://virtualenv.pypa.io/en/latest/
[venv]: https://docs.python.org/3/library/venv.html
