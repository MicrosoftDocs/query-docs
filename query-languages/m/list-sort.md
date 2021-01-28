---
description: "Learn more about: List.Sort"
title: "List.Sort | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.Sort

## Syntax

<pre>
List.Sort(<b>list</b> as list, optional <b>comparisonCriteria</b> as any) as list  
</pre>
  
## About  
Sorts a list of data, `list`, according to the optional criteria specified. An optional parameter, `comparisonCriteria`, can be specified as the comparison criterion. This can take the following values: <ul> <li> To control the order, the comparison criterion can be an Order enum value. (<code>Order.Descending</code>, <code>Order.Ascending</code>). </li> <li> To compute a key to be used for sorting, a function of 1 argument can be used. </li> <li> To both select a key and control order, comparison criterion can be a list containing the key and order (<code>{each 1 / _, Order.Descending}</code>). </li> <li> To completely control the comparison, a function of 2 arguments can be used that returns -1, 0, or 1 given the relationship between the left and right inputs. Value.Compare is a method that can be used to delegate this logic. </li> </ul>

## Example 1
Sort the list {2, 3, 1}.

```powerquery-m
List.Sort({2, 3, 1})
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> </table>

## Example 2
Sort the list {2, 3, 1} in descending order.

```powerquery-m
List.Sort({2, 3, 1}, Order.Descending)
```

<table> <tr><td>3</td></tr> <tr><td>2</td></tr> <tr><td>1</td></tr> </table>

## Example 3
Sort the list {2, 3, 1} in descending order using the Value.Compare method.

```powerquery-m
List.Sort({2, 3, 1}, (x, y) => Value.Compare(1/x, 1/y))
```

<table> <tr><td>3</td></tr> <tr><td>2</td></tr> <tr><td>1</td></tr> </table>
