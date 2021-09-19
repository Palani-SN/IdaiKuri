@echo off
set PYTHONPATH=..\SRCS;%PYTHONPATH%
echo Running ... [ %1% ]
python %1%
pause