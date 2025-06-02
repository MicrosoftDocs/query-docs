---
description: "Learn more about: Value.FromText"
title: "Value.FromText"
ms.subservice: m-source
---
# Value.FromText

## Syntax

<pre>
Value.FromText(<b>text</b> as any, optional <b>culture</b> as nullable text) as any
</pre>

## About

Decodes a value from a textual representation and interprets it as a value with an appropriate type.

* `text`: The text to interpret.
* `culture` (Optional) A specific culture used to interpret the text (for example, "en-US").

This function takes a text value and returns a value of type `number`, `logical`, `null`, `datetime`, `duration`, or `text`. An empty text value is interpreted as a `null` value.

## Example 1

Convert text representing a number to its corresponding number value.

**Usage**

```powerquery-m
Value.FromText("12345.6789")
```

**Output**

`12345.6789`

## Example 2

Convert text representing a percentage to its corresponding number value.

**Usage**

```powerquery-m
Value.FromText("25.4%")
```

**Output**

`0.254`


## Example 3

Convert text representing a French Euro value to its corresponding number value.

**Usage**

```powerquery-m
Value.FromText("€1,190", "fr-FR")
```

**Output**

`1.19`

## Example 4

Convert text representing a German date and time to its corresponding date and time value.

**Usage**

```powerquery-m
Value.FromText("24 Dez 2024 14:33:20", "de-DE")
```

**Output**

`#datetime(2024, 12, 24, 14, 33, 20)`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
