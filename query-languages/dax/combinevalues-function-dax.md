---
title: "COMBINEVALUES Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# COMBINEVALUES Function (DAX)
The COMBINEVALUES function joins two or more text strings into one text string. The primary purpose of this function is to support multi-column relationships in DirectQuery models, see **Remarks** for details.  
  
## Syntax  
  
```  
COMBINEVALUES(<delimiter>, <expression>, <expression>[, <expression>]…)
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|delimiter|A separator to use during concatenation. Must be a constant value.|  
|expression|A DAX expression whose value will be be joined into a single text string.|  
  
## Return Value  
The concatenated string.  
  
## Remarks  

The COMBINEVALUES function assumes, but does not validate, that when the input values are different, the output strings are also different. Based on this assumption, when COMBINEVALUES is used to create calculated columns in order to build a relationship that joins multiple columns from two DirectQuery tables, an optimized join condition is generated at query time. For example, if users want to create a relationship between Table1(Column1, Column2) and Table2(Column1, Column2), they can create two calculated columns, one on each table, as:   

```Table1[CalcColumn] = COMBINEVALUES(",", Table1[Column1], Table1[Column2])```

and   

```Table2[CalcColumn] = COMBINEVALUES(",", Table2[Column1], Table2[Column2])```,   

And then create a relationship between `Table1[CalcColumn]` and `Table2[CalcColumn]`. Unlike other DAX functions and operators, which are translated literally to the corresponding SQL operators and functions, the above relationship generates a SQL join predicate as:   

```(Table1.Column1 = Table2.Column1 OR Table1.Column1 IS NULL AND Table2.Column1 IS NULL)```

and   

```(Table1.Column2 = Table2.Column2 OR Table1.Column2 IS NULL AND Table2.Column2 IS NULL)```.  
 
The join predicate can potentially deliver much better query performance than one that involves complex SQL operators and functions.

The COMBINEVALUES function relies on users to choose the appropriate delimiter to ensure that unique combinations of input values produce distinct output strings but it does not validate that the assumption is true. For example, if users choose `"| "` as the delimiter, but one row in Table1 has `Table1[Column1] = "| "` and `Table2 [Column2] = " "`, while one row in Table2 has `Table2[Column1] = " "` and `Table2[Column2] = "| "`, the two concatenated outputs will be the same `"|| "`,  which seem to indicate that the two rows are a match in the join operation. The two rows are not joined together if both tables are from the same DirectQuery source although they are joined together if both tables are imported.

  
## Example  

The following DAX query:
  
```EVALUATE DISTINCT(SELECTCOLUMNS(DimDate, "Month", COMBINEVALUES(",", [MonthName], [CalendarYear])))```

Returns the following single column table:

|[Month]  |
|---------|
|January,2007     |
|February,2007    |
|March,2007    |
|April,2007     |
|May,2007     |
|June,2007     |
|July,2007     |
|August,2007     |
|September,2007     |
|October,2007     |
|November,2007    |
|December,2007     |
|January,2008     |
|January,2008     |
|February,2008    |
|March,2008    |
|April,2008     |
|May,2008     |
|June,2008     |
|July,2008     |
|August,2008     |
|September,2008     |
|October,2008     |
|November,2008    |
|December,2008     |
