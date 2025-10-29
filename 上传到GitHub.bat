@echo off
chcp 65001 >nul
cls
echo ========================================
echo   Upload to GitHub - Quick Script
echo ========================================
echo.
echo This script will help you upload the project to GitHub.
echo.
echo ========================================
echo   Prerequisites:
echo ========================================
echo.
echo 1. You have a GitHub account
echo 2. You have created a repository
echo 3. Git is installed on your computer
echo.
echo ========================================
echo.

REM Check if Git is installed
where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Git is not installed!
    echo.
    echo Please download and install Git from:
    echo https://git-scm.com/download/win
    echo.
    pause
    exit /b 1
)

echo [OK] Git is installed
echo.

REM Check if already initialized
if exist ".git" (
    echo [INFO] Git repository already initialized
    echo.
    goto :commit
)

echo ========================================
echo   Step 1: Initialize Git Repository
echo ========================================
echo.

git init
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to initialize Git repository
    pause
    exit /b 1
)

echo [OK] Git repository initialized
echo.

:commit
echo ========================================
echo   Step 2: Add Files
echo ========================================
echo.

git add .
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to add files
    pause
    exit /b 1
)

echo [OK] Files added
echo.

echo ========================================
echo   Step 3: Commit Changes
echo ========================================
echo.

git commit -m "Initial commit: Dual Video Player Android version"
if %ERRORLEVEL% NEQ 0 (
    echo [INFO] No changes to commit or commit failed
)

echo.

echo ========================================
echo   Step 4: Add Remote Repository
echo ========================================
echo.
echo Please enter your GitHub repository URL:
echo Example: https://github.com/username/dual-video-player-android.git
echo.
set /p REPO_URL="Repository URL: "

if "%REPO_URL%"=="" (
    echo [ERROR] Repository URL cannot be empty
    pause
    exit /b 1
)

REM Check if remote already exists
git remote get-url origin >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [INFO] Remote 'origin' already exists, updating...
    git remote set-url origin %REPO_URL%
) else (
    git remote add origin %REPO_URL%
)

if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to add remote repository
    pause
    exit /b 1
)

echo [OK] Remote repository added
echo.

echo ========================================
echo   Step 5: Push to GitHub
echo ========================================
echo.

git branch -M main
git push -u origin main

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Failed to push to GitHub
    echo.
    echo Possible reasons:
    echo 1. Authentication failed (need to login)
    echo 2. Repository doesn't exist
    echo 3. No internet connection
    echo.
    echo Please check and try again manually:
    echo   git push -u origin main
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   SUCCESS!
echo ========================================
echo.
echo Your project has been uploaded to GitHub!
echo.
echo Next steps:
echo 1. Go to your GitHub repository
echo 2. Click on "Actions" tab
echo 3. Wait for the build to complete (20-30 minutes)
echo 4. Download the APK from Artifacts
echo.
echo Repository URL: %REPO_URL%
echo.
echo ========================================
pause
