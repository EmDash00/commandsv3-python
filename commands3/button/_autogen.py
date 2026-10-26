"""Generate explicit command-based wrappers for RobotPy controller classes
using specs in _controller_specs.py.

Generated files are explicit and do not add methods at runtime or depend
any runtime code generation.
"""

from __future__ import annotations

from pathlib import Path

from commands3.button._controller_specs import CONTROLLER_SPECS


def render_fstring_template(template_path: Path, context: dict[str, Any]) -> str:
    """Evaluate one trusted template file as a Python f-string."""
    template = template_path.read_text(encoding="utf-8")
    return eval(f"f{template!r}", {}, context)


def generate_controller(spec: ControllerSpec, template_dir: Path = Path(".")) -> str:
    """Render a wrapper by composing module, button, and axis templates."""
    button_template = template_dir / "button_methods.py.tmpl"
    axis_template = template_dir / "axis_methods.py.tmpl"
    module_template = template_dir / "controller.py.tmpl"

    button_methods = "\n".join(
        render_fstring_template(button_template, {"button": button})
        for button in spec.buttons
    )
    axis_methods = "\n".join(
        render_fstring_template(axis_template, {"axis": axis, "spec": spec})
        for axis in spec.axes
    )
    return (
        render_fstring_template(
            module_template,
            {
                "spec": spec,
                "button_methods": button_methods,
                "axis_methods": axis_methods,
            },
        ).rstrip()
        + "\n"
    )


def main() -> None:
    for spec in CONTROLLER_SPECS:
        destination = Path(spec.filename)
        destination.write_text(generate_controller(spec), encoding="utf-8")
        print(f"Generated {destination}")


if __name__ == "__main__":
    main()
