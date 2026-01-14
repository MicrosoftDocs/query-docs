---
description: "Learn more about: Combiner.CombineTextByLengths"
title: "Combiner.CombineTextByLengths"
ms.subservice: m-source
ms.topic: reference
---
# Combiner.CombineTextByLengths

## Syntax

<pre>
Combiner.CombineTextByLengths(<b>lengths</b> as list, optional <b>template</b> as nullable text) as function
</pre>

## About

Returns a function that combines a list of text values into a single text value using the specified lengths.

## Example 1

Combine a list of text values by extracting the specified numbers of characters from each input value.

**Usage**

```powerquery-m
Combiner.CombineTextByLengths({1, 2, 3})({"aaa", "bbb", "ccc"})
```

**Output**

`"abbccc"`

## Example 2

Combine a list of text values by extracting the specified numbers of characters, after first pre-filling the result with the template text.

**Usage**

```powerquery-m
Combiner.CombineTextByLengths({1, 2, 3}, "*********")({"aaa", "bbb", "ccc"})
```

**Output**

`"abbccc***"`
