# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import List, Set
import yaml
from jinja2 import Template

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

    def __init__(self, name: str, states: List[str],
                 transition_table, reset_events :List[str]=[]):
        self._name = name
        self._states = states
        self._transition_table = transition_table
        self._reset_events = reset_events

    @property
    def name(self) -> str:
        return self._name

    @property
    def events(self) -> Set[str]:
        return set([x['name'] for x in self._transition_table] + self._reset_events)

    @property
    def reset_events(self) -> Set[str]:
        return set(self._reset_events)

    #@property
    #def states(self) -> List[str]:
    #    # Generate a list of lists of states from the transitation table
    #    l = [[x['from'], x['to']] for x in self._transition_table]
    #    # Flatten the list of lists (https://stackoverflow.com/a/952952)
    #    return set([item for sublist in l for item in sublist])

    @property
    def states(self) -> List[str]:
        return self._states

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
                           y['statemachine']['states'],
                           y['statemachine']['events'],
                           y['statemachine']['reset_events'])

            except yaml.YAMLError as exc:
                print(exc)


def render(state_machine: StateMachine=None, template: Template=None,
           **kwargs) -> str:
    assert state_machine
    assert template

    return template.render(statemachine=state_machine, **kwargs)
