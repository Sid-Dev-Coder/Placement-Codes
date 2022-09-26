# //heap sort in python?
def heapsort(sqc):
    def down_heap(sqc, k, n):
        parent = sqc[k]

        while 2*k+1 < n:
            child = 2*k+1
            if child+1 < n and sqc[child] < sqc[child+1]:
                child += 1
            if parent >= sqc[child]:
                break
            sqc[k] = sqc[child]
            k = child
        sqc[k] = parent

    size = len(sqc)

    for i in range(size/2-1, -1, -1):
        down_heap(sqc, i, size)

    for i in range(size-1, 0, -1):
        sqc[0], sqc[i] = sqc[i], sqc[0]
        down_heap(sqc, 0, i)


def heapsort(sequence):
    sequence_length = len(sequence)

    def swap_if_greater(parent_index, child_index):
        if sequence[parent_index] < sequence[child_index]:
            sequence[parent_index], sequence[child_index] =\
                sequence[child_index], sequence[parent_index]

    def sift(parent_index, unsorted_length):
        def index_of_greater(
            a, b): return a if sequence[a] > sequence[b] else b
        while parent_index*2+2 < unsorted_length:
            left_child_index = parent_index*2+1
            right_child_index = parent_index*2+2

            greater_child_index = index_of_greater(left_child_index,
                                                   right_child_index)

            swap_if_greater(parent_index, greater_child_index)

            parent_index = greater_child_index

    def heapify():
        for i in range((sequence_length/2)-1, -1, -1):
            sift(i, sequence_length)

    def sort():
        count = sequence_length
        while count > 0:
            count -= 1
        swap_if_greater(count, 0)
        sift(0, count)

    heapify()
    sort()


def opt_heapsort(s):
    sl = len(s)

    def swap(pi, ci):
        if s[pi] < s[ci]:
            s[pi], s[ci] = s[ci], s[pi]

    def sift(pi, unsorted):
        def i_gt(a, b): return a if s[a] > s[b] else b
        while pi*2+2 < unsorted:
            gtci = i_gt(pi*2+1, pi*2+2)
            swap(pi, gtci)
            pi = gtci
    # heapify
    for i in range((sl/2)-1, -1, -1):
        sift(i, sl)
    # sort
    for i in range(sl-1, 0, -1):
        swap(i, 0)
        sift(0, i)
