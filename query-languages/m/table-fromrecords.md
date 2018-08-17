---
title: "Table.FromRecords | Microsoft Docs"
ms.date: 8/17/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.FromRecords
<code>Table.FromRecords(<b>records</b> as list, optional <b>columns</b> as any, optional <b>missingField</b> as nullable number) as table</code>

## About
Converts <code>records</code>, a list of records, into a table.

## Example 1
Create a table from records, using record field names as column names.

<code>Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"], [CustomerID = 2, Name = "Jim", Phone = "987-6543"], [CustomerID = 3, Name = "Paul", Phone = "543-7890"]})</code>

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> </tr> <tr> <td>2</td> <td>Jim</td> <td>987-6543</td> </tr> <tr> <td>3</td> <td>Paul</td> <td>543-7890</td> </tr> </table>

## Example 2
Create a table from records with typed columns and select the number columns.

<code>Table.ColumnsOfType(Table.FromRecords({[CustomerID=1, Name="Bob"]}, type table[CustomerID=Number.Type, Name=Text.Type]), {type number})</code>

<table> <tr><td>CustomerID</td></tr> </table>

