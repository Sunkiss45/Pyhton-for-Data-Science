def all_thing_is_obj(object: any) -> int:
	my_type = {
		list : f"List : {type(object)}",
		tuple : f"Tuple : {type(object)}",
		set : f"Set : {type(object)}",
		dict : f"Dict : {type(object)}",
		str : f"{object} is in the kitchen : {type(object)}"
	}
	print(my_type.get(type(object), "Type not found"))
	return 42