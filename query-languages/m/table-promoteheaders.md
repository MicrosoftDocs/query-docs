---
title: "Table.PromoteHeaders | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.PromoteHeaders

  
`Table.PromoteHeaders(<b>table</b> as table, optional <b>options</b> as nullable record) as table`  
## About  
Promotes the first row of values as the new column headers (i.e. column names). By default, only text or number values are promoted to headers. Valid options: `PromoteAllScalars` : If set to `true`, all the scalar values in the first row are promoted to headers using the `Culture`, if specified (or current document locale). For values that cannot be converted to text, a default column name will be used.  `Culture` : A culture name specifying the culture for the data.   
  
## Example 1  
Promote the first row of values in the table.  
  
`Table.PromoteHeaders(Table.FromRecords({[Column1 = "CustomerID", Column2 = "Name", Column3 = #date(1980,1,1)], [Column1 = 1, Column2 = "Bob", Column3 = #date(1980,1,1)]}))`  
  
<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Column3</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>1/1/1980 12:00:00 AM</td> </tr> </table>  
  
## Example 2  
Promote all the scalars in the first row of the table to headers.  
  
`Table.PromoteHeaders(Table.FromRecords({[Rank = 1, Name = "Name", Date = #date(1980,1,1)],[Rank = 1, Name = "Bob", Date = #date(1980,1,1)]}), [PromoteAllScalars = true, Culture = "en-US"])`  
  
<table> <tr> <th>1</th> <th>Name</th> <th>1/1/1980</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>1/1/1980 12:00:00 AM</td> </tr> </table>