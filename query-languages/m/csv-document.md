---
title: "Csv.Document | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Csv.Document

  
## About  
Returns the contents of the CSV document as a table. <ul> <li> <code>columns</code>: If a record is specified and <code>delimiter</code>, <code>extraValues</code>, <code>encoding</code> are null, all of parameters <code>Delimiter</code>, <code>Columns</code>, <code>Encoding</code>, <code>CsvStyle</code> and <code>QuoteStyle</code> are obtained from the record.</li> <li> <code>delimiter</code> can take a single character or a list; Comma is used if not specified or null.</li> <li> Please refer to <code>ExtraValues.Type</code> for supported values of optional <code>extraValues</code>.</li> <li> <code>encoding</code> specifies the text encoding type.</li> </ul>   
  
  
```  
Csv.Document(source as any, optional columns as any,  optional delimiter as nullable text,  optional extraValues as nullable number, optional encoding as nullable number) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|source|The CSV file to parse.|  
|optional columns|Optional column names.|  
|optional delimiter|Delimiters between values.|  
|optional extraValues|Specification for extra value handling.|  
|optional encoding|Encoding value.|  
  
## Remarks  
  
-   QuoteStyle.Csv is used during the parsing. With this QuoteStyle, a double quote character is used to demarcate such regions, and a pair of double quote characters is used to indicate a single double quote character within such a region.  
  
## Example  
  
```  
//Assume the following SalesForce contacts CSV file.  
  
FirstName,LastName,Title,ReportsTo.Email,Birthdate,Description  
  
Tom,Jones,Senior Director,buyer@salesforcesample.com,1940-06-07Z,"Self-described as ""the top"" branding guru on the West Coast"  
  
Ian,Dury,Chief Imagineer,cto@salesforcesample.com,,"World-renowned expert in fuzzy logic design.  
  
Influential in technology purchases."  
  
let  
  
    Source = Csv.Document(File.Contents("C:\Projects\Examples\SalesForceContacts.txt"),[Delimiter=",",Encoding=1252]),  
  
    #"First Row as Header" = Table.PromoteHeaders(Source),  
  
    #"Changed Type" = Table.TransformColumnTypes  
  
(#"First Row as Header",{{"FirstName", type text},  
  
{"LastName", type text}, {"Title", type text}, {"ReportsTo.Email", type text}, {"Birthdate", type datetime}, {"Description", type text}}),  
  
    #"Removed Columns" = Table  
  
.RemoveColumns(#"Changed Type", {"Description", "Birthdate"})  
  
in  
  
    #"Removed Columns"  
  
equals  
```  
  
|FirstName|LastName|Title|ReportsTo.Email|  
|-------------|------------|---------|-------------------|  
|Tom|Jones|Senior Director|buyer@salesforcesample.com|  
|Ian|Dury|Chief Imagineer|cto@salesforcesample.com|  
  
