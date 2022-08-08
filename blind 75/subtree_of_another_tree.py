def isMatch(r, sr):
    if not(r and sr):
        return r is sr

    if r.val == sr.val:
        return isMatch(r.left, sr.left) and isMatch(r.right, sr.right)

def isSubtree(r, sr):
    if isMatch(r, sr):
        return True

    if r is None:
        return False

    return isSubtree(r.left, sr) or isSubtree(r.right, sr)


