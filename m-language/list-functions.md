---
title: "List functions | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "index-page "
ms.assetid: 26a1201b-0192-4111-8d42-50f0ea479a75
caps.latest.revision: 12
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List functions
The Power Query Formula Language (informally known as "M") is a powerful **mashup query language** optimized for building queries that mashup data. It is a functional, case sensitive language similar to F#, which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) in Excel and [Power BI Desktop ](http://go.microsoft.com/fwlink/p/?LinkId=618607). To learn more, see the [Power Query Formula Language (informally known as "M")](https://msdn.microsoft.com/library/mt211003.aspx).  
  
## <a name="__toc360789201"></a>  
  
### <a name="__toc286150735"></a>Information  
  
|Function|Description|  
|------------|---------------|  
|[List.Count](../PowerQuery/list-count.md)|Returns the number of items in a list.|  
|[List.NonNullCount](../PowerQuery/list-nonnullcount.md)|Returns the number of items in a list excluding null values|  
|[List.IsEmpty](../PowerQuery/list-isempty.md)|Returns whether a list is empty.|  
  
### <a name="__toc286150738"></a>Selection  
  
|Function|Description|  
|------------|---------------|  
|[List.Alternate](../PowerQuery/list-alternate.md)|Returns a list with the items alternated from the original list based on a count, optional repeatInterval, and an optional offset.|  
|[List.Buffer](../PowerQuery/list-buffer.md)|Buffers the list in memory. The result of this call is a stable list, which means it will have a determinimic count, and order of items.|
|[List.Distinct](../PowerQuery/list-distinct.md)|Filters a list down by removing duplicates. An optional equation criteria value can be specified to control equality comparison. The first value from each equality group is chosen.|  
|[List.FindText](../PowerQuery/list-findtext.md)|Searches a list of values, including record fields, for a text value.|
|[List.First](../PowerQuery/list-first.md)|Returns the first value of the list or the specified default if empty. Returns the first item in the list, or the optional default value, if the list is empty. If the list is empty and a default value is not specified, the function returns.|  
|[List.FirstN](../PowerQuery/list-firstn.md)|Returns the first set of items in the list by specifying how many items to return or a qualifying condition provided by **countOrCondition**.|  
|[List.InsertRange](../PowerQuery/list-insertrange.md)|Inserts items from values at the given index in the input list.|  
|[List.IsDistinct](../PowerQuery/list-isdistinct.md)|Returns whether a list is distinct.|
|[List.Last](../PowerQuery/list-last.md)|Returns the last set of items in the list by specifying how many items to return or a qualifying condition provided by **countOrCondition**.|  
|[List.LastN](../PowerQuery/list-lastn.md)|Returns the last set of items in a list by specifying how many items to return or a qualifying condition.|  
|[List.MatchesAll](../PowerQuery/list-matchesall.md)|Returns true if all items in a list meet a condition.|  
|[List.MatchesAny](../PowerQuery/list-matchesany.md)|Returns true if any item in a list meets a condition.|  
|[List.Positions](../PowerQuery/list-positions.md)|Returns a list of positions for an input list.|  
|[List.Range](../PowerQuery/list-range.md)|Returns a count items starting at an offset.|  
|[List.Select](../PowerQuery/list-select.md)|Selects the items that match a condition.|
|[List.Single](../PowerQuery/list-single.md)|Returns the single item of the list or throws an Expression.Error if the list has more than one item.|  
|[List.SingleOrDefault](../PowerQuery/list-singleordefault.md)|Returns a single item from a list.|  
|[List.Skip](../PowerQuery/list-skip.md)|Skips the first item of the list. Given an empty list, it returns an empty list. This function takes an optional parameter countOrCondition to support skipping multiple values.|  
  
  
### <a name="__toc286150757"></a>Transformation functions  
  
|Function|Description|  
|------------|---------------|  
|[List.Accumulate](../PowerQuery/list-accumulate.md)|Accumulates a result from the list. Starting from the initial value seed this function applies the accumulator function and returns the final result.|  
|[List.Combine](../PowerQuery/list-combine.md)|Merges a list of lists into single list.|  
|[List.RemoveRange](../PowerQuery/list-removerange.md)|Returns a list that removes count items starting at offset. The default count is 1.|  
|[List.RemoveFirstN](../PowerQuery/list-removefirstn.md)|Returns a list with the specified number of elements removed from the list starting at the first element. The number of elements removed depends on the optional countOrCondition parameter.|  
|[List.RemoveItems](../PowerQuery/list-removeitems.md)|Removes items from list1 that are present in list2, and returns a new list.|
|[List.RemoveLastN](../PowerQuery/list-removelastn.md)|Returns a list with the specified number of elements removed from the list starting at the last element. The number of elements removed depends on the optional countOrCondition parameter.|  
|[List.Repeat](../PowerQuery/list-repeat.md)|Returns a list that repeats the contents of an input list count times.|  
|[List.ReplaceRange](../PowerQuery/list-replacerange.md)|Returns a list that replaces count values in a list with a replaceWith list starting at an index.|
|[List.RemoveMatchingItems](../PowerQuery/list-removematchingitems.md)|Removes all occurrences of the given values in the list.|  
|[List.RemoveNulls](../PowerQuery/list-removenulls.md)|Removes null values from a list.|  
|[List.ReplaceMatchingItems](../PowerQuery/list-replacematchingitems.md)|Replaces occurrences of existing values in the list with new values using the provided equationCriteria. Old and new values are provided by the replacements parameters. An optional equation criteria value can be specified to control equality comparisons. For details of replacement operations and equation criteria, see Parameter Values.|  
|[List.ReplaceValue](../PowerQuery/list-replacevalue.md)|Searches a list of values for the value and replaces each occurrence with the replacement value.|  
|[List.Reverse](../PowerQuery/list-reverse.md)|Returns a list that reverses the items in a list.|
|[List.Transform](../PowerQuery/list-transform.md)|Performs the function on each item in the list and returns the new list.|  
|[List.TransformMany](../PowerQuery/list-transformmany.md)|Returns a list whose elements are projected from the input list.|
  
### <a name="__toc286150761"></a>Membership functions  
Since all values can be tested for equality, these functions can operate over heterogeneous lists.  
  
|Function|Description|  
|------------|---------------|  
|[List.AllTrue](../PowerQuery/list-alltrue.md)|Returns true if all expressions in a list are true|
|[List.AnyTrue](../PowerQuery/list-anytrue.md)|Returns true if any expression in a list in true|
|[List.Contains](../PowerQuery/list-contains.md)|Returns true if a value is found in a list.|  
|[List.ContainsAll](../PowerQuery/list-containsall.md)|Returns true if all items in values are found in a list.|  
|[List.ContainsAny](../PowerQuery/list-containsany.md)|Returns true if any item in values is found in a list.|  
|[List.PositionOf](../PowerQuery/list-positionof.md)|Finds the first occurrence of a value in a list and returns its position.|  
|[List.PositionOfAny](../PowerQuery/list-positionofany.md)|Finds the first occurrence of any value in values and returns its position.|  
 
  
### <a name="__toc360789336"></a>Set operations  
  
|Function|Description|  
|------------|---------------|  
|[List.Difference](../PowerQuery/list-difference.md)|Returns the items in list 1 that do not appear in list 2. Duplicate values are supported.|  
|[List.Intersect](../PowerQuery/list-intersect.md)|Returns a list from a list of lists and intersects common items in individual lists. Duplicate values are supported.|  
|[List.Union](../PowerQuery/list-union.md)|Returns a list from a list of lists and unions the items in the individual lists. The returned list contains all items in any input lists. Duplicate values are matched as part of the Union.| 
|[List.Zip](../PowerQuery/list-zip.md)|Returns a list of lists combining items at the same position.| 
  
### <a name="__toc360789347"></a>Ordering  
Ordering functions perform comparisons.  All values that are compared must be comparable with each other.  This means they must all come from the same datatype (or include null, which always compares smallest).  Otherwise, an Expression.Error is thrown.  
  
**Comparable data types**  
  
-   Number  
  
-   Duration  
  
-   DateTime  
  
-   Text  
  
-   Logical  
  
-   Null  
  
|Function|Description|  
|------------|---------------|  
|[List.Max](../PowerQuery/list-max.md)|Returns the maximum item in a list, or the optional default value if the list is empty.|  
|[List.MaxN](../PowerQuery/list-maxn.md)|Returns the maximum values in the list. After the rows are sorted, optional parameters may be specified to further filter the result|  
|[List.Median](../PowerQuery/list-median.md)|Returns the median item from a list.|
|[List.Min](../PowerQuery/list-min.md)|Returns the minimum item in a list, or the optional default value if the list is empty.|  
|[List.MinN](../PowerQuery/list-minn.md)|Returns the minimum values in a list.|  
|[List.Sort](../PowerQuery/list-sort.md)|Returns a sorted list using comparison criterion.|
  
### <a name="__toc360789369"></a>Averages  
These functions operate over homogeneous lists of Numbers, DateTimes, and Durations.  
  
|Function|Description|  
|------------|---------------|  
|[List.Average](../PowerQuery/list-average.md)|Returns an average value from a list in the datatype of the values in the list.|  
|[List.Mode](../PowerQuery/list-mode.md)|Returns an item that appears most commonly in a list.|  
|[List.Modes](../PowerQuery/list-modes.md)|Returns all items that appear with the same maximum frequency.|
|[List.StandardDeviation](../PowerQuery/list-standarddeviation.md)|Returns the standard deviation from a list of values. List.StandardDeviation performs a sample based estimate. The result is a number for numbers, and a duration for DateTimes and Durations.|  
  
### <a name="__toc286150788"></a>Addition  
These functions work over homogeneous lists of Numbers or Durations.  
  
|Function|Description|  
|------------|---------------|  
|[List.Sum](../PowerQuery/list-sum.md)|Returns the sum from a list.|  
  
### <a name="__toc286150790"></a>Numerics  
These functions only work over numbers.  
  
|Function|Description|  
|------------|---------------|  
|[List.Covariance](../PowerQuery/list-covariance.md)|Returns the covariance from two lists as a number.|  
|[List.Product](../PowerQuery/list-product.md)|Returns the product from a list of numbers.|  
  
### <a name="__toc286150793"></a>Generators  
These functions generate list of values.  
  
|Function|Description|  
|------------|---------------|  
|[List.DateTimes](../PowerQuery/list-datetimes.md)|Returns a list of datetime values from size count, starting at start and adds an increment to every value.|  
|[List.Dates](../PowerQuery/list-dates.md)|Returns a list of date values from size count, starting at start and adds an increment to every value.|  
|[List.DateTimeZones](../PowerQuery/list-datetimezones.md)|Returns a list of of datetimezone values from size count, starting at start and adds an increment to every value.|  
|[List.Durations](../PowerQuery/list-durations.md)|Returns a list of durations values from size count, starting at start and adds an increment to every value.|  
|[List.Generate](../PowerQuery/list-generate.md)|Generates a list from a value function, a condition function, a next function, and an optional transformation function on the values.|  
|[List.Numbers](../PowerQuery/list-numbers.md)|Returns a list of numbers from size count starting at initial, and adds an increment. The increment defaults to 1.|  
|[List.Random](../PowerQuery/list-random.md)|Returns a list of count random numbers, with an optional seed parameter.|  
|[List.Times](../PowerQuery/list-times.md)|Returns a list of time values of size count, starting at start.| 
  
## Parameter values  
  
### Occurrence specification  
  
-   Occurrence.First = 0;  
  
-   Occurrence.Last = 1;  
  
-   Occurrence.All = 2;  
  
### Sort order  
  
-   Order.Ascending = 0;  
  
-   Order.Descending = 1;  
  
### Equation criteria  
Equation criteria for list values can be specified as either a  
  
-   A function value that is either  
  
    -   A key selector that determines the value in the list to apply the equality criteria, or  
  
    -   A comparer function that is used to specify the kind of comparison to apply. Built in comparer functions can be specified, see section for Comparer functions.  
  
-   A list value which has  
  
    -   Exactly two items  
  
    -   The first element is the key selector as specified above  
  
    -   The second element is a comparer as specified above.  
  
For more information and examples, see [List.Distinct](../PowerQuery/list-distinct.md).  
  
### Comparison criteria  
Comparison criterion can be provided as either of the following values:  
  
-   A number value to specify a sort order. For more inforarmtion, see sort order in Parameter values.  
  
-   To compute a key to be used for sorting, a function of 1 argument can be used.  
  
-   To both select a key and control order, comparison criterion can be a list containing the key and order.  
  
-   To completely control the comparison, a function of 2 arguments can be used that returns -1, 0, or 1 given the relationship between the left and right inputs.  Value.Compare is a method that can be used to delegate this logic.  
  
For more information and examples, see [List.Sort](../PowerQuery/list-sort.md).  
  
### Replacement operations  
Replacement operations are specified by a list value, each item of this list must be  
  
-   A list value of exactly two items  
  
-   Fist item is the old value in the list, to be replaced  
  
-   Second item is the new which should replace all occurrences of the old value in the list  
  
