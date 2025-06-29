[app]
title = FarmAccountingApp
package.name = farmaccounting
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,sqlite3
version = 1.0
requirements = python3,kivy,sqlite3
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.minapi = 19
android.arch = armeabi-v7a
android.minapi = 21
android.api = 30
android.sdk = 24
android.ndk = 23b
android.debug = 1

[buildozer]
log_level = 2
warn_on_root = 1
android.debug = 1
