# frozen_string_literal: true

source "https://rubygems.org"
gemspec

gem 'jekyll'

group :jekyll_plugins do
  gem 'jekyll-sitemap'
  gem 'jekyll-feed'
  gem 'jekyll-toc'
  gem 'jekyll-seo-tag'
end

gem "kramdown-parser-gfm" if ENV["JEKYLL_VERSION"] == "~> 3.9"
gem "webrick", "~> 1.7"