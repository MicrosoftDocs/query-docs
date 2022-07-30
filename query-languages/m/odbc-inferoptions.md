---
description: "Learn more about: Odbc.InferOptions"
title: "Odbc.InferOptions"
ms.date: 3/14/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Odbc.InferOptions

## Syntax

<pre>
Odbc.InferOptions(<b>connectionString</b> as any) as record
</pre>

## About

Returns the result of trying to infer SQL capbabilities with the connection string `connectionString` using ODBC. `connectionString` can be text or a record of property value pairs. Property values can either be text or number.

## Example 1

Return the inferred SQL capabilities for a connection string.

**Usage**

```powerquery-m
Odbc.InferOptions("dsn=your_dsn")
```

**Output**

```powerquery-m
record
```
