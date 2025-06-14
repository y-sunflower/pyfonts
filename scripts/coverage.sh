uv run coverage run --source=pyfonts -m pytest
uv run coverage report -m
uv run coverage xml
PYTHONWARNINGS="ignore::UserWarning" uv run genbadge coverage -i coverage.xml
rm coverage.xml
