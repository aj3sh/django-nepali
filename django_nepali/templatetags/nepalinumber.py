from typing import Any

from django import template

from nepali.number import (
    add_comma,
    add_comma_english,
    convert_and_add_comma,
    english_to_nepali,
)

register = template.Library()


@register.filter(name="nepalinumber")
def nepalinumber(value: Any) -> str:
    """
    Converts the number into nepali number and renders it.

    Usage:
    ```
    {{ number|nepalinumber }}
    ```

    :param value: Number to be converted
    :returns: Nepali output of given number
    """
    return english_to_nepali(value)


@register.filter(name="nepalinumber_with_comma")
def nepalinumber_with_comma(value: Any) -> str:
    """
    Converts the number into nepali number and renders it.

    Usage:
    ```
    {{ number|nepalinumber_with_comma }}
    ```
    Basically same as `{{ number|nepalinumber|nepali_comma }}`

    :param value: Number to be converted and commas added
    :returns: Nepali output of given number with commas
    """
    return convert_and_add_comma(value)


@register.filter(name="nepali_comma")
def nepali_comma(value: Any) -> str:
    """
    Renders the given value with commas added in Nepali style without converting the number.

    Usage:
    ```
    {{ number|nepali_comma }}
    ```

    :param value: Number to be added with commas
    :returns: Output of given number with commas
    """
    return add_comma(value)


@register.filter(name="english_comma")
def english_comma(value: Any) -> str:
    """
    Renders the given value with commas added in English style without converting the number.

    Usage:
    ```
    {{ number|english_comma }}
    ```

    :param value: Number to be added with commas
    :returns: Output of given number with commas
    """
    return add_comma_english(value)
