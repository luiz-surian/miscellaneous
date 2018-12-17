@echo off &setlocal
echo #############################################
echo # Checking PEP8 compliance with pycodestyle #
echo #############################################

setlocal enabledelayedexpansion
set COUNTER=0
set PASSED=0
set PERCENT=0

FOR %%G in (*.py) DO (
    set "fpath=%%G"
    set "fname=%%~nG"
    if "!fname!"=="!fname:ui_=!" (
        echo Checking "!fpath!"
	echo.
	set /A COUNTER=COUNTER+1
	pycodestyle "!fpath!" > tmp.txt
	for %%R in (tmp.txt) do (
		if not %%~zR lss 1 (
			type tmp.txt
		) else (
			echo PASS
			set /A PASSED=PASSED+1
		)
	)
	echo ---------------------------------------------
    )
)

del tmp.txt
set /A PERCENT=(PASSED*100)/COUNTER
echo QA: %PASSED% / %COUNTER% files passed (%PERCENT%%%)
echo.

endlocal
pause