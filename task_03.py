a = 3
b = 6
c = 5
d = 1
e = 2


def is_triplet(one, two, thre):
    result = one + two > thre
    return result

def is_triangles(a,b,c):
    val_list = [a, b, c]
    val_list.sort()
    if is_triplet(val_list[0], val_list[1], val_list[2]):
        return "is triangle"
    return "is not"

if __name__ == '__main__':
    print(is_triangles(a,b,c))
    print(is_triangles(a,d,e))
