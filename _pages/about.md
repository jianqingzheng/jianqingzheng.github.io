---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}
{% assign url_hindex = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio_hindex.json" %}
{% assign url_i10 = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio_i10.json" %}

<span class='anchor' id='about-me'></span>
{% include_relative includes/intro.md %}

___
<span class='anchor' id='news'></span>
{% include_relative includes/news.md %}

___
---
{% include_relative includes/pubs.md %}


___
---
{% include_relative includes/awards.md %}

___
---
{% include_relative includes/education.md %}

___
---
{% include_relative includes/talks.md %}

___
---
{% include_relative includes/service.md %}

___
---
{% include_relative includes/works.md %}

___
---
{% include_relative includes/acknowledge.md %}