---
description: "Learn more about: Text.Insert"
title: "Text.Insert"
---
# Text.Insert

## Syntax

<pre>
Text.Insert(<b>text</b> as nullable text, <b>offset</b> as number, <b>newText</b> as text) as nullable text
</pre>
  
## About

Returns the result of inserting text value `newText` into the text value `text` at position `offset`. Positions start at number 0.

## Example 1

Insert "C" between "B" and "D" in "ABD".

**Usage**

```powerquery-m
Text.Insert("ABD", 2, "C")
```

**Output**

`"ABCD"`
