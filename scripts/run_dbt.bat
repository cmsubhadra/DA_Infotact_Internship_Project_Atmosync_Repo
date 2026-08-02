@echo off

cd /d "C:\Users\cmsub\Documents\GitHub\DA_Infotact_Internship_Project_Atmosync_Repo\atmosync_dbt"

call "C:\Users\cmsub\dbt_env\Scripts\activate.bat"

dbt run

pause