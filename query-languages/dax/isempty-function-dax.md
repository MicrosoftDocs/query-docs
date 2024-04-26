---
description: "Learn more about: ISEMPTY"
title: "ISEMPTY function (DAX) | Microsoft Docs"
---
# ISEMPTY

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]
  
Checks if a table is empty.  
  
## Syntax  
  
```dax
ISEMPTY(<table_expression>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table_expression|A table reference or a DAX expression that returns a table.|  
  
## Return value

True if the table is empty (has no rows), if else, False.  

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

For the below table named 'Info':  
  
|Country/Region|State|County|Total|  
|-----------|---------|----------|---------|  
|IND|JK|20|800|  
|IND|MH|25|1000|  
|IND|WB|10|900|  
|USA|CA|5|500|  
|USA|WA|10|900|  
  
```dax
EVALUATE
ROW("Any countries with count > 25?", NOT(ISEMPTY(FILTER(Info, [County]>25))))  
```

Return value: **FALSE**  
