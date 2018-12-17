@echo off

echo Building Executable
pyinstaller --windowed --onefile --icon=logo.ico --version-file=file_version_info.txt --name=foo_bar foo_bar.py
echo ..................................................

echo Script End
pause