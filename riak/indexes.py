
def get_index_type(value):
    "Use duck-typing to determine what the index's internal type should be"
    index_type = "bin"
	
    if type(value) is int:
        index_type = "int"

    return index_type


def get_index_name(name, value):
    "Return the true index name with the embedded type"
    return "%s_%s" % (name, get_index_type(value))
