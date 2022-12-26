---
title: categories
layout: post
category: Guides
permalink: /categories/
lang: en
---
{% assign categories = site.pages | group_by: 'category' %}
{% for category in categories %}
  * {{ category.name }}
    {% for page in category.items %}
      * <a href="{{site.baseurl}}{{page.url}}">{{ page.title | escape }}</a>
    {% endfor %}
{% endfor %}
