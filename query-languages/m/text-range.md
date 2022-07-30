---
description: "Learn more about: Text.Range"
title: "Text.Range"
ms.date: 3/14/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Text.Range

## Syntax

<pre>
Text.Range(<b>text</b> as nullable text, <b>offset</b> as number, optional <b>count</b> as nullable number) as nullable text
</pre>
  
## About

Returns the substring from the text `text` found at the offset `offset`. An optional parameter, `count`, can be included to specify how many characters to return. Throws an error if there aren't enough characters.

## Example 1

Find the substring from the text "Hello World" starting at index 6.

**Usage**

```powerquery-m
Text.Range("Hello World", 6)
```

**Output**

`"World"`

## Example 2

Find the substring from the text "Hello World Hello" starting at index 6 spanning 5 characters.

**Usage**

```powerquery-m
Text.Range("Hello World Hello", 6, 5)
```

**Output**

`"World"`
