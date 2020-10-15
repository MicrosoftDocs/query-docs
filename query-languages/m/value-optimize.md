---
title: "Value.Optimize | Microsoft Docs"
ms.date: 06/16/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Value.Optimize

## Syntax

<pre>
Value.Optimize(<b>value</b> as any) as any
</pre>
  
## About  
When used within Value.Expression, if `value` represents a query that can be optimized, this function indicates that the optimized expression should be returned. Otherwise, `value` will be passed through with no effect.
