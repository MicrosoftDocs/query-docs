---
description: "Learn more about: Text.PositionOfAny"
title: "Text.PositionOfAny"
---
# Text.PositionOfAny

## Syntax

<pre>
Text.PositionOfAny(<b>text</b> as text, <b>characters</b> as list, optional <b>occurrence</b> as nullable number) as any
</pre>
  
## About

Returns the first position of any character in the list `characters` that is found in `text`. An optional parameter `occurrence` may be used to specify which occurrence position to return.

## Example 1

Find the first position of "W" or "H" in text "Hello, World!".

**Usage**

```powerquery-m
Text.PositionOfAny("Hello, World!", {"H", "W"})
```

**Output**

`0`

## Example 2

Find all the positions of "W" or "H" in text "Hello, World!".

**Usage**

```powerquery-m
Text.PositionOfAny("Hello, World!", {"H", "W"}, Occurrence.All)
```

**Output**

{0, 7}
