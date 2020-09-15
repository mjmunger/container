import hashlib
import importlib
from importlib._bootstrap import ModuleSpec
from importlib.util import find_spec

class Container:

    definitions = {}
    constructors = {}
    vars = {}

    def __init__(self):
        self.definitions = {}
        self.constructors = {}
        self.vars = {}

    def add(self, tag : str, payload, constructor_args=None) -> None:
        self.definitions[tag] = payload

    def get(self, tag):
        payload = self.definitions[tag]

        if type(payload) is not str:
            return payload

        spec = find_spec(payload)
        if isinstance(spec, ModuleSpec):

            if tag in self.constructors:
                constructors = list(self.constructors[tag])
                return getattr(importlib.import_module(payload), tag, None)(*constructors)

            r = getattr(importlib.import_module(payload), tag, None)

            if r is None:
                return payload

            return r()

    def with_constructors(self, tag, constructors : list):
        self.constructors[tag] = constructors