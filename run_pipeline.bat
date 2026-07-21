@echo off
echo Starting CI Pipeline...

echo Installing dependencies...
pip install pytest

echo Running tests...
pytest

echo Pipeline Finished.
pause