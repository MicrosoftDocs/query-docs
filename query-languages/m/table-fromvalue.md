---
description: "Learn more about: Table.FromValue"
title: "Table.FromValue | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.FromValue

## Syntax

<pre>
Table.FromValue(<b>value</b> as any, optional <b>options</b> as nullable record) as table  
</pre>
  
## About  
Creates a table with a column containing the provided value or list of values, `value`. An optional record parameter, `options`, may be specified to control the following options: <ul> <li> <code>DefaultColumnName</code> : The column name used when constructing a table from a list or scalar value.</li> </ul> 

## Example 1
Create a table from the value 1.

```powerquery-m
Table.FromValue(1)
```

<table> <tr> <th>Value</th> </tr> <tr> <td>1</td> </tr> </table>

## Example 2
Create a table from the list.

```powerquery-m
Table.FromValue({1, "Bob", "123-4567"})
```

<table> <tr> <th>Value</th> </tr> <tr> <td>1</td> </tr> <tr> <td>Bob</td> </tr> <tr> <td>123-4567</td> </tr> </table>

## Example 3
Create a table from the value 1, with a custom column name.

```powerquery-m
Table.FromValue(1, [DefaultColumnName = "MyValue"])
```

<table> <tr> <th>MyValue</th> </tr> <tr> <td>1</td> </tr> </table>
