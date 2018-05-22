---
title: "Type.ForFunction | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Type.ForFunction
<code>Type.ForFunction(<b>signature</b> as record, <b>min</b> as number) as type</code>
## About
Creates a <code>function type</code> from <code>signature</code>, a record of <code>ReturnType</code> and <code>Parameters</code>, and <code>min</code>, the minimum number of arguments required to invoke the function.

## Example 1
Creates the type for a function that takes a number parameter named X and returns a number.

<code>Type.ForFunction([ReturnType = type number, Parameters = [X = type number]], 1)</code>

<code>type function (X as number) as number</code>