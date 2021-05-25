#! /bin/bash

pygettext -d base -o locales/base.pot extensions/faq.py

msgmerge locales/en/LC_MESSAGES/base.po locales/base.pot -U --no-fuzzy-matching
msgmerge locales/ar/LC_MESSAGES/base.po locales/base.pot -U --no-fuzzy-matching

msgfmt locales/en/LC_MESSAGES/base.po -o locales/en/LC_MESSAGES/base.mo
msgfmt locales/ar/LC_MESSAGES/base.po -o locales/ar/LC_MESSAGES/base.mo
