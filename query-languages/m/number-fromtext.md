---
description: "Learn more about: Number.FromText"
title: "Number.FromText"
---
# Number.FromText

## Syntax

<pre>
Number.FromText(<b>text</b> as nullable text, optional <b>culture</b> as nullable text) as nullable number
</pre>

## About

Returns a `number` value from the given text value, `text`.

* `text`: The textual representation of a number value. The representation must be in a common number format, such as "15", "3,423.10", or "5.0E-10".
* `culture`: An optional culture that controls how `text` is interpreted (for example, "en-US").

## Example 1

Get the number value of `"4"`.

**Usage**

```powerquery-m
Number.FromText("4")
```

**Output**

`4`

## Example 2

Get the number value of `"5.0e-10"`.

**Usage**

```powerquery-m
Number.FromText("5.0e-10")
```

**Output**

`5E-10`
