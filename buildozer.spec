
[[app]
title = FarmAccountingApp
package.name = farmaccounting
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png
version = 1.0
requirements = python3,kivy,sqlite3
orientation = portrait
fullscreen = 0

# ✅ Add these lines if not already present:
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.minapi = 21
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1]
title = FarmAccountingApp
package.name = farmaccounting
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,sqlite3,db
version = 1.0
requirements = python3,kivy,sqlite3
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
