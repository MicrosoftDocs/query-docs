---
description: "Learn more about: List.Zip"
title: "List.Zip"
ms.subservice: m-source
ms.topic: reference
---
# List.Zip

## Syntax

<pre>
List.Zip(<b>lists</b> as list) as list
</pre>

## About

Takes a list of lists, `lists`, and returns a list of lists combining items at the same position.

## Example 1

Zips the two simple lists {1, 2} and {3, 4}.

**Usage**

```powerquery-m
List.Zip({{1, 2}, {3, 4}})
```

**Output**

```powerquery-m
{
    {1, 3},
    {2, 4}
}
```

## Example 2

Zips the two simple lists of different lengths {1, 2} and {3}.

**Usage**

```powerquery-m
List.Zip({{1, 2}, {3}})
```

**Output**

```powerquery-m
{
    {1, 3},
    {2, null}
}
```
