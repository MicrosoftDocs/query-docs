---
title: "Type.RecordFields | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Type.RecordFields


## Syntax

<pre>
Type.RecordFields(<b>type</b> as type) as record
</pre> 


## About  
Returns a record describing the fields of a record <code>type</code>. Each field of the returned record type has a corresponding name and a value, in the form of a record <code>[ Type = type, Optional = logical ]</code>.
  

  
## Example  

Find the name and value of the record <code>[ A = number, optional B = any]</code>.   

```powerquery-m
Type.RecordFields(type [A = number, optional B = any])
```   
<table> <tr> <th>A</th> <td>[Record]</td> </tr> <tr> <th>B</th> <td>[Record]</td> </tr> </table>
