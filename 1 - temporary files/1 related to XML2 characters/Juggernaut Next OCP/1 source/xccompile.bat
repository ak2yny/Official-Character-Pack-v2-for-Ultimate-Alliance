@echo off
if .%1==. goto xhlp
set f=%1
for %%x in (%f%) do xmlb-compile %%x %%~nx
for %%x in (%f%) do echo new.%%~nx xml created
goto xend
:xhlp
echo %0 file.engb.src
:xend