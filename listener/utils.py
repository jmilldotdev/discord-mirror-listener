def pythonify(json_data):

    correctedDict = {}

    for key, value in json_data.items():
        if isinstance(value, list):
            value = [
                pythonify(item) if isinstance(item, dict) else item for item in value
            ]
        elif isinstance(value, dict):
            value = pythonify(value)
        try:
            key = int(key)
        except Exception:
            pass
        correctedDict[key] = value

    return correctedDict
