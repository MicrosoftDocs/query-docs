---
description: "Learn more about: List functions"
title: "List functions | Microsoft Docs"
ms.date: 8/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List functions

These functions create and manipulate list values.
  
## <a name="__toc360789201"></a>  
  
### <a name="__toc286150735"></a>Information  
  
|Function|Description|  
|------------|---------------|  
|[List.Count](list-count.md)|Returns the number of items in a list.|  
|[List.NonNullCount](list-nonnullcount.md)|Returns the number of items in a list excluding null values|  
|[List.IsEmpty](list-isempty.md)|Returns whether a list is empty.|  
  
### <a name="__toc286150738"></a>Selection  
  
|Function|Description|  
|------------|---------------|  
|[List.Alternate](list-alternate.md)|Returns a list with the items alternated from the original list based on a count, optional repeatInterval, and an optional offset.|  
|[List.Buffer](list-buffer.md)|Buffers the list in memory. The result of this call is a stable list, which means it will have a determinimic count, and order of items.|
|[List.Distinct](list-distinct.md)|Filters a list down by removing duplicates. An optional equation criteria value can be specified to control equality comparison. The first value from each equality group is chosen.|  
|[List.FindText](list-findtext.md)|Searches a list of values, including record fields, for a text value.|
|[List.First](list-first.md)|Returns the first value of the list or the specified default if empty. Returns the first item in the list, or the optional default value, if the list is empty. If the list is empty and a default value is not specified, the function returns.|  
|[List.FirstN](list-firstn.md)|Returns the first set of items in the list by specifying how many items to return or a qualifying condition provided by **countOrCondition**.|  
|[List.InsertRange](list-insertrange.md)|Inserts items from values at the given index in the input list.|  
|[List.IsDistinct](list-isdistinct.md)|Returns whether a list is distinct.|
|[List.Last](list-last.md)|Returns the last set of items in the list by specifying how many items to return or a qualifying condition provided by **countOrCondition**.|  
|[List.LastN](list-lastn.md)|Returns the last set of items in a list by specifying how many items to return or a qualifying condition.|  
|[List.MatchesAll](list-matchesall.md)|Returns true if all items in a list meet a condition.|  
|[List.MatchesAny](list-matchesany.md)|Returns true if any item in a list meets a condition.|  
|[List.Positions](list-positions.md)|Returns a list of positions for an input list.|  
|[List.Range](list-range.md)|Returns a count items starting at an offset.|  
|[List.Select](list-select.md)|Selects the items that match a condition.|
|[List.Single](list-single.md)|Returns the single item of the list or throws an Expression.Error if the list has more than one item.|  
|[List.SingleOrDefault](list-singleordefault.md)|Returns a single item from a list.|  
|[List.Skip](list-skip.md)|Skips the first item of the list. Given an empty list, it returns an empty list. This function takes an optional parameter countOrCondition to support skipping multiple values.|  
  
  
### <a name="__toc286150757"></a>Transformation functions  
  
|Function|Description|  
|------------|---------------|  
|[List.Accumulate](list-accumulate.md)|Accumulates a result from the list. Starting from the initial value seed this function applies the accumulator function and returns the final result.|  
|[List.Combine](list-combine.md)|Merges a list of lists into single list.|
|[List.ConformToPageReader](list-conformtopagereader.md)|This function is intended for internal use only.|  
|[List.RemoveRange](list-removerange.md)|Returns a list that removes count items starting at offset. The default count is 1.|  
|[List.RemoveFirstN](list-removefirstn.md)|Returns a list with the specified number of elements removed from the list starting at the first element. The number of elements removed depends on the optional countOrCondition parameter.|  
|[List.RemoveItems](list-removeitems.md)|Removes items from list1 that are present in list2, and returns a new list.|
|[List.RemoveLastN](list-removelastn.md)|Returns a list with the specified number of elements removed from the list starting at the last element. The number of elements removed depends on the optional countOrCondition parameter.|  
|[List.Repeat](list-repeat.md)|Returns a list that repeats the contents of an input list count times.|  
|[List.ReplaceRange](list-replacerange.md)|Returns a list that replaces count values in a list with a replaceWith list starting at an index.|
|[List.RemoveMatchingItems](list-removematchingitems.md)|Removes all occurrences of the given values in the list.|  
|[List.RemoveNulls](list-removenulls.md)|Removes null values from a list.|  
|[List.ReplaceMatchingItems](list-replacematchingitems.md)|Replaces occurrences of existing values in the list with new values using the provided equationCriteria. Old and new values are provided by the replacements parameters. An optional equation criteria value can be specified to control equality comparisons. For details of replacement operations and equation criteria, see Parameter Values.|  
|[List.ReplaceValue](list-replacevalue.md)|Searches a list of values for the value and replaces each occurrence with the replacement value.|  
|[List.Reverse](list-reverse.md)|Returns a list that reverses the items in a list.|   
|[List.Split](list-split.md)|Splits the specified list into a list of lists using the specified page size.|
|[List.Transform](list-transform.md)|Performs the function on each item in the list and returns the new list.|  
|[List.TransformMany](list-transformmany.md)|Returns a list whose elements are projected from the input list.|
  
### <a name="__toc286150761"></a>Membership functions  
Since all values can be tested for equality, these functions can operate over heterogeneous lists.  
  
|Function|Description|  
|------------|---------------|  
|[List.AllTrue](list-alltrue.md)|Returns true if all expressions in a list are true|
|[List.AnyTrue](list-anytrue.md)|Returns true if any expression in a list in true|
|[List.Contains](list-contains.md)|Returns true if a value is found in a list.|  
|[List.ContainsAll](list-containsall.md)|Returns true if all items in values are found in a list.|  
|[List.ContainsAny](list-containsany.md)|Returns true if any item in values is found in a list.|  
|[List.PositionOf](list-positionof.md)|Finds the first occurrence of a value in a list and returns its position.|  
|[List.PositionOfAny](list-positionofany.md)|Finds the first occurrence of any value in values and returns its position.|  
 
  
### <a name="__toc360789336"></a>Set operations  
  
|Function|Description|  
|------------|---------------|  
|[List.Difference](list-difference.md)|Returns the items in list 1 that do not appear in list 2. Duplicate values are supported.|  
|[List.Intersect](list-intersect.md)|Returns a list from a list of lists and intersects common items in individual lists. Duplicate values are supported.|  
|[List.Union](list-union.md)|Returns a list from a list of lists and unions the items in the individual lists. The returned list contains all items in any input lists. Duplicate values are matched as part of the Union.| 
|[List.Zip](list-zip.md)|Returns a list of lists combining items at the same position.| 
  
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
|[List.Max](list-max.md)|Returns the maximum item in a list, or the optional default value if the list is empty.|  
|[List.MaxN](list-maxn.md)|Returns the maximum values in the list. After the rows are sorted, optional parameters may be specified to further filter the result|  
|[List.Median](list-median.md)|Returns the median item from a list.|
|[List.Min](list-min.md)|Returns the minimum item in a list, or the optional default value if the list is empty.|  
|[List.MinN](list-minn.md)|Returns the minimum values in a list.|  
|[List.Sort](list-sort.md)|Returns a sorted list using comparison criterion.|
|[List.Percentile](list-percentile.md) | Returns one or more sample percentiles corresponding to the given probabilities.|
|[PercentileMode.ExcelExc](percentilemode-excelexc.md) | When interpolating values for <code>List.Percentile</code>, use a method compatible with Excel's <code>PERCENTILE.EXC</code>.|
|[PercentileMode.ExcelInc](percentilemode-excelinc.md) | When interpolating values for <code>List.Percentile</code>, use a method compatible with Excel's <code>PERCENTILE.INC</code>.|
|[PercentileMode.SqlCont](percentilemode-sqlcont.md) | When interpolating values for <code>List.Percentile</code>, use a method compatible with SQL Server's <code>PERCENTILE_CONT</code>.|
|[PercentileMode.SqlDisc](percentilemode-sqldisc.md) | When interpolating values for <code>List.Percentile</code>, use a method compatible with SQL Server's <code>PERCENTILE_DISC</code>.|
  
### <a name="__toc360789369"></a>Averages  
These functions operate over homogeneous lists of Numbers, DateTimes, and Durations.  
  
|Function|Description|  
|------------|---------------|  
|[List.Average](list-average.md)|Returns an average value from a list in the datatype of the values in the list.|  
|[List.Mode](list-mode.md)|Returns an item that appears most commonly in a list.|  
|[List.Modes](list-modes.md)|Returns all items that appear with the same maximum frequency.|
|[List.StandardDeviation](list-standarddeviation.md)|Returns the standard deviation from a list of values. List.StandardDeviation performs a sample based estimate. The result is a number for numbers, and a duration for DateTimes and Durations.|  
  
### <a name="__toc286150788"></a>Addition  
These functions work over homogeneous lists of Numbers or Durations.  
  
|Function|Description|  
|------------|---------------|  
|[List.Sum](list-sum.md)|Returns the sum from a list.|  
  
### <a name="__toc286150790"></a>Numerics  
These functions only work over numbers.  
  
|Function|Description|  
|------------|---------------|  
|[List.Covariance](list-covariance.md)|Returns the covariance from two lists as a number.|  
|[List.Product](list-product.md)|Returns the product from a list of numbers.|  
  
### <a name="__toc286150793"></a>Generators  
These functions generate list of values.  
  
|Function|Description|  
|------------|---------------|  
|[List.Dates](list-dates.md)|Returns a list of date values from size count, starting at start and adds an increment to every value.|
|[List.DateTimes](list-datetimes.md)|Returns a list of datetime values from size count, starting at start and adds an increment to every value.|   
|[List.DateTimeZones](list-datetimezones.md)|Returns a list of of datetimezone values from size count, starting at start and adds an increment to every value.|  
|[List.Durations](list-durations.md)|Returns a list of durations values from size count, starting at start and adds an increment to every value.|  
|[List.Generate](list-generate.md)|Generates a list from a value function, a condition function, a next function, and an optional transformation function on the values.|  
|[List.Numbers](list-numbers.md)|Returns a list of numbers from size count starting at initial, and adds an increment. The increment defaults to 1.|  
|[List.Random](list-random.md)|Returns a list of count random numbers, with an optional seed parameter.|  
|[List.Times](list-times.md)|Returns a list of time values of size count, starting at start.| 
  
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
  
For more information and examples, see [List.Distinct](list-distinct.md).  
  
### Comparison criteria  
Comparison criterion can be provided as either of the following values:  
  
-   A number value to specify a sort order. For more inforarmtion, see sort order in Parameter values.  
  
-   To compute a key to be used for sorting, a function of 1 argument can be used.  
  
-   To both select a key and control order, comparison criterion can be a list containing the key and order.  
  
-   To completely control the comparison, a function of 2 arguments can be used that returns -1, 0, or 1 given the relationship between the left and right inputs.  Value.Compare is a method that can be used to delegate this logic.  
  
For more information and examples, see [List.Sort](list-sort.md).  
  
### Replacement operations  
Replacement operations are specified by a list value, each item of this list must be  
  
-   A list value of exactly two items  
  
-   Fist item is the old value in the list, to be replaced  
  
-   Second item is the new which should replace all occurrences of the old value in the list  
  
