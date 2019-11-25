---
title: "Character.ToNumber | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

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

```powerquery-m
Character.ToNumber("#(tab)")
```

`9`
