---
title: "SELECTCOLUMNS Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# SELECTCOLUMNS Function (DAX)
Adds calculated columns to the given table or table expression.  
  
## Syntax  
  
```dax
SELECTCOLUMNS(<table>, <name>, <scalar_expression> [, <name>, <scalar_expression>]…) 
```
  
#### Parameters  

|Term|Definition|  
|--------|--------------|  
|  table|  Any DAX expression that returns a table. |  
| name |  The name given to the column, enclosed in double quotes. |
|expression|Any expression that returns a scalar value like a column reference, integer, or string value.|
  
## Return value  
A table with the same number of rows as the table specified as the first argument. The returned table has one column for each pair of \<name>, \<scalar_expression> arguments, and each expression is evaluated in the context of a row from the specified \<table> argument. 
  
## Remarks  

SELECTCOLUMNS has the same signature as ADDCOLUMNS, and has the same behavior except that instead of starting with the \<table> specified, SELECTCOLUMNS starts with an empty table before adding columns.
  
## Example  

For the following table named **Info**:

Country  |State  |Count  |Total  
---------|---------|---------|---------
IND     |   JK      |    20     |  800       
IND     |   MH      |    25     |  1000       
IND     |   WB      |    10     |  900       
USA     |   CA      |    5     |   500      
USA     |   WA      |    10     |  900       

   




```dax
SELECTCOLUMNS(Info, “StateCountry”, [State]&”, ”&[Country])
```

Returns:
  
<table>
	<tr>
		<th>StateCountry</th>
	</tr>
    <tr>
		<td>IND, JK</td>
	</tr>
	<tr>
		<td>IND, MH</td>
	</tr>
	<tr>
		<td>IND, WB</td>
	</tr>
	<tr>
		<td>USA, CA</td>
	</tr>
	<tr>
		<td>USA, WA</td>
	</tr>
</table>
