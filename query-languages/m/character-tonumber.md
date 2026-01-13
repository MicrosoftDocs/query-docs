---
description: "Learn more about: Character.ToNumber"
title: "Character.ToNumber"
ms.subservice: m-source
ms.topic: reference
---
# Character.ToNumber

## Syntax

<pre>
Character.ToNumber(<b>character</b> as nullable text) as nullable number
</pre>

## About

Returns the number equivalent of the character, `character`.

The result will be the 21-bit Unicode code point represented by the provided character or surrogate pair.

## Example 1

Convert a character to its equivalent number value.

**Usage**

```powerquery-m
Character.ToNumber("#(tab)")
```

**Output**

`9`

## Example 2

Convert the UTF-16 surrogate pair for the "grinning face" emoticon to its equivalent hexadecimal code point.

**Usage**

```powerquery-m
Number.ToText(Character.ToNumber("#(0001F600)"), "X")
```

**Output**

`"1F600"`
