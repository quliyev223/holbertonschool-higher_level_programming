#!/usr/bin/python3
"""Abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class, subclass of Animal."""

    def sound(self):
        return "Bark"


class Cat(animal):
    """Cat class, subclass of Animal."""

    def sound(self):
        return "Meow"
