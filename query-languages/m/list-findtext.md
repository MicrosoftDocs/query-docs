---
description: "Learn more about: List.FindText"
title: "List.FindText"
---
# List.FindText

## Syntax

<pre>
List.FindText(<b>list</b> as list, <b>text</b> as text) as list
</pre>

## About

Returns a list of the values from the list `list` which contained the value `text`.

## Example 1

Find the text values in the list {"a", "b", "ab"} that match "a".

**Usage**

```powerquery-m
List.FindText({"a", "b", "ab"}, "a")
```

**Output**

`{"a", "ab"}`
