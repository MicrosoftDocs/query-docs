---
title: "Type.FunctionParameters | Microsoft Docs"
ms.date: 7/26/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Type.FunctionParameters


## Syntax

<pre>
Type.FunctionParameters(<b>type</b> as type) as record
</pre>
  

## About  
Returns a record with field values set to the name of the parameters of <code>type</code>, and their values set to their corresponding types.

  
## Example  

Find the types of the parameters to the function <code>(x as number, y as text)</code>.

```powerquery-m 
Type.FunctionParameters(type function (x as number, y as text) as any)
```   

<table> <tr> <th>x</th> <td>[Type]</td> </tr> <tr> <th>y</th> <td>[Type]</td> </tr> </table>
