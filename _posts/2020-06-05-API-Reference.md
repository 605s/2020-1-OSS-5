---
layout: post
title: "[한글 문서화] API Reference"
tags: [Documentation]
---

>word_cloud GitHub Page의 [API Reference][API] 항목을 한국어로 번역 및 보완한 문서입니다.
<hr>

[toc]


## API Reference
모든 기능은 WordCloud 클래스에 캡슐화되어 있습니다.

|---|---|
|[`WordCloud`](#wordcloud.wordcloud)([font_path, width, height, …])|생성 및 그리기를 위한 Word Cloud 객체|
|[`ImageColorGenerator`](#wordcloud.ImageColorGenerator)(image[, default_color])|컬러 이미지를 기반으로 한 컬러 생성기|
|[`random_color_func`](#wordcloud.random_color_func)([word, font_size, …])|임의의 색조 색상 생성|
|`colormap_color_func`||
|[`get_single_color_func`](#wordcloud.get_single_color_func)(color)|단일 색조와 채도를 반환하는 color function을 생성|
<br>



[API]: http://amueller.github.io/word_cloud/references.html
