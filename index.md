---
#
# By default, content added below the "---" mark will appear in the home page
# between the top bar and the list of recent posts.
# To change the home page layout, edit the _layouts/home.html file.
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: home
---

This website is the anchor for my internet presence and a platform for my writings, projects, and notebooks.

# Blog posts by topics

<ul class="topic_list">
  {% for topic in site.data.topics %}
    <li>
      <a href="/topics/{{ topic.slug }}">{{ topic.name }}</a>
    </li>
  {% endfor %}
</ul>

# Blog posts

<ul class="spaced_list">
  {% for post in site.categories.blog %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> {{ post.date | date_to_long_string }}
    </li>
  {% endfor %}
</ul>
