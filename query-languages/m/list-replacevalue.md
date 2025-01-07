---
description: "Learn more about: List.ReplaceValue"
title: "List.ReplaceValue"
ms.subservice: m-source
---
# List.ReplaceValue

## Syntax

<pre>
List.ReplaceValue(<b>list</b> as list, <b>oldValue</b> as any, <b>newValue</b> as any, <b>replacer</b> as function) as list
</pre>
  
## About

Searches a list of values, `list`, for the value `oldValue` and replaces each occurrence with the replacement value `newValue`.

## Example 1

Replace all the "a" values in the list {"a", "B", "a", "a"} with "A".

**Usage**

```powerquery-m
List.ReplaceValue({"a", "B", "a", "a"}, "a", "A", Replacer.ReplaceText)
```

**Output**

{"A", "B", "A", "A"}
