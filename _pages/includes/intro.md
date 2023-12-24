{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}
{% assign url_hindex = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio_hindex.json" %}
{% assign url_i10 = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio_i10.json" %}

<p style="text-align:justify">
<i class="fas fa-quote-left fa-2x fa-pull-left fa-border" aria-hidden="true"></i>
I am a DPhil student at the <a href='https://www.kennedy.ox.ac.uk'>Kennedy institute</a>, University of Oxford, under the supervision of <a href='https://www.kennedy.ox.ac.uk/team/tonia-vincent'>Tonia Vincent (FRCP, Prof)</a>, <a href='https://scholar.google.co.uk/citations?user=jMFx-usAAAAJ'>Ngee Han Lim (PhD)</a> and <a href='https://www.bdi.ox.ac.uk/Team/bartek-papiez'>Bartlomiej W. Papiez (Assoc Prof)</a>. 
<br>
Prior to this, I obtained my MRes degree at the <a href='https://www.imperial.ac.uk/hamlyn-centre'>Hamlyn Center for Robotic Surgery</a>, Imperial College London, under the supervision of <a href='https://imr.sjtu.edu.cn/en/ab_lead/210.html'>Guang-Zhong Yang (CBE, FREng, FIEEE, Prof)</a>, 
and a BEng degree at University of Liverpool, with my final year project supervised by <a href='https://www.liverpool.ac.uk/electrical-engineering-and-electronics/staff/lin-jiang/'>Lin Jiang (PhD)</a> and my second year project supervised by <a href='https://gr.xjtu.edu.cn/web/shusenyang'>Shusen Yang (Prof)</a>.
<br>
My current research interests are in biomedical data analysis and computational biology, with an emphasis on the computational models and machine learning approaches. 
<i class="fas fa-quote-right fa-2x fa-pull-right fa-border" aria-hidden="true"></i>
</p>

- <i>Citation statistics:</i>
<a href='https://scholar.google.com/citations?user=2bNsYR0AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>
\|
<a href='https://scholar.google.com/citations?user=2bNsYR0AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url_hindex | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=h-index"></a>
\|
<a href='https://scholar.google.com/citations?user=2bNsYR0AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url_i10 | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=i10-index"></a>
