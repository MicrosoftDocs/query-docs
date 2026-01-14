---
description: "Learn more about: Text.Remove"
title: "Text.Remove"
ms.subservice: m-source
ms.topic: reference
---
# Text.Remove

## Syntax

<pre>
Text.Remove(<b>text</b> as nullable text, <b>removeChars</b> as any) as nullable text
</pre>
  
## About

Returns a copy of the text value `text` with all the characters from `removeChars` removed.

## Example 1

Remove characters , and ; from the text value.

**Usage**

```powerquery-m
Text.Remove("a,b;c", {",",";"})
```

**Output**

`"abc"`
