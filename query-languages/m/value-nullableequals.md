---
description: "Learn more about: Value.NullableEquals"
title: "Value.NullableEquals"
ms.subservice: m-source
ms.topic: reference
---
# Value.NullableEquals

## Syntax

<pre>
Value.NullableEquals(
    <b>value1</b> as any,
    <b>value2</b> as any,
    optional <b>precision</b> as nullable number
) as nullable logical
</pre>

## About

Returns null if either argument `value1`, `value2` is null, otherwise equivalent to [Value.Equals](value-equals.md).
