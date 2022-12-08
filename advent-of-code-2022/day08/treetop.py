def get_visibility(raw):
    trees = _build_trees_list_of_lists(raw)

    rows = len(trees)
    cols = len(trees[0])
    visible = rows * 2 + (cols - 2) * 2
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            our_tree = trees[row][col]
            if _is_visible_left(our_tree, row, col, trees)[0]:
                visible += 1
            elif _is_visible_right(our_tree, row, col, cols, trees)[0]:
                visible += 1
            elif _is_visible_top(our_tree, row, col, trees)[0]:
                visible += 1
            elif _is_visible_down(our_tree, row, rows, col, trees)[0]:
                visible += 1

    return visible


def get_scenic_score(raw):
    trees = _build_trees_list_of_lists(raw)

    scenic_scores = []
    rows = len(trees)
    cols = len(trees[0])
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            our_tree = trees[row][col]
            scenic_score = _is_visible_left(our_tree, row, col, trees)[1]
            scenic_score *= _is_visible_right(our_tree, row, col, cols, trees)[1]
            scenic_score *= _is_visible_top(our_tree, row, col, trees)[1]
            scenic_score *= _is_visible_down(our_tree, row, rows, col, trees)[1]
            scenic_scores.append(scenic_score)

    return max(scenic_scores)


def _build_trees_list_of_lists(raw):
    trees = []
    for line in raw.splitlines():
        trees.append([int(num) for num in line])
    return trees


def _is_visible_left(our_tree, row, col, trees):
    other_col = col - 1
    score = 0
    while other_col >= 0:
        if trees[row][other_col] >= our_tree:
            score += 1
            return False, score
        other_col -= 1
        score += 1
    return True, score


def _is_visible_right(our_tree, row, col, cols, trees):
    other_col = col + 1
    score = 0
    while other_col < cols:
        if trees[row][other_col] >= our_tree:
            score += 1
            return False, score
        other_col += 1
        score += 1
    return True, score


def _is_visible_top(our_tree, row, col, trees):
    other_row = row - 1
    score = 0
    while other_row >= 0:
        if trees[other_row][col] >= our_tree:
            score += 1
            return False, score
        other_row -= 1
        score += 1
    return True, score


def _is_visible_down(our_tree, row, rows, col, trees):
    other_row = row + 1
    score = 0
    while other_row < rows:
        if trees[other_row][col] >= our_tree:
            score += 1
            return False, score
        other_row += 1
        score += 1
    return True, score
