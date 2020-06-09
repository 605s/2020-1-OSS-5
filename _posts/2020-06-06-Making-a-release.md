---
layout: post
title: "[한글 문서화] Making a release"
tags: [WordCloud Docs]
---

>word_cloud GitHub Page의 [Making a release][MR] 항목을 한국어로 번역 및 보완한 문서입니다.
<hr>

## Making a release
<hr>

### 
<hr>

### 
<hr>

### PyPI : 단계별 설명


1． 모든 CI 테스트([AppVeyor][AppVeyor], [CircleCI][CircleCI] 및 [Travis CI][Travis CI])를 통과했는지 확인하십시오.
<br>

2． 버전별로 정렬된 모든 태그를 나열하십시오.

```
$ git tag -l | sort -V
```
<br>

3． 다음 릴리스 버전 번호를 선택하십시오.

```
release=X.Y.Z
```
<br>

><span style="color:red">**Warning**</span><br>
>패키지가 PyPI에 업로드되도록 하려면 태그가 이 정규식과 일치해야합니다.<br>
>`^[0-9]+(\.[0-9]+)*(\.post[0-9]+)?$`
<br>

4． 최신 소스 다운로드

```
cd /tmp && git clone git@github.com:amueller/word_cloud && cd word_cloud
```
<br>

5． *doc/changelog.rst*에서 `Next Release` 섹션 헤더를 `WordCloud X.Y.Z`로 변경한 후 동일한 이름을 사용하여 변경을 commit합니다.

```
$ git add doc/changelog.rst
$ git commit -m "WordCloud ${release}"
```
<br>

6． 릴리스 태그

```
$ git tag --sign -m "WordCloud ${release}" ${release} master
```
<br>

><span style="color:blue">**Note**</span><br>
>태그에 서명하려면 GPG 키를 사용하는 것이 좋습니다.
<br>

7． 태그 게시

```
$ git push origin ${release}
```
<br>

><span style="color:blue">**Note**</span><br>
>그러면 각 CI 서비스에서 빌드가 시작되고 PyPI에서 휠 및 소스 배포가 자동으로 업로드됩니다.
<br>

8． AppVeyor, CircleCI 및 Travis CI에서 빌드 상태를 확인하십시오.
<br>

9． 빌드가 완료되면 PyPI에서 배포가 가능한지 확인하십시오.
<br>

10． 깨끗한 테스트 환경을 만들어 설치를 테스트하십시오.

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

11． 정리하기

```
$ deactivate  && \
  rm -rf dist/* && \
  rmvirtualenv wordcloud-${release}-install-test
```
<br>

12． *doc/changelog.rst*에 `Next Release` 섹션을 다시 추가하고 결과를 merge하고 로컬 변경사항을 push하십시오.

```
$ git push origin master
```


[MR]: http://amueller.github.io/word_cloud/make_a_release.html#
[AppVeyor]: https://ci.appveyor.com/project/amueller/word-cloud/history
[CircleCI]: https://circleci.com/gh/amueller/word_cloud
[Travis CI]: https://travis-ci.org/amueller/word_cloud/pull_requests
[virtualenvwrapper]: https://virtualenvwrapper.readthedocs.io/en/latest/
[virtualenv]: https://virtualenv.pypa.io/en/latest/
[venv]: https://docs.python.org/3/library/venv.html
