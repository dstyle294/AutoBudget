## Decision Flow

To categorize transactions, the following fields will be used (in order of priority) to categorize:
1. If it is a credit card transaction, it contains a Category which will be used. Those fields include
   1. Fees & Adjustments
   2. Food & Drink
   3. Groceries
   4. Travel
   5. Shopping
   6. Health & Wellness
   7. Bills & Utilities
   8. Personal
   9. [Blank] 
2. Else, we will follow this pipeline
   1. Remove noise: strip sequence numbers, date strings, pending flags, and terminal IDs
   2. Extract location data: Isolate state/zip codes at the end of the line
   3. Normalize cases and spacing
3. If there is a key-value mapping of merchant to category, use that.
4. Use LLM to categorize transaction
5. If it doesn't fit into any of the categories, flag the transaction. 