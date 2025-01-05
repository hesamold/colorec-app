[app]

# (str) Title of your application
title = Color Picker App

# (str) Package name
package.name = colorpicker

# (str) Package domain (used for namespace and package name)
package.domain = org.example

# (list) Application requirements
# These are additional dependencies needed for the app
requirements = python3,kivy,requests

# (list) List of inclusions using pattern matching
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version (needs to be updated on each release)
version = 1.0.0

# (str) Application identifier
android.package = org.example.colorpicker

# (str) Android NDK version
android.ndk = 21b

# (int) Target Android API
android.api = 30

# (str) Android SDK
android.sdk = 30

# (str) Android build tools
android.build_tools = 30.0.3

# (list) Additional Android permissions
android.permissions = INTERNET

# (list) Android extra libraries to be added (optional)
android.add_dependencies =

[buildozer]

# (int) Buildozer version
buildozer.version = 2.0.0
