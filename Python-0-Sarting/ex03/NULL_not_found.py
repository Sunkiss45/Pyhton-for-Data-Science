def NULL_not_found(object: any) -> int:

	fl_nan = float("NaN")

	my_null = {
		None : f"Nothing : {object} {type(object)}",
		fl_nan : f"Cheese : {object} {type(object)}",
		0 : f"Zero : {object} {type(object)}",
		'' : f"Empty : {object} {type(object)}",
		False if isinstance(object, bool) else float("NaN") : f"Fake : {object} {type(object)}"
	}

	if isinstance(object, float) and object != object:
		key = fl_nan
	else:
		key = object

	ret = my_null.get(key, "Type not found")

	print(ret)
	if ret == "Type not found":
		return 1
	return 0