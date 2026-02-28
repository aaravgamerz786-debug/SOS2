[app]
title = SOS App
package.name = sosapp
package.domain = org.sos
source.dir = .
source.include_exts = py
version = 1.0
requirements = python3,kivy==2.2.1,pyjnius
orientation = portrait
android.permissions = WAKE_LOCK
android.api = 31
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True
android.archs = arm64-v8a
log_level = 2

[buildozer]
log_level = 2
