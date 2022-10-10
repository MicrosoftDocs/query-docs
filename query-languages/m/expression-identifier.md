---
description: "Learn more about: Expression.Identifier"
title: "Expression.Identifier"
ms.date: 10/7/2022
---
# Expression.Identifier

## Syntax

<pre>
Expression.Identifier(<b>name</b> as text) as text
</pre>

## About

Returns the M source code representation of an identifier `name`.

## Example 1

Get the M source code representation of an identifier.

**Usage**

```powerquery-m
Expression.Identifier("MyIdentifier")
```

**Output**

`"MyIdentifier"`

## Example 2

Get the M source code representation of an identifier that contains a space.

**Usage**

```powerquery-m
Expression.Identifier("My Identifier")
```

**Output**

`"#""My Identifier"""`
