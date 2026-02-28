[app]
title = SOS App
package.name = sosapp
package.domain = org.sos

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 1

android.permissions = WAKE_LOCK

android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True

log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
warn_on_root = 1
