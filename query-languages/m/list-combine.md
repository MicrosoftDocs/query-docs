---
description: "Learn more about: List.Combine"
title: "List.Combine"
---
# List.Combine

## Syntax

<pre>
List.Combine(<b>lists</b> as list) as list
</pre>

## About

Takes a list of lists, `lists`, and merges them into a single new list.

## Example 1

Combine the two simple lists {1, 2} and {3, 4}.

**Usage**

```powerquery-m
List.Combine({{1, 2}, {3, 4}})
```

**Output** 

```powerquery-m
{
    1,
    2,
    3,
    4
}
```

## Example 2

Combine the two lists, {1, 2} and {3, {4, 5}}, one of which contains a nested list.

**Usage**

```powerquery-m
List.Combine({{1, 2}, {3, {4, 5}}})
```

**Output**

```powerquery-m
{
    1,
    2,
    3,
    {4, 5}
}
```
