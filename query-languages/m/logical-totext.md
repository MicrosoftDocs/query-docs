---
description: "Learn more about: Logical.ToText"
title: "Logical.ToText"
ms.subservice: m-source
---
# Logical.ToText

## Syntax

<pre>
Logical.ToText(<b>logicalValue</b> as nullable logical) as nullable text  
</pre>
  
## About

Creates a text value from the logical value `logicalValue`, either `true` or `false`. If `logicalValue` is not a logical value, an error is raised.

## Example 1

Create a text value from the logical `true`.

**Usage**

```powerquery-m
Logical.ToText(true)
```

**Output**

`"true"`
