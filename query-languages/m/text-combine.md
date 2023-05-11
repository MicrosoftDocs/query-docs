---
description: "Learn more about: Text.Combine"
title: "Text.Combine"
ms.date: 5/11/2023
---
# Text.Combine

## Syntax

<pre>
Text.Combine(<b>texts</b> as list, optional <b>separator</b> as nullable text) as text
</pre>
  
## About

Returns the result of combining the list of text values, `texts`, into a single text value. Any `null` values present in `texts` are ignored.

An optional separator used in the final combined text may be specified, `separator`.

## Example 1

Combine text values "Seattle" and "WA".

**Usage**

```powerquery-m
Text.Combine({"Seattle", "WA"})
```

**Output**

`"SeattleWA"`

## Example 2

Combine text values "Seattle" and "WA", separated by a comma and a space, ", ".

**Usage**

```powerquery-m
Text.Combine({"Seattle", "WA"}, ", ")
```

**Output**

`"Seattle, WA"`

## Example 3

Combine values "Seattle", `null`, and "WA", separated by a comma and a space, ", ". (The `null` will be ignored.)

**Usage**

```powerquery-m
Text.Combine({"Seattle", null, "WA"}, ", ")
```

**Output**

`"Seattle, WA"`
