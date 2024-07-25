from .._exceptions import NeoSpaceError

INSTRUCTIONS = """

NeoSpace error:

    missing `{library}`

This feature requires additional dependencies:

    $ pip install neospace[{extra}]

"""


def format_instructions(*, library: str, extra: str) -> str:
    return INSTRUCTIONS.format(library=library, extra=extra)


class MissingDependencyError(NeoSpaceError):
    pass
