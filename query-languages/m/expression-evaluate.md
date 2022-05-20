---
description: "Learn more about: Expression.Evaluate"
title: "Expression.Evaluate | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery
ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

Evaluate a more complex sum.

**Usage**

```powerquery-m
Expression.Evaluate("List.Sum({1, 2, 3})", [List.Sum = List.Sum])
```

**Output**

`6`

## Example 3

Evaluate the concatenation of a text value with an identifier.

**Usage**

```powerquery-m
Expression.Evaluate(Expression.Constant("""abc") & " & " & Expression.Identifier("x"), [x = "def"""])
```

**Output**

`"""abcdef"""`
