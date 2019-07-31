---
title: "List.Reverse | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Reverse

## Syntax

<pre>
List.Reverse(<b>list</b> as list) as list
</pre>
  
## About  
Returns a list with the values in the list `list` in reversed order.

## Example 1
Create a list from {1..10} in reverse order.

```powerquery-m
List.Reverse({1..10})
```

<table> <tr><td>10</td></tr> <tr><td>9</td></tr> <tr><td>8</td></tr> <tr><td>7</td></tr> <tr><td>6</td></tr> <tr><td>5</td></tr> <tr><td>4</td></tr> <tr><td>3</td></tr> <tr><td>2</td></tr> <tr><td>1</td></tr> </table>
