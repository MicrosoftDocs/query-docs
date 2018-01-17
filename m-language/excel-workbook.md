---
title: "Excel.Workbook | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e6c44c88-67ad-4fb1-b07c-6c238c865326
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
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
  
