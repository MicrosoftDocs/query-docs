---
title: "Table.FillDown | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.FillDown
  <code>Table.FillDown(<b>table</b> as table, <b>columns</b> as list) as table</code>

## About
Returns a table from the <code>table</code> specified where the value of a previous cell is propagated to the null-valued cells below in the <code>columns</code> specified.

## Example 1
Return a table with the null values in column [Place] filled with the value above them from the table.

<code>Table.FillDown(Table.FromRecords({[Place=1, Name="Bob"], [Place=null, Name="John"], [Place=2, Name="Brad"], [Place=3, Name="Mark"], [Place=null, Name="Tom"], [Place=null, Name="Adam"]}), {"Place"})</code>

<table> <tr> <th>Place</th> <th>Name</th> </tr> <tr> <td>1</td> <td>Bob</td> </tr> <tr> <td>1</td> <td>John</td> </tr> <tr> <td>2</td> <td>Brad</td> </tr> <tr> <td>3</td> <td>Mark</td> </tr> <tr> <td>3</td> <td>Tom</td> </tr> <tr> <td>3</td> <td>Adam</td> </tr> </table>

  
