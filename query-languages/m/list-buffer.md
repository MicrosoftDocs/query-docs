---
title: "List.Buffer | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Buffer

## Syntax

<pre>
List.Buffer(<b>list</b> as list) as list 
</pre>
  
## About  
Buffers the list `list` in memory. The result of this call is a stable list.

## Example 1
Create a stable copy of the list {1..10}.

```powerquery-m
List.Buffer({1..10})
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>5</td></tr> <tr><td>6</td></tr> <tr><td>7</td></tr> <tr><td>8</td></tr> <tr><td>9</td></tr> <tr><td>10</td></tr> </table>

