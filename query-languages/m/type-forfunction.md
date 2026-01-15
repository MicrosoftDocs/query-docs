---
description: "Learn more about: Type.ForFunction"
title: "Type.ForFunction"
ms.subservice: m-source
ms.topic: reference
---
# Type.ForFunction

## Syntax

<pre>
Type.ForFunction(<b>signature</b> as record, <b>min</b> as number) as type
</pre>

## About

Creates a `function type` from `signature`, a record of `ReturnType` and `Parameters`, and `min`, the minimum number of arguments required to invoke the function.

## Example 1

Creates the type for a function that takes a number parameter named X and returns a number.

**Usage**

```powerquery-m
Type.ForFunction([ReturnType = type number, Parameters = [X = type number]], 1)
```

**Output**

`type function (X as number) as number`
