---
title: "VAR Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# VAR (DAX)
> [!NOTE]  
> This feature is included in SQL Server 2016 Analysis Services (SSAS), Power Pivot in Excel 2016, and Power BI Desktop only. Information provided here is subject to change.  
  
Stores the result of an expression as a named variable, which can then be passed as an argument to other measure expressions. Once resultant values have been calculated for a variable expression, those values do not change, even if the variable is referenced in another expression.  

## Syntax  
  
```  
VAR <name> = <expression>  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|name|The name of the variable (identifier).<br /><br /><ul><li>Delimiters are not supported. For example, ‘varName’ or [varName] will result in an error.</li><li>Supported character set: a-z, A-Z, 0-9.<br /><br /><ul><li>0-9 are not valid as first character.</li><li>__ (double underscore) is allowed as a prefix to the identifier name. No other special characters are supported.</li></ul></li></ul>Reserved keywords not allowed.<br /><br />Names of existing tables are not allowed.<br /><br />Empty spaces are not allowed.|  
|expression|A DAX expression which returns a scalar or table value.|  
  
## Return Value  
A named variable containing the result of the expression argument.  
  
## Exceptions  
  
## Remarks  
An expression passed as an argument to VAR can contain another VAR declaration.  
  
When referencing a variable:  
  
-   Measures cannot refer to variables defined outside the measure expression, but can refer to functional scope variables defined within the expression.  
  
-   Variables can refer to measures.  
  
-   Variables can refer to previously defined variables.  
  
-   Columns in table variables cannot be referenced via TableName[ColumnName] syntax.  
  
## Example  
To calculate a percentage of year-over-year growth without using a variable, you could create three separate measures. This first measure calculates Sum of Sales Amount:  
  
```  
Sum of SalesAmount = SUM(SalesTable[SalesAmount])  
```  
A second measure calculates the sales amount for the previous year:  
  
```  
SalesAmount PreviousYear=CALCULATE([Sum of SalesAmount], SAMEPERIODLASTYEAR(Calendar[Date]))  
```  
You can then create a third measure that combines the other two measures to calculate a growth percentage. Notice the Sum of SalesAmount measure is used in two places; first to determine if there is a sale, then again to calculate a percentage.  
  
```  
Sum of SalesAmount YoY%:=IF([Sum of SalesAmount] ,  
DIVIDE(([Sum of SalesAmount] – [SalesAmount PreviousYear]), [Sum of SalesAmount]))  
```  
By using a variable, you can create a single measure that calculates the same result:  
  
```  
YoY% = var Sales = SUM(SalesTable[SalesAmount])  
var SalesLastYear=CALCULATE(Sales, SAMEPERIODLASTYEAR(‘Calendar'[Date]))  
return if(Sales, DIVIDE(Sales – SalesLastYear, Sales))  
```  
By using a variable, you can get the same outcome, but in a more readable way. In addition, the result of the expression is stored in the variable upon declaration. It doesn’t have to be recalculated each time it is used, as it would without using a variable. This can improve the measure’s performance.  
  
