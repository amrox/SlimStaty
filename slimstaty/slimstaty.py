# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import List, Set
import yaml

"""Main module."""


class StateMachine(object):

    class Transition(object):

        def __init__(self, event: str, from_state: str, to_state: str):
            self._event = event
            self._from_state = from_state
            self._to_state = to_state

        @property
        def event(self) -> str:
            return self._event

        @property
        def from_state(self) -> str:
            return self._from_state

        @property
        def to_state(self) -> str:
            return self._to_state

        def __repr__(self):
            return f"Transition({self._event}: \
                {self._from_state} -> {self._to_state})"

    def __init__(self, name: str, transition_table):
        self._name = name
        self._transition_table = transition_table

    @property
    def name(self) -> str:
        return self._name

    @property
    def events(self) -> Set[str]:
        return set([x['name'] for x in self._transition_table])

    @property
    def states(self) -> List[str]:
        # Generate a list of lists of states from the transitation table
        l = [[x['from'], x['to']] for x in self._transition_table]
        # Flatten the list of lists (https://stackoverflow.com/a/952952)
        return set([item for sublist in l for item in sublist])

    @property
    def transitions(self) -> List[self.Transition]:
        return [self.Transition(x['name'], x['from'], x['to'])
                for x in self._transition_table]

    @classmethod
    def from_yaml(cls, path: str) -> StateMachine:
        with open(path, 'r') as stream:
            try:
                y = yaml.full_load(stream)
                return cls(y['statemachine']['name'],
                           y['statemachine']['events'])

            except yaml.YAMLError as exc:
                print(exc)
