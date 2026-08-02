@echo off

cd /d "C:\FILES\INTERNSHIP\DA_Infotact_Internship_Project_Atmosync_Repo\atmosync_dbt"

call "C:\Users\vinud\dbt_env\Scripts\activate.bat"

dbt run
dbt test

pause