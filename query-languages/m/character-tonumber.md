---
description: "Learn more about: Character.ToNumber"
title: "Character.ToNumber"
ms.date: 3/11/2022
---
# Character.ToNumber

## Syntax

<pre>
Character.ToNumber(<b>character</b> as nullable text) as nullable number
</pre>
  
## About

Returns the number equivalent of the character, `character`.

## Example 1

Given the character "#(tab)" 9, find the number value.

**Usage**

```powerquery-m
Character.ToNumber("#(tab)")
```

**Output**

`9`
