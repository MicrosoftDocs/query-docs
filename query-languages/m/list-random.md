---
title: "List.Random | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.Random

## Syntax

<pre>
List.Random(<b>count</b> as number, optional <b>seed</b> as nullable number) as list
</pre>
  
## About  
Returns a list of random numbers between 0 and 1, given the number of values to generate and an optional seed value. <ul> <li><code>count</code>: The number of random values to generate.</li> <li><code>seed</code>: <i>[Optional]</i> A numeric value used to seed the random number generator. If omitted a unique list of random numbers is generated each time you call the function. If you specify the seed value with a number every call to the function generates the same list of random numbers.</li> </ul>

## Example 1
Create a list of 3 random numbers.

```powerquery-m
List.Random(3)
```

<table> <tr><td>0.992332</td></tr> <tr><td>0.132334</td></tr> <tr><td>0.023592</td></tr> </table>

## Example 2
Create a list of 3 random numbers, specifying seed value.

```powerquery-m
List.Random(3, 2)
```

<table> <tr><td>0.883002</td></tr> <tr><td>0.245344</td></tr> <tr><td>0.723212</td></tr> </table>
