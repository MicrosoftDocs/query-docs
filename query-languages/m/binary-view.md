---
description: "Learn more about: Binary.View"
title: "Binary.View"
ms.date: 7/19/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo
---
# Binary.View

## Syntax

<pre>
Binary.View(<b>binary</b> as nullable binary, <b>handlers</b> as record) as binary
</pre>

## About

Returns a view of `binary` where the functions specified in `handlers` are used in lieu of the default behavior of an operation when the operation is applied to the view.

If `binary` is provided, all handler functions are optional. If `binary` isn't provided, the `GetStream` handler function is required. If a handler function isn't specified for an operation, the default behavior of the operation is applied to `binary` instead (except in the case of `GetExpression`).

Handler functions must return a value that is semantically equivalent to the result of applying the operation against `binary` (or the resulting view in the case of `GetExpression`).

If a handler function raises an error, the default behavior of the operation is applied to the view.

`Binary.View` can be used to implement folding to a data source–the translation of M queries into source-specific operations (for example, to download a section of a file).

Refer to the published Power Query custom connector documentation for a more complete description of `Binary.View`.

## Example 1

Create a basic view that doesn't require accessing the data in order to determine the length.

**Usage**

```powerquery-m
Binary.View(
    null,
    [
        GetLength = () => 12,
        GetStream = () => Text.ToBinary("hello world!")
    ]
)
```

**Output**

```powerquery-m
Text.ToBinary("hello world!")
```
