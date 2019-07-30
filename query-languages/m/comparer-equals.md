---
title: "Comparer.Equals | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Comparer.Equals

## Syntax

<pre>
Comparer.Equals(comparer as function, x as any, y as any) as logical  
</pre>
  
## About  
Returns a `logical` value based on the equality check over the two given values, `x` and `y`, using the provided `comparer`. <div> `comparer` is a `Comparer` which is used to control the comparison. Comparers can be used to provide case insensitive or culture and locale aware comparisons. </div> <div> The following built in comparers are available in the formula language: </div> <ul> <li><code>Comparer.Ordinal</code>: Used to perform an exact ordinal comparison</li> <li><code>Comparer.OrdinalIgnoreCase</code>: Used to perform an exact ordinal case-insensitive comparison</li> <li> <code>Comparer.FromCulture</code>: Used to perform a culture aware comparison</li> </ul>

## Example 1
Compare "1" and "A" using "en-US" locale to determine if the values are equal.

```powerquery-m
Comparer.Equals(Comparer.FromCulture("en-us"), "1", "A")
```

`false`