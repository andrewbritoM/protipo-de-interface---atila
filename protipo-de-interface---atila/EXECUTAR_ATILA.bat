@echo off
title ATILA - Sistema de Gestao e Agendamento de Salas
color 0B

cd /d "%~dp0"

echo ==============================================
echo              ATILA
echo   Sistema de Gestao e Agendamento de Salas
echo ==============================================
echo.

where python >nul 2>nul
if errorlevel 1 (
    echo [ERRO] Python nao foi encontrado.
    echo Instale o Python 3.10 ou superior e marque "Add Python to PATH".
    pause
    exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
    echo [1/3] Criando ambiente virtual...
    python -m venv .venv
    if errorlevel 1 (
        echo [ERRO] Nao foi possivel criar o ambiente virtual.
        pause
        exit /b 1
    )
)

echo [2/3] Verificando dependencias...
".venv\Scripts\python.exe" -m pip install --upgrade pip >nul 2>nul
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (
    echo [ERRO] Falha ao instalar as dependencias.
    pause
    exit /b 1
)

echo.
echo [3/3] Iniciando ATILA...
echo.
echo O navegador sera aberto automaticamente.
echo Para encerrar o sistema, feche esta janela.
echo.

".venv\Scripts\python.exe" -m streamlit run app.py

pause
