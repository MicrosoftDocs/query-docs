---
description: "Learn more about: Expression.Evaluate"
title: "Expression.Evaluate"
ms.subservice: m-source
ms.topic: reference
---

# Expression.Evaluate

## Syntax

<pre>
Expression.Evaluate(<b>document</b> as text, optional <b>environment</b> as nullable record) as any
</pre>

## About

Returns the result of evaluating an M expression `document`, with the available identifiers that can be referenced defined by `environment`.

## Example 1

Evaluate a simple sum.

**Usage**

```powerquery-m
Expression.Evaluate("1 + 1")
```

**Output**

`2`

## Example 2

Evaluate a more complex sum using a function that's defined via the environment record.

**Usage**

```powerquery-m
Expression.Evaluate("List.Sum({1, 2, 3})", [List.Sum = List.Sum])
```

**Output**

`6`

## Example 3

Evaluate the concatenation of a text value with a custom identifier that's defined via the environment record.

**Usage**

```powerquery-m
Expression.Evaluate(Expression.Constant("""abc") & " & " & Expression.Identifier("x"), [x = "def"""])
```

**Output**

`"""abcdef"""`
