---
description: "Learn more about: Logical.FromText"
title: "Logical.FromText"
ms.subservice: m-source
---
# Logical.FromText

## Syntax

<pre> 
Logical.FromText(<b>text</b> as nullable text) as nullable logical
</pre>
  
## About

Creates a logical value from the text value `text`, either "true" or "false". If `text` contains a different string, an error is raised. The text value `text` is case insensitive.

## Example 1

Create a logical value from the text string "true".

**Usage**

```powerquery-m
Logical.FromText("true")
```

**Output**

`true`

## Example 2

Create a logical value from the text string "a".

**Usage**

```powerquery-m
Logical.FromText("a")
```

**Output**

`[Expression.Error] Could not convert to a logical.`
