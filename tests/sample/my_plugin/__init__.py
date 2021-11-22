from typing import Any, Dict, List, Tuple

from pydantic import BaseModel

from npe2 import PluginContext


def activate(context: PluginContext):
    @context.register_command("my_plugin.hello_world")
    def _hello():
        ...

    context.register_command("my_plugin.another_command", lambda: print("yo!"))


def get_reader(path: str):
    if path.endswith(".fzzy"):

        def read(path):
            return [(None,)]

        return read


def url_reader(path: str):
    if path.startswith("http"):

        def read(path):
            return [(None,)]

        return read


def writer_function(path: str, layer_data: List[Tuple[Any, Dict, str]]) -> List[str]:
    class Arg(BaseModel):
        data: Any
        meta: Dict
        layer_type: str

    for e in layer_data:
        Arg(data=e[0], meta=e[1], layer_type=e[2])

    return [path]


def writer_function_single(path: str, layer_data: Any, meta: Dict) -> List[str]:
    class Arg(BaseModel):
        data: Any
        meta: Dict

    Arg(data=layer_data, meta=meta)

    return [path]


class SomeWidget:
    ...


def random_data():
    import numpy as np

    return [(np.random.rand(10, 10))]