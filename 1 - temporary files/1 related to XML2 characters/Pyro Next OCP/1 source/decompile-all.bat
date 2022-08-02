
rem @echo off
for %%x in (*.engb *.xmlb *.pkgb) do xmlb-compile -s -d %%x > %%x.src

