@echo off
echo ##############################
echo #     Convert .ui to .py     #
echo ##############################


for %%f in (./*.ui) do (
	echo Converting %%~nf
	pyuic5 %%f -o %%~nf.py
	echo ------------------------------
)