---
description: "Learn more about: Function.Invoke"
title: "Function.Invoke"
---
# Function.Invoke

## Syntax

<pre>
Function.Invoke(<b>function</b> as function, <b>args</b> as list) as any
</pre>

## About

Invokes the given function using the specified list of arguments and returns the result.

## Example 1

Invokes [Record.FieldNames](record-fieldnames.md) with one argument [A=1,B=2]

**Usage**

```powerquery-m
Function.Invoke(Record.FieldNames, {[A = 1, B = 2]}
```

**Output**

`{"A", "B"}`
