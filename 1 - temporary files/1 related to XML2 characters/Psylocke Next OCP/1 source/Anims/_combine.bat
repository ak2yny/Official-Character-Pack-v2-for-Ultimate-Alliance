@echo off
setlocal enableDelayedExpansion


REM Settings:   valid terms: "true", "false"
REM ---------
REM Delete copied/duplicate individual animation files
    set deligb=false


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
 if exist "%~dp0combine.txt" (
  choice /m "Do you want to use the existing combine database (combine.txt)"
  if not ERRORLEVEL 2 goto combineanim
 )
)

for %%p in (%*) do 2>nul pushd "%~1" && goto isfolder || goto isfiles

:isbatch
call :combineFolder "%~dp0"
goto end

:isfolder
for %%p in (%*) do (
 call :combineFolder "%%~p\"
)
goto end

:isfiles
set filename=%~dp1
call :askFilename
(call :writeTop) > "%~dp0combine.txt"
for %%i in (%*) do (
 (call :writeFiles "%%~fi") >> "%~dp0combine.txt"
 copy "%%~fi" "%~dp0"
)
call :combineAnims "%~dp0"
if "!deligb!" == "true" for %%i in (%*) do (if not "%%~dpi" == "%~dp0" del "%~dp0%%~nxi")
goto end


:combineFolder
set filename=%~1
call :askFilename
(call :writeTop) > "%~1combine.txt"
for %%i in ("%~1*.igb") do (
 (call :writeFiles "%%~fi") >> "%~1combine.txt"
)
call :combineAnims "%~1"
Exit /b

:askFilename
for %%f in ("!filename:~0,-1!") do set filename=%%~nf
set /p filename=Please enter the name you want to save your new animation set as (without extension). Press enter to use !filename!: 
CLS
echo Creating combine list for !filename!...
Exit /b

:writeTop
echo create_animation_database				!filename!
echo load_actor								_fightstyle_default
echo extract_skeleton						defaultSkeleton
Exit /b

:writeFiles
echo load_actor								%~nx1
echo extract_animation						%~n1
Exit /b

:combineAnims
(
echo save_external_animation_database		!filename!.igb
) >> "%~1combine.txt"

if not "%~1" == "%~dp0" copy "%~dp0_fightstyle_default" "%~1"
cd /d "%~1"
"%IG_ROOT%\bin\animationProducer.exe" combine.txt
if not "%~1" == "%~dp0" del "%~1_fightstyle_default"
Exit /b


:fail
endlocal
echo.
echo Failed to complete.
Pause
EXIT

:end
endlocal
pause