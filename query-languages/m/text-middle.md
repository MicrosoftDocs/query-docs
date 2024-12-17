---
description: "Learn more about: Text.Middle"
title: "Text.Middle"
ms.subservice: m-source
---
# Text.Middle

## Syntax

<pre>
Text.Middle(<b>text</b> as nullable text, <b>start</b> as number, optional <b>count</b> as nullable number) as nullable text
</pre>
  
## About

Returns `count` characters, or through the end of `text`; at the offset `start`.

## Example 1

Find the substring from the text "Hello World" starting at index 6 spanning 5 characters.

**Usage**

```powerquery-m
Text.Middle("Hello World", 6, 5)
```

**Output**

`"World"`

## Example 2

Find the substring from the text "Hello World" starting at index 6 through the end.

**Usage**

```powerquery-m
Text.Middle("Hello World", 6, 20)
```

**Output**

`"World"`

## Example 3

Find the substring from the text "Hello World" starting at index 0 spanning 2 characters.

**Usage**

```powerquery-m
Text.Middle("Hello World", 0, 2)
```

**Output**

`"He"`
