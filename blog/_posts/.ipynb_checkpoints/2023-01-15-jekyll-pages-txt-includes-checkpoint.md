---
layout: post
title: "Including text in Jekyll pages using _includes"
---

# TSV

`cities.tsv`

<pre>
{% include txt/cities.tsv %}
</pre>

```bash
cut -f1 cities.tsv > output1
```

<pre>
{% include txt/output1 %}
</pre>

```bash
cut -f2 cities.tsv > output2
```

<pre>
{% include txt/output2 %}
</pre>

`phonebook.tsv`

<pre>
{% include txt/phonebook.tsv %}
</pre>

```bash
join --header phonebook.tsv cities.tsv > output3
```

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

```bash
join -t , --header phonebook.csv cities.csv > output1.csv
```

<pre>
{% include txt/output1.csv %}
</pre>

`phonebookA.csv`

<pre>
{% include txt/phonebookA.csv %}
</pre>

```bash
join -t , -1 2 -2 1 --header phonebookA.csv cities.csv > output2.csv
```

<pre>
{% include txt/output2.csv %}
</pre>

---

[Includes \| Jekyll](https://jekyllrb.com/docs/includes/)

[join invocation \| GNU Coreutils 9.1](https://www.gnu.org/software/coreutils/manual/html_node/join-invocation.html)