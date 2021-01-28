---
description: "Learn more about: ALLSELECTED"
title: "ALLSELECTED function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ALLSELECTED

Removes context filters from columns and rows in the current query, while retaining all other context filters or explicit filters.  
  
The ALLSELECTED function gets the context that represents all rows and columns in the query, while keeping explicit filters and contexts other than row and column filters. This function can be used to obtain visual totals in queries.  
  
## Syntax  
  
```dax
ALLSELECTED([<tableName> | <columnName>[, <columnName>[, <columnName>[,…]]]] )
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|tableName|The name of an existing table, using standard DAX syntax. This parameter cannot be an expression. This parameter is optional.  | 
|columnName|The name of an existing column using standard DAX syntax, usually fully qualified. It cannot be an expression. This parameter is optional.    |
  
## Return value

The context of the query without any column and row filters.  
  
## Remarks  
  
- If there is one argument, the argument is either *tableName* or *columnName*. If there is more than one argument, they must be columns from the same table.  
  
- This function is different from ALL() because it retains all filters explicitly set within the query, and it retains all context filters other than row and column filters.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following example shows how to generate different levels of visual totals in a table report using DAX expressions. In the report two (2) previous filters have been applied to the Reseller Sales data; one on Sales Territory Group = *Europe* and the other on Promotion Type = *Volume Discount*. Once filters have been applied, visual totals can be calculated for the entire report, for All Years, or for All Product Categories. Also, for illustration purposes the grand total for All Reseller Sales is obtained too, removing all filters in the report. Evaluating the following DAX expression results in a table with all the information needed to build a table with Visual Totals.  
  
```dax
define  
measure 'Reseller Sales'[Reseller Sales Amount]=sum('Reseller Sales'[Sales Amount])  
measure 'Reseller Sales'[Reseller Grand Total]=calculate(sum('Reseller Sales'[Sales Amount]), ALL('Reseller Sales'))  
measure 'Reseller Sales'[Reseller Visual Total]=calculate(sum('Reseller Sales'[Sales Amount]), ALLSELECTED())  
measure 'Reseller Sales'[Reseller Visual Total for All of Calendar Year]=calculate(sum('Reseller Sales'[Sales Amount]), ALLSELECTED('Date'[Calendar Year]))  
measure 'Reseller Sales'[Reseller Visual Total for All of Product Category Name]=calculate(sum('Reseller Sales'[Sales Amount]), ALLSELECTED('Product Category'[Product Category Name]))  
evaluate  
CalculateTable(  
    //CT table expression  
    summarize(
//summarize table expression  
crossjoin(distinct('Product Category'[Product Category Name]), distinct('Date'[Calendar Year]))  
//First Group by expression  
, 'Product Category'[Product Category Name]  
//Second Group by expression  
, 'Date'[Calendar Year]  
//Summary expressions  
, "Reseller Sales Amount", [Reseller Sales Amount]  
, "Reseller Grand Total", [Reseller Grand Total]  
, "Reseller Visual Total", [Reseller Visual Total]  
, "Reseller Visual Total for All of Calendar Year", [Reseller Visual Total for All of Calendar Year]  
, "Reseller Visual Total for All of Product Category Name", [Reseller Visual Total for All of Product Category Name]  
)  
//CT filters  
, 'Sales Territory'[Sales Territory Group]="Europe", 'Promotion'[Promotion Type]="Volume Discount"  
)  
order by [Product Category Name], [Calendar Year]  
```

After executing the above expression in SQL Server Management Studio against AdventureWorks DW Tabular Model, you obtain the following results:  
  
|[Product Category Name]|[Calendar Year]|[Reseller Sales Amount]|[Reseller Grand Total]|[Reseller Visual Total]|[Reseller Visual Total for All of Calendar Year]|[Reseller Visual Total for All of Product Category Name]|  
|----------------------------|--------------------|----------------------------|---------------------------|----------------------------|-----------------------------------------------------|-------------------------------------------------------------|  
|Accessories|2000||80450596.9823|877006.7987|38786.018||  
|Accessories|2001||80450596.9823|877006.7987|38786.018||  
|Accessories|2002|625.7933|80450596.9823|877006.7987|38786.018|91495.3104|  
|Accessories|2003|26037.3132|80450596.9823|877006.7987|38786.018|572927.0136|  
|Accessories|2004|12122.9115|80450596.9823|877006.7987|38786.018|212584.4747|  
|Accessories|2005||80450596.9823|877006.7987|38786.018||  
|Accessories|2006||80450596.9823|877006.7987|38786.018||  
|Bikes|2000||80450596.9823|877006.7987|689287.7939||  
|Bikes|2001||80450596.9823|877006.7987|689287.7939||  
|Bikes|2002|73778.938|80450596.9823|877006.7987|689287.7939|91495.3104|  
|Bikes|2003|439771.4136|80450596.9823|877006.7987|689287.7939|572927.0136|  
|Bikes|2004|175737.4423|80450596.9823|877006.7987|689287.7939|212584.4747|  
|Bikes|2005||80450596.9823|877006.7987|689287.7939||  
|Bikes|2006||80450596.9823|877006.7987|689287.7939||  
|Clothing|2000||80450596.9823|877006.7987|95090.7757||  
|Clothing|2001||80450596.9823|877006.7987|95090.7757||  
|Clothing|2002|12132.4334|80450596.9823|877006.7987|95090.7757|91495.3104|  
|Clothing|2003|58234.2214|80450596.9823|877006.7987|95090.7757|572927.0136|  
|Clothing|2004|24724.1209|80450596.9823|877006.7987|95090.7757|212584.4747|  
|Clothing|2005||80450596.9823|877006.7987|95090.7757||  
|Clothing|2006||80450596.9823|877006.7987|95090.7757||  
|Components|2000||80450596.9823|877006.7987|53842.2111||  
|Components|2001||80450596.9823|877006.7987|53842.2111||  
|Components|2002|4958.1457|80450596.9823|877006.7987|53842.2111|91495.3104|  
|Components|2003|48884.0654|80450596.9823|877006.7987|53842.2111|572927.0136|  
|Components|2004||80450596.9823|877006.7987|53842.2111|212584.4747|  
|Components|2005||80450596.9823|877006.7987|53842.2111||  
|Components|2006||80450596.9823|877006.7987|53842.2111||  
  
The columns in the report are:  
  
Reseller Sales Amount  
The actual value of Reseller Sales for the year and product category. This value appears in a cell in the center of your report, at the intersection of year and catergory.  
  
Reseller Visual Total for All of Calendar Year  
The total value for a product category across all years. This value appears at the end of a column or row for a given product category and across all years in the report.  
  
Reseller Visual Total for All of Product Category Name  
The total value for a year across all product categories. This value appears at the end of a column or row for a given year and across all product categories in the report.  
  
Reseller Visual Total  
The total value for all years and product categories. This value usually appears in the bottom rightmost corner of the table.  
  
Reseller Grand Total  
This is the grand total for all reseller sales, before any filter has been applied; you should notice the difference with [Reseller Visual Total]. You do remember that this report includes two (2) filters, one on Product Category Group and the other in Promotion Type.  
  
 > [!NOTE]
> if you have explicit filters in your expression, those filters are also applied to the expression.  
