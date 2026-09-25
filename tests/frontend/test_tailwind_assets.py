from pathlib import Path
import subprocess

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CSS_DIR = PROJECT_ROOT / "internship_management/static/css"


def test_tailwind_input_uses_official_import():
    input_css = (CSS_DIR / "input.css").read_text()
    assert '@import "tailwindcss";' in input_css
    assert "@source" in input_css


def test_base_template_loads_generated_output_css():
    template = (PROJECT_ROOT / "internship_management/templates/base.html").read_text()
    assert "{% static 'css/output.css' %}" in template


def test_tailwind_cli_builds_output_css():
    result = subprocess.run(
        ["npm", "run", "css:build"],
        cwd=PROJECT_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    output_css = CSS_DIR / "output.css"
    assert output_css.exists()
    assert output_css.stat().st_size > 0
