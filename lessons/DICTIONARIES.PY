while True:
    def histogram(seq):
        d = dict()
        for element in seq:
            if element not in d:
                d[element] = 1
            else:
              d[element] += 1
        return d
h = histogram('brontosaurus')
Print(h)