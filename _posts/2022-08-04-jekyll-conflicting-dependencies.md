---
layout: post
title:  "Bundler could not find compatible versions for gem 'jekyll-feed'"
date:   2022-08-04 19:28:30 +0300
categories: jekyll bug solved
---
# Bug
While trying to install gem `github-pages` needed to deploy this site, I ran into dependency conflict
```bash
Bundler found conflicting requirements for the Ruby version:
  In Gemfile:
    github-pages was resolved to 1, which depends on
      Ruby (~> 1.9.3)

    jekyll-feed (~> 0.12) was resolved to 0.16.0, which depends on
      Ruby (>= 2.5.0)

  Current Ruby version:
    Ruby (= 3.0.0)

Bundler could not find compatible versions for gem "jekyll-feed":
  In snapshot (Gemfile.lock):
    jekyll-feed (= 0.16.0)

  In Gemfile:
    github-pages was resolved to 36, which depends on
      jekyll-feed (= 0.2.3)

    minima (~> 2.5) was resolved to 2.5.1, which depends on
      jekyll-feed (~> 0.9)

Deleting your Gemfile.lock file and running `bundle install` will rebuild your snapshot from scratch, using only
the gems in your Gemfile, which may resolve the conflict.
```

# Solution
Comment out this line in `Gemfile`:
```ruby
# gem "jekyll", "~> 3.9.2"
```

Gem `github-pages` will import older version of jekyll and everything should work normally.

Apparently, gem `github-pages` relies on old version of jekyll, and imports it. I don't know why is it done this way. It's mentioned in Gemfile comments, though. But I rarely read comments in Gemfile, because usually there is usually only broilerplate there.
