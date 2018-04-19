---
title: "Excel.Workbook | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Excel.Workbook
  
<code>Excel.Workbook(**workbook** as binary, optional **useHeaders** as nullable logical, optional **delayTypes** as nullable logical) as table </code>

## About  
Returns a table representing sheets in the given excel workbook.  

  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|workbook|The workbook to retrieve the sheets for.|  
|optional useHeaders|Use the first row of the excel sheets as table headers.|  
  
## Example  
  
```  
Excel.Workbook(File.Contents("localExcelFile.xlsx"))  
  
      let  
  
    Source = Excel.Workbook(File.Contents("C:\Projects\Examples\Customers and Orders.xlsx"), true),  
  
    Customers_Sheet = Source{[Item="Customers",Kind="Sheet"]}[Data]  
  
in  
  
    Customers_Sheet  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
|3|Paul|543-7890|  
|4|Ringo|232-1550|  
  
