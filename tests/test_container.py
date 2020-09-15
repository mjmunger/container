import unittest
from typing import List

from container.container import Container
from tests.fixtures.test_classes.bar import Bar
from tests.fixtures.test_classes.foo import Foo
from tests.fixtures.test_classes.baz import Baz

from unittest_data_provider import data_provider



class TestContainer(unittest.TestCase):
    provider_sample_data = lambda : (
        ('fruitlist', ["apple", "orange"], List, None),
        ('identity', "I'm a little teapot", None, None),
        ('Foo', Foo.__module__, Foo, None),
        ('Bar', Bar.__module__, Bar, ["michael"]),
        ('Baz', Baz.__module__, Baz, ['748 parkside dr', 'woodstock', 'ga'])
    )

    @data_provider(provider_sample_data)
    def test_add(self, tag, payload, expected_class, constructors):

        container = Container()
        container.add(tag, payload)
        self.assertEqual(1, len(container.definitions))
        self.assertEqual(container.definitions[tag], payload)

    @data_provider(provider_sample_data)
    def test_get(self, tag, payload, expected_class, constructors):
        print("=====")
        container = Container()
        container.add(tag, payload)
        if constructors is not None:
            container.with_constructors(tag, constructors)

        object = container.get(tag)
        if expected_class is None:
            return False

        self.assertTrue(isinstance(object, expected_class))

if __name__ == '__main__':
    unittest.main()
