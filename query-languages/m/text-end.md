---
description: "Learn more about: Text.End"
title: "Text.End"
---
# Text.End

## Syntax

<pre>
Text.End(<b>text</b> as nullable text, <b>count</b> as number) as nullable text
</pre> 
  
## About

Returns a `text` value that is the last `count` characters of the `text` value `text`.

## Example 1

Get the last 5 characters of the text "Hello, World".

**Usage**

```powerquery-m
Text.End("Hello, World", 5)
```

**Output**

`"World"`
