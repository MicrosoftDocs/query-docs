---
title: "VALUES Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# VALUES Function (DAX)
Returns a one-column table that contains the distinct values from the specified table or column. In other words, duplicate values are removed and only unique values are returned.  
  
> [!NOTE]  
> This function cannot be used to return values into a cell or column on a worksheet; rather, you use it as an intermediate function, nested in a formula, to get a list of distinct values that can be counted, or used to filter or sum other values.  
  
## Syntax  
  
```  
VALUES(<TableNameOrColumnName>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**Table or column**|The table or column from which unique values are to be returned.|  
  
## Return Value  
A column of unique values.  
  
## Remarks  
When you use the VALUES function in a context that has been filtered, such as in a PivotTable, the unique values returned by VALUES are affected by the filter. For example, if you filter by Region, and return a list of the values for City, the list will include only those cities in the regions permitted by the filter. To return all of the cities, regardless of existing filters, you must use the ALL function to remove filters from the table. The second example demonstrates use of ALL with VALUES.  
  
## Related Functions  
In most scenarios, when the argument is a column name, the results of the VALUES function are identical to those of the **DISTINCT** function. Both functions remove duplicates and return a list of the possible values in the specified column. However, the VALUES function can also return a blank value. This blank value is useful in cases where you are looking up distinct values from a related table, but a value used in the relationship is missing from one table. In database terminology, this is termed a violation of referential integrity. Such mismatches in data can occur when one table is being updated and the related table is not. 

When the argument is a table name, the result of the VALUES function returns all rows in the specified table plus a blank row, if there is a violation of referential integrity. The DISTINCT function removes duplicate rows and returns unique rows in the specified table.

>[!NOTE]  
> The DISTINCT function allows a column name or any valid table expression to be its argument but the VALUES function only accepts a column name or a table name as the argument.
 
  
The following table summarizes the mismatch between data that can occur in two related tables when referential integrity is not preserved.  
  
|MyOrders table|MySales table|  
|------------------|-----------------|  
|June 1|June 1 sales|  
|June 2|June 2 sales|  
|(no order dates have been entered)|June 3 sales|  
  
If you used the DISTINCT function to return a list of dates from the PivotTable containing these tables, only two dates would be returned. However, if you use the VALUES function, the function returns the two dates plus an additional blank member. Also, any row from the MySales table that does not have a matching date in the MyOrders table will be "matched" to this unknown member.  
  
## Example  
The following formula counts the number of unique invoices (sales orders), and produces the following results when used in a report that includes the Product Category Names:  
  
|Row Labels|Count Invoices|  
|--------------|------------------|  
|Accessories|18,208|  
|Bikes|15,205|  
|Clothing|7,461|  
|Grand Total|27,659|  
  
```  
=COUNTROWS(VALUES('InternetSales_USD'[SalesOrderNumber]))  
```  
  
## See Also  
[FILTER Function &#40;DAX&#41;](filter-function-dax.md)  
[COUNTROWS Function &#40;DAX&#41;](countrows-function-dax.md)  
[Filter Functions &#40;DAX&#41;](filter-functions-dax.md)  
  
