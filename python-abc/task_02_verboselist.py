class VerboseList(list):
    def append(self, item):
        super().append(item)  # Call the original append method
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        super().extend(iterable)  # Call the original extend method
        print(f"Extended the list with [{len(iterable)}] items.")
    
    def remove(self, item):
        if item in self:
            super().remove(item)  # Call the original remove method
            print(f"Removed [{item}] from the list.")
        else:
            print(f"Item [{item}] not found in the list.")  # Handle case when item doesn't exist

    def pop(self, index=-1):
        item = super().pop(index)  # Call the original pop method
        print(f"Popped [{item}] from the list.")
        return item
