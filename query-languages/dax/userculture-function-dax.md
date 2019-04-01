---
title: "USERCULTURE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 04/01/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# USERCULTURE

Returns the user’s Locale Name.
  
## Syntax  
  
```dax
USERCULTURE()
```
  
## Return value  

User’s locale name based on the two-letter ISO-639 and ISO-3166 codes for language and country code, detected from the user’s application or browser settings. When using Power BI Desktop, this reflects the application language set in **Options** > **Regional Settings**. When viewing a report in the Power BI service, it reflects the browser language.
  
## Example  

```dax
EVALUATE
Row (“Culture”, USERCULTURE())
```

Returns

|Culture  |
|---------|
|en-US     |

For a user using an English language browser in the USA.