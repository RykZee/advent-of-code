def get_marker_from_message(raw_data, limit=4):
    results = []
    for line in [item for item in raw_data.splitlines() if item != ""]:
        seq = []
        for i, char in enumerate(line):
            seq += char
            if len(set(seq[-limit:])) == limit:
                results.append(i + 1)
                break
    return results
