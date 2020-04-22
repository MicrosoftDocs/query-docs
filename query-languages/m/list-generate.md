---
title: "List.Generate | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.Generate
  
## Syntax

<pre>
List.Generate(<b>initial</b> as function, <b>condition</b> as function, <b>next</b> as function, optional <b>selector</b> as nullable function) as list
</pre>

## About

Generates a list of values given four functions that generate the initial value `initial`, test against a condition `condition`, and if successful select the result and generate the next value `next`. An optional parameter, `selector`, may also be specified.

## Example 1
Create a list that starts at 10, remains greater than 0 and decrements by 1.


```powerquery-m
List.Generate(() => 10, each _ > 0, each _ - 1)
```

<table> <tr><td>10</td></tr> <tr><td>9</td></tr> <tr><td>8</td></tr> <tr><td>7</td></tr> <tr><td>6</td></tr> <tr><td>5</td></tr> <tr><td>4</td></tr> <tr><td>3</td></tr> <tr><td>2</td></tr> <tr><td>1</td></tr> </table>

## Example 2
Generate a list of records containing x and y, where x is a value and y is a list. x should remain less than 10 and represent the number of items in the list y. After the list is generated, return only the x values.

```powerquery-m
List.Generate( 
    () => [x = 1, y = {}], 
    each [x] < 10, 
    each [x = List.Count([y]), y = [y] & {x}], 
    each [x] 
)
```

<table> <tr><td>1</td></tr> <tr><td>0</td></tr> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>5</td></tr> <tr><td>6</td></tr> <tr><td>7</td></tr> <tr><td>8</td></tr> <tr><td>9</td></tr> </table>


