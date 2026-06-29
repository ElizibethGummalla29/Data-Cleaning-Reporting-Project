@echo off

echo Starting Data Cleaning...

python scripts/data_cleaning.py


echo.
echo Generating Reports...

python scripts/report_generation.py


echo.
echo Project Completed Successfully!

pause