---
description: "Learn more about: Text.RemoveRange"
title: "Text.RemoveRange"
ms.subservice: m-source
ms.topic: reference
---

# Text.RemoveRange

## Syntax

<pre>
Text.RemoveRange(
    <b>text</b> as nullable text,
    <b>offset</b> as number,
    optional <b>count</b> as nullable number
) as nullable text
</pre>

## About

Returns a copy of the text value `text` with all the characters from position `offset` removed. An optional parameter, `count` can by used to specify the number of characters to remove. The default value of `count` is 1. Position values start at 0.

## Example 1

Remove one character from the text value starting at position 2.

**Usage**

```powerquery-m
Text.RemoveRange("ABCDE", 2)
```

**Output**

`"ABDE"`

## Example 2

Remove two characters from the text value starting at position 1.

**Usage**

```powerquery-m
Text.RemoveRange("ABCDE", 1, 2)
```

**Output**

`"ADE"`
