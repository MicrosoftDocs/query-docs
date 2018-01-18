---
title: "Error handling | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "index-page "
ms.assetid: defd5222-fb73-4ce7-b6d4-d2c72d0c2967
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Error handling
The Power Query Formula Language is a mashup language for transforming data. It's a functional, case sensitive language similar to F\#. Power Query Formula Language is used in a number of Microsoft products such as Power BI Desktop, Excel, and Analysis Services. To learn more about the language, see [PowerQueryName reference](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## <a name="__toc360789892"></a>Error  
  
|Function|Description|  
|------------|---------------|  
|[Diagnostics.ActivityId](../PowerQuery/diagnostics-activityid.md)|Returns an opaque identifier for the currently-running evaluation.|
|[Diagnostics.Trace](../PowerQuery/diagnostics-trace.md)|Writes a trace message, if tracing is enabled, and returns value.|  
|[Error.Record](../PowerQuery/error-record.md)|Returns a record containing fields ?Reason?, ?Message?, and ?Detail? set to the provided values. The record can be used to raise or throw an error.|  
|[TraceLevel.Critical](../PowerQuery/tracelevel-critical.md)|Returns 1, the value for Critical trace level.|  
|[TraceLevel.Error](../PowerQuery/tracelevel-error.md)|Returns 2, the value for Error trace level.|
|[TraceLevel.Information](../PowerQuery/tracelevel-information.md)|Returns 4, the value for Information trace level.|
|[TraceLevel.Verbose](../PowerQuery/tracelevel-verbose.md)|Returns 5, the value for Verbose trace level.|
|[TraceLevel.Warning](../PowerQuery/tracelevel-warning.md)|Returns 3, the value for Warning trace level.|