from PySide6.QtWidgets import QWidget


class UiCorruptionError(Exception):
    """Raised on an unexpected condition on the Ui. Examples including some
    RadioButtons with none of them selected (while there must be at least 1)."""

    def __init__(self, widgets: list[QWidget], *args: object) -> None:
        super().__init__(*args)
        self.widgets = widgets

    def __str__(self) -> str:
        return f"{super().__str__()}. Related widgets: {[widget.objectName() for widget in self.widgets]}"