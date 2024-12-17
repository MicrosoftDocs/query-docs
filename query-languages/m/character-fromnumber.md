---
description: "Learn more about: Character.FromNumber"
title: "Character.FromNumber"
ms.subservice: m-source
---
# Character.FromNumber

## Syntax

<pre>
Character.FromNumber(<b>number</b> as nullable number) as nullable text
</pre>

## About

Returns the character equivalent of the number.

The provided `number` should be a 21-bit Unicode code point.

## Example 1

Convert a number to its equivalent character value.

**Usage**

```powerquery-m
Character.FromNumber(9)
```

**Output**

`"#(tab)"`

## Example 2

Convert a character to a number and back again.

**Usage**

```powerquery-m
Character.FromNumber(Character.ToNumber("A"))
```

**Output**

`"A"`

## Example 3

Convert the hexadecimal code point for the "grinning face" emoticon to its equivalent UTF-16 surrogate pair.

**Usage**

```powerquery-m
Character.FromNumber(0x1F600)
```

**Output**

`"#(0001F600)"`
