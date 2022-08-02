@echo off
setlocal enableDelayedExpansion
REM if "%~1" == "" if not exist *.igb EXIT


REM Settings:   valid terms: "true", "false"
REM ---------
REM Never use existing extraction.txt files
    set nevtxt=false
REM Extract animations with wrong names as well
    set extall=false


:checkAnimProducer
CLS
if not exist "%IG_ROOT%\bin\animationProducer.exe" (
	if not exist "%IG_ROOT%\animationProducer\DX\animationProducer.exe" (
		echo.
		echo "%IG_ROOT%\bin\animationProducer.exe" or "%IG_ROOT%\animationProducer\DX\animationProducer.exe" must exist. Please check your Alchemy 5 installation.
		goto fail
	)
)

:checkOptimizer
if not exist "%IG_ROOT%\bin\sgOptimizer.exe" (
	echo.
	echo "%IG_ROOT%\bin\sgOptimizer.exe" must exist. Please check your Alchemy 5 installation.
	goto fail
)

:checktxt
if "!nevtxt!" == "false" (
 if exist "%~dp0extract*.txt" (
  choice /m "Do you want to use an existing extraction database (extract.txt)"
  if not ERRORLEVEL 2 goto quickext
 )
)

:createOpt
(
echo [OPTIMIZE]
echo optimizationCount = 1
echo hierarchyCheck = true
echo 
echo [OPTIMIZATION1]
echo name = igEnbayaCompressAnimations
echo quantizationError = 0.0001
echo sampleRate = -1
echo forceTrackCount = -1
echo printStatistics = true
echo ignoreBones = 
echo specialCaseIniFilename = 
echo separator = :
echo sortColumn = -1
) > "%~dp0list_animations.ini"

for %%p in (%*) do 2>nul pushd "%~1" && goto isfolder || goto isfiles

:isbatch
for %%i in (*.igb) do (
 call :readAnims "%%~fi"
 call :extractAnims "%%~fi"
)
goto end

:isfolder
for %%p in (%*) do (
 for %%i in ("%%~p\*.igb") do (
  call :readAnims "%%~fi"
  call :extractAnims "%%~fi"
 )
)
goto end

:isfiles
for %%i in (%*) do (
 call :readAnims "%%~fi"
 call :extractAnims "%%~fi"
)
goto end


:readAnims
CLS
REM the animationProducer needs the file locally and without spaces:
set "filespaces=%~n1"
set "igbfile=!filespaces: =_!"
if /i not "%~f1" == "%~dp0!igbfile!.igb" (
 copy "%~f1" "%~dp0!igbfile!.igb"
 if errorlevel 1 echo %~nx1 includes spaces in the filename. Please remove them. & goto fail
)

echo Extracting animations from %~nx1...
("%IG_ROOT%\bin\sgOptimizer.exe" "%~dp0!igbfile!.igb" "%~dp0!igbfile!.tmp.igb" "%~dp0list_animations.ini") > "%~dp0!igbfile!.txt"

(call :writeAnims) > "%~dp0extract-%~n1.txt"
EXIT /b

:writeAnims
echo create_animation_database				!igbfile!
echo load_actor								!igbfile!.igb
echo extract_skeleton						defaultSkeleton
mkdir "%~dp0!igbfile!" > nul 2> nul
for /f "delims=:" %%a in ('findstr /n "configured" "%~dp0!igbfile!.txt"') do set skipl=%%a
for /f "skip=%skipl% tokens=1-3 usebackq" %%a in ("%~dp0!igbfile!.txt") do (
 (echo %%a | find "---------------------------------------------------------------" && EXIT /b)>nul
 if not "%%a" == "Name" (
  if "%%a" == "Skipping" (
   set skippedanimname=%%c
   set animname=!skippedanimname:~1,-1!
  ) else (
   set animname=%%a
  )
 )
 if "!extall!" == "false" (
  findstr /i "\<!animname!\>" "%~dp0_animations.txt" >nul
  if not errorlevel 1 (
   echo extract_animation						!animname!
   echo save_external_animation_database		!igbfile!\!animname!.igb
   echo remove_animation						!animname!
  )
 ) else (
  echo extract_animation						!animname!
  echo save_external_animation_database		!igbfile!\!animname!.igb
  echo remove_animation						!animname!
 )
)
EXIT /b

:extractAnims
cd /d "%~dp0"
"%IG_ROOT%\bin\animationProducer.exe" "%~dp0extract-%~n1.txt"

REM Remove duplicate temporary files:
if /i not "%~f1" == "%~dp0!igbfile!.igb" del "%~dp0!igbfile!.igb"
del "%~dp0!igbfile!.tmp.igb"
del "%~dp0!igbfile!.txt"
REM del "%~dp0extract-%~n1.txt"
endlocal
EXIT /b


:quickext
if exist "%~dp0extract.txt" (
 "%IG_ROOT%\bin\animationProducer.exe" "%~dp0extract.txt"
) else (
 for %%t in ("%~dp0extract*.txt") do (
  set loop=
  for /f "usebackq tokens=1*" %%a in ("%%~ft") do (
   if not "!loop!" == "done" (
    set "extfile=%%~nt"
    if not "%%b" == "!extfile:~8!" move "!extfile:~8!.igb" "%%b.igb" & set "igbfile=%%b.igb"
    cd /d "%~dp0"
    mkdir %%b > nul 2> nul
    "%IG_ROOT%\bin\animationProducer.exe" "%%~ft"
    set loop=done
	move "%%b.igb" "!extfile:~8!.igb"
   )
  )
 )
)
goto end


:fail
endlocal
echo.
echo Failed to complete.
Pause
EXIT

:end
endlocal
del "%~dp0list_animations.ini"