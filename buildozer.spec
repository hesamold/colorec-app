# (List of default directories to search for .py files)
# You can set this to 'src' if you want to store your main Python file in a sub-directory.
source.include_exts = py,png,jpg,kv,atlas

# (The title of your application)
# This is what will be displayed in the system when running the app.
app_name = ColorPicker

# (Package name)
# Unique identifier for your app, following the reverse domain notation.
# e.g., com.example.colorpicker
package = com.example.colorpicker

# (Package version)
# Version of your app. This should follow a scheme like `1.0.0` or `2.1.3`.
# Increment this number for each new release.
version = 1.0.0

# (The folder where your main Python file is stored)
# If your main Python file is in a sub-directory like `src`, change this.
source.dir = .

# (The file name of the main Python file)
# The Python file to run when the app starts.
# e.g., 'main.py' or whatever your entry script is.
# Make sure this is the same as your main Python file.
main.python_file = main.py

# (Set to True to include a splash screen, False to disable it)
# splashscreen = True

# (The icon to use for your app)
# Set this to the path of your app's icon (icon.png)
icon = %(source.dir)s/icon.png

# (Requirements)
# A list of Python packages that your app needs to run.
# E.g., kivy, requests, numpy, etc.
# In this case, the app is using kivy for the GUI.
requirements = kivy

# (Android permissions)
# If your app needs to request special permissions, list them here.
# For example, if you need to read files, you will need to add permissions.
android.permissions = INTERNET, ACCESS_NETWORK_STATE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (The minimum API level for your Android app)
# This will define the minimum Android version required for your app.
# Default is 21 (Android 5.0 Lollipop), which is fine for most modern devices.
android.minapi = 21

# (Package architecture)
# If you want to target specific architectures, you can specify them here.
# You can leave this as the default to target both ARMv7 and ARM64 devices.
android.arch = armeabi-v7a, arm64-v8a

# (Debugging configuration)
# By default, it creates a debug build. You can set this to False to build a release version.
debug = 1

# (Additional arguments to pass to build)
# If you want additional flags passed to the build process, you can specify them here.
# For instance, you can use --no-copy-deps to skip copying dependencies.
# However, this is usually not needed for standard builds.
# buildozer.android.extra_args = --no-copy-deps

# (Android NDK path)
# Set this to the correct path where you installed the Android NDK in your WSL.
# The NDK path should point to the location of the NDK in your system.
# You need to set the path in your system environment or in this file.
android.ndk_path = /path/to/android-ndk

# (Add any additional files or assets you want to include in your app)
# If you have any images, sounds, or other files, you can include them like this.
# e.g., source.include_exts = png,jpg,kv,atlas,sound

# (Python version)
# The version of Python to use for the app. In this case, we are using Python 3.
python.version = 3.9

# (Support for other platforms)
# If you want to add support for other platforms, uncomment and configure them here.
# iOS platform is unsupported for Windows users, so we leave it out.

# (Buildozer will make this app installable on Android, but you can also build for desktop or other platforms)
# It is possible to build a Windows version or others as well.

