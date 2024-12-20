---
description: "Learn more about: Splitter.SplitTextByRepeatedLengths"
title: "Splitter.SplitTextByRepeatedLengths"
ms.subservice: m-source
---
# Splitter.SplitTextByRepeatedLengths

## Syntax

<pre>
Splitter.SplitTextByRepeatedLengths(<b>length</b> as number, optional <b>startAtEnd</b> as nullable logical) as function
</pre>

## About

Returns a function that splits text into a list of text after the specified length repeatedly.

## Example 1

Repeatedly split the input into chunks of three characters, starting from the beginning of the input.

**Usage**

```powerquery-m
Splitter.SplitTextByRepeatedLengths(3)("12345678")
```

**Output**

`{"123", "456", "78"}`

## Example 2

Repeatedly split the input into chunks of three characters, starting from the end of the input.

**Usage**

```powerquery-m
let
    startAtEnd = true
in
    Splitter.SplitTextByRepeatedLengths(3, startAtEnd)("87654321")
```

**Output**

`{"87", "654", "321"}`
