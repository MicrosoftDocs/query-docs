---
title: "COUNTROWS Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# COUNTROWS Function (DAX)
The COUNTROWS function counts the number of rows in the specified table, or in a table defined by an expression.  
  
## Syntax  
  
```dax
COUNTROWS(<table>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**table**|The name of the table that contains the rows to be counted, or an expression that returns a table.|  
  
## Return Value  
A whole number.  
  
## Remarks  
This function can be used to count the number of rows in a base table, but more often is used to count the number of rows that result from filtering a table, or applying context to a table.  
  
Whenever there are no rows to aggregate, the function returns a blank.  However, if there are rows, but none of them meet the specified criteria, the function returns 0. Microsoft Excel also returns a zero if no rows are found that meet the conditions.  
  
## Example  
The following example shows how to count the number of rows in the table Orders. The expected result is 52761.  
  
```dax
=COUNTROWS('Orders')  
```
  
## Example  
The following example demonstrates how to use COUNTROWS with a row context. In this scenario, there are two sets of data that are related by order number. The table Reseller contains one row for each reseller; the table ResellerSales contains multiple rows for each order, each row containing one order for a particular reseller. The tables are connected by a relationship on the column, ResellerKey.  
  
The formula gets the value of ResellerKey and then counts the number of rows in the related table that have the same reseller ID. The result is output in the column, **CalculatedColumn1**.  
  
```dax
=COUNTROWS(RELATEDTABLE(ResellerSales))  
```dax
The following table shows a portion of the expected results:  
  
|ResellerKey|CalculatedColumn1|  
|---------------|---------------------|  
|1|73|  
|2|70|  
|3|394|  
  
## See Also  
[COUNT Function &#40;DAX&#41;](count-function-dax.md)  
[COUNTA Function &#40;DAX&#41;](counta-function-dax.md)  
[COUNTAX Function &#40;DAX&#41;](countax-function-dax.md)  
[COUNTX Function &#40;DAX&#41;](countx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
