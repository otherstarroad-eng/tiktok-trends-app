[app]
title = USA TikTok Trends Generator
package.name = tiktoktrends
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,openssl,requests,urllib3
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
