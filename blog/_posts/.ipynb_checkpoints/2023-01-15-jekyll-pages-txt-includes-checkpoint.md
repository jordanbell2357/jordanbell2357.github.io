---
layout: post
title: "Including text in Jekyll pages using _includes"
---

# TSV

`cities.tsv`

<pre>
{% include txt/cities.tsv %}
</pre>

`phonebook.tsv`

<pre>
{% include txt/phonebook.tsv %}
</pre>

`join phonebook.tsv cities.tsv > output1.tsv`

<pre>
{% include txt/output1.tsv %}
</pre>

# CSV

`cities.csv`

<pre>
{% include txt/cities.csv %}
</pre>

`phonebook.csv`

<pre>
{% include txt/phonebook.csv %}
</pre>

`join -t , phonebook.csv cities.csv > output1.csv`

<pre>
{% include txt/output1.csv %}
</pre>

`phonebookA.csv`

<pre>
{% include txt/phonebookA.csv %}
</pre>

`join -t , -1 2 -2 1 phonebookA.csv cities.csv > output2.csv`

<pre>
{% include txt/output2.csv %}
</pre>

---

[Includes \| Jekyll](https://jekyllrb.com/docs/includes/)