@echo off
if .%1==. goto xhlp
xmlb-compile -d %1 > %1.src
echo %1.src xml source created
goto xend
:xhlp
echo %0 file.engb
:xend